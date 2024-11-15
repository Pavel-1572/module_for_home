class UrTube:

    def __init__(self, users, videos, current_user):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname, password):
        for i in self.users:
            if nickname in i and password in i:
                self.current_user = nickname

    def register(self, nickname, password, age,):
        flag = True
        for i in self.users:
            if nickname.__eq__ (i[0]):
                print(f'Пользователь {nickname} уже существует')

    def log_out(self):


    def add(self, other):


    def get_videos(self):

    def watch_video(self):





class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __hash__(self):
        return hash((self.age, self.name))


class Video:

    def __init__(self, title, duration, time_now, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode



