import tkinter as tk                        #importo la libreria de GUI
from tkinter import tkinter                 #importo la nueva libreria ttk     

raiz = tk.Tk()                              #creo una interfaz grafica de usuario
raiz.title("Notas v0.01")                   #especifico el titulo de la ventana
raiz.geometry('300x300+50+50')              #geometria de la ventana y margen con la pantalla
raiz.attributes("-topmost",True)            #siempre encima del resto de las ventanas
raiz.attributes("-alpha",0.9)               #añado un efecto de transparencia
raiz.resizable(0,0)                         #impido que el usuario pueda redimensionar la ventana


try:                                        #intento ejecutar
    from ctypes import windll               #importo la libreria especifica de GUI de Windows
    windll.shcore.SetProcessDpiAwareness(1) #activo el antialias para texto etc dentro de las interfaces
except Exception as e:                      #atrapo la excepcion en caso de que se produzca
    print(e)                                #saco la excepcion por pantalla
finally:                                    #en todo caso:    
    raiz.mainloop()                         #detiene la ejecucion y previene que la ventana se cierre
