import tkinter as tk                                                                #importo la libreria de GUI
from tkinter import ttk                                                             #importo la nueva libreria ttk
import sqlite3 as bd                                                                #importo la libreria SQLite
from tkinter.colorchooser import askcolor                                           #importo el selector de color
import time

class Nota:                                                                         #Declaramos una clase
    def __init__(self,identificador,texto,color,fecha):                                           #Metodo constructor
        self.identificador = identificador
        self.texto = texto                                                          #Creo una propiedad texto
        self.color = color                                                          #Creo una propiedad color
        self.fecha = fecha                                                          #Creo una propiedad fecha


####################################CONEXION INICIAL CON LA BASE DE DATOS##########################

conexion = bd.connect("notas.sqlite")                                               #Indico el nombre de la base de datos
cursor = conexion.cursor()                                                          #Creo un cursor
#Sobre el cursor, ejecuto una peticón para crear una tabla en la base de datos en el caso de que no exista
cursor.execute("""
    CREATE TABLE IF NOT EXISTS 'notas'(
        'id' INTEGER,
        'texto' TEXT,
        'color' TEXT,
        'fecha' TEXT,
        PRIMARY KEY('id' AUTOINCREMENT)
    );
""")
#Sobre el cursor ejecuto una petición para crear una tabla de usuarios en el caso de que no exista
cursor.execute("""
    CREATE TABLE IF NOT EXISTS 'usuarios'(
        'id' INTEGER,
        'usuario' TEXT,
        'password' TEXT,
        'correo' TEXT,
        PRIMARY KEY('id' AUTOINCREMENT)
    );
""")


#####################DECLARO FUNCIONES PARA EL PROGRAMA#############################

def login():                                                                        #función de inicio de sesion
    print("vamos a iniciar sesion")                                                 #imprime en pantalla
    print("El nombre de usuario es "+usuario.get())
    print("La contraseña es "+password.get())
    print("El correo del usuario es "+correo.get())
    #Voy a comprobar si existe un usuario en la base de datos
    cursor = conexion.cursor() 
    cursor.execute('SELECT * FROM usuarios')                                        #Ejecuto una petición para seleccionar usuarios
    datos = cursor.fetchall()                                                       #cargo los datos
    numerousuarios = 0                                                              #creo una varible contador
    for i in datos:                                                                 #para cada uno de los registros
        numerousuarios = numerousuarios + 1                                         #le sumo valor al contador
    if(numerousuarios == 0):                                                        #si no hay usuarios
        print("No hay usuarios en la base de datos")
        cursor.execute("INSERT INTO usuarios VALUES(NULL,'"+usuario.get()+"','"+password.get()+"','"+correo.get()+"');") #Inserto una a una las notas en la base de datos
        conexion.commit()                                                           #ejecuto la insercion
    else:                                                                           #si hay usuarios
        #cursor.execute("INSERT INTO usuarios VALUES(NULL,'"+usuario.get()+"','"+password.get()+"','"+correo.get()+"');") #Inserto una a una las notas en la base de datos
        #conexion.commit()
        print("Actualmente en la base de datos hay esta cantidad de usuarios "+str(numerousuarios))
        cursor.execute('SELECT * FROM usuarios WHERE usuario = "'+usuario.get()+'" AND contrasena = "'+password.get()+'" AND email = "'+correo.get()+'"')
        
        existe = False
        existe = True   #FUERZO PARA NO TENER QUE VALIDAR DURANTE EL RESARROLLO
        datos = cursor.fetchall()                                                   #cargo los datos
        for i in datos:                                                             #para cada uno de los registros
            existe = True                                                           #actualizo el valor
        if existe == True:                                                          #si existe
            print("el usuario introducido es correcto")
            marco.destroy()                                                          #cierra la secundaria y me quedo con la principal
            marco2 = ttk.Frame(raiz)                                                #creo un nuevo marco
            marco2.pack()                                                           #empaqueto
            iconoaplicacion = tk.PhotoImage(file="icono.png")                       #cargo la imagen
            etiquetaicono = ttk.Label(marco2,text="Notas v0.01",image=iconoaplicacion,compound=tk.TOP,font=("sans-serif",14))   #muestro la imagen en el label
            etiquetaicono.image = iconoaplicacion                                   #especifico de nuevo la imagen
            etiquetaicono.pack()                                                    #empaqueto
            botonnuevanota = ttk.Button(marco2,text="Nueva nota",command=crearNota)          #creo el boton de iniciar sesion
            botonnuevanota.pack(pady=10,expand=True)                                    #lo empaqueto
        
        else:                                                                       #si no existe
            print("el usuario no es correcto")
            raiz.after(3000,lambda:raiz.destroy())                                  #cierra la ventana

