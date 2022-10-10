#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

def checking_the_day_of_the_week(day):    
    if day<=7 and day>0:
        if day==6:
            print('Это выходной день недели')
        elif day==7:
            print('Это выходной день недели')
        else:
            print('Это рабочий день недели')  
    else:
            print('Это не день недели')  

try:
   day=int(input('введите цифру от 1 до 7: '))
   numDay= checking_the_day_of_the_week(day) 
except:
    print('Введите целое число')