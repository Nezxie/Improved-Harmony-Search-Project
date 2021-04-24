from task_function import TaskFunction 
from random import randint
import math
# from math import sin, cos, exp, sqrt, pi, log   # Instead of 'math.sin' -> 'sin'

class SolutionVector:
    """ - What is my purpose? 
        - You store basic data.
        - Oh my god.
        - Yeah, welcome to the club, pal.    """
    def __init__(self, x_vector=[0,0], calculated_f_x=0.0):    
        self.x_values = x_vector
        self.f_x = calculated_f_x
    def display_data(self):
        print('f_x =', round(self.f_x,2), '   x =', self.x_values)


class IHS:
    """ Handles the best algorithm in the whole galaxy. """
    
    def __init__(self, FncToCalculate):
        # Step 1: Initialize Paramters:
        self.f_x = FncToCalculate.fnc #funkcja - czy to tak po prostu zadziala? ~Raczej tak
        # self.x = [] #zmienna decyzyjna, czy to sie tak inicjalizuje, nie wiem xd
        self.xRanges = FncToCalculate.x # 1:1 przepisz z TaskFunction danych
        self.N = len(self.xRanges) # ilosc zmiennych decyzyjnych 

        self.HMS = 3 # ilosc wektorow rozwiazan w HM
        self.HMCR = 0.95 # (0,1) decyduje czy wybieramy historyczny czy losowy wektor
        self.PAR = 0.1 #to mielismy zmieniac, prawdopodobienstwo pitch adjustingu -> x=x+rand*bw
        self.bw = 1/10000 # distance bound wide, liczone w step3
        #NI= 0 #liczba generacji wektora rozwiazan, ile razy powtórzy się algorytm

        
        # Step 2: Initialize HM:
        self.HM = []
        HM_i = [] # vector that stores randomized x values
        # generuje losowe wektory rozwiazan
        for i in range(self.HMS):
            for j in range(self.N):
                # wylosuj x_j = rand(x_j_min, x_j_max):
                x_j = randint(self.xRanges[j][0], self.xRanges[j][1]) 
                HM_i.append(x_j) # dodaj do HM_i wszystkie losowe wartości x_1...x_N
            # Calculate solution value for randomized vector HM_i
            score_f_x = self.calculate_f_x(HM_i)
            # Save decision vector and solution as an ADT class and append to HM
            self.HM.append(SolutionVector(HM_i, score_f_x))
            self.HM[-1].display_data() # for debug
            HM_i.clear() # clear after each vector in HMS


    def calculate_f_x(self, x_vector):       
        x = x_vector       # something for eval() to work on
        return eval(self.f_x)


    def displayParameters(self):
        """ Simply prints anything interesting"""
        print('Improved Harmony Search z parametrami:')
        print('HMS: ', self.HMS)
        print('HMCR: ', self.HMCR)
        print('PAR: ', self.PAR)
        print('bw: ', self.bw)
        print('Obecne HM: ')
        for solution_vector in self.HM:
            solution_vector.display_data()
        print()
        print('Równanie funkcji: ')
        print('      ', self.f_x)
        i=0
        for x_i_Range in self.xRanges:
            print('Zakres x[', i, ']: ', '[', x_i_Range[0], x_i_Range[1],']')
            i = i+1
        
    def improvise_new(self):
        ran = random()
        NHV=[]
        PVB=[]

        for i in range(self.N):
            self.PAR=PAR(gn) #gn = dana generacja numer
            self.bw=bw(gn)
            if ran<self.HMCR:
                D_1=int(ran*self.HMS)+1
                D_2=self.HM(D_1,i)
                NHV[i]=D_2
                if ran<self.PAR:
                    if ran<0.5:
                        D_3=NHV[i]-ran*self.bw
                        if PVB[0]<=D_3:
                            NHV[i]=D_3
                    else:
                        D_3=NHV[i]+ran*self.bw
                        if PVB[0]>=D_3:
                            NHV[i]=D_3
            else:
                NHV[i]=randint(PVB[0],PVB[1]) #co to pvb?
        return NHV

    def update_HM(self,x, f_x):     # TODO
        self.calculate_f_x(self)
        #czy lepszy?
        #dodaj nowa, usun najgorsza
        #work still in progress :/