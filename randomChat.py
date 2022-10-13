from constantMessages import CONNECTED_SUCCESSFULLY, STRANGER_DISCONNECTED, UNSUPPORTED_MEDIA_TYPE, YOU_STOPPED_CHAT
from dataAccessor import DataAccessor
from utils import Utils
import response
from telegram import *
from telegram.ext import *

class RandomChat:
    def __init__(self):
        self.dataAccessor = DataAccessor()

    def add_user(self, update):
        user_id = Utils.extract_user_id(update)
        user_name = Utils.extract_user_name(update)

        new_user_data = {
            'user_name': user_name
        }
        self.dataAccessor.add_user_data(user_id=user_id, user_data=new_user_data)

    def add_new_idle_user(self, update):
        user_id = Utils.extract_user_id(update)

        user_details = {
            'user_id': user_id
            # more data can be added for smart user search
        }

        self.dataAccessor.put_new_user_to_idle(user_details=user_details)

    def search_idle_user(self):
        user = self.dataAccessor.get_idle_user()

        if user is not None:
            return user
        else:
            return None

    def connect_new_user_to_idle_user(self, update, context, idle_user_details):
        user_id = Utils.extract_user_id(update)
        idle_user_id = idle_user_details['user_id']

        user_value = {
            'connected_to': idle_user_id,
        }

        idle_user_value = {
            'connected_to': user_id,
        }

        self.dataAccessor.add_new_connected_user(user_id=user_id, user_data=user_value)
        self.dataAccessor.add_new_connected_user(user_id=idle_user_id, user_data=idle_user_value)

        self.send_message_via_user_id_2(context, user_id, CONNECTED_SUCCESSFULLY)
        self.send_message_via_user_id_2(context, idle_user_id, CONNECTED_SUCCESSFULLY)   

    def disconnect_user(self, update, context):
        user_id = Utils.extract_user_id(update)
        connected_user = self.dataAccessor.get_connected_user(user_id)

        if connected_user is not None:
            connected_user_id = connected_user['connected_to']
            self.dataAccessor.delete_conneted_uesr(user_id)
            self.dataAccessor.delete_conneted_uesr(connected_user_id)

            self.send_message_via_user_id_2(context, user_id, YOU_STOPPED_CHAT)
            self.send_message_via_user_id_2(context, connected_user_id, STRANGER_DISCONNECTED)

    def send_message_to_connected_user(self, update, context):
        msg_type = Utils.identify_message_type(update.message)
        message = update.message[msg_type]

        user_id = Utils.extract_user_id(update)
        connected_user = self.dataAccessor.get_connected_user(user_id)

        if connected_user is not None:
            connected_user_id = connected_user['connected_to']
            self.send_message_via_user_id_2(context, connected_user_id, message, type=msg_type)
    
    def send_help_menu(self, update, context):
        self.send_message2(update, context, response.help['response'])

    def send_message_via_user_id_2(self, context: CallbackContext, user_id, message, type='text'):
        if type == 'text':
            context.bot.send_message(chat_id=user_id, text=message)
        elif type == 'sticker':
            context.bot.send_sticker(chat_id=user_id, sticker=message)
        elif type == 'audio':
            context.bot.send_audio(chat_id=user_id, audio=message)
        elif type == 'animation':
            context.bot.send_animation(chat_id=user_id, animation=message)
        elif type == 'voice':
            context.bot.send_voice(chat_id=user_id, voice=message)
        elif type == 'video':
            context.bot.send_video(chat_id=user_id, video=message)
        elif type == 'video_note':
            context.bot.send_video_note(chat_id=user_id, video_note=message)
        elif type == 'photo':
            context.bot.send_photo(chat_id=user_id, photo=message[0])
        else:
            context.bot.send_message(chat_id=user_id, text=UNSUPPORTED_MEDIA_TYPE)   

    def send_message2(self, update, context, message, type='text'):
        user_id = Utils.extract_user_id(update)
        self.send_message_via_user_id_2(context, user_id, message, type=type)

    def send_buttons(self, user_context, context_object, buttons, text=''):
        context_object.bot.send_message(
            chat_id=1157727203,
            text=text
        )

        # context_object.bot.send_message(
        #     chat_id=user_context.effective_chat.id,
        #     reply_markup=InlineKeyboardMarkup(buttons), text=text
        # )

# 1157727203
