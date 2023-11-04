import tkinter as tk                        #importo la libreria de GUI
from tkinter import ttk                     #importo la nueva libreria ttk     

#######################CREACION DE LA VENTANA PRINCIPAL Y ESTILO DE LA VENTANA##################

raiz = tk.Tk()                              #creo una interfaz grafica de usuario
raiz.title("Notas v0.01")                   #especifico el titulo de la ventana
raiz.geometry('300x300+50+50')              #geometria de la ventana y margen con la pantalla
raiz.attributes("-topmost",True)            #siempre encima del resto de las ventanas
raiz.attributes("-alpha",0.9)               #añado un efecto de transparencia
raiz.resizable(0,0)                         #impido que el usuario pueda redimensionar la ventana
estilo = ttk.Style()                        #añado soporte para estilos
estilo.theme_use('default')                 #selecciono el estilo clasico de aplicaciones

#########################AÑADIMOS WIDGETS A LA VENTANA############################

version = tk.Label(raiz,text="Notas v0.01") #creamos un label
version.pack()                              #lo añadimos a la ventana

inputusuario = ttk.Entry(raiz)              #creo una entrada para que el usuario diga quien es
inputusuario.insert(0,'Introduce tu usuario')   #creo un texto de inicio en la entrada
inputusuario.pack(pady=20)                  #empaqueto la entrada

inputcontrasena = ttk.Entry(raiz)           #creo una entrada para que el usuario diga su contraseña
inputcontrasena.insert(0,'Introduce tu contraseña')   #creo un texto de inicio en la entrada
inputcontrasena.pack(pady=20)               #empaqueto la entrada

inputemail = ttk.Entry(raiz)                #creo una entrada para que el usuario diga su email
inputemail.insert(0,'Introduce tu email')   #creo un texto de inicio en la entrada
inputemail.pack(pady=20)                    #empaqueto la entrada

botonlogin = ttk.Button(raiz,text="Enviar") #creo el boton de iniciar sesion
botonlogin.pack(pady=10,expand=True)        #lo empaqueto

#########################INTENTO INTRODUCIR ANTIALIAS EN WINDOWS Y LANZO EL BUCLE###############

try:                                        #intento ejecutar
    from ctypes import windll               #importo la libreria especifica de GUI de Windows
    windll.shcore.SetProcessDpiAwareness(1) #activo el antialias para texto etc dentro de las interfaces
except Exception as e:                      #atrapo la excepcion en caso de que se produzca
    print(e)                                #saco la excepcion por pantalla
finally:                                    #en todo caso:    
    raiz.mainloop()                         #detiene la ejecucion y previene que la ventana se cierre
