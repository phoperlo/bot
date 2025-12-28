import logging
import random
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "8505977032:AAFpiI7A4nFu--_xmw9Hiy8Dmr7NkoQc5C8"
FIXED_USERNAME = "@Welcome775"

# Разные варианты ответов
RESPONSES = [
    f"я думаю это этот еблан {FIXED_USERNAME}",
    f"наверное, это всё из-за пидораса {FIXED_USERNAME}",
    f"уебан {FIXED_USERNAME}, я уверен!",
    f"это точно дела {FIXED_USERNAME}",
    f"100% это этот хуйлан {FIXED_USERNAME}",
    f"без сомнений, этот гондон {FIXED_USERNAME}",
    f"опять этот хуесос {FIXED_USERNAME}...",
    f"все беды от {FIXED_USERNAME}",
]

async def handle_all_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Отвечает на все сообщения случайной фразой"""
    message = update.message
    
    # Выбираем случайный ответ
    response = random.choice(RESPONSES)
    
    await message.reply_text(response)
    print(f"👤 {message.from_user.first_name}: {message.text if message.text else '[медиа]'}")
    print(f"🤖 Бот: {response}")

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.ALL, handle_all_messages))
    
    print("="*50)
    print(f"🤖 Бот запущен!")
    print(f"🔤 Варианты ответов: {len(RESPONSES)}")
    print("="*50)
    
    application.run_polling()

if __name__ == '__main__':
    main()