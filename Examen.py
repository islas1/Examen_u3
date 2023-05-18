from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk 
import sqlite3
import pymysql
import random

def validacionC(valor):
    conexion = sqlite3.connect("Servicio2.db")
    pichula = conexion.execute("select * from clientes where nombre = ?", (valor, ))
    valid = False
    # El método fechone de la clase Cursor retorna una tupla con la fila de la tabla que coincide con el código ingresado o retorna 'None':
    fila= pichula.fetchone()
    if fila == None :
        messagebox.showerror("Dato erroneo","No hay cita registrada a ese nombre")
        return valid
    else:
         valid= True
         return valid
    
conexion = sqlite3.connect("vet.db")

def validacionB(valor):
    pichula = conexion.execute("select nombre from admins where nombre = ?", (valor, ))
    valid = False
    # El método fechone de la clase Cursor retorna una tupla con la fila de la tabla que coincide con el código ingresado o retorna 'None':
    fila= pichula.fetchone()
    if fila == None :
        messagebox.showerror("Dato erroneo","no se encontro un perfil asociado a ese nombre ")
        return valid
    else:
         valid= True
         return valid

def validacion(valor):
    pichula = conexion.execute("select nombre from admins where nombre = ?", (valor, ))
    valid = False
    # El método fechone de la clase Cursor retorna una tupla con la fila de la tabla que coincide con el código ingresado o retorna 'None':
    fila= pichula.fetchone()
    if fila == None :
        messagebox.showerror("Dato erroneo","no se encontro un perfil asociado a ese nombre ")
        return valid
    else:
         messagebox.showinfo("CONEXION","Se accedio a su perfil con exito")
         valid= True
         return valid
    
def validacion2(valor):
    valid = False
    pichula = conexion.execute("select contraseña from admins where contraseña = ?", (valor, ))
    # El método fechone de la clase Cursor retorna una tupla con la fila de la tabla que coincide con el código ingresado o retorna 'None':
    fila= pichula.fetchone()
    if fila == None :
        messagebox.showerror("Dato erroneo","La contraseña ingresada no es válido")
    else:
         valid= True
         return valid

def limit_nombre(x):
	if len(x.get()) > 0:
		x.set(x.get()[:30])
		
def limit_contra(y):
	if len(y.get()) > 0:
		y.set(y.get()[:30])
		
def limit_puesto(z):
	if len(z.get()) > 0:
		z.set(z.get()[:30])

def conectar2():
    conexion=sqlite3.connect("vet.db")
    conexion.execute("""create table if not exists admins(
                    id integer primary key AUTOINCREMENT,
                    nombre varchar,
                    contraseña varchar,
                    cargo varchar
                    )""")
    conexion.close()
#se crea la base de datos
def conectar_db():
    conexion = sqlite3.connect("Servicio2.db")
    conexion.execute("""
                create table if not exists clientes(
                    id integer primary key AUTOINCREMENT,
                    nombre varchar,
                    apellido varchar,
                    edad integer,
                    correo varchar,
                    contraseña varchar
                    direccion varchar,
                    raza varchar,
                    masc varchar,
                    ubi varchar,
                    servi varchar)
                    """)
    conexion.close()
#Funcion para la ventana de eleccion del usuario
def eleccion_usuario():
    ventana1 = tk.Tk()
    ventana1.configure(bg="beige")
    ventana1.resizable(width=False,height=False)
    #ventana1.iconbitmap("pet.ico")
    ventana1.title("Login cliente",)
    ventana1.configure(padx=100)
    mi_label5 = tk.Label(ventana1,
                        text="  Bienvenido a Pet World  ",
                        bg="beige",font=("Bahnschrift",15))
    mi_label5.pack()

    mi_label6 = tk.Label(ventana1,
                        text=""" El objetivo principal de Pet World es brindar una atención médica
    de calidad y un servicio excepcional a las mascotas y sus dueños,
    nos esforzamos por crear un ambiente tranquilo y relajado para que
    las mascotas se sientan seguras y cómodas durante su visita  """,
                        bg="beige")
    mi_label6.pack()
    mi_label7 = tk.Label(ventana1,
                        text="""Pet World ofrece un servicio estetico de primera el cual incluye:
    baño y secado, corte de pelo, corte de garras, peinado y perfumado,
    etc, tambien ofrecemos un servicio medico muy completo
    como exámenes de salud regulares, vacunas, cirugía, análisis de laboratorio, 
    radiografías, pruebas de diagnóstico y tratamientos especializados para
    una amplia variedad de enfermedades y dolencias.  """,
                        bg="beige")
    mi_label7.pack()
    tk.Label(ventana1, text="  ", bg="beige",
          fg="black", width="20", height="1", font=("Bahnschrift", 15)).pack()
    mi_label8 = tk.Label(ventana1,
                        text="Registrar usuario",
                        bg="beige", font=("Bahnschrift", 15))
    mi_label8.pack()
    iniciar_Cliente = tk.Button(ventana1, text="Registrar", command=ubicaciones)
    iniciar_Cliente.pack(padx=40, pady=40)
    regresar = tk.Button(ventana1, text="Regresar", command=ventana1.destroy)
    regresar.pack(padx=40, pady=40)

conectar_db()

