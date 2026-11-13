class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

def is_admin(func):
    def wrapper(user):
        if user.role == "admin":
            return func(user)
        else:
            print("У вас нет доступа")
    return wrapper

@is_admin
def delete_video(user):
    print("Видео удалено")

admin = User("Ardager", "admin")
user = User("Bek", "user")

delete_video(admin)
delete_video(user)
