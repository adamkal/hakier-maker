print('start')
lista = []
def odczyt_pliku():
    with open('lista.txt') as plik:
        for linia in plik:
            lista.append(linia.strip())
     
def zapis():
    with open('lista.txt','w') as plik:
        plik.write('\n'.join(lista))

def todo_add(a):
    lista.append(a)

    drukuj()

    
def drukuj():
    print('\n-- '.join(lista))


def todo_done(index):
    lista.pop(index)
    drukuj()

odczyt_pliku()
drukuj()

for i in range(5):
    a = input('Podaj element \n')
    todo_add(a)


todo_done(int(input('Podaj element do usuniecia \n')))
zapis()