def crearNota():
    global notas                                                                    #traigo la variable global notas
    global identificador                                                            #traigo la variable global identificador
    fecha = str(int(time.time()))                                                   #saco la fecha actual
    
    notas.append(Nota(identificador,'','',fecha))                                   #añado la nota a la lista
    
    for i in notas:                                                                 #Para cada una de las notas
        print(i.identificador)                                                      #imprimo el identificador
        print(i.texto)                                                              #Imprimo su contenido
        print(i.color)                                                              #Imprimo su color
        print(i.fecha)                                                              #Imprimo su fecha
   
    
    ventananuevanota = tk.Toplevel()                                                #nueva ventana flotante
    anchura = 400                                                                   #defino anchura
    altura = 500                                                                    #defino altura
    ventananuevanota.geometry(str(anchura)+'x'+str(altura)+'+100+100')              #geometria de la ventana y margen con la pantalla
    ventananuevanota.iconbitmap("icono.ico")                                        #icono de la ventana
    texto = tk.Text(ventananuevanota,bg="white")
    texto.pack()
    identificadorpropio = identificador
    selectorcolor = ttk.Button(ventananuevanota,text="Cambiar color",command=lambda:cambiaColor(ventananuevanota,texto,identificadorpropio))
    selectorcolor.pack()
    identificador = identificador + 1                                               #subo el identificador

def cambiaColor(ventana,texto,identificador):                                       #creo la funcion de cambio de color
    nuevocolor = askcolor(title="Selecciona un color")                              #saco un selector de color
    ventana.configure(bg = nuevocolor[1])                                           #cambio el color de fondo a la ventana a la ventana seleccionada
    texto.configure(bg = nuevocolor[1])                                             #cambio el color del cuadro de texto de la nota
    notas[identificador].color = nuevocolor[1]
    print("El identificador es "+str(identificador))
    for i in notas:                                                                 #Para cada una de las notas
        print(i.identificador)                                                      #imprimo el identificador
        print(i.texto)                                                              #Imprimo su contenido
        print(i.color)                                                              #Imprimo su color
        print(i.fecha)                                                              #Imprimo su fecha

#######################CREACION DE LA VENTANA PRINCIPAL Y ESTILO DE LA VENTANA##################

raiz = tk.Tk()                                                                      #creo una interfaz grafica de usuario
raiz.title("Notas v0.01")                                                           #especifico el titulo de la ventana
raiz.geometry('350x300+50+50')                                                      #geometria de la ventana y margen con la pantalla
raiz.attributes("-topmost",True)                                                    #siempre encima del resto de las ventanas
raiz.attributes("-alpha",0.9)                                                       #añado un efecto de transparencia
raiz.resizable(0,0)                                                                 #impido que el usuario pueda redimensionar la ventana
estilo = ttk.Style()                                                                #añado soporte para estilos
estilo.theme_use('default')                                                         #selecciono el estilo clasico de aplicaciones
raiz.iconbitmap("icono.ico")                                                        #icono de la ventana
    
####################DECLARO VARIABLES GLOBALES DEL PROGRAMA#############################

usuario = tk.StringVar()                                                            #variable para almacenar el usuario
password = tk.StringVar()                                                           #variable para almacenar la contraseña
correo = tk.StringVar()                                                             #variable para almacenar el correo
notas = []                                                                          #creo una lista vacia
identificador = 0                                                                   #inicializo un identificador

#########################AÑADIMOS WIDGETS A LA VENTANA############################

marco = ttk.Frame(raiz)
marco.pack()

version = tk.Label(marco,text="Notas v0.01")                                         #creamos un label
version.pack()                                                                      #lo añadimos a la ventana

inputusuario = ttk.Entry(marco,textvariable = usuario)                               #creo una entrada para que el usuario diga quien es
inputusuario.insert(0,'Introduce tu usuario')                                       #creo un texto de inicio en la entrada
inputusuario.pack(pady=20)                                                          #empaqueto la entrada

inputcontrasena = ttk.Entry(marco,textvariable = password)                           #creo una entrada para que el usuario diga su contraseña
inputcontrasena.insert(0,'Introduce tu contraseña')                                 #creo un texto de inicio en la entrada
inputcontrasena.pack(pady=20)                                                       #empaqueto la entrada

inputemail = ttk.Entry(marco,textvariable = correo)                                  #creo una entrada para que el usuario diga su email
inputemail.insert(0,'Introduce tu email')                                           #creo un texto de inicio en la entrada
inputemail.pack(pady=20)                                                            #empaqueto la entrada

botonlogin = ttk.Button(marco,text="Enviar",command=login)                           #creo el boton de iniciar sesion
botonlogin.pack(pady=10,expand=True)                                                #lo empaqueto

#########################INTENTO INTRODUCIR ANTIALIAS EN WINDOWS Y LANZO EL BUCLE###############

try:                                                                                #intento ejecutar
    from ctypes import windll                                                       #importo la libreria especifica de GUI de Windows
    windll.shcore.SetProcessDpiAwareness(1)                                         #activo el antialias para texto etc dentro de las interfaces
except Exception as e:                                                              #atrapo la excepcion en caso de que se produzca
    print(e)                                                                        #saco la excepcion por pantalla
finally:                                                                            #en todo caso:    
    raiz.mainloop()                                                                 #detiene la ejecucion y previene que la ventana se cierre







    
