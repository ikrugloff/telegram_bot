import os


class MyTelegramData:
    PROXY = {
        'http': 'socks5://telegram:telegram@qcpfo.tgproxy.me:3128',
        'https': 'socks5://telegram:telegram@qcpfo.tgproxy.me:1080'
    }
    USERS = set()

    @staticmethod
    def get_token():
        current_file_path = __file__
        current_file_dir = os.path.dirname(__file__)
        other_file_path = os.path.join(current_file_dir, 'token.txt')
        f = open(other_file_path, 'r')
        token = f.read().rstrip()
        f.close()
        return token

    @staticmethod
    def get_chat_id():
        current_file_path = __file__
        current_file_dir = os.path.dirname(__file__)
        other_file_path = os.path.join(current_file_dir, 'chat_id.txt')
        f = open(other_file_path, 'r')
        chat_id = f.read().rstrip()
        f.close()
        return chat_id

    @staticmethod
    def get_user_id():
        current_file_path = __file__
        current_file_dir = os.path.dirname(__file__)
        other_file_path = os.path.join(current_file_dir, 'user_id.txt')
        f = open(other_file_path, 'r')
        user_id = f.read().rstrip()
        f.close()
        return user_id

    @staticmethod
    def get_joke():
        current_file_path = __file__
        current_file_dir = os.path.dirname(__file__)
        other_file_path = os.path.join(current_file_dir, 'joke.txt')
        with open(other_file_path, 'r') as content_file:
            joke = content_file.read()
        return joke


if __name__ == '__main__':
    token = MyTelegramData.get_token()
    chat_id = MyTelegramData.get_chat_id()
    user_id = MyTelegramData.get_user_id()
    joke = MyTelegramData.get_joke()
