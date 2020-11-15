from os import getenv
from sys import argv

print(argv)

if len(argv) >= 1 :
    plik = argv[1]
    print(plik)
else :
    plik = input("wprowadź ścieżkę i nazwę pliku: ")
    print(plik)
