# Kwranking App

# librería requests para peticiones http

import requests
from bs4 import BeautifulSoup

# Función que se encarga de mostrar el menú
def muestra_menu():
    print("-------------Kwranking-------------")
    print("[1] - Import keywords")
    print("[2] - Show keywords")
    print("[3] - Check keywords")
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

# Función que encuentra el dominio
def aparece_el_dominio(link, domain):
    found = False
    fin = link.find("&")
    page = link[:fin]
    if domain in page:
        found = True
    return found

# Función que devuelve la posición en la que rankea
# la palabra clave para el dominio definido
def comprueba_keywords(kw, domain):
    continuar = True
    start = 0
    position = 1
    found = False
    while continuar and not found:
        parametros = {'q': kw, 'start': start}
        resp = requests.get(f'https://www.google.com/search', params=parametros)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'lxml')
            div_principal = soup.find('div', {'id': 'main'})
            results = div_principal.find_all('div', {'class', 'ZINbbc xpd O9g5cc uUPGi'})
            for res in results:
                if res.div and res.div.a:
                    if aparece_el_dominio(res.div.a['href'], domain):
                        found = True
                        break
                    else:
                        position += 1
            if not found:
                footer = div_principal.find('footer')
                siguiente = footer.find('a', {'aria-label': 'Página siguiente'})
                if siguiente:
                    start += 10
                    if start == 100:
                        continuar = False
                else:
                    continuar = False
        else:
            continuar = False
    if not found:
        position = 100
    return position

# Función principal que ejecuta el programa
def run():
    # lista de palabras en la variable "keywords"
    keywords = []
    domain = "j2logo.com"
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
            elif option == 3:
                kw = input("Enter the keywords to check: ")
                position = comprueba_keywords(kw, domain)
                if position < 100:
                    print(f"keywords {kw} found in position {position} for domain {domain}")
                else:
                    print(f"At the moment, keywords {keywords} don't rank for domain {domain}")
            else:
                print("\nError! Select a correct option!\n")
        except ValueError:
            print("\n-------Enter only numbers!-------")

# ejecución del programas
run()