from os import getenv
from sys import argv

slownik = {"name":"_spam", "enabled":"no", "type":"176", "action":"Move to folder"}
def rozbij(lista):
    for cos in lista:
        if cos == "":
            continue
        cos_podzielone = cos.split("=")
        # print("cos_podzielone1 " + cos_podzielone[0])
        # print("cos_podzielone2 " + cos_podzielone[1].replace('"',''))
        slownik[cos_podzielone[0]] = cos_podzielone[1].replace('"','').replace(") OR (all addresses,contains,", " ").replace("OR (all addresses,contains,", "")
        # print(type(slownik))
    print (slownik)


if len(argv) > 1 :
    plik = argv[1]
#    print("więcej " + plik)
else :
    plik = input("wprowadź ścieżkę i nazwę pliku: ")
#    print("mniej " + plik)

# # tylko na czas testów
plik = "source\\beka_msgFilterRules.txt"
# plik = "source\msgFilterRules.txt"

f = open(plik, "r", encoding='utf8')

tresc_pliku = f.read()

f.close()
jedno_pole = tresc_pliku.split(')\"')

i = len(jedno_pole)
licznik = 0

while licznik < i:
    slownik_do_bazy = jedno_pole[licznik]
    # print("slownik_do_bazy " + slownik_do_bazy)
    do_slownika = slownik_do_bazy.splitlines()
    # print(do_slownika)
    rozbij(do_slownika)
    print(" ")
    licznik += 1
    