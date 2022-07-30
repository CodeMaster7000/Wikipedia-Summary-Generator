from tkinter import Tk, Frame, Toplevel, Entry, Button, Text, Scrollbar, END, INSERT
from tkinter.messagebox import showerror
from wikipedia import summary
def get_summary():
	try:
		answer.delete(1.0, END)
		answer.insert(INSERT, summary(keyword_entry.get()))
	except Exception as error:
		showerror("Error", error)
root = Tk()
root.title("Wikipedia Summarizer")
root.geometry("770x650")
root.resizable(False, False)
root.configure(bg="dark grey")
top_frame = Frame(root, bg="dark grey")
top_frame.pack(side="top", fill="x", padx=50, pady=10)
bottom_frame = Frame(root, bg="dark grey")
bottom_frame.pack(side="top", fill="x", padx=10, pady=10)
keyword_entry = Entry(top_frame, font=("Arial", 20, "bold"), width=25, bd=4)
keyword_entry.pack(side="left", ipady=6)
search_button = Button(top_frame, text="SEARCH", font=(
	"Arial", 18, "bold"), width=15, bd=4, command=get_summary)
search_button.pack(side="right")
scroll = Scrollbar(bottom_frame)
answer = Text(bottom_frame, font=("Calibri", 18), fg="red",
			width=55, height=20, bd=5, yscrollcommand=scroll.set)
answer.pack(side="left", fill="y")
scroll.pack(side="left", fill="y")
root.mainloop()
