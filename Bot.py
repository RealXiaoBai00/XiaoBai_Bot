from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = 8707659243:AAHSFJWFCBixgH9l7yM4OVyWYv3nHHP1kNs

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot အလုပ်လုပ်နေပြီ ✅")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
