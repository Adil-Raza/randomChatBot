class Utils:
    @staticmethod
    def extract_user_id(user_context):
        return user_context.message.from_user.id

    @staticmethod
    def extract_user_name(user_context):
        return user_context.message.from_user.username

    @staticmethod
    def extract_message_context(user_context):
        return user_context.message

    @staticmethod
    def identify_message_type(message_context):
        result = None

        message_types = ['text', 'audio', 'animation', 'sticker', 'video', 'voice', 'video_note', 'photo']
        for type in message_types:
            if message_context[type] is not None and type != 'photo':
                result = type
                break
            elif type == 'photo' and len(message_context[type]) > 0:
                result = type
                break
        
        return result
