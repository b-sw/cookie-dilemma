<!-- TABLE OF CONTENTS -->
## Table of Contents

* [Authors](#authors)
* [Context](#context)
* [Description of the Problem](#description)
* [Run guide](#run-guide)

## Authors
Bartosz Świtalski

Marcel Kawski

## Context
Nauczycielka w przedszkolu chce rozdać ciastka dzieciom w swojej grupie. Dzieci
siedzą w linii obok siebie (i nie zmieniają tych pozycji). Każde dziecko ma przypisaną ocene si
, i ∈ (1, 2, ..., n), zgodnie z wynikiem testu umiejetności. Nauczycielka chce dać każdemu dziecku co najmniej jedno ciastko. Jeśli dzieci siedzą
obok siebie, dziecko z wyższą ocena musi dostać więcej ciastek niż to z nizszą
oceną. Nauczycielka ma ograniczony budżet, więc chce rozdać jak najmniej ciastek. Zaimplementuj program bazujacy na dowolnych 2-ch wybranych rodzajach
Algorytmów Ewolucyjnych, który zwróci najmniejszą liczbę ciastek, które musi
rozdać nauczycielka. Należy dokładnie porównać wybrane algorytmy. Zalecana
jest konsultacja z prowadzącym przed pracą nad projektem.

## Description
Finding optimal solution to a cookie giveaway problem using different evolutionary algorithms.

## Run guide
### with args:
```
/cookie-dilemma$ python3 ./main.py -s -p -o -k -d -r -a
```
#### flags: <br />
s - seed <br />
p - population size <br />
o - offspring size <br />
k - k value for k-iterations criterion <br />
d - dimensions <br />
r - # of runs <br />
a - algorithm ('es' or 'ga') <br />


### without args:
```
/cookie-dilemma$ python3 ./main.py
```
