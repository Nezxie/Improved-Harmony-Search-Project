import math
from math import sin, cos, exp, sqrt, pi, log
from task_function import TaskFunction
from os import system
from os import listdir

# Initialization
quit_bool = False
filesDir = './Templates/'
currentFunction = None

fncDatabase = []
fncDisplay = {} # For switching between templates

for file in listdir(filesDir):
    if not currentFunction: # make the first file a default function
        currentFunction = TaskFunction(filesDir + file)

    fncDatabase.append(TaskFunction(filesDir + file))
    fncDisplay[len(fncDatabase)] = [fncDatabase[-1].fncName, fncDatabase[-1].fnc]

# system('pause')
    
def change_current_parameters():
    system('cls')
    print('chaning parameters')
    system('pause')

def change_to_template():
    global currentFunction
    system('cls')
    print('Wybierz funckję zadania do rozwiązania: ')
    for k, v in fncDisplay.items():
        print(k, ' - ', v[0])
        # print('   ', v[1])                      
    
    newFncNr = int(input('Wybrana funkcja: ')) # get the input and make it an int

    if newFncNr in fncDisplay: # does input exist as a key in the fnc dictionary
        currentFunction = fncDatabase[newFncNr-1]
    else:
        print('Zly nr funkcji :(')
    
    # fncIndex = fncDisplay.get(newFncNr, lambda: 'Zly nr funkcji :(')
    # print(fncIndex)
    
    # system('pause')

def change_to_test():
    system('cls')
    print('chaning to test')
    system('pause')

def change_to_manual():
    system('cls')
    print('chaning to manual')
    system('pause')

def calculate_task():
    system('cls')
    print('calculate_task')
    system('pause')

def quit_program():
    # system('cls')
    global quit_bool # explicite adress global, not local, variable

    # print('quit_program')
    quit_bool = True
    # system('pause')

def invalid_menu_input():
    system('cls')
    print("\n Wpisano zły numerek :( \n")
    system('pause')    


def handle_menu_input(argument):
    menu_functions = {
        '1': change_current_parameters,   # '1 - Zmień parametry aktualnego zadania'
        '2': change_to_template,           # '2 - Zmień f. celu na gotowy szablon'
        '3': change_to_test,              # '3 - Zmień f. celu na testową(f. kwadratowa)'
        '4': change_to_manual,            # '4 - Wpisz ręcznie nową f. celu'        
        '5': calculate_task,              # '5 - Policz'
        '6': quit_program,                # '6 - Wyjdź'
    }
    # Get the function from menu_functions dictionary
    # menu_functions.get(argument, invalid_menu_input())()
    func = menu_functions.get(argument)
    if func:
        # Execute the function
        func()
    else:
        invalid_menu_input()


def display_menu():
    system('cls')
    print('Aktualne zadanie:')
    print('-----------------------------------------------')
    currentFunction.displayData()
    print('-----------------------------------------------')
    print('1 - Zmień parametry aktualnego zadania')
    print('2 - Zmień f. celu na gotowy szablon')
    print('3 - Zmień f. celu na testową(f. kwadratowa)')
    print('4 - Wpisz ręcznie nową f. celu')
    print('5 - Policz')
    print('6 - Wyjdź')
    print()


if __name__ == '__main__':

    while(not quit_bool):
        display_menu()
        menu_option = input('Wybór: ')
        system('cls')
        handle_menu_input(menu_option)


        

