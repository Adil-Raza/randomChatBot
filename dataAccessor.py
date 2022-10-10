from data import Data

class DataAccessor:
    def __init__(self):
        self.data = Data()

    def add_user_data(self, user_id, user_data):
        self.data.users[user_id] = user_data

    def get_user_data(self, user_id):
        if user_id in self.data.users:
            return self.data.users[user_id]
        else:
            return None

    def update_user_data(self, user_id, user_data):
        self.data.users[user_id] = user_data

    def delete_user_data(self, user_id):
        if user_id in self.data.users:
            del self.data.users[user_id]
    
    def get_connected_users(self):
        return self.data.connected_users
    
    def get_connected_user(self, user_id):
        if user_id in self.data.connected_users:
            return self.data.connected_users[user_id]
        else:
            return None

    def add_new_connected_user(self, user_id, user_data):
        self.data.connected_users[user_id] = user_data

    def update_connected_user(self, user_id, user_data):
        self.data.connected_users[user_id] = user_data

    def delete_conneted_uesr(self, user_id):
        if user_id in self.data.connected_users:
            del self.data.connected_users[user_id]

    def get_idle_users_queue(self):
        return self.data.idle_users_queue;

    def put_new_user_to_idle(self, user_details):
        self.data.idle_users_queue.put(user_details)

    def get_idle_user(self):
        if not self.data.idle_users_queue.empty():
            return self.data.idle_users_queue.get()
        else:
            return None
