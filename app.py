# Kwranking App


def menu():
    # lista de palabras en la variable "keywords"
    keywords = carga_keywords()

    while True:
        print("[1] - Import keywords")
        print("[2] - Show keywords")
        print("[0] - Exit")
        try:
            # lectura del valor que ingresa
            option = int(input("Select an option: "))
            if option == 1:
                print(keywords)
                break
            elif option == 2:
                # variable para imprimir el límite de 20 palabras
                limit = 20
                # contador para comparar e imprimir cada 20 palabras
                counter = 0
                for i in keywords:
                    print(i)
                    counter += 1
                    if counter == limit:
                        input("Press enter to continue")
                        limit += 20
                break
            elif option == 0:
                print("Finalized")
                break
            else:
                print("\nError! Select a correct option!\n")
        except ValueError:
            print("\n-------Enter only numbers!-------")


def carga_keywords():
    # lista que almacena cada palabra del fichero
    keywords_list = []
    with open("prueba.txt", "r") as f:
        for linea in f:
            lines = linea.replace("\n", "")
            keywords_list.append(lines)
    return keywords_list

# ejecución del programa
menu()