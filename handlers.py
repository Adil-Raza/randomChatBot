from randomChat import RandomChat
import response
from constantMessages import *
from telegram import *
from utils import Utils

class Handlers:
    chat = RandomChat()

    @staticmethod
    def start_command(update, context):
        Handlers.chat.add_user(update)
        print('new User: ', update)

        Handlers.chat.send_message2(update, context, response.start['response'])

    @staticmethod
    def help_command(update, context):
        Handlers.chat.send_help_menu(update, context)

    @staticmethod
    def search_command(update, context):
        Handlers.chat.send_message2(update, context, SEARCHING)

        idle_user_details = Handlers.chat.search_idle_user()
        if idle_user_details is not None:
            Handlers.chat.connect_new_user_to_idle_user(update, context, idle_user_details)
        else:
            Handlers.chat.add_new_idle_user(update)
            Handlers.chat.send_message2(update, context, WAIT)

    @staticmethod
    def stop_command(update, context):
        Handlers.chat.disconnect_user(update, context)

    @staticmethod
    def next_command(update, context):
        Handlers.chat.send_message2(update, context, SEARCHING_NEXT)
        Handlers.stop_command(update, context)
        Handlers.search_command(update, context)

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