from tkinter import *
from stack import *

class Aplicacion():
	pila = Stack()
	
	def insertar(self):
		dato = self.txt1.get()
		if dato != "":
			self.pila.push(dato)
			datos = StringVar()
			datos.set(self.pila)
			self.label2.config(textvariable=datos)
			#self.txt1.delete ( 0, len(dato))
	def extraer(self):
		self.pila.pop()
		datos = StringVar()
		datos.set(self.pila)
		self.label2.config(textvariable=datos)
	def __init__(self):
#crear la ventana
		self.root=Tk()
		self.root.title("Estructura de datos")
# definir el tamaño de la ventana
		#self.root.resizable(True, False)
		self.root.minsize(1200, 800)
		self.root.resizable(False,False)
		self.frame1 = Frame(self.root, width = 595, height = 795)
		self.frame1.config(bg = "blue")
		self.frame1.pack()
		self.label1 = Label(self.frame1, text = "Etiqueta1")
		self.label1.grid(row =0,column =0)
		self.txt1 = Entry(self.frame1)
		self.txt1.grid(row =0, column =1,columnspan = 2)

		self.btn1 = Button(self.frame1, text = "push", command = self.insertar)
		self.btn1.grid (row=1 , column =1)

		self.btn2 = Button(self.frame1, text = "pop",command = self.extraer)
		self.btn2.grid(row =1 , column = 2)

		self.label2 = Label(self.frame1 , text = "")
		self.label2.grid (row=2 , column = 1)


		#self.btn1 = Button(self.frame1, text = "oprimir", command =self.agregar)
		#self.btn1.grid(row=2 , column =1)
		self.root.mainloop()

	def agregar(self):
		txtNuevo = StringVar()
		txtNuevo.set("Se oprimio el boton")
		self.label2.config(textvariable =txtNuevo)


def main():
	app = Aplicacion()
	return 0

if __name__ == '__main__' :
	main()

