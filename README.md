<h1 align="center">🔍 PriceSniffer_Telegram Bot</h1>

<p align="center">
Bot + Userbot para monitoramento em tempo real de mensagens do Telegram e enviar alertas automáticos quando palavras-chave forem detectadas em grupos, canais ou chats privados.
</p>

<p align="center">
<img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge">
<img src="https://img.shields.io/badge/Telethon-API-success?style=for-the-badge">
<img src="https://img.shields.io/badge/Status-Ativo-green?style=for-the-badge">
</p>

---

## Funcionalidades

✔ Monitora mensagens em tempo real usando **Userbot**  
✔ Detecta palavras-chave definidas em arquivo **config.yaml**  
✔ Retorna notificações automáticas via **Bot Oficial**  
✔ Funciona em grupos, canais e mensagens privadas  
✔ Código modular com suporte para deploy 24/7

---

*Antes de rodar o script, instale as dependências:
pip install -r requirements.txt
*Adicione as palavras que o bot deve rastrear em config.yaml

Os dados do telegram devem ser preenchidos como variáveis de ambiente: 

API_ID=seu_id
API_HASH=hash_aqui
BOT_TOKEN=token_do_botfather (Recomendo o uso do BotFather)
USER_ID=seu_user_id

inicie com: 
python main.py
