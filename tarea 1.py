'''              Programación de computadores 
                  Karen Rocio Ruiz Zárate
               Estudiante de ingeniería agricola
               Universidad Nacional de Colombia
                     Tame - 2021
'''
#kruizz
a=input("¿quiere guardar el archivo? ")
if a=="si":
    f = open("tarea1.txt", "w")
    print("hola mundo", file=f)
    f.close()
elif a=="no":
    print("hola mundo")
else:
    print("escriba si o no (sin tildes)")