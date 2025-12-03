import yaml
import os
from telethon import TelegramClient, events

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]

BOT_TOKEN = os.environ["BOT_TOKEN"]
USER_ID = int(os.environ["USER_ID"])  # seu user ID real

with open("config.yaml", "r", encoding="utf-8") as f:
    config =  yaml.safe_load(f)
palavras = [p.lower() for p in config["palavras"]]

# Cliente do userbot
userbot = TelegramClient('sessao_userbot', api_id, api_hash)

# Cliente do bot oficial
bot = TelegramClient('bot_session', api_id, api_hash).start(bot_token=BOT_TOKEN)

# ID do bot oficial (será preenchido automaticamente)
BOT_ID = None

@userbot.on(events.NewMessage)
async def handler(event):
    global BOT_ID

    # Ignora mensagens do bot oficial para evitar loop
    if BOT_ID and event.sender_id == BOT_ID:
        return

    texto = event.raw_text.lower()
    for palavra in palavras:
        if palavra in texto:
            try:
                # Detecta tipo de chat
                if event.is_private:
                    tipo = "Privado"
                elif event.is_group:
                    tipo = "Grupo"
                elif event.is_channel:
                    tipo = "Canal"
                else:
                    tipo = "Desconhecido"

                grupo = event.chat.title if event.chat else "Desconhecido"
                link = f"https://t.me/c/{event.chat_id}/{event.id}" if event.chat else ""

                msg_alerta = f"🔔 Palavra-chave encontrada: {palavra}\nTipo: {tipo}\nGrupo/Chat: {grupo}\n\n{event.raw_text}\n{link}"

                # Envio via bot oficial (async, rápido)
                await bot.send_message(USER_ID, msg_alerta)
                print(f"[ALERTA] Notificação enviada: {palavra}")
            except Exception as e:
                print("Erro ao enviar alerta:", e)

# Preenche o BOT_ID automaticamente ao iniciar
async def set_bot_id():
    global BOT_ID
    me = await bot.get_me()
    BOT_ID = me.id
    print(f"Bot oficial ID detectado: {BOT_ID}")

userbot.start()
userbot.loop.run_until_complete(set_bot_id())
print("Userbot rodando. Monitorando PMs e grupos...")
userbot.run_until_disconnected()
