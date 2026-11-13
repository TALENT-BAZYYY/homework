import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = round(end_time - start_time, 1)
        print(f"Время выполнения: {elapsed_time} секунд")
        return result
    return wrapper

@timer
def download_video():
    time.sleep(2)
    print("Видео загружено")

download_video()
