import os
import random
import logging
from telegram import Update
from telegram.ext import (
    filters,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    ApplicationBuilder,
    ConversationHandler
)

TOKEN = os.environ['my_bot_token']

logging.basicConfig(
    format='%(asctime)s - %(message)s',
    level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Hi {update.effective_user.first_name}, I am a bot created by Rany.\nPlease select a command from the menu."
    )


def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()


if __name__ == '__main__':
    main()