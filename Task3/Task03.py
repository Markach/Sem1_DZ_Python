# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#  в которой находится эта точка (или на какой оси она находится).
def find_quarter_plain(x,y):
    if x>0 and y>0:
        print('I четверть ')
    elif x<0 and y>0:
        print('II четверть ')
    elif x<0 and y<0:
        print('III четверть ')
    elif x>0 and y<0:
        print('IV четверть ')

    else:
        print('Точка находится на оси ', end= '')
        if x>0 and y==0:
            print('абсцисс, положительной её части')
        elif x==0 and y>0:
            print('ординат, положительной её части')
        elif x<0 and y==0:
            print('абсцисс, отрицательной её части')
        elif x==0 and y<0:
            print('ординат, отрицательной её части')    
    if x==0 and y==0:
        print('Точка начала координат ')


try:
    x = float(input("Введите координату точки А по x= "))
    y = float(input("Введите координату точки А по y= ")) 
    resalt=find_quarter_plain(x,y)
except:
     print('Введите числo')
