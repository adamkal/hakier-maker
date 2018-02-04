# najczęściej importujemy paczki przez zaimportowanie konkretnej rzeczy 
from paczka.modul import test
test()

# importować możemy cały moduł
import paczka_ns # paczki tzw. namespace: nie posiadają pliku __init__.py
import paczka # paczki zwykłe posiadają __init__.py

# wtedy do zmiennych tego modułu dostajemy się w ten sposób:
paczka.test()



from paczka import modul
from paczka_ns import modul as modul_ns
modul.test()
modul_ns.test()


# można też importować wszystko z modułu
from paczka_ns.modul import *
# ale jest to zła praktyka bo często nie wiemy co jest w module bo jest on 
# tworzony przez kogoś innego. Ponieważ importowanie polega na łatowaniu no 
# bieżącego kontekstu zmiennych z innych modułów, może to spowodować nadpisanie
# jakiejś naszej zmiennej. Znalezienie takiego błędu to koszmar.
from paczka.modul import *
test()
print(zmienna)

