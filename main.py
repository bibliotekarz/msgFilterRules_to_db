import os
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


        slownik[cos_podzielone[0]] = cos_podzielone[1].replace('"','').replace(") OR (all addresses,contains,", " ").replace("OR (all addresses,contains,", "").replace(") OR (from,contains,", " ").replace("OR (from,contains,", "").replace(") OR (\\return-path\\,contains,", " ").replace(") OR (\\x-wp-ip\\,contains,", " ").replace(") OR (\\x-originator\\,contains,", " ").replace(") OR (\\x-originating-ip\\,contains,"," ").replace(") OR (\\received\\,contains,", " ")
        # print(type(slownik))


        
    print (slownik)
    print(" ")


if len(argv) > 1 :
    plik = argv[1]
else :
    plik = input("wprowadź ścieżkę i nazwę pliku: ")


# # tylko na czas testów
pobierz = "source/beka_msgFilterRules.txt"
# pobierz = "source/msgFilterRules.txt"
fileDir = os.path.dirname(os.path.realpath(__file__))
plik = os.path.join(fileDir, pobierz)

f = open(plik, "r", encoding='utf8')

tresc_pliku = f.read()

f.close()
jedno_pole = tresc_pliku.split(')\"')

i = len(jedno_pole)
licznik = 0

while licznik < i:
    slownik_do_bazy = jedno_pole[licznik]
    do_slownika = slownik_do_bazy.splitlines()
    rozbij(do_slownika)
    licznik += 1
    