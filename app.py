# Kwranking App

# Función que se encarga de mostrar el menú
def muestra_menu():
    print("-------------Kwranking-------------")
    print("[1] - Import keywords")
    print("[2] - Show keywords")
    print("[0] - Exit")

# Función que carga el fichelo con las plaabras clave
def carga_keywords():
    # lista que almacena cada palabra del fichero
    keywords_list = []
    try:
        with open("prueba.txt", "r") as f:
            for linea in f:
                lines = linea.replace("\n", "")
                keywords_list.append(lines)
    except FileNotFoundError:
        print("File Not Found\n")
    return keywords_list

# Función que muestra las palabras claves contenidas en el fichero
def muestra_keywords(keywords):
    # contador para saber cuando se muestra 20 palabras
    counter = 0
    for i in keywords:
        print(i)
        counter += 1
        if counter == 20:
            counter = 0
            input("Press enter to continue")

# Función principal que ejecuta el programa
def run():
    # lista de palabras en la variable "keywords"
    keywords = []

    while True:
        muestra_menu()
        try:
            # lectura del valor que ingresa
            option = int(input("Select an option: "))
            if option == 0:
                print("Finalized")
                break
            elif option == 1:
                keywords = carga_keywords()
                print("\n")
            elif option == 2:
                print("\n")
                muestra_keywords(keywords)
            else:
                print("\nError! Select a correct option!\n")
        except ValueError:
            print("\n-------Enter only numbers!-------")

# ejecución del programas
run()