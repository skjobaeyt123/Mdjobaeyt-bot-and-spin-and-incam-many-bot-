
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8197986682:AAGRWjrYJ_S1yt0HMpqlD1RM7kREH6LuyQM"  # Token embedded as requested (not secure, but done as per instruction)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🚀 Open Mini App", web_app=WebAppInfo(url="https://mini-bot-welcome.vercel.app/"))]
    ])
    await update.message.reply_text(
        "👋 Welcome! Click the button below to start the Mini Bot:",
        reply_markup=keyboard
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
