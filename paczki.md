# Paczki

Jendym z najsilniejszych atutów Pythona jest ogromne środowisko ludzi, którzy
tworzą i dzielą się swoim kodem. Python mocno to wspiera dając narzędzia, które
w łatwy sposób pomagają korzystać z dobrodziejstw Open Source.

Zanim jednak przejdziemy do tego jak korzystać z kodu mądrych (bardziej lub 
mniej) głow powtórzmy jak wygląda re-używanie kodu.

## Re-używanie kodu

Generalna zasada jest taka:

* kod jest w [funkcjach](https://docs.python.org/3/glossary.html#term-function)
* funkcje są w [klasach](https://docs.python.org/3/glossary.html#term-class), wtedy nazywamy je [metodami](https://docs.python.org/3/glossary.html#term-method)
* klasy są w [modułach](https://docs.python.org/3/glossary.html#term-module), czyli w pliku z rozszerzeniem `py`
* moduły są w [paczkach](https://docs.python.org/3/glossary.html#term-package), czyli katalogach

To jest oczywiście uproszczenie, które ma na celu łatwiejsze czytanie kodu. 

### Importowanie kodu

Aby zyskać dostęp do kodu spoza obecnego modułu musimy go jakoś zaimportować.

Najlepiej uczyć się na przykładach dlatego w katalogu [paczki](./paczki) jest
kilka przykładów.

Uruchomienie pliku `main.py` powinno dawać taki efekt:
```
>>> paczka.__init__.py
<<< paczka.__init__.py
>>> paczka.modul.py
<<< paczka.modul.py
To jest funkcja test z modułu `modul.py` w katalogu `paczka`
To jest funkcja test z modułu `paczka` (plik `__init__.py`) w katalogu `paczka`
>>> paczka_ns.modul.py
<<< paczka_ns.modul.py
To jest funkcja test z modułu `modul.py` w katalogu `paczka`
To jest funkcja test z modułu `modul.py` w katalogu `niepaczka`
To jest funkcja test z modułu `modul.py` w katalogu `paczka`
cześć
```

Zwróćcie uwagę:

* to co importujemy może być wszystkim: zmienną lokalną,
  modułem czy nawet paczką. To może zdawać się dziwne, ale tak naprawdę to dobrze.
  Nas nie obchodzi czym jest to coś co importujemy tylko jak to działa.
* kiedy uruchamiany jest kod (linie z `>>>` i `<<<`)


## Instalowanie paczek OpenSource

No dobra. To już coś wiemy o tym jak jest kod zorganizowany, jak go importować
i mniej więcej co to znaczy.

Co jeśli, stwierdzimy, że wynik naszych danych chcemy zapisać do pliku Excela.
Moglibyśmy zacząć implementować bibliotekę, która stworzyłaby plik excela, ale
łatwiej posłużyć się czymś co ktoś już kiedyś napisał. Patrzymy na
[Awesome Python](https://awesome-python.com/#specific-formats-processing) i
znajdujemy kilka opcji. Załóżmy, że `tablib` wydał nam się wystarczający dla
naszych potrzeb. Co teraz?

Tutaj z pomocą przychodzi nam narzędzie o nazwie `pip`(https://pip.pypa.io/).
Wystarczy, że w konsoli wpiszemy (sorry Maciuś):

```pip install tablib```

i po chwili możemy napisać w naszym kodzie:

```python

import tablib
headers = ('first_name', 'last_name')

data = [
    ('John', 'Adams'),
    ('George', 'Washington')
]

data = tablib.Dataset(*data, headers=headers)

with open('people.xls', 'wb') as f:
    f.write(data.export('xls'))

```

`pip` załatwia za nas prawie wszystko: znajduje najświeższą wersję biblioteczki,
znajduje jej zależności i je również zainstaluje. Jest super!

Co więcej `pip` daje możliwość zapisania listy paczek i załadowania ich z tej
listy, co umożliwia załączanie takich list do projektów by zawsze mieć to co
potrzeba. Super użyteczne!

### .. a teraz zejdźmy na ziemię

No dobra. Prawda jest taka, że przez pierwszy rok kodowania w Pythonie `pip`
będzie super. Załatwi każdy problem (bo 90% waszych problemów już ktoś kiedyś
rozwiązał) i życie będzie piękne.

Problem zacznie się jak zaczniecie pracować na więcej niż jednym projekcie gdzie
każdy z nich trochę różni się użyciem. Co jeśli dwie biblioteczki w swoich
zależnościach będą wymagały dwóch różnych wersji jakieś innej biblioteczki?
Dupa.

I na to mamy rozwiązanie! Nazywa się wirtualny środowiskiem. Oznacza to tylko
tyle, że jesteśmy wstanie stworzyć taką wirtualną instalację Pythona dla każdego
projektu i będzie ona zupełnie niezależna od innych takich instalacji.

Nie musimy za bardzo wchodzić w szczegóły tzw. `virtualenv`'ów czy też 
`venv`'ów, bo przeskoczymy o jeden krok dalej czyli połączenie pipa z
virtualenv'mi: `pipenv`.

> Uwaga! `pipenv` będzie naszym narzędziem więc je zainstalujcie!

Jak zdobyć `pipenv`? No to chyba proste:

`pip install pipenv` :troll:

W tym momencie chyba powinniście już zauważyć, że coś jest nie tak bo dostajecie
błąd w stylu "permissin denied". Tak. `pip` główny (nie w `virtualenv`ie) jest
pod kontrolą systemu więc bez uprawnień administratora nie uda wam się nic
zainstalować. Dlatego pod linux'em trzeba użyć przedrostka `sudo` 
(`sudo pip install pipenv`), a na Windowsie trzeba uruchomić PowerShell'a z
uprawnieniami administratora (jest taka opcja jeśli klikniesz w znaczek
windowsa/start prawym klawiszem myszki)

Takie harce nie są potrzebne przy używaniu `virtualenv`ów co jest dodatkowym 
atutem.

`pipenv`'a używa się bardzo podobnie do normalnego `pip`a:

* `pipenv install tablib` - instaluje paczkę
* `pipenv run todo.py` - uruchom program w tym środowisku
* `pipenv shell` - wejdź do wirtualnego środowiska (wygląda jak normalne tylko
  używa środowiska wirtualnego zamiast systemowego pythona)