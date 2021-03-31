import math
N=0
x=[]
# HMS=0
# HMCR=0
# PAR=0

    


def menu(menu_param2):
    return{
        '1':['1 - Funkcja z czterema minimami lokalnymi','x[0]**4+x[1]**4-(0.62*x[0]**2)-(0.62*x[1]**2)'],
        '2':['2 - Funkcja Rosenbrocka', '100*(x[1]-x[0]**2)**2+(1-x[0])**2'],
        '3':['3 - Funkcja Zangwill’a', '(x[0]-x[1]+x[2])**2+(-x[0]+x[1]+x[2])**2+(x[0]+x[1]-x[2])**2'],
        '4':['4 - Funkcja Goldsteina-Price’a z czterema minimami lokalnymi','(1+((x[0]+x[1]+1)**2)*(19-14*x[0]+3*(x[0]**2)-14*x[1]+6*x[0]*x[1]+3*(x[1]**2))*(30+((2*x[0]-3*x[1])**2)*(18-32*x[0]+12*(x[0]**2)+48*x[1]-36*x[0]*x[1]+27*(x[1]**2))))'], 
        '5':['5 - Funkcja celu', 'math.exp(-2*math.log(2)*(x[0]-0.08)**2/0.854**2)*math.sin(5*math.pi*(x[0]**0.75-0.05))**6'],
        '6':['6 - Zmodyfikowana funkcja Himmelblau’a', '(x[0]**2+x[1]-11)**2+(x[0]+x[1]**2-7)**2-200 '],
        '7':['7 - Funkcja Ackley’a', '-20*math.exp(-0.2*math.sqrt(0.5)*((x[0]**2)+(x[1]**2)))-math.exp(0.5*(math.cos(2*math.pi*x[0])+math.cos(2*math.pi*x[1])))'],
        '8':['8 - Funkcja Rastrigina', '(x[0]**2)-math.cos(18*x[0])+(x[1]**2)-math.cos(18*x[1])'],
        '9':['9 - Funkcja testowa Geem’a', '4*(x[0]**2)-2.1*(x[0]**4)+(1/3)*(x[0]**6)+x[0]*x[1]-4*(x[1]**2)+4*(x[1]**4)'],
        '10':['10 - sinusy * exp ujemnej sumy kwadratow', 'math.sin(x[0])*math.sin(x[1])*math.exp(-(x[0]**2+x[1]**2))'],
        '11':['11 - x * exp ujemnej sumy kwadratow', 'x[0]*math.exp(-(x[0]**2+x[1]**2))'],
        '12':['12 - Funkcja celu (sin)', 'math.sin(5.1*math.pi*x[0]+0.5)**6'], 
    }[menu_param2]
            
while 1:

    print("1 - Wybierz gotowa funkcje \n 2 - Wczytaj funkcje z pliku \n 3 - Wprowadz funkcje recznie ")
    menu_param1=input()
    if menu_param1=='1':
        for fnc in range(1,13):
            print(menu(str(fnc))[0])
        menu_param2=input()
        print('Wybrano:')
        print('   ', menu(str(menu_param2))[1])
        f_x=menu(menu_param2)[1]
    elif menu_param1=='2':
        print("Podaj sciezke do pliku: ")
        file=input()
        with open(file) as f:
            f_x = f.readline()
    elif menu_param1=='3':
        print("Podaj funkcje w formie x[0]+x[1]*math.sin(x[2])... ")
        f_x=input()  
    else: 
        print("Wybrana opcja nie istnieje")

    # Tutaj koncz pętle 

    print("Ile warunkow poczatkowych?")
    N=int(input())
    print("Podaj warunki poczatkowe")
    for i in range(N):
        x.append(float(input()))
    # print("Podaj PAR")2

    # PAR=float(input())
    y=eval(f_x)
    print(y)

    x.clear()  # czyszczenie tablicy war. początkowych
    # for i in range(N): #czyszczenie tablicy zeby sie wartosci nie dopisywaly
    #     del x[i]
    # print(x)