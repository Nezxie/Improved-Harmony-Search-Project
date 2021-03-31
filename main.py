import math
from task_function import TaskFunction
from os import system

# Initialization
quit_bool = False
filesDir = './Templates/'
currentFunction = TaskFunction(filesDir + '2_Rosenbrock.txt')

def change_current_parameters():
    print('chaning parameters')
    system('pause')

def change_to_template():
    print('chaning to temp')
    system('pause')

def change_to_test():
    print('chaning to test')
    system('pause')

def change_to_manual():
    print('chaning to manual')
    system('pause')

def calculate_task():
    print('calculate_task')
    system('pause')

def quit_program():
    global quit_bool # explicite adress global, not local, variable

    print('quit_program')
    quit_bool = True
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
    func = menu_functions.get(argument)
    if func:
        # Execute the function
        func()
    else:
        print("\n Wpisano zły numerek :( \n")
        system('pause')
    


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
    print('Wybór: ')


if __name__ == '__main__':

    while(not quit_bool):
        display_menu()
        menu_option = input()
        system('cls')
        handle_menu_input(menu_option)


        

