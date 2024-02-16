import tkinter

class myGUI:
	def __init__(self):
		self.main_window = tkinter.Tk()
		self.top = tkinter.Frame(self.main_window)
		self.bottom = tkinter.Frame(self.main_window)

		self.label1 = tkinter.Label(self.top, text= "HELLO")
		self.label2 = tkinter.Label(self.top, text= "BITHCHES")
		self.label3 = tkinter.Label(self.bottom, text= "YOU")
		self.label4 = tkinter.Label(self.bottom, text= "ALL")
		self.label5 = tkinter.Label(self.bottom, text= "BITCHES")
		self.label1.pack()
    	self.label2.pack()

    	self.label3.pack()
    	self.label4.pack()
    	self.label5.pack()
    	self.top.pack()
		self.bottom.pack()

		tkinter.mainloop()


mygui = myGUI()