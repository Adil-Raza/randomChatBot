from constantMessages import CONNECTED_SUCCESSFULLY, STRANGER_DISCONNECTED, UNSUPPORTED_MEDIA_TYPE, YOU_STOPPED_CHAT
from dataAccessor import DataAccessor
from utils import Utils
import response
from telegram import *

class RandomChat:
    def __init__(self):
        self.dataAccessor = DataAccessor()

    def add_user(self, user_context):
        user_id = Utils.extract_user_id(user_context)
        user_name = Utils.extract_user_name(user_context)
        message_context = Utils.extract_message_context(user_context)

        new_user_data = {
            'user_name': user_name,
            'message_context': message_context
        }
        self.dataAccessor.add_user_data(user_id=user_id, user_data=new_user_data)

    def add_new_idle_user(self, user_context):
        user_id = Utils.extract_user_id(user_context)

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

    def connect_new_user_to_idle_user(self, user_context, idle_user_details):
        user_id = Utils.extract_user_id(user_context)
        idle_user_id = idle_user_details['user_id']

        user_value = {
            'connected_to': idle_user_id,
        }

        idle_user_value = {
            'connected_to': user_id,
        }

        self.dataAccessor.add_new_connected_user(user_id=user_id, user_data=user_value)
        self.dataAccessor.add_new_connected_user(user_id=idle_user_id, user_data=idle_user_value)

        self.send_message_via_user_id(idle_user_id, CONNECTED_SUCCESSFULLY)
        self.send_message_via_user_id(user_id, CONNECTED_SUCCESSFULLY)        

    def disconnect_user(self, user_context):
        user_id = Utils.extract_user_id(user_context)
        connected_user = self.dataAccessor.get_connected_user(user_id)

        if connected_user is not None:
            connected_user_id = connected_user['connected_to']
            self.dataAccessor.delete_conneted_uesr(user_id)
            self.dataAccessor.delete_conneted_uesr(connected_user_id)

            self.send_message_via_user_id(connected_user_id, STRANGER_DISCONNECTED)
            self.send_message_via_user_id(user_id, YOU_STOPPED_CHAT)

    def send_message_to_connected_user(self, user_context, message_context):
        msg_type = Utils.identify_message_type(message_context)
        message = message_context[msg_type]

        user_id = Utils.extract_user_id(user_context)
        connected_user = self.dataAccessor.get_connected_user(user_id)

        if connected_user is not None:
            connected_user_id = connected_user['connected_to']
            self.send_message_via_user_id(connected_user_id, message, type=msg_type)

    def send_message(self, message_context, message, type='text'):
        if type == 'text':
            message_context.reply_text(message)
        elif type == 'sticker':
            message_context.reply_sticker(message)
        elif type == 'audio':
            message_context.reply_audio(message)
        elif type == 'animation':
            message_context.reply_animation(message)
        elif type == 'voice':
            message_context.reply_voice(message)
        elif type == 'video':
            message_context.reply_video(message)
        elif type == 'video_note':
            message_context.reply_video_note(message)
        elif type == 'photo':
            message_context.reply_photo(message[0])
        else:
            message_context.reply_text(UNSUPPORTED_MEDIA_TYPE)

    def send_message_via_user_id(self, user_id, message, type='text'):
        user_context = self.dataAccessor.get_user_data(user_id=user_id)

        if user_context is not None:
            self.send_message(user_context['message_context'], message, type)
    
    def send_help_menu(self, user_context):
        self.send_message(user_context.message, response.help['response'])

    def send_buttons(self, user_context, context_object, buttons, text=''):
        # context_object.bot.send_message(
        #     chat_id=1157727203,
        #     reply_markup=InlineKeyboardMarkup(buttons), text=text
        )

        context_object.bot.send_message(
            chat_id=user_context.effective_chat.id,
            reply_markup=InlineKeyboardMarkup(buttons), text=text
        )

# 1157727203
