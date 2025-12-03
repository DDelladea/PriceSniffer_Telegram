import yaml
import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
BOT_TOKEN = os.environ["BOT_TOKEN"]
USER_ID = int(os.environ["USER_ID"])
SESSION = os.environ["SESSION"]   # ⬅ sessão do userbot

with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)
palavras = [p.lower() for p in config["palavras"]]

# Userbot via Sessão (não pede telefone)
userbot = TelegramClient(StringSession(SESSION), api_id, api_hash)

# Bot normal
bot = TelegramClient('bot_session', api_id, api_hash).start(bot_token=BOT_TOKEN)

BOT_ID = None

@userbot.on(events.NewMessage)
async def handler(event):
    global BOT_ID
    if BOT_ID and event.sender_id == BOT_ID:
        return

    texto = event.raw_text.lower()
    for palavra in palavras:
        if palavra in texto:
            try:
                tipo = "Privado" if event.is_private else "Grupo" if event.is_group else "Canal" if event.is_channel else "Desconhecido"
                grupo = event.chat.title if event.chat else "Desconhecido"
                link = f"https://t.me/c/{event.chat_id}/{event.id}" if event.chat else ""

                msg = f"🔔 Palavra-chave encontrada: {palavra}\nTipo: {tipo}\nGrupo/Chat: {grupo}\n\n{event.raw_text}\n{link}"

                await bot.send_message(USER_ID, msg)
                print(f"[ALERTA] Enviado: {palavra}")

            except Exception as e:
                print("Erro:", e)

async def set_bot_id():
    global BOT_ID
    me = await bot.get_me()
    BOT_ID = me.id
    print("Bot ID:", BOT_ID)

userbot.start()
userbot.loop.run_until_complete(set_bot_id())
print("Userbot online e monitorando 🔥")
userbot.run_until_disconnected()