def tabla_admin():
    str_nameadmin = str(name.get())
    int_age = int(age.get())
    str_serv = str(serv.get())
    int_str_age = str(age.get())
    str_name = str(name.get())
    str_raza = str(raza.get())
    str_calle = str(calle.get())
    str_namemasc = str(namemasc.get())
    ventana24 = tk.Tk()
    ventana24.configure(bg="beige")
    ventana24.resizable(width=False, height=False)
    # ventana3.iconbitmap("pet.ico")
    ventana24.title("Ficha de cita", )
    ventana24.configure(padx=200)
    ventana24.configure(pady=50)
    marco = LabelFrame(ventana24, text="Datos de la cita agendada", font=("Comic Sans", 10, "bold"), bg="white")
    marco.config(bd=9, pady=9)
    marco.pack()
    # Crear la etiqueta y el campo de entrada de los datos
    persona = tk.Label(marco, text="______________________________________________________________________________________________________",
                          bg="white", font=("Comic Sans", 10, "bold"))
    persona.grid(row=0, column=0, padx=(10, 0))
    persona2 = tk.Label(marco,
                        text="Nombre""          ""          ""Nombre de la mascota""          ""Raza         ""          ""Servicio""                  ""          Ubicacion""    ",
                            bg="white", font=("Comic Sans", 10, "bold"))
    persona2.grid(row=1, column=0, padx=(10, 0))
    persona6 = tk.Label(marco,
                        text="-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",
                            bg="white", font=("Comic Sans", 10, "bold"))
    persona6.grid(row=2, column=0, padx=(10, 0))
    persona3 = tk.Label(marco,
                       text=         str_name+"          ""          "        "     "       +str_namemasc+"             "         +str_raza+     "                  "      +str_serv+ "                       "  +str_calle+ "    ",
                       bg="white", font=("Comic Sans", 10, "bold"))
    persona3.grid(row=3, column=0, padx=(10, 0))
    persona4 = tk.Label(marco,
                         text="                         ""        ""               ""      ""          ""          ""                    ""        ""                      ""  ",
                            bg="white", font=("Comic Sans", 10, "bold"))
    persona4.grid(row=4, column=0, padx=(10, 0))

    ventana24.mainloop()

def elec_serv():
    servx = str(serv.get())
    servicio1 = "corte de pelo"
    servicio2 = "Baño y secado"
    servicio3 = "corte de garras"
    servicio4 = "peinado y perfumado"
    servicio5 = "analisis"
    servicio6 = "esterilizacion"
    servicio7 = "interventiva"
    servicio8 = "vacunas"
    servicio9 = "radiografias"
    servicio10 = "prueba diagnostica"
    if servx != servicio1 and servx != servicio2 and servx != servicio3 and servx != servicio4 and servx != servicio5 and servx != servicio6 and servx != servicio7 and servx != servicio8 and servx != servicio9 and servx != servicio10:
            messagebox.showerror("Dato erroneo","El servicio ingresado no es válido")
    else:
        conexion = sqlite3.connect("Servicio2.db")
        db = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="Servicio2"
        )

        base = "INSERT INTO clientes (Nombre, Nombremasc, Ubi, Edad, Servicio, Raza) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(    
            name.get(), namemasc.get(), calle.get(), age.get(), serv.get(), raza.get())

        fcursor = db.cursor()
        consulta = "SELECT * FROM clientes"
        fcursor.execute(consulta)
        datos = fcursor.fetchall()
        print(datos)

        fcursor.execute(base)
        db.commit()
        db.close

        conexion = sqlite3.connect("Servicio2.db")
        "---------------------------------------------------------------------------------------------------------------------------------------"
        str_nameadmin = str(name.get())
        int_age = int(age.get())
        str_serv = str(serv.get())
        int_str_age = str(age.get())
        str_name = str(name.get())
        str_raza = str(raza.get())
        str_calle = str(calle.get())
        str_namemasc = str(namemasc.get())
        strbonito_namemasc = str_namemasc.replace("'","")
        conexion.execute("insert into clientes(nombre,edad,raza,masc,ubi,servi) values (?,?,?,?,?,?)", (name.get(), int_age, raza.get(), namemasc.get(),calle.get(),serv.get()))
        conexion.commit()
        conexion.close()
        ventana_nuevo.destroy()
        "----------------------------------------------------------"
        ventana4 = tk.Tk()
        ventana4.configure(bg="beige")
        ventana4.resizable(width=False, height=False)
        # ventana3.iconbitmap("pet.ico")
        ventana4.title("Ficha de cita", )
        ventana4.configure(padx=200)
        ventana4.configure(pady=50)
        marco = LabelFrame(ventana4, text="Datos de la cita agendada", font=("Comic Sans", 10, "bold"), bg="white")
        marco.config(bd=9, pady=9)
        marco.pack()
        # Crear la etiqueta y el campo de entrada de los datos
        persona = tk.Label(marco, text="______________________________________________________________________________________________________",
                           bg="white", font=("Comic Sans", 10, "bold"))
        persona.grid(row=0, column=0, padx=(10, 0))
        persona2 = tk.Label(marco,
                            text="Nombre""          ""          ""Nombre de la mascota""          ""Raza         ""          ""Servicio""                  ""          Ubicacion""    ",
                            bg="white", font=("Comic Sans", 10, "bold"))
        persona2.grid(row=1, column=0, padx=(10, 0))
        persona6 = tk.Label(marco,
                            text="-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",
                            bg="white", font=("Comic Sans", 10, "bold"))
        persona6.grid(row=2, column=0, padx=(10, 0))
        persona3 = tk.Label(marco,
                           text=         str_name+"          ""          "        "     "       +strbonito_namemasc+"             "         +str_raza+     "                  "      +str_serv+ "                       "  +str_calle+ "    ",
                           bg="white", font=("Comic Sans", 10, "bold"))
        persona3.grid(row=3, column=0, padx=(10, 0))
        persona4 = tk.Label(marco,
                            text="                         ""        ""               ""      ""          ""          ""                    ""        ""                      ""  ",
                            bg="white", font=("Comic Sans", 10, "bold"))
        persona4.grid(row=4, column=0, padx=(10, 0))

        global variable
        variable = str_nameadmin

        ventana4.mainloop()

def servicios():
    #creacion de la ventana de eleccion de servicio
    ventana10 = tk.Tk()
    ventana10.title("Eleccion de servicios")
    ventana10.geometry("500x400")
    ventana10.config(bg="beige")
    ventana10.resizable(width=False, height=False)

    tk.Label(ventana10, text="                   Servicios                  ", bg="navajo white",fg="black", width="50", height="2", font=("Bahnschrift", 15)).pack()
    tk.Label(ventana10, text="""Bienvenido a la pestaña de servicios,
    por favor de las siguientes opciones ingrese el servicio que desea para su mascota
    Respetando mayusculas y espacios""", bg="beige",fg="black", width="100", height="3", font=("Bahnschrift", 10)).pack()

    tk.Label(ventana10, text="""Servicio Estetico: 
         corte de pelo,  Baño y secado,
         corte de garras o  peinado y perfumado""", bg="beige",fg="black", width="100", height="4", font=("Bahnschrift", 10)).pack()

    tk.Label(ventana10, text="""Servicio Medico: 
         analisis,  esterilizacion,  interventiva 
         vacunas,  radiografias o  prueba diagnostica """, bg="beige",fg="black", width="100", height="4", font=("Bahnschrift", 10)).pack()

    # Crear campos de entrada
    marco2 = LabelFrame(ventana10, text="", font=("Comic Sans", 10, "bold"), bg="beige")
    marco2.config(bd=2,pady=5)
    marco2.pack()
    persona = tk.Label(marco2,text="", bg="beige", font=("Comic Sans", 10, "bold"))
    persona.grid(row=0, column=0, padx=(10, 0))
    servi_entry = tk.Entry(marco2)
    servi_entry.grid(row=0, column=1,sticky='s', padx=(0, 10), pady=(10, 0))
    iniciar_sesion = tk.Button(ventana10, text="Siguiente",command=elec_serv)
    iniciar_sesion.pack(padx=20, pady=20)
    salir = tk.Button(ventana10, text="Regresar", command=ventana10.destroy)
    salir.pack()

    global serv
    serv = servi_entry

    ventana10.mainloop()

def ubicaciones():
    def compro():
        callex = str(calle.get())
        calle1 = "C. 74 x 23 y 45"
        calle2 = "C. 32 x 96 y 98"
        calle3 = "C. 96 x 114 y 116"
        calle4 = "C. 14 x 18 y 20"
        calle5 = "C. 104 x 176 y 178"
        calle6 = "C. 77 x 56 y 58"
        if callex != calle1 and callex != calle2 and callex != calle3 and callex != calle4 and callex != calle5 and callex != calle6:
            messagebox.showerror("Dato erroneo","La direccion ingresada no es válida")
        else:
            conexion = sqlite3.connect("Servicio2.db")
            ventana3 = tk.Tk()
            ventana3.configure(bg="beige")
            ventana3.resizable(width=False, height=False)
            #ventana3.iconbitmap("pet.ico")
            ventana3.title("Registro",)
            ventana3.configure(padx=200)
            ventana3.configure(pady=50)
            marco = LabelFrame(ventana3, text="Datos Generales", font=("Comic Sans", 10, "bold"), bg="beige")
            marco.config(bd=2,pady=5)
            marco.pack()
            # Crear la etiqueta y el campo de entrada de los datos
            persona = tk.Label(marco,text="datos del ciente", bg="beige", font=("Comic Sans", 10, "bold"))
            persona.grid(row=0, column=0, padx=(10, 0))
            "---------------edad-------------"
            age_label = tk.Label(marco, text="Edad:", bg="beige", font=("Comic Sans", 10, "bold"))
            age_label.grid(row=1, column=0, padx=(10, 0))
            age_entry = tk.Entry(marco)
            age_entry.grid(row=1, column=1,sticky='s', padx=(0, 10), pady=(10, 0))
            "-------------nombre-------------"
            name_label = tk.Label(marco, text="Nombre  :", bg="beige", font=("Comic Sans", 10, "bold"))
            name_label.grid(row=2, column=0, padx=(10, 0))
            name_entry = tk.Entry(marco)
            name_entry.grid(row=2, column=1, sticky='s', padx=(0, 10), pady=(10, 0))
            "------------separacion--------------"
            mascota = tk.Label(marco, text="datos de la mascota", bg="beige", font=("Comic Sans", 10, "bold"))
            mascota.grid(row=4, column=0, padx=(10, 0))
            "-------------nombre_masc-------------"
            namemasc_label = tk.Label(marco, text="Nombre:", bg="beige", font=("Comic Sans", 10, "bold"))
            namemasc_label.grid(row=5, column=0, padx=(10, 0))
            namemasc_entry = tk.Entry(marco)
            namemasc_entry.grid(row=5, column=1,sticky='s', padx=(0, 10), pady=(10, 0))
            "---------------raza-------------"
            raza_label = tk.Label(marco, text="Raza:", bg="beige", font=("Comic Sans", 10, "bold"))
            raza_label.grid(row=6, column=0, padx=(10, 0))
            raza_entry = tk.Entry(marco)
            raza_entry.grid(row=6, column=1, sticky='s', padx=(0, 10), pady=(10, 0))
            "------------boton------------"
            submit_button = tk.Button(marco, text="Guardar e iniciar sesión", bg="Light cyan", command=servicios)
            submit_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10)
            submit_button2 = tk.Button(marco, text="Regresar", bg="Light cyan", command=ventana3.destroy)
            submit_button2.grid(row=9, column=0, columnspan=2, pady=10, padx=10)
            #creamos las variables globales

            global name
            name = name_entry
            global age
            age = age_entry
            global namemasc
            namemasc = namemasc_entry
            global raza
            raza = raza_entry
            global ventana_nuevo
            ventana_nuevo = ventana3

            ventana3.mainloop
            
    #creacion de la ventana de eleccion de servicio
    ventana5 = tk.Tk()
    ventana5.title("Selección de ubicación")
    ventana5.geometry("500x300")
    ventana5.resizable(width=False,height=False) 
    ventana5.config(bg="beige")

    tk.Label(ventana5, text="Por favor, escoja y escriba una ubicacion de las siguientes", bg="navajo white", fg="black", width="70", height="2", font=("Bahnschrift", 13)).pack()
    tk.Label(ventana5, text="C. 74 x 23 y 45  |  C. 32 x 96 y 98     |  C. 96 x 114 y 116 ", bg="navajo white", fg="black", width="50", height="0", font=("Bahnschrift", 8)).pack()
    tk.Label(ventana5, text="C. 14 x 18 y 20  |C. 104 x 176 y 178    |  C. 77 x 56 y 58   ", bg="navajo white", fg="black", width="50", height="0", font=("Bahnschrift", 8)).pack()

    mi_label4 = tk.Label(ventana5,
                        text="",
                        bg="beige")
    mi_label4.pack()
    marco2 = LabelFrame(ventana5, text="", font=("Comic Sans", 10, "bold"), bg="beige")
    marco2.config(bd=2,pady=5)
    marco2.pack()
    # Crear la etiqueta y el campo de entrada de los datos
    persona = tk.Label(marco2,text="", bg="beige", font=("Comic Sans", 10, "bold"))
    persona.grid(row=0, column=0, padx=(10, 0))
    calle_entry = tk.Entry(marco2)
    calle_entry.grid(row=1, column=1,sticky='s', padx=(0, 10), pady=(10, 0))
    #calle_entry = tk.Entry(ventana5)
    #calle_entry.ggrid(row=1, column=1, padx=(0, 10), pady=(10, 0))
    iniciar_sesion = tk.Button(ventana5, text="Siguiente",command=compro)
    iniciar_sesion.pack(padx=20, pady=20)
    salir = tk.Button(ventana5, text="Regresar", command=ventana5.destroy)
    salir.pack()
    
    global calle
    calle = calle_entry

    ventana5.mainloop()

def salirAplicacion():
	valor=messagebox.askquestion("Salir","¿Está seguro que desea salir de la Aplicación?")
	if valor=="yes":
		ventanaaa.destroy()

def mensaje():
	acerca='''
	Aplicación Veterinaria
	Perfil: Administrador
	Version 2.0
	Desarrolladores
	Jonathan Islas, Amanda chan
	'''
	messagebox.showinfo(title="INFORMACION", message=acerca)

def agregar():
    try:
        conexion=sqlite3.connect("vet.db")

        conexion.execute("""create table if not exists admins(
                    id integer primary key AUTOINCREMENT,
                    nombre varchar,
                    contraseña varchar,
                    cargo varchar
                    )""")
        conexion.close()
        messagebox.showinfo(":D","¡Registro exitoso!")
        validddd = True
    except :
        messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro, verifique conexión con BBDD")
    conexion=sqlite3.connect("vet.db")
    miCursor= conexion.cursor()

    miNombre_str = str(nombre_admin.get())
    miCargo_str = str(cargo_admin.get())
    miContra_str = str(contra_admin.get())
    miNombremin = miNombre_str.lower()
    miCargomin = miCargo_str.lower()
    miContramin = miContra_str.lower()
    try:
        for i in range(10): 
            num = random.randint(9999, 99999)
        datos=miNombremin,miCargomin,miContramin
        miCursor.execute("INSERT INTO admins (id,nombre,contraseña,cargo) VALUES(?,?,?,?)", (num,miNombremin,miContramin,miCargomin))
        conexion.commit()
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro, verifique su conexion con la base de datos")
        pass
    juga = conexion.execute("select * from admins where nombre = ?", (miNombremin, ))
    fila = juga.fetchone()

def update2():
    conexion=sqlite3.connect("vet.db")

    conexion.execute("""create table if not exists admins(
                id integer primary key AUTOINCREMENT,
                nombre varchar,
                contraseña varchar,
                cargo varchar
                )""")
    conexion.close()
    conexion=sqlite3.connect("vet.db")
    miCursor=conexion.cursor()
    myid = idact
    nombre_act2str = str(nombre_act2.get())
    contra_act2str = str(contra_act2.get())
    cargo_act2str = str(cargo_act2.get())
    nombre_act2min = nombre_act2str.lower()
    contra_act2min = contra_act2str.lower()
    cargo_act2min = cargo_act2str.lower()
    try :
        datos= nombre_act2min,cargo_act2min,contra_act2min
        miCursor.execute("UPDATE admins SET nombre=?, contraseña=?, cargo=? WHERE ID="+myid, (datos))
        conexion.commit()
        messagebox.showinfo("UPDATE","¡Los datos se actualizaron correctamente!")
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrió un error al actualizar los datos")
        pass
    juga = conexion.execute("select * from admins where nombre = ?", (nombre_act2min, ))
    fila = juga.fetchone()
    strfila = str(fila)
    filabonita = strfila.replace("(","")
    filabonita2 = filabonita.replace(")","")
    filabonita3 = filabonita2.replace(",","")
    filabonita4 = filabonita3.replace("'","")
    filabonita5 = filabonita4.replace(" ", "  ")

def eliminar3():
    conexion=sqlite3.connect("vet.db")
    miCursor=conexion.cursor()
    name4 = str(admin5.get())
    namemin = name4.lower()
    variable = str(validacionB(namemin))
    variablex = str(variable)
    if variable == False :
        messagebox.showerror("Dato erroneo"," no se encontro un perfil asociado a ese nombre ")
    elif variablex == "True":
        juga2 = conexion.execute("select id from admins where nombre = ?", (namemin, ))
        fila2 = juga2.fetchone()
        strfila2 = str(fila2)
        filabonitax = strfila2.replace("(","")
        filabonitax2 = filabonitax.replace(")","")
        filabonitax3 = filabonitax2.replace(",","")
        filabonitax4 = filabonitax3.replace("'","")
        filabonitax5 = filabonitax4.replace(" ", "  ")
        try:
            if messagebox.askyesno(message="¿Realmente desea eliminar el perfil?", title="ADVERTENCIA"):
                miCursor.execute("DELETE FROM admins WHERE ID="+filabonitax5)
                conexion.commit()
                messagebox.showinfo("DELETE","¡El perfil se elimino correctamente!")
        except :
            messagebox.showwarning("ADVERTENCIA","Ocurrió un error al tratar de eliminar el registro")
            pass        

def eliminar():
    def eliminar2():
        name4 = str(admin5.get())
        namemin = name4.lower()
        variable = str(validacion(namemin))
        variablex = str(variable)
        if variable == False :
            messagebox.showerror("Dato erroneo"," no se encontro un perfil asociado a ese nombre ")
        elif variablex == "True":
            ventanacomp5= tk.Tk()
            ventanacomp5.resizable(width=False, height=False)
            ventanacomp5.configure(background="beige")
            #ventanaadmi3.iconbitmap("pet.ico")
            ventanacomp5.title("eliminacion de perfil")
            ventanacomp5.geometry("500x300")
            tk.Label(ventanacomp5, text=""" si esta seguro de querer eliminar sus datos presione "Borrar", si no, presione "Cerrar" """, bg="beige",
                fg="black", width="80", height="5", font=("Bahnschrift", 8)).pack()
            b2=Button(ventanacomp5, text="Borrar", command=eliminar3)
            b2.place(x=120, y=200)
            b4=Button(ventanacomp5, text="Cerrar",bg="red",command=ventanacomp5.destroy)
            b4.place(x=330, y=200)
            
    ventanacomp2= tk.Tk()
    ventanacomp2.resizable(width=False, height=False)
    ventanacomp2.configure(background="beige")
    #ventanaadmi3.iconbitmap("pet.ico")
    ventanacomp2.title("comprobacion de datos")
    ventanacomp2.geometry("600x350")
    tk.Label(ventanacomp2, text=" Por favor ingrese su nombre de usuario ", bg="beige",
          fg="black", width="50", height="5", font=("Bahnschrift", 12)).pack()
    nombre_admin4 = tk.Entry(ventanacomp2)
    nombre_admin4.place(x=240,y=80)
    b1=Button(ventanacomp2, text="Verificar",command=eliminar2)
    b1.place(x=280, y=120)

    global admin5
    admin5 = nombre_admin4 

def comprobacion():
    def update():
        name4 = str(admin5.get())
        namemin = name4.lower()
        variable = str(validacion(namemin))
        variablex = str(variable)
        if variable == False :
            messagebox.showerror("Dato erroneo"," no se encontro un perfil asociado a ese nombre ")
        elif variablex == "True":
            ventanaup = tk.Tk()
            ventanaup.resizable(width=False, height=False)
            ventanaup.configure(background="beige")
            ventanaup.title("Update")
            ventanaup.geometry("600x350")
            juga = conexion.execute("select nombre from admins where nombre = ?", (namemin, ))
            juga2 = conexion.execute("select id from admins where nombre = ?", (namemin, ))
            juga3 = conexion.execute("select contraseña from admins where nombre = ?", (namemin, ))
            juga4 = conexion.execute("select cargo from admins where nombre = ?", (namemin, ))
            fila = juga.fetchone()
            fila2 = juga2.fetchone()
            fila3 = juga3.fetchone()
            fila4 = juga4.fetchone()
            strfila = str(fila)
            filabonita = strfila.replace("(","")
            filabonita2 = filabonita.replace(")","")
            filabonita3 = filabonita2.replace(",","")
            filabonita4 = filabonita3.replace("'","")
            filabonita5 = filabonita4.replace(" ", "  ")
            strfila2 = str(fila2)
            filabonitax = strfila2.replace("(","")
            filabonitax2 = filabonitax.replace(")","")
            filabonitax3 = filabonitax2.replace(",","")
            filabonitax4 = filabonitax3.replace("'","")
            filabonitax5 = filabonitax4.replace(" ", "  ")
            strfila3 = str(fila3)
            filabonitaxx = strfila3.replace("(","")
            filabonitaxx2 = filabonitaxx.replace(")","")
            filabonitaxx3 = filabonitaxx2.replace(",","")
            filabonitaxx4 = filabonitaxx3.replace("'","")
            filabonitaxx5 = filabonitaxx4.replace(" ", "  ")
            strfila4 = str(fila4)
            filabonitaxxx = strfila4.replace("(","")
            filabonitaxxx2 = filabonitaxxx.replace(")","")
            filabonitaxxx3 = filabonitaxxx2.replace(",","")
            filabonitaxxx4 = filabonitaxxx3.replace("'","")
            filabonitaxxx5 = filabonitaxxx4.replace(" ", "  ")
            nombre_valid =StringVar()
            cargo_valid =StringVar()
            contra_valid =StringVar()

            tk.Label(ventanaup,bg="peach puff", text="Sus datos actuales son: ").pack()
            tk.Label(ventanaup,bg="beige", text=" ID = "+filabonitax5+", NOMBRE = "+filabonita5+", CONTRASEÑA = "+filabonitaxx5+",  PUESTO = "+filabonitaxxx5).pack()
            tk.Label(ventanacomp, text=" ", bg="beige",
                fg="black", width="50", height="5", font=("Bahnschrift", 12)).pack()
            tk.Label(ventanaup,bg="beige", text="   ").pack()
            tk.Label(ventanaup,bg="peach puff", text="Ingrese sus nuevos datos").pack()
            
            l2=Label(ventanaup,bg="beige", text="Nombre")
            l2.place(x=50,y=100)
            nombre_act=Entry(ventanaup, textvariable=nombre_valid, width=20)
            nombre_act.place(x=100, y=100)

            l3=Label(ventanaup,bg="beige", text="Cargo")
            l3.place(x=50,y=150)
            cargo_act=Entry(ventanaup, textvariable=cargo_valid)
            cargo_act.place(x=100, y=150)

            l4=Label(ventanaup,bg="beige", text="Contraseña")
            l4.place(x=280,y=125)
            contra_act=Entry(ventanaup, textvariable=contra_valid, width=20)
            contra_act.place(x=350, y=125)

            b1=Button(ventanaup, text="Actualizar",command=update2)
            b1.place(x=250, y=200)

            global idact
            idact = filabonitax5
            global nombre_act2
            nombre_act2 = nombre_act
            global cargo_act2
            cargo_act2 = cargo_act
            global contra_act2
            contra_act2 = contra_act

            
        
    ventanacomp= tk.Tk()
    ventanacomp.resizable(width=False, height=False)
    ventanacomp.configure(background="beige")
    #ventanaadmi3.iconbitmap("pet.ico")
    ventanacomp.title("comprobacion de datos")
    ventanacomp.geometry("600x350")
    tk.Label(ventanacomp, text=" Por favor ingrese su nombre de usuario ", bg="beige",
          fg="black", width="50", height="5", font=("Bahnschrift", 12)).pack()
    nombre_admin4 = tk.Entry(ventanacomp)
    nombre_admin4.place(x=240,y=80)
    b1=Button(ventanacomp, text="Verificar",command=update)
    b1.place(x=280, y=120)

    global admin5
    admin5 = nombre_admin4   

def creacion_admin():
    ventanaadmin3 = tk.Tk()
    ventanaadmin3.resizable(width=False, height=False)
    ventanaadmin3.configure(background="beige")
    #ventanaadmi3.iconbitmap("pet.ico")
    ventanaadmin3.title("Login administrador prime")
    ventanaadmin3.geometry("600x350")
    # Menu
    menubar=Menu(ventanaadmin3,bg="paleturquoise")
    menubasedat=Menu(menubar,tearoff=0)
    menubasedat.add_command(label="Salir", command=salirAplicacion)
    menubar.add_cascade(label="Inicio", menu=menubasedat)

    ayudamenu=Menu(menubar,tearoff=0)
    ayudamenu.add_command(label="Acerca", command=mensaje)
    menubar.add_cascade(label="Ayuda",menu=ayudamenu)

    # widgets y entradas de texto
    nombre_entry = StringVar()
    contra_entry = StringVar()
    
    nombre_valid =StringVar()
    cargo_valid =StringVar()
    contra_valid =StringVar()

    l2=Label(ventanaadmin3,bg="beige", text="Nombre")
    l2.place(x=50,y=10)
    nombre_entry=Entry(ventanaadmin3, textvariable=nombre_valid, width=20)
    nombre_entry.place(x=100, y=10)

    l3=Label(ventanaadmin3,bg="beige", text="Cargo")
    l3.place(x=50,y=40)
    cargo_entry=Entry(ventanaadmin3, textvariable=cargo_valid)
    cargo_entry.place(x=100, y=40)

    l4=Label(ventanaadmin3,bg="beige", text="Contraseña")
    l4.place(x=280,y=25)
    contra_entry=Entry(ventanaadmin3, textvariable=contra_valid, width=20)
    contra_entry.place(x=350, y=25)
    
    nombre_valid.trace("w", lambda *args: limit_nombre(nombre_valid))
    contra_valid.trace("w", lambda *args: limit_contra(contra_valid))
    cargo_valid.trace("w", lambda *args: limit_puesto(cargo_valid))

    b1=Button(ventanaadmin3, text="Crear Registro",command=agregar)
    b1.place(x=250, y=90)
    b2=Button(ventanaadmin3, text="Modificar Registro", command=comprobacion)
    b2.place(x=120, y=200)
    b4=Button(ventanaadmin3, text="Eliminar Registro",bg="red",command=eliminar)
    b4.place(x=330, y=200)

    ventanaadmin3.config(menu=menubar)

    l5=Label(ventanaadmin3,bg="beige", text="¿Desea actualizar o eliminar su usuario? de ser asi seleccione uno.")
    l5.place(x=100,y=150)
    b5=Button(ventanaadmin3, text="Finalizar creacion de la cuenta",command=ventanaadmin3.destroy)
    b5.place(x=200, y=250)
    b6=Button(ventanaadmin3, text=" Iniciar sesion con mi cuenta ",command=login_admin)
    b6.place(x=200, y=290)

    #global tree
    #tree = tree2
    global nombre_admin
    nombre_admin = nombre_entry
    global contra_admin 
    contra_admin = contra_entry
    global cargo_admin
    cargo_admin = cargo_entry
    global ventanaaa
    ventanaaa = ventanaadmin3

def admin_al_cuadrado():
    ventanaadmin2 = tk.Tk()
    ventanaadmin2.resizable(width=False, height=False)
    ventanaadmin2.configure(background="beige")
    #ventanaadmin2.iconbitmap("pet.ico")
    ventanaadmin2.title("Login administrador prime")
    ventanaadmin2.configure(padx=165)
    ventanaadmin2.configure(pady=20)
    tk.Label(ventanaadmin2, text=" Seleccione un perfil ", bg="beige",
          fg="black", width="20", height="1", font=("Bahnschrift", 15)).pack()
    #tk.Label(ventanaadmin2, text=" ", bg="beige",
    #          fg="black", width="3", height="3", font=("Bahnschrift", 15)).pack()
    iniciar_usuario = tk.Button(ventanaadmin2, text="     INICIAR SESIÓN    ", command=login_admin)
    iniciar_usuario.pack(padx=20, pady=20)
    iniciar_usuario = tk.Button(ventanaadmin2, text="      CREAR CUENTA     ", command=creacion_admin)
    iniciar_usuario.pack(padx=20, pady=20)
    tk.Label(ventanaadmin2, text=" ", bg="beige",
              fg="black", width="3", height="3", font=("Bahnschrift", 3)).pack()


    # Botones
    salir = tk.Button(ventanaadmin2, text="  Regresar  ", command=ventanaadmin2.destroy)
    salir.pack()

