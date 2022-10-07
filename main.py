import constants as constants
from telegram.ext import *
import response as response


print("started")

def start_command(update, context):
    update.message.reply_text("type your name")

def handle_message(update, context):
    print("-------Message handler-------")
    print(update)

    text = str(update.message.text).lower()

    res = response.sample_response(text)

    update.message.reply_text(res)

def error(update, context):
    print(f"update {update} caused error {context.error}")

def main():
    updater = Updater(constants.API_KEY, use_context = True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)
    
    updater.start_polling()
    updater.idle()

main()
