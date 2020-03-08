import numpy as np
from numpy import float32
import matplotlib.pyplot as pyplot

def blad_wzgledny(number,result):
    return (number - result) / number

def blad_bezwzgledny(number,result):
    return (number - result)

def tradycyjne_sumowanie(numbers):
    result = float32(0.0)
    blad_talbe = []

    c = 0
    for i in numbers:
        result = result + i
        if c%25000 == 0:
            blad_talbe.append(blad_wzgledny(v*(c + 1),result))
        c += 1

    pyplot.plot(blad_talbe)
    pyplot.show()

    return result

def tree_sum(numbers):
    if len(numbers) == 0:
        return float32(0.0)
    if len(numbers) == 1:
        return numbers[0]
    if len(numbers) == 2:
        return numbers[0] + numbers[1]

    return tree_sum(numbers[ :int(len(numbers)/2 )]) + tree_sum(numbers[ int(len(numbers)/2): ])

#zad 2
def kahan(numbers):
    suma = float32(0.0)
    err = float32(0.0)

    for i in numbers:
        y = i - err
        temp = suma + y
        err = (temp - suma) - y
        suma = temp

    return suma


v = float32(0.53125)
numbers = [v]*10**7

first = tradycyjne_sumowanie(numbers)

print(blad_wzgledny(5312500,first))
print(blad_bezwzgledny(5312500,first))

tree_numbers_sum = tree_sum(numbers)

print(blad_bezwzgledny(5312500,tree_numbers_sum))
print(blad_wzgledny(5312500,tree_numbers_sum))

kahan_sum = kahan(numbers)

print(blad_bezwzgledny(5312500,kahan_sum))
print(blad_wzgledny(5312500,kahan_sum))

#Ponieważ eliminuje błąd utraty low-order bitów,
#za kazdym razem jest wyliczany errr czyli bity ktore zostaly utracone w sumowaniu duzej liczby i malej
#bity te są dodawane w nastepnym obiegu petli do kolejenj liczby

#Sumowanie rekurencyjne zajumje wiecej czasu gdyn ma zlozonosc O(n*log(n))
#podczas gdy algorytm Kahana ma czas liniowy