def create_admin():
    conexion =sqlite3.connect("veterinaria.db")
    conexion.execute("""create table if not exists datos(
                    id integer primary key AUTOINCREMENT,
                    nombre varchar,
                    contraseña varchar
                    )""")
    conexion.close()
    ventanaadmin = tk.Tk()
    ventanaadmin.resizable(width=False, height=False)
    ventanaadmin.configure(background="beige")
    #ventana2.iconbitmap("pet.ico")
    ventanaadmin.title("Login administrador")
    ventanaadmin.configure(padx=165)
    ventanaadmin.configure(pady=20)
    mi_label3 = tk.Label(ventanaadmin,
                        text="Bienvenido a la ventana de creacion de tu cuenta ",
                        bg="beige")
    mi_label3.pack()
    tk.Label(ventanaadmin, text="  ", bg="beige",
          fg="black", width="20", height="1", font=("Bahnschrift", 15)).pack()
    mi_label4 = tk.Label(ventanaadmin,
                        text="Cree su usuario",
                        bg="beige")
    mi_label4.pack()
    nombre_usuario = tk.Entry(ventanaadmin)
    nombre_usuario.pack(pady=20)
    mi_label5 = tk.Label(ventanaadmin,
                        text="Cree su contraseña",
                        bg="beige")
    mi_label5.pack()
    contrasena_usuario = tk.Entry(ventanaadmin, show="*")
    contrasena_usuario.pack()


