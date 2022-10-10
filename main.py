import constants as constants
from telegram.ext import *
from handlers import Handlers
import response

print("started")

def main():
    handlers = Handlers()

    updater = Updater(constants.API_KEY, use_context = True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler(response.start['command'], handlers.start_command))
    dp.add_handler(CommandHandler(response.help['command'], handlers.help_command))
    dp.add_handler(CommandHandler("search", handlers.search_command))
    dp.add_handler(CommandHandler("stop", handlers.stop_command))
    dp.add_handler(CommandHandler("test", handlers.gender_settings))

    dp.add_handler(MessageHandler(Filters.all, handlers.handle_message))

    # callback handler register
    dp.add_handler(CallbackQueryHandler(handlers.queryHandler))


    dp.add_error_handler(handlers.error)
    
    updater.start_polling()
    updater.idle()

main()
