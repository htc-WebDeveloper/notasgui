import tkinter as tk                        #importo la libreria de GUI

raiz = tk.Tk()                              #creo una interfaz grafica de usuario

try:                                        #intento ejecutar
    from ctypes import windll               #importo la libreria especifica de GUI de Windows
    windll.shcore.SetProcessDpiAwareness(1) #activo el antialias para texto etc dentro de las interfaces
except Exception as e:                      #atrapo la excepcion en caso de que se produzca
    print(e)                                #saco la excepcion por pantalla
finally:                                    #en todo caso:    
    raiz.mainloop()                         #detiene la ejecucion y previene que la ventana se cierre
