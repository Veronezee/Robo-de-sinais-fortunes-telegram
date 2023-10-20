import telebot
import random
import datetime
import time

# Define o bot e o chat_id
bot = telebot.TeleBot ("ID DO SEU BOT")
chat_id = "SEU CHAT ID"

# Define a frequência em que o campo é atualizado (em segundos)
ENVIO_RESULTADO = 120 #120 segundos
FREQUENCIA_ATUALIZACAO = 300 #5 minutos

while True:
    # Numeros de jogadas 
    jogadas = random.randint(15, 20)

    agora = datetime.datetime.now()
    depois = agora + datetime.timedelta(minutes=3)
    hora_fim = depois.strftime('%H:%M')

    hora = agora.strftime('%H:%M')

    # Define as informações da mensagem
    mensagem = "🔔 OPORTUNIDADE IDENTIFICADA 🔔\n\n"
    jogo_nome = "🐯 Fortune Tiger\n"
    numero_jogadas = f"🔥 Número máximo de jogadas: {jogadas}\n"
    validade = f"⏰ Válido até: {hora_fim}\n"
    link_cadastro = '[Jogar Fortune Tiger]({})'.format('https://google.com/')
    link_cadastro2 = '[100% de Bônus Aqui]({})'.format('https://google.com/')


    # Envia a mensagem de oportunidade
    bot.send_message(chat_id, f'''

🚨 *ENTRADA CONFIRMADA* 🚨

🍀 Fortune Tiger 🐯
⏰ Estratégia: *Horários pagantes*
⚠️ *Válido das*: {hora} até {hora_fim}
⭐️ *Máximo de jogadas*: {jogadas}

💰 7x *Normal*
🔃 *Intercalando*
🚀 7x *Turbo*


📲 {"https://funbbr.com/?v=4PARPSSYM2U"} 🐯🍀
🎁 {"https://funbbr.com/?v=4PARPSSYM2U"} 🤑💰

''', parse_mode='Markdown', disable_web_page_preview=True)

    # Aguarda 2 minutos
    time.sleep(ENVIO_RESULTADO)

    # Envia a mensagem de encerramento
    mensagem_encerramento = f"✅ Sinal Fortune Tiger finalizado, aguarde o próximo sinal.\n⏰ Entrada encerrada às: {hora_fim}"
    bot.send_message(chat_id=chat_id, text=mensagem_encerramento)

    # Aguarda 5 minutos para reiniciar o loop
    time.sleep(FREQUENCIA_ATUALIZACAO)
