# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. Отсортировать элементы по возрастанию слева направо и сверху вниз.
# Например, задан массив:
# 1 4 7 2
# 5 9 10 3
# После сортировки
# 1 2 3 4
# 5 7 9 10
from random import random
m = int(input('Введите целое число '))  ### Это только попытки решения, буду далее разбираться
n = int(input('введите целое число ')) 
a = []
for i in range(m):
    z = []
    for j in range(n):
        b = int(random() * 100)
        z.append(b)
        print("%3d" % b, end='')
    print()
    a.append(z)              ## задала двумерный массив
print()

a2 = [0]*n*m              ##захотела сделать его одномерным, но обнаружила, что работает корректно только когда m=n, буду еще разбираться
k=-1
for i in range(n):
    for j in range(m):
        k += 1
        a2[k] = a[i][j]
        print("%3d" % a2[k], end='')
print()
print()

N=len(a2)                      # сортировка массива
for i in range(N-1):
    m=a2[i]
    p=i
    for j in range(i+1,N): 
        if m > a2[j]:
            m=a2[j]
            p=j
    if p !=i:
        t=a2[i]
        a2[i]=a2[p]
        a2[p]=t
print(a2)  
print()
## не совсем придумала как перезаписать одномерный снова в двумерный в виде табл, пока так
a2 = [a2[i:i + n] for i in range(0, len(a2), n)]
print(a2)