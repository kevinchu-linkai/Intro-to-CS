import tkinter
import tkinter.messagebox

class myGUI:
	def __init__(self):
		self.main_window = tkinter.Tk()
		self.top = tkinter.Frame(self.main_window)
		self.bottom = tkinter.Frame(self.main_window)
		self.label = tkinter.Label(self.top, text= "enter distance in km")
		self.entry = tkinter.Entry(self.top, width = 10)
		self.button = tkinter.Button(self.bottom, text= "convert", command= self.do)
		self.label.pack()
		self.entry.pack()
		self.button.pack()
		self.top.pack()
		self.bottom.pack()

		tkinter.mainloop()

	def do(self):
		km = int(self.entry.get())
		mile = km *0.6214
		tkinter.messagebox.showinfo("result", str(mile))

mygui = myGUI()