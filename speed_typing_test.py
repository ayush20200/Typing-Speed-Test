import tkinter as tk
import random
import time
from gui import SpeedTypingTestGUI


class SpeedTypingTest:
    def __init__(self, gui):
        self.gui = gui
        self.gui.start_button.config(command=self.start_test)

        self.target_text = "My name is mr.ayush sanjay dadwe, i am pursuing btech from sb jain institute of technology management and research nagpur."
        self.current_text = ""

        self.timer_running = False
        self.start_time = 0
        self.elapsed_time = 0

        self.gui.target_label.config(text=self.target_text)

    def start_test(self):
        if not self.timer_running:
            self.gui.input_entry.delete(0, tk.END)
            self.current_text = ""

            self.start_time = time.time()
            self.timer_running = True

            self.gui.start_button.config(text="Stop", command=self.stop_test)

            self.gui.root.after(10, self.update_timer)

    def stop_test(self):
        if self.timer_running:
            self.timer_running = False
            self.gui.start_button.config(text="Start", command=self.start_test)
            self.calculate_result()

    def update_timer(self):
        if self.timer_running:
            self.elapsed_time = time.time() - self.start_time
            self.gui.timer_label.config(text="Time: {:.2f}s".format(self.elapsed_time))
            self.gui.root.after(10, self.update_timer)

    def calculate_result(self):
        input_text = self.gui.input_entry.get()

        if input_text == self.target_text:
            accuracy = 100.0
        else:
            num_mistakes = sum(a != b for a, b in zip(input_text, self.target_text))
            accuracy = (len(input_text) - num_mistakes) / len(self.target_text) * 100.0

        wpm = len(self.target_text) / 5 / (self.elapsed_time / 60.0)

        result_text = "Accuracy: {:.2f}%   WPM: {:.2f}".format(accuracy, wpm)
        self.gui.result_label.config(text=result_text)


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("700x400")
    gui = SpeedTypingTestGUI(root)
    app = SpeedTypingTest(gui)
    root.mainloop()
