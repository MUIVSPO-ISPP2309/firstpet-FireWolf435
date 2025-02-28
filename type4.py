import time
import winsound
import threading
import tkinter as tk

class Timer:
    def __init__(self):
        self.time = 0
        self.running = False
        self.stopped = True
        self.root = tk.Tk()
        self.root.title("Таймер")
        self.label = tk.Label(self.root, text="Таймер: 00:00", font=('Helvetica', 24))
        self.label.pack()
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.set_button = tk.Button(self.root, text="Установить время", command=self.set_time)
        self.set_button.pack()
        self.start_button = tk.Button(self.root, text="Запустить", command=self.start)
        self.start_button.pack()
        self.stop_button = tk.Button(self.root, text="Остановить", command=self.stop)
        self.stop_button.pack()

    def set_time(self):
        self.time = int(self.entry.get())
        self.label['text'] = f"Таймер: {self.time // 60:02d}:{self.time % 60:02d}"

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
            self.label['text'] = f"Таймер: {mins:02d}:{secs:02d}"
            self.root.update()
            time.sleep(1)
            self.time -= 1
        if not self.stopped:
            self.label['text'] = "Время истекло!"
            winsound.Beep(2500, 1000)  # Звуковой сигнал
        self.running = False

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    timer = Timer()
    timer.run()
