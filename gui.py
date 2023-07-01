import tkinter as tk

class SpeedTypingTestGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Speed Typing Test")
        self.root.configure(bg="#FFFAE8")  # Set light yellow background color

        self.create_widgets()

    def create_widgets(self):
        self.target_label = tk.Label(self.root, text="", font=("Helvetica", 18), wraplength=600)
        self.target_label.pack(pady=10)

        self.input_entry = tk.Entry(self.root, font=("Helvetica", 16), width=40)
        self.input_entry.pack(pady=10)
        self.input_entry.focus_set()

        self.timer_label = tk.Label(self.root, text="Time: 0.00s", font=("Helvetica", 14))
        self.timer_label.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Start", font=("Helvetica", 14))
        self.start_button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 18))
        self.result_label.pack(pady=10)

def run_gui():
    root = tk.Tk()
    root.geometry("700x400")
    app = SpeedTypingTestGUI(root)
    root.mainloop()
