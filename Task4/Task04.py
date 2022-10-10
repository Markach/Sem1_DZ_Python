# Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.

# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
# Обратите внимание, что на вход программе приходят вещественные числа
def calculator(firstValue, secondValue, action):
    if action == '+':
        print(firstValue + secondValue) 
    elif action == '-':
        print(firstValue - secondValue) 
    elif action == '/':
        if secondValue == 0:
            print('Деление на 0!')
        else:            
            print(firstValue / secondValue)
    elif action == '*':
        print(firstValue * secondValue)  
    elif action == 'mod':
        print(firstValue % secondValue)                                      
    elif action == 'pow':
        print(firstValue ** secondValue)
    elif action == 'div':
        print(firstValue // secondValue)   
    else:
        print('Ошибка, неизвестное действие')

try:
    firstValue = float(input("Введите первое число = "))
    secondValue = float(input("Введите второе число = ")) 
    action = input("Выберите операцию: '+', '-', '*', '/', 'mod', 'pow', 'div' : ")
    resalt = calculator(firstValue, secondValue, action)
except:
     print('Введите числo')
