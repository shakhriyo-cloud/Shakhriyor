from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8771714483:AAFfPjpJNzQq2zW65rpIFl1667z1ylMkP4o"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Bot ishlayapti ✅")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Yordam bo‘limi")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))

print("Bot ishga tushdi")

app.run_polling()
