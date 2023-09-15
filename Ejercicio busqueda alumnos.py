import numpy as np
import time
from colorama import Fore, Back, Style, init
init(autoreset=True)

#Esto es no más pa' darle color a las cosas
colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN]

#Lista con nombres 
nombres = ["Juan", "María", "Carlos", "Laura", "Manuel", "Ana", "José", "Patricia", "Luis", "Gabriela", "Miguel", "Sandra", "Antonio", "Andrea", "Alejandro", "Natalia", "Pedro", "Raquel", "Daniel", "Claudia", "Javier", "Valentina", "Francisco", "Paola", "David", "Carolina", "Roberto", "Isabel", "Fernando", "Victoria", "Sergio", "Elena", "Ernesto", "Marta", "Oscar", "Paula", "Guillermo", "Diana", "Eduardo", "Beatriz", "Ricardo", "Adriana", "Jorge", "Lorena", "Gustavo", "Teresa", "Alberto", "Sofía", "Rodrigo", "Julia", "Gabriel", "Camila", "Humberto", "Gabriela", "Arturo", "Lourdes", "Armando", "Susana", "Héctor", "Mercedes", "Raúl", "Valeria", "Enrique", "Roxana", "Mario", "Mariana", "Gerardo", "Natalia", "Marco", "Adriana", "Gonzalo", "Lorena", "Hugo", "Isabel", "Alejandro", "Verónica", "Ignacio", "Laura", "Eduardo", "Alejandra", "Víctor", "Patricia", "Óscar", "Carmen", "Andrés", "Blanca", "Alfonso", "Rosa", "Federico", "Marisol", "Javier", "Adriana", "Martín", "Alejandra", "Israel", "Marcela", "Leonel", "Roxana", "Guillermo", "Raquel", "Ángel", "Lorena", "Mauricio", "Patricia", "Germán", "Carla", "Raúl", "Valentina", "Emiliano", "Diana", "Guillermo", "Cecilia", "Sergio", "Sonia", "Cristian", "Valeria", "Rafael", "Andrea", "Felipe", "Isabel", "Eduardo", "Beatriz", "Simón", "Brenda", "Felipe", "Ana María", "Luis Miguel", "Laura Sofía", "Roberto Carlos", "María José", "José Luis", "Patricia María", "Juan Carlos", "Carolina Andrea", "Javier Alejandro", "Diana Patricia", "Pedro José", "Laura Isabel", "Manuel Antonio", "María Fernanda", "Miguel Ángel", "Gabriela Alejandra", "Luis Enrique", "Valentina Sofía", "Carlos Andrés", "Paula Andrea", "Francisco Javier", "Andrea Carolina", "Ricardo Andrés", "Natalia Alejandra", "Juan Pablo", "María Elena", "Andrés Felipe", "Ana María José", "Ernesto Alberto", "Laura Marcela", "David Alejandro", "Claudia Patricia", "Roberto Andrés", "Sofía Alejandra", "Óscar Eduardo", "Andrea Marcela", "Sergio Andrés", "Isabel María", "Eduardo José", "Beatriz Elena", "Gustavo Adolfo", "Diana Marcela", "Alberto José", "Rosa María", "Rodrigo Andrés", "Julia Carolina", "Gabriel Alberto", "Camila Sofía", "Humberto José", "Gabriela Alejandra", "Arturo Andrés", "Lourdes María", "Armando José", "Susana Patricia", "Héctor Manuel", "Mercedes María", "Raúl Andrés", "Valeria Sofía", "Enrique José", "Roxana Patricia", "Mario Alberto", "Mariana Alejandra", "Gerardo Andrés", "Natalia María", "Marco Antonio", "Adriana Patricia", "Gonzalo José", "Lorena Andrea", "Hugo Alberto", "Isabel María", "Alejandro José", "Verónica Patricia", "Ignacio José", "Laura María"]
rangocod = np.arange(1000000,10000000)

#Aquí almacenamos los datos aleatorios porque escribir 6500 datos es tenaz.
alumnos = 6500
nombressel = np.random.choice(nombres, 6500)

codigo = np.random.choice(rangocod,6500,replace = False)

nota = np.random.uniform(0.0,5.1,6500)
notadec = np.round(nota,1)

carreras = {10: 'Biologia', 11:'Ing. Sistemas',14:'Quimica',16:'Lic. Matemáticas',18:'Fisica',19:'Lic. en educ básica enfasis en Ciencias Nat.',20: 'Lic. Inglés',21:'Ing. Civil',22:'Ing. eléctirca',23:'Ing. Industrial',24: 'Ing. Mecáncia',26:'Ing. Elelctrónica',27: 'Diseño Industrial',28: 'Lic. Educ básica énfasis en lengua castellana',29: 'Lic. Español y Literatura',30: 'Lic. Música',31: 'Ing. Metalúrgica',32: 'Ing. Petroleos',33: 'Ing. Quimcia',34: 'Geologia', 37: 'Filosofia',39: 'Matemáticas', 41: 'Trabajo Social', 44: 'Historia',45: 'Economía',46:'Derecho',51: 'Enfermería', 52: 'Medicina',56: 'Fisioterapia',57: 'Nutricion',58:'Microbiología',60: 'Historia y archivistica',63:'Lic. lenguas extra. énfasis en ingles',64: 'Lic. en literatura y lengua castellana',68: 'Lic. eduación básica primaria'}
carreras_estudiantes = np.random.choice(list(carreras.keys()), 6500)

anio = np.random.randint(1980,2024,6500,dtype=int)

#Acá se están guardando los datos correspondientes según su pocisión, tipo matríz
información = list(zip(nombressel,codigo,notadec,carreras_estudiantes,anio))


#Creamos finalmente el bucle que nos pregunta la información que deseamos extraer hasta que le demos en 'salir' (^u^)
while True: 
    
    print(Back.RED+"\tELIJA SU MÉTODO DE BÚSQUEDA:")
    print("\n 1. Código de carrera (con promedio mayor/igual a 4)")
    print("\n 2. Estudiantes antes de 1990 y condicionales")
    print("\n 3. Total de estudiantes")
    print("\n 4. Salir ")
    opción = int(input("\n"))

    if opción == 4: 
        texto = "\tBuen día! Hasta luego."
        while True:
            for color in colors:
            
                print("\033[K" + color + texto + Style.RESET_ALL, end="\r")
                time.sleep(0.5)  
            break
        break

    elif opción == 1:
        carX = int(input("\tIngrese el código de la carrera a buscar: "))
        totalumnos = 0

        for name,code,sign,degree,year in información:
            if degree == carX and 4.0 <= sign <= 5.0:
                print(Fore.GREEN+f"\nNombre:" + Fore.WHITE+ f" {name}" +Fore.BLUE+ f"    Codigo:"+ Fore.WHITE + f" {code}" +Fore.MAGENTA+ f"    Carrera:"+Fore.WHITE + f" {carreras[degree]}"+Fore.CYAN+f"    Nota promedio:"+Fore.WHITE+ f" {sign}" + Fore.YELLOW+f"    Año de ingreso:"+Fore.WHITE+f" {year} ")
                totalumnos += 1 



        print("\n\n\t\t" + Fore.CYAN + f"El total de alumnos con ponderado mayor/igual a 4.0 es:"+Fore.WHITE+f" {totalumnos}"+Style.RESET_ALL+"\n\n\n\n")



    elif opción == 2:
        print("\t\t\t\t"+Back.GREEN+"CONDICIONALIDAD: 2.6 - 3.2")

        for name,code,sign,degree,year in información:
            if year < 1990 and 2.6 <= sign <= 3.2:

                print(Fore.GREEN+f"\nNombre:" + Fore.WHITE+ f" {name}" +Fore.BLUE+ f"    codigo:"+ Fore.WHITE + f" {code}" +Fore.MAGENTA+ f"    carrera:"+Fore.WHITE + f" {carreras[degree]}"+Fore.CYAN+f"    nota promedio:"+Fore.WHITE+ f" {sign}" + Fore.YELLOW+f"    año de ingreso:"+Fore.WHITE+f" {year} ")
        print("\n\n\n")
    elif opción == 3: 
        
        cantele = len(nombressel)

        print("\t\t\n"+Fore.MAGENTA +"La cantidad total de alumnos es: "+Fore.WHITE+f"{cantele}"+Style.RESET_ALL+"\n\n\n\n")

    else: print("\t\t\t"+Fore.RED + "Favor ingrese una opción válida"+Style.RESET_ALL+"\n\n\n\n")

            







