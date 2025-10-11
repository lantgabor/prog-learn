import tkinter as tk

root = tk.Tk()
root.title("Tkinter Test")
root.resizable(False, False)
root.geometry("640x480")
label = tk.Label(root, text="Hello, Tkinter!")

label.place(x=100, y=80)

root.mainloop()