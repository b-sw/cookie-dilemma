#!/bin/sh

mkdir output

# uncomment to run evolutionary strategy testing on different threads simultaneously
taskset -c 7 python3 main.py 'es' 100 5 25 5 &
taskset -c 7 python3 main.py 'es' 100 10 25 5 &
taskset -c 6 python3 main.py 'es' 100 20 25 5 &
taskset -c 4 python3 main.py 'es' 100 40 25 5 &
taskset -c 1 python3 main.py 'es' 100 80 25 5 &
taskset -c 0 python3 main.py 'es' 100 160 25 5 &

# uncomment to run genetic algorithm testing on different threads simultaneously
 taskset -c 7 python3 main.py 'ga' 100 5 25 5 &
 taskset -c 7 python3 main.py 'ga' 100 10 25 5 &
 taskset -c 6 python3 main.py 'ga' 100 20 25 5 &
 taskset -c 5 python3 main.py 'ga' 100 40 25 5 &
 taskset -c 3 python3 main.py 'ga' 100 80 25 5 &
 taskset -c 2 python3 main.py 'ga' 100 160 25 5 &

