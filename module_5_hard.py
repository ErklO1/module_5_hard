import time

class UrTube:
    """
    Класс UrTube, содержащий атрибуты: users(список объектов User), videos(список объектов Video),
    current_user(текущий пользователь, User)
    """
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, login, password):
        self.login = str(login)
        self.password = str(password)
        for user in self.users:
            if login == user.nickname and password == user.password:
                self.current_user = user

    def register(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = str(password)
        self.age = int(age)
        password = hash(password)
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return

        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for movie in args:
            if movie not in self.videos:
                self.videos.append(movie)

    def get_videos(self, text):
        self.text = str(text)
        list_movie = []
        for video in self.videos:
            if text.upper() in video.title.upper():
                list_movie.append(video.title)
        return list_movie

    def watch_video(self, movie):
        self.movie = str(movie)
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for x in self.videos:
            if x.title == movie:
                if x.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста, покиньте страницу')
                    return

                for i in range(1, 11):
                    print(i, end=' ')
                    time.sleep(1)
                    x.time_now += 1
                x.time_now = 0
                print('Конец видео')

class Video:
    """
    Класс видео, содержащий атрибуты: title(заголовок, строка), duration(продолжительность, секунды),
    time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
    """
    def __init__(self, title, duration, adult_mode : bool = False):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = 0
        self.adult_mode = adult_mode
        self.bool = bool

    def __eq__(self, other):
        return self.title == other.title

    def __contains__(self, item):
        return item in self.title

class User:
    """
       Класс пользователя, содержащий атрибуты:  nickname(имя пользователя, строка),
       password(в хэшированном виде, число), age(возраст, число)
       """

    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = int(password)
        self.age = int(age)

    def __str__(self):
        return self.nickname

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
