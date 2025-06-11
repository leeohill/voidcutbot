from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    ConversationHandler,
    filters
)
import os

ASK_CODE = 1

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Please enter your invitation code:")
    return ASK_CODE

async def receive_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Incorrect code entered")
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Cancelled.")
    return ConversationHandler.END

def main():
    token = "7386758129:AAG0gB9WPJ1gT7UXKR1UIwR8FNu9xAJ8k4A"
    # token = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={ASK_CODE: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_code)]},
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    app.add_handler(conv_handler)

    print("Bot started!")
    app.run_polling()

if __name__ == '__main__':
    main()
