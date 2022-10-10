from queue import Queue

class Data:
    def __init__(self):
        '''
            users:
                key: user_id
                value: {
                    message_context
                    user_name
                }
        '''
        self.users = {}
        self.connected_users = {}
        self.idle_users_queue = Queue(maxsize=0)

    