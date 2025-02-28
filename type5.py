import time
import winsound
import threading

class Timer:
    def __init__(self):
        self.time = 0
        self.running = False
        self.stopped = True

    def set_time(self, seconds):
        self.time = seconds

    def start(self):
        if not self.running and not self.stopped:
            print("Таймер уже запущен.")
            return
        self.stopped = False
        self.running = True
        threading.Thread(target=self.count).start()

    def stop(self):
        self.stopped = True
        self.running = False

    def count(self):
        while self.time > 0 and not self.stopped:
            mins, secs = divmod(self.time, 60)
            print(f"\rТаймер: {mins:02d}:{secs:02d}", end="")
            time.sleep(1)
            self.time -= 1
        if not self.stopped:
            print("\nВремя истекло!")
            winsound.Beep(2500, 1000)  # Звуковой сигнал
        self.running = False

def main():
    timer = Timer()
    while True:
        print("\n1. Установить время")
        print("2. Запустить таймер")
        print("3. Остановить таймер")
        print("4. Выход")
        choice = input("Выберите действие: ")
        
        if choice == "1":
            seconds = int(input("Введите время в секундах: "))
            timer.set_time(seconds)
        elif choice == "2":
            if timer.running:
                print("Таймер уже запущен.")
            else:
                timer.start()
        elif choice == "3":
            timer.stop()
        elif choice == "4":
            break
        else:
            print("Неправильный выбор.")

if __name__ == "__main__":
    main()
