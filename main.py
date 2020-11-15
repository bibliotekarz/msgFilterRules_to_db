import re
from os import getenv
from sys import argv

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
    do_slownika = slownik_do_bazy.splitlines()
    print(do_slownika)
    print(" ")
    licznik += 1
    