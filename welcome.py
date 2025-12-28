import os
import logging
import random
import asyncio
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Безопасное получение токена
TOKEN = os.environ.get('TELEGRAM_TOKEN')
if not TOKEN:
    raise ValueError("Токен не найден! Установите переменную TELEGRAM_TOKEN")

FIXED_USERNAME = "@Welcome775"

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
    if not update.message or not update.message.text:
        return
    
    # Игнорируем команды
    if update.message.text.startswith('/'):
        return
    
    response = random.choice(RESPONSES)
    await update.message.reply_text(response)
    
    # Логирование
    user = update.message.from_user
    logging.info(f"👤 {user.first_name} (@{user.username}): {update.message.text[:50]}")
    logging.info(f"🤖 Бот: {response}")

def run_bot():
    """Запуск бота с обработкой ошибок"""
    try:
        # Настройка логирования
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO,
            handlers=[
                logging.StreamHandler(),  # Вывод в консоль
                logging.FileHandler('bot.log')  # Логи в файл
            ]
        )
        
        # Создаем приложение
        application = Application.builder().token(TOKEN).build()
        
        # Добавляем обработчик ТОЛЬКО текстовых сообщений (не команд)
        application.add_handler(MessageHandler(
            filters.TEXT & ~filters.COMMAND, 
            handle_all_messages
        ))
        
        logging.info("="*50)
        logging.info(f"🤖 Бот запущен и слушает сообщения...")
        logging.info(f"🔤 Вариантов ответов: {len(RESPONSES)}")
        logging.info(f"🎯 Цель: {FIXED_USERNAME}")
        logging.info("="*50)
        
        # Запускаем polling с обработкой ошибок
        application.run_polling(
            drop_pending_updates=True,
            allowed_updates=Update.ALL_TYPES,
            close_loop=False
        )
        
    except Exception as e:
        logging.error(f"Ошибка при запуске бота: {e}")
        # Перезапуск через 30 секунд
        logging.info("Перезапуск через 30 секунд...")
        time.sleep(30)
        run_bot()

if __name__ == '__main__':
    run_bot()
