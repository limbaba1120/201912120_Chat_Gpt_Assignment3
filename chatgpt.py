import telebot
from openai import OpenAI

# https://www.linkedin.com/pulse/chatgpt-telegram-bot-dasaraju-abhishek-varma 참고

# OpenAI에서 받은 TOKEN 입력
client = OpenAI(
    api_key="sk-YOUR OPENAI KEY"
)

# Telegram TOKEN 입력
bot_token = "YOUR TELEGRAM TOKEN"

# 봇 객체를 만든다
bot = telebot.TeleBot(bot_token)

# 들어오는 메시지를 처리하는 함수
@bot.message_handler(func=lambda message: True)
def Echo(message):
    # Get the text of the incoming message
    message_text = message.text.lower()

    # 만약에 결제를 하고 실제 연동 시 해당 코드 사용. Incoming 메시지가 들어오면 사용자에게 답변을 함
    # completion = client.chat.completions.create(
    #         model="gpt-3.5-turbo",
    #         messages=[
    #             {"role": "user", "content": "Tell the world about the ChatGPT API in the style of a pirate."}
    #         ]
    #     )
    
    # 연동 하지 않을 경우 사용자에게 'hello' 라는 답변만 보낸다.
    content = 'hello'
    bot.send_message(message.chat.id, text=content)
       
# Start the bot
bot.polling()

