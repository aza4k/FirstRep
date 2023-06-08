import tkinter 
class App(tkinter.Tk):

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.title('Calculator')
		self.geometry('400x600')
		self.config(bg='#ebeced')
		self.resizable(0,0)
	
		self.entry = tkinter.Entry(self,
		font='sans-serif 60',
        foreground='#7e7d87',
		width=9,
        
		)
		self.entry.place(x=0,y=0)





		# ----------------------------
		self.btnall = tkinter.Button(self,
        text='C',
        font='sans-serif 40',
        width=9,
        height=1,
        command=self.clear
        )
		self.btnall.place(x=0,y=92)

		self.btnx = tkinter.Button(self,
        text='X',
        font='sans-serif 44',
        width=3,
        height=1,
        command=self.xbtn)
		self.btnx.place(x=287,y=92)


# --------------------------------
		self.btn_7 = self.btns1('7')
		self.btn_7.place(x=0,y=195)


		self.btn_8 = self.btns1('8')
		self.btn_8.place(x=100,y=195)
#        ).place(x=100,y=195)
		self.btn_9 = self.btns1('9')
		self.btn_9.place(x=200,y=195)
#        height=1).place(x=200,y=195)
		

		
		self.btn_4 = self.btns1('4')
		self.btn_4.place(x=0,y=298)
#        height=1).place(x=0,y=298)
		self.btn_5 = self.btns1('5')
		self.btn_5.place(x=100,y=298)
#        ).place(x=100,y=298)
		
		self.btn_6 = self.btns1('6')
		self.btn_6.place(x=200,y=298)
#        height=1).place(x=200,y=298)

		



		self.btn_1 = self.btns1('1')
		self.btn_1.place(x=0,y=401)
#        height=1).place(x=0,y=401)

		self.btn_2 = self.btns1('2')
		self.btn_2.place(x=100,y=401)
#        height=1).place(x=100,y=401)

		self.btn_3 = self.btns1('3')
		self.btn_3.place(x=200,y=401)
#        height=1).place(x=200,y=401)



		self.btn_0 = self.btns1('0')
		self.btn_0.place(x=0,y=503)
        #command=lambda :self.to_entry(text)
#        ).place(x=0,y=503)

		self.btn = tkinter.Button(self,
        text='.',
        font='sans-serif 40',
        activebackground='white',
        activeforeground='#7e7d87',

        width=3,
        height=1)
		self.btn.place(x=100,y=503)

		self.btn_ten = tkinter.Button(self,
        text='=',
        font='sans-serif 40',
        foreground='#fff',
        background='#ff5467',
        activebackground='#fff',
        activeforeground='#ff5467',
        width=3,
        height=1)
		self.btn_ten.place(x=200,y=503)

		self.btn_plus = self.qosiw('+')
		self.btn_plus.place(x=300,y=195)

		self.btn_boliw = self.boliw('/')
		self.btn_boliw.place(x=300,y=401)

		self.btn_kobeytiw = self.kobeytiw('*')
		self.btn_kobeytiw.place(x=300,y=503)

		self.btn_minus =self.aliw('-')
		self.btn_minus.place(x=300,y=298)

		# 	#command=lambda :self.to_entry(numbers)



	def btns1(self,sanlar):
		return tkinter.Button(
		text=sanlar,
		font='sans-serif 40',
		activebackground='white',
		activeforeground='#7e7d87',
		width=3,
		height=1,
		command=lambda : self.to_entry(sanlar)
        )
	def boliw(self,sanlar):
		return tkinter.Button(
        text=sanlar,
        font='sans-serif 40',
        activebackground='white',
        activeforeground='#7e7d87',
        width=3,
        height=1,
		command=lambda : self.to_entry(sanlar)
        )

	def qosiw(self,sanlar):
		return tkinter.Button(
		text='+',
        font='sans-serif 40',
        activebackground='white',
        activeforeground='#7e7d87',
        width=3,
        height=1,
		command=lambda : self.to_entry(sanlar)
        )

	def aliw(self,sanlar):
		return tkinter.Button(
		text='-',
        font='sans-serif 40',
        activebackground='white',
        activeforeground='#7e7d87',
        width=3,
        height=1,
		command=lambda : self.to_entry(sanlar)

        )

	def kobeytiw(self,sanlar):
		return tkinter.Button(
		text='*',
        font='sans-serif 40',
        activebackground='white',
        activeforeground='#7e7d87',
        width=3,
        height=1,
		command=lambda : self.to_entry(sanlar)

        )

	def to_entry(self,symbol):
		value = self.entry.get()+symbol
		self.entry.delete(0,tkinter.END)
		self.entry.insert(0,value)

	def clear(self):
		self.entry.delete(0,tkinter.END)

	def xbtn(self):
		x = self.entry.get()
		x = list(x)
		x.pop(-1)
		y = ''.join(x)
		self.entry.delete(0,tkinter.END)
		self.entry.insert(0,y)
		
	


if __name__ == '__main__':
	window = App()
	window.mainloop()
