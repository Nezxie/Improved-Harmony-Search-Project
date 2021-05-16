import math
from math import sin, cos, exp, sqrt, pi, log   # Instead of 'math.sin' -> 'sin' #TO NIE DZIALA PRZYNAJMNIEJ U MNIE TRZEBA PISAC MATH.EXP, NIE MOZE TAK BYC :<
from task_function import TaskFunction # Class handling task/function data
from os import system, listdir
from IHS import IHS
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
# from menu import handle_menu_input, display_menu # waits for extra program modules

# I use those interchangeably: 
# task - function - file
# currentFunction - default - currFnc


####### Initialization #######

quit_bool = False           # For exiting the main loop
filesDir = './Templates/'   # Directory with templates functions .txt files
currentFunction = None      # Fnc which you will be working on

fncDatabase = []        # Stores fnc in current session
fncDisplay = {}         # For displaying/switching between templates

# Read all fnc into the fncDatabase
for file in listdir(filesDir): 
    if not currentFunction: # make the first file a default function
        currentFunction = TaskFunction(filesDir + file)

    # Database of TaskFunction class objects

    fncDatabase.append(TaskFunction(filesDir + file)) 
    # Display tries to keeps up; Stores task name and equation
    fncDisplay[len(fncDatabase)] = [fncDatabase[-1].fncName, fncDatabase[-1].fnc]



####### Various cool functions (which should be in seperate modules) #######

def change_current_parameters(): 
    """Change parameters of the current task."""
    global currentFunction
    system('cls')

    print('Jakie parametry, aktualnego zadania, chcesz zmienić?')
    print('(Uwaga zmiany działają tylko podczas tej sesji!)')
    print('1 - Wzór')
    print('     ', currentFunction.fnc)
    print()
    print('2 - Komentarz')     # Yup, has to be on nr. 2, look below
    print('     ', currentFunction.scoreComment)
    print()
    print('(Zakres podaj jako dwa int, rozdzielone spacją)')
    for i in range(len(currentFunction.x)):
        print(3+i, '- zakres x[',i,']: ', currentFunction.x[i])
    print()

    fncParameter = int(input('Wybrana opcja: ')) # get the input and make it an int

    # Primitive switch for updating the currFnc
    # ranges of x[n] have to be for fncParameter >= 3 to handle varying n dimension
    if fncParameter == 1:
        currentFunction.fnc = input('Nowy wzór f(x): ')
    elif fncParameter == 2:
        currentFunction.scoreComment = input('Nowy komentarz f(x): ')
    elif fncParameter >= 3:
        idx = fncParameter-3 # idx is a subset of 0..4
        input_text = 'Nowy zakres x[' + str(idx) + ']: '
        new_x = list(map(int, input(input_text).split()))
        currentFunction.x[idx] = new_x
    else:
        print('Zly nr opcji :(')
    system('pause')

def change_to_template():
    """Change currentFunction to one of templates"""
    global currentFunction
    system('cls')
    print('Wybierz funckję zadania do rozwiązania: ')
    for k, v in fncDisplay.items():
        print(k, ' - ', v[0])
        # print('   ', v[1])  # Don't reckon equation is necessary 
    
    newFncNr = int(input('Wybrana funkcja: '))

    if newFncNr in fncDisplay: # Checks whether input exist as a key in the fnc dictionary
        currentFunction = fncDatabase[newFncNr-1]
    else:
        print('Zly nr funkcji :(')
    
    # fncIndex = fncDisplay.get(newFncNr, lambda: 'Zly nr funkcji :(')
    # print(fncIndex)
    
    # system('pause')

def change_to_test():
    """Quickly change currFnc to a simple, test one, from the first file."""
    global currentFunction
    system('cls')
    # Assumes the first fnc/file is the test one
    currentFunction = fncDatabase[0] 

def change_to_manual():
    """Manually enter new task, also creating new file. Update currFnc"""
    global currentFunction, fncDatabase
    system('cls')
    
    fileName = input('Podaj nazwę zadania(pliku bez ".txt"): ')
    fullFilePath = filesDir + fileName + '.txt'
    newEquation = input('Podaj wzór funkcji celu: ')
    variableQnt = int(input('Podaj ile jest zmiennych x[n]: '))
    rangeInfoLine = str()
    for n in range(variableQnt):
        inputInfo = 'Podaj zakres wartości dla x[' + str(n) + '], (np. "-5 5"): '
        rangeInfoLine = rangeInfoLine + input(inputInfo) + ' '
    
    newComment = input('Podaj komentarz, wynik itp.: ')
    
    outF = open(fullFilePath, 'w')
    # Write data to output file
    outF.write(newEquation + '\n')
    outF.write(rangeInfoLine + '\n')
    outF.write(newComment)
    outF.close()    # Always clean after yourself!

    # If everything checks out(or even when not) 
    # add new class to the Database and Display
    fncDatabase.append(TaskFunction(fullFilePath))
    fncDisplay[len(fncDatabase)] = [fncDatabase[-1].fncName, fncDatabase[-1].fnc]
    # Update the currFnc
    currentFunction = fncDatabase[-1]

    # system('pause')

def calculate_task():
    """ 2nd Stage of the Project: calculations"""
    global currentFunction
    system('cls')

    x = []      # something for eval() to work on
    print('Podaj wartosci x dla ktorych trza policzyc: ')
    for i in range(len(currentFunction.x)):
        inputInfo = 'Wartość x[' + str(i) + ']: '
        x.append(float(input(inputInfo)))
    
    y=eval(currentFunction.fnc)
    print(y, ' B) ')
    
    system('pause')

def calculate_IHS():
    max_iterations = 200000
    desired_result = 0.01 # TODO change to lack of progress in last iterations
    min_result_change=0.00001
    
    algo = IHS(currentFunction,max_iterations) # without "algo": missing 1 required positional argument: 'self'
    algo.displayParameters() 
    print('Nacisnij przycisk aby zaczac obliczac: ')
    system('pause')

    ###################################
    # Step 5: Check Stopping Criteria
    ###################################
    iterations = 0
    # Improvise and update until max iterations passed or algo is better than desired result. 
    while iterations < max_iterations: #algo.best_f_x() > desired_result and
        result_change=algo.improvise_and_update(iterations)
        
        if result_change<min_result_change:
            break
        iterations += 1
    # Summary after hard work:
    #print('TU JEST RESULT CHANGE!!!!!' ,result_change)
    algo.displayParameters() 
    print('Komentarz z obecnej funkcji: ')
    print('     ', currentFunction.scoreComment)

     ###################################
    # Rysowanie dla funkcji dwuch zmiennych (wykres 2D)
    ###################################

    if  len(currentFunction.x)==2:
        point=algo.HM.get(algo.best_f_x())
        delta = 0.1 #co ile krok, im mniejszy tym lepiej
        x=[0,0,0,0,0]
        Z=[]
        a = np.arange(currentFunction.x[0][0], currentFunction.x[0][1], delta)
        y = np.arange(currentFunction.x[1][0], currentFunction.x[1][1], delta)
        X, Y = np.meshgrid(a, y)
        for i in range(len(Y)): #po wszystich Y
           x[1]=Y[i,0]
           tmpZ=[]
           for j in range(len(X[0])):
               x[0]=X[0,j]
               tmpZ.append(eval(currentFunction.fnc))
           Z.append(tmpZ)

        fig,ax = plt.subplots()
        CS = ax.contour(X, Y, Z,levels=20) #wyswietlanie, levels = ilosc lini
        ax.clabel(CS, inline=True, fontsize=10)  #numerowanie warotsci warstwic
        ax.set_title('Warstwica ')
        ax.plot(point[0],point[1],'o',color='red')
        fig=plt.figure()
        ax3D= plt.axes(projection='3d')
        ax3D.contour3D(X,Y,Z,50) #50 - ilosc warstwic
        ax3D.plot3D(point[0],point[1],algo.best_f_x(),'red',marker='o')
        plt.show()
    #print(algo.HM.get(algo.best_f_x()))
    system('pause')

'''    f_values=[] #wartosci funkcji
    iter=0
    max_iter=1000
    kryt_wzrostu=0.001
    zmiana=1
    while iter<max_iter && zmiana>kryt_wzrostu:
        new_x=IHS.improvise_new()
        f_values(iter)=IHS.calculate(new_x)
        zmiana=IHS.update(new_x,f(iter))
    plot(iter,f_values)
    #if TaskFunction.x=2
        #graph()  #co przyjmuje graph sprawdzic sobie !!!!
'''

def quit_program():
    """Quit main loop using bool variable"""
    global quit_bool 

    quit_bool = True



####### Menu Functions #######



def invalid_menu_input():
    system('cls')
    print("\n Wpisano zły numerek :( \n")
    system('pause')    


def handle_menu_input(argument):
    """Based on argument(int), use functions. Hardwired with display_menu()!"""
    # Dictionary of options
    menu_functions = {
        '1': change_current_parameters,   # '1 - Zmień parametry aktualnego zadania'
        '2': change_to_template,           # '2 - Zmień f. celu na gotowy szablon'
        '3': change_to_test,              # '3 - Zmień f. celu na testową(f. kwadratowa)'
        '4': change_to_manual,            # '4 - Wpisz ręcznie nową f. celu'        
        '5': calculate_task,              # '5 - Policz'
        '6': calculate_IHS,              
        '7': quit_program,                # '7 - Wyjdź'
    }
    # Get the function from menu_functions dictionary
    # niewypał: menu_functions.get(argument, invalid_menu_input())()
    # wypał:
    func = menu_functions.get(argument)
    if func:
        func() # Execute the function
    else:
        invalid_menu_input() # such func() doesn't exist!


def display_menu(currentFnc):
    """Displays the menu. Hardwired with handle_menu_input()!"""
    system('cls')
    print('Aktualne zadanie:')
    print('-----------------------------------------------')
    currentFnc.displayData()
    print('-----------------------------------------------')
    print('1 - Zmień parametry aktualnego zadania')
    print('2 - Zmień f. celu na gotowy szablon')
    print('3 - Zmień f. celu na testową(f. kwadratowa)')
    print('4 - Wpisz ręcznie nową f. celu(utwórz plik)')
    print('5 - Policz')
    print('6 - IHS')
    print('7 - Wyjdź')
    print()



####### The Holy Main #######


while(not quit_bool):
    display_menu(currentFunction)
    menu_option = input('Wybór: ')
    system('cls')
    handle_menu_input(menu_option)