def login_admin():
    def comprobacion():
        def datos_finales():
            conexion=sqlite3.connect("Servicio2.db")
            miCursor=conexion.cursor()
            name4 = str(nommmm.get())
            namemin = name4.lower()
            variable = str(validacionC(name4))
            variable22 = str(variable)
            if variable == False :
                messagebox.showerror("Dato erroneo","No hay cita registrada a ese nombre")
            elif variable22 == "True" :
                ventana111 = tk.Tk()
                ventana111.configure(bg="beige")
                ventana111.resizable(width=False,height=False)
                #ventana1.iconbitmap("pet.ico")
                ventana111.title("Login cliente",)
                ventana111.geometry("600x350")
                juga = conexion.execute("select nombre from clientes where nombre = ?", (name4, ))
                juga2 = conexion.execute("select edad from clientes where nombre = ?", (name4, ))
                juga3 = conexion.execute("select masc from clientes where nombre = ?", (name4, ))
                juga4 = conexion.execute("select raza from clientes where nombre = ?", (name4, ))
                juga5 = conexion.execute("select ubi from clientes where nombre = ?", (name4, ))
                juga6 = conexion.execute("select servi from clientes where nombre = ?", (name4, ))
                fila = juga.fetchall()
                fila2 = juga2.fetchall()
                fila3 = juga3.fetchall()
                fila4 = juga4.fetchall()
                fila5 = juga5.fetchall()
                fila6 = juga6.fetchall()
                strfila = str(fila)
                strfila2 = str(fila2)
                strfila3 = str(fila3)
                strfila4 = str(fila4)
                strfila5 = str(fila5)
                strfila6 = str(fila6)
                filabonita = strfila.replace("(","")
                filabonita2 = filabonita.replace(")","")
                filabonita3 = filabonita2.replace("]","")
                filabonita4 = filabonita3.replace("'","")
                filabonita5 = filabonita4.replace(" ", "  ")
                filabonita6 = filabonita5.replace("[", "  ")
                filabonita7 = filabonita6.replace(",", "  ")    #nombre
                filabonitax = strfila2.replace("(","")
                filabonitax2 = filabonitax.replace(")","")
                filabonitax3 = filabonitax2.replace("]","")
                filabonitax4 = filabonitax3.replace("'","")
                filabonitax5 = filabonitax4.replace(" ", "  ")
                filabonitax6 = filabonitax5.replace("[", "  ")
                filabonitax7 = filabonitax6.replace(",", "  ")    #edad
                filabonitaxx = strfila3.replace("(","")
                filabonitaxx2 = filabonitaxx.replace(")","")
                filabonitaxx3 = filabonitaxx2.replace("]","")
                filabonitaxx4 = filabonitaxx3.replace("'","")
                filabonitaxx5 = filabonitaxx4.replace(" ", "  ")
                filabonitaxx6 = filabonitaxx5.replace("[", "  ")
                filabonitaxx7 = filabonitaxx6.replace(",", "  ")    #masc
                filabonitaxxx = strfila4.replace("(","")
                filabonitaxxx2 = filabonitaxxx.replace(")","")
                filabonitaxxx3 = filabonitaxxx2.replace("]","")
                filabonitaxxx4 = filabonitaxxx3.replace("'","")
                filabonitaxxx5 = filabonitaxxx4.replace(" ", "  ")
                filabonitaxxx6 = filabonitaxxx5.replace("[", "  ")
                filabonitaxxx7 = filabonitaxxx6.replace(",", "  ")    #raza
                filabonitaxxxx = strfila5.replace("(","")
                filabonitaxxxx2 = filabonitaxxxx.replace(")","")
                filabonitaxxxx3 = filabonitaxxxx2.replace("]","")
                filabonitaxxxx4 = filabonitaxxxx3.replace("'","")
                filabonitaxxxx5 = filabonitaxxxx4.replace(" ", "  ")
                filabonitaxxxx6 = filabonitaxxxx5.replace("[", "  ")
                filabonitaxxxx7 = filabonitaxxxx6.replace(",", "  ")    #ubi
                filabonitaxxxxx = strfila6.replace("(","")
                filabonitaxxxxx2 = filabonitaxxxxx.replace(")","")
                filabonitaxxxxx3 = filabonitaxxxxx2.replace("]","")
                filabonitaxxxxx4 = filabonitaxxxxx3.replace("'","")
                filabonitaxxxxx5 = filabonitaxxxxx4.replace(" ", "  ")
                filabonitaxxxxx6 = filabonitaxxxxx5.replace("[", "  ")
                filabonitaxxxxx7 = filabonitaxxxxx6.replace(",", "  ")    #ubi
                mi_label3 = tk.Label(ventana111,
                        text="  Datos de la  cita agendada ",
                        bg="beige")
                mi_label3.pack()
                mi_label4 = tk.Label(ventana111,
                        text="  ",
                        bg="beige")
                mi_label4.pack()
                mi_label4 = tk.Label(ventana111,
                        text="Nombre: "+filabonita7+", Edad: "+filabonitax7+", Nombre de la mascota: "+filabonitaxx7,
                        bg="beige")
                mi_label4.pack()
                mi_label4 = tk.Label(ventana111,
                        text="Tipo de animal: "+filabonitaxxx7+", Ubicacion: "+filabonitaxxxx7+", Servicio: "+filabonitaxxxxx7,
                        bg="beige")
                mi_label4.pack()

        conexion=sqlite3.connect("Servicio2.db")
        miCursor=conexion.cursor()
        name4 = str(nombre_admin2.get())
        contra4 = str(contra_admin2.get())
        namemin = name4.lower()
        contramin = contra4.lower()
        variable = str(validacion(namemin))
        variablex = str(validacion2(contramin))
        variable22 = str(variable)
        variablexx = str(variablex)
        if variable == False :
            messagebox.showerror("Dato erroneo","Alguno de los datos no es correcto")
        elif variable22 == "True" and variablexx == "True" :
            ventana111 = tk.Tk()
            ventana111.configure(bg="beige")
            ventana111.resizable(width=False,height=False)
            #ventana1.iconbitmap("pet.ico")
            ventana111.title("Login cliente",)
            ventana111.geometry("600x350")
            mi_label3 = tk.Label(ventana111,
                        text="  Personas con cita agendada ",
                        bg="beige")
            mi_label3.pack()
            juga = conexion.execute("select nombre from clientes ")
            fila = juga.fetchall()
            strfila = str(fila)
            filabonita = strfila.replace("(","")
            filabonita2 = filabonita.replace(")","")
            filabonita3 = filabonita2.replace("]","")
            filabonita4 = filabonita3.replace("'","")
            filabonita5 = filabonita4.replace(" ", "  ")
            filabonita6 = filabonita5.replace("[", "  ")
            filabonita7 = filabonita6.replace(",", "  ")
            mi_label3 = tk.Label(ventana111,
                        text=filabonita7,
                        bg="beige")
            mi_label3.pack()
            mi_label3 = tk.Label(ventana111,
                        text="   ",
                        bg="beige")
            mi_label3.pack()
            mi_label3 = tk.Label(ventana111,
                        text=" Ingrese un nombre para ver su cita agendada ",
                        bg="beige")
            mi_label3.pack()
            nombre_entry=Entry(ventana111, width=20)
            nombre_entry.place(x=220, y=150)
            b5=Button(ventana111, text="Buscar cita",command=datos_finales)
            b5.place(x=220, y=250)
            global nommmm
            nommmm = nombre_entry

    #se crea la ventana donde el admin ingresa sus datos
    ventana2 = tk.Tk()
    ventana2.resizable(width=False, height=False)
    ventana2.configure(background="beige")
    #ventana2.iconbitmap("pet.ico")
    ventana2.title("Login administrador")
    ventana2.geometry("600x350")
    entry_text = StringVar() 

    # Entrada para la contraseña
    mi_label3 = tk.Label(ventana2,
                        text="  BIENVENIDO ADMINISTRADOR  ",
                        bg="beige")
    mi_label3.pack()
    tk.Label(ventana2, text="  ", bg="beige",
          fg="black", width="20", height="1", font=("Bahnschrift", 15)).pack()
    l2=Label(ventana2,bg="beige", text="Nombre")
    l2.place(x=50,y=40)
    nombre_entry=Entry(ventana2, width=20)
    nombre_entry.place(x=100, y=40)
    l4=Label(ventana2,bg="beige", text="Contraseña")
    l4.place(x=280,y=40)
    contra_entry=Entry(ventana2, show="*", width=20)
    contra_entry.place(x=350, y=40)
    # Botones
    iniciar_sesion = tk.Button(ventana2, text="Iniciar sesión", command=comprobacion)
    iniciar_sesion.pack(padx=40, pady=40)
    salir = tk.Button(ventana2, text="Regresar", command=ventana2.destroy)
    salir.pack()

    global nombre_admin2
    nombre_admin2 = nombre_entry
    global contra_admin2 
    contra_admin2 = contra_entry

    # Widgets
    resultado = tk.Label(ventana2, text="")
    resultado.pack(pady=90)
    ventana2.mainloop()

#ventana de elección de usuario
ventana = Tk()
ventana.configure(bg="beige")
ventana.resizable(width=False, height=False)
#ventana.iconbitmap("pet.ico")
ventana.title("Elección de usuario",)
ventana.configure(padx=200)
tk.Label(ventana, text=" Seleccione un perfil ", bg="beige",
          fg="black", width="20", height="1", font=("Bahnschrift", 15)).pack()
tk.Label(ventana, text=" ", bg="beige",
          fg="black", width="3", height="3", font=("Bahnschrift", 15)).pack()
iniciar_cuenta = Tk =Button(ventana, text="Administrador", command=admin_al_cuadrado)
iniciar_cuenta.pack(padx=20, pady=20)
iniciar_usuario = Tk =Button(ventana, text="       Cliente      ", command=eleccion_usuario)
iniciar_usuario.pack(padx=20, pady=20)
global ventana1 
ventana1 = ventana
# Botones
salir = Tk =Button(ventana, text="Cerrar", command=ventana.quit)
salir.pack()

# Widgets
resultado = Tk =Label(ventana, text="")
resultado.pack(pady=90)
ventana.mainloop()