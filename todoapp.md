# To Do List

Możemy się uczyć niuansów składni Python'a, ale najlepiej pisać po prostu programy. Dlatego najwyższa pora zacząć robić coś realnie użytecznego. 

Do tego celu stworzymy aplikację do kontrolowania listy rzeczy do zrobienia

## Założenia

Na początek zaczniemy prosto z kilkoma wymaganiami:

1. możemy dodać zadanie do listy
2. możemy zaznaczyć że zadanie zostało zrobione
3. możemy odczytać listę zadań
4. musimy zapisywać naszą listę 
5. musimy odczytywać zapisaną listę


## Interfejs

Czyli jak będziemy komunikowali się z naszą listą. 

Wraz ze zdobywaniem doświadczenia, zrozumiecie jak bardzo istotne jest to by program i jego interfejs były od siebie logicznie odseparowane. Mówi się tutaj między innymi o czymś takim jak *poziomy abstrakcji* (chociaż to jest dużo szersze pojęcie).

Dlaczego jest to ważne? Ponieważ dobrze napisana logika programu może przetrwać zmiany czasów i zmieniających się interfejsów. Już dzisiaj mamy ich dużo:

* program uruchamiany z linii komend (cały czas cieszy się niemalejącą popularnością w świecie Linuxa. Dlaczego? Kiedyś o tym mogę opowiedzieć więcej).
* aplikacja "okienkowa". Tu warto zauważyć, że okienka pisze się w różnych systemach inaczej więc mamy jeszcze podział na:
    * Windows
    * Linux (GTK)
    * Linux (KDE)
    * Mac (OSX)
* strona internetowa (czyli "w chmurze" ;) ).
* aplikacja na komórki. Tu znowu podział
    * Android
    * iOS 
    * Windows Phone

Jeśli napiszecie program dobrze, to dopisanie "interfejsu" dla nowego systemu jest dość prostę. Jeśli natomiast za bardzo pomieszacie logikę z wyglądem dopisanie programu będzie równało się z napisaniem go od nowa.
### Testy

Pierwszym interfejsem użytkownika z jakim będziecie mieli styczność to sam kod. Na przykład jako programista dostajesz interfejs `add()` albo `remove()` na liście. Nazywa się to API czyli Application Programming Interface. Jest to, w pewnym sensie, interfejs idealny bo nie wymaga żadnego dodatkowego kodu i nie granicza naszych możliwości. Natomiast tak samo jak można zrobić nieintuicyjny program okienkowy czy stronę internetową tak można i zrobić nieintuicyjne API (warto o tym pamiętać).

No dobra, ale napisanie programu, który ma kompletne API, ale nigdzie nie jest wywoływane jest bezcelowe. Ba! Nawet jeśli kod się kompiluje to nie wiemy czy on działa!

No właśnie. Tutaj pojawiają się testy. Tak naprawdę przed napisaniem pierwszej linii kodu powinniście pisać testy jak chcecie by Wasz kod działał. 

Jak napisać test? To dość proste. Wyobraźcie sobie, że wasz kod już istnieje, a wy z poziomu [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)'a próbujecie zobaczyć jak to działa. Np.

```python
>>> todo = ToDoApp()

>>> todo
[]

>>> todo.add('zadanie pierwsze')

>>> todo
['zadanie pierwsze']

>>> todo.add('zadanie drugie')

>>> todo
['zadanie pierwsze', 'zadanie drugie']

>>> todo.remove(1)

>>> todo
['zadanie pierwsze']
```

W zasadzie to jest właśnie test. Jeśli ubierzemy to w funkcję będziemy mieli prosty test

```python
def test_todoapp():
    todo = ToDoApp()
    assert todo == []
    todo.add('zadanie pierwsze')
    assert todo == ['zadanie pierwsze']
    todo.add('zadanie drugie')
    assert todo == ['zadanie pierwsze', 'zadanie drugie']
    todo.remove(1)
    assert todo ==  ['zadanie pierwsze']
```

Jeśli wrzucimy taką funkcję do pliku `test_todoapp.py` i wywołamy funkcję `test_todoapp()` to jest to pełnoprawny test! Jeśli ten program skończy się bez błędów to mamy poprawny kod.

Oczywiście jest wiele narzędzi, które sporo pomagają nam w uruchamianiu testów. Jednym z najlepszych jest [py.test](https://docs.pytest.org/) i z niego będziemy starali się korzystać.

#### Testy jednostkowe

Powyższy test nie jest idealny. Tak naprawdę każda funkcja i metoda powinna być testowana w oddzielnym teście. W ten sposób możemy bardzo dokładnie dowiedzieć się co sie popsuło (jak ktoś coś zmieni i nie zawuważy, że psuje to inną funkcję).

Warto przyjrzeć się jak to działa na stronie [py.test](https://docs.pytest.org)


### Linia komend

Najprostrzym interfejsem użytkownika (nie tylko programisty) jest linia komend. Od niej zaczniemy. 

Najpierw mały wstęp do filozofii Linuxa. Pełniejsze wytłumaczenie znajdziecie [tutaj](https://en.wikipedia.org/wiki/Unix_philosophy), ale na nasze potrzeby to wystarczy:

1. Pisz programy, które robią jedną rzecz, ale robią ją dobrze.
2. Pisz programy, które współpracują ze sobą.
3. Pisz programy, które obsługują strumienie tekstowe, bo to jest uniwersalny interfejs.

Ogólny zarys tej koncepcji jest taki by koncentrować się na małych, łatwo podmienialnych programach, które mogą ze sobą wpółpracować. 

Myślę, że najlepiej posłuży tutaj przykład:

`ls | sort | head -n 10`

Wykonanie tego w konsoli linuxowej wyświetli listę plików w katalogu, posortuje tą listę, a następnie wyświetli 10 pierwszych. 

Rozbijmy to na kawałki
* `ls` produkuje strumień na tzw. standardowe wyjście (`stdout`)
* `sort` przyjmuje na swoje standardowe wejście (`stdin`) wynik `ls` przez użycie tzw. pipe'a czyli `|` i wypluwa wynik na `stdout`
* `head` przyjmuje wyjście z `sort`a i wypluwa `stdout`, który z braku laku, przejmuje konsola więc wylatuje nam to na ekran

Mamy dwa rodzaje "komunikacji" z programem w linii komend:
1. strumienie (`stdin`, `stdout`, `stderr`)
2. argumentu (`ls -l`)

#### Strumienie

Strumienie w Pythonie po części poznaliśmy już. Strumień (w uproszczeniu) to wszystko co wpiszemy w konsolę pomiędzy rozpoczęciem, a zakończeniem programu. Czyli za każdym razem jak używaliśmy `input()` tak naprawdę korzystaliśmy z standardowego wejścia. 

Strumienie pozwalają na modyfikowanie przebiegu już działającego programu co daje im praktycznie nieograniczone możliwości w tej dziedzinie.

#### Argumenty

Innym rodzajem komunikacji są argumenty. Argumenty potrafią ustawić to jak program będzie działał i nie da się ich zmienić po uruchomieniu programu.

Jest wiele bibliotek do tego by uprościć czytanie argumentów tj. [argparse](https://docs.python.org/3/howto/argparse.html) czy biblioteka [Click](http://click.pocoo.org/), ale na razie nam wystarczy [`sys.argv`](https://docs.python.org/3.6/library/sys.html#sys.argv).

Załóżmy że mamy program `argreader.py`:

```python
import sys

for arg in sys.argv:
    print(arg)
```

Ten program wyświetli nam listę argumentów. Np.

`> python argreader.py raz dwa raz dwa trzy pięć sześć siedem osiem`

Otrzymamy odpowiedź następującą:
```
argreader.py
raz
dwa 
raz
dwa
trzy
pięć
sześć
siedem
osiem
```

## Zadanie

Naszym następnym zadaniem jest stworzenie programu pod konsolę, który będzie realizował założenia naszej aplikacji To Do.


### Challenge 1

* Stworzyć interfejs API dla naszej aplikacji.
* Stworzyć testy dla tego interfejsu
* Napisać kod tak by testy przechodziły

_Tip: zacznijcie od interfejsu dla pkt. 1-3_

### Challenge 2

Stworzyć iterfejs konsolowy dla aplikacji To Do.

Akcja powinna być podawana jako argument, ale treść zadania powinna być przekazywana jako stream. Czyli.

```
$ todoapp.py add "zadanie pierwsze"
$ todoapp.py 
1. zadanie pierwsze

$ todoapp.py add "zadanie drugie"
$ todoapp.py
1. zadanie pierwsze
2. zadanie drugie

$ todoapp.py remove 1
$ todoapp.py 
1. zadanie drugie
```