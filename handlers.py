from randomChat import RandomChat
import response
from constantMessages import *
from telegram import *

class Handlers:
    chat = RandomChat()

    @staticmethod
    def start_command(update, context):
        Handlers.chat.add_user(update)
        print('new User: ', update)
        Handlers.chat.send_message(update.message, response.start['response'])

    @staticmethod
    def help_command(update, context):
        Handlers.chat.send_help_menu(update)

    @staticmethod
    def search_command(update, context):
        Handlers.chat.send_message(update.message, SEARCHING)

        idle_user_details = Handlers.chat.search_idle_user()
        if idle_user_details is not None:
            Handlers.chat.connect_new_user_to_idle_user(update, idle_user_details)
        else:
            Handlers.chat.add_new_idle_user(update)
            Handlers.chat.send_message(update.message, WAIT)

    @staticmethod
    def stop_command(update, context):
        Handlers.chat.disconnect_user(update)

    @staticmethod
    def next_command(update, context):
        Handlers.chat.send_message(update.message, SEARCHING_NEXT)

    @staticmethod
    def handle_message(update, context):
        Handlers.chat.send_message_to_connected_user(update, update.message)

    @staticmethod
    def error(update, context):
        print(f"update {update} caused error {context.error}")

    @staticmethod
    def gender_settings(update, context):
        buttons = [
            [InlineKeyboardButton('Male', callback_data="MALE"), InlineKeyboardButton('Female', callback_data="FEMALE")]
        ]
        
        Handlers.chat.send_buttons(update, context, buttons, 'Select your gender')

    @staticmethod
    def queryHandler(update, context):
        query = update.callback_query.data
        update.callback_query.answer()

        print(update.callback_query)

        print(query)

        if 'MALE' in query:
            print('male')
        if 'FEMALE' in query:
            print('female')