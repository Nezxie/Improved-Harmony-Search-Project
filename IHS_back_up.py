# IHS backup, after raw HS was completed. Still has ADT SolutionVector


from hashlib import new
from task_function import TaskFunction 
from random import randint, random, uniform # uniform used in improvise_new
import math
from math import sin, cos, exp, sqrt, pi, log   # Instead of 'math.sin' -> 'sin'

class SolutionVector:
    """ - What is my purpose? 
        - You store basic data.
        - Oh my god.
        - Yeah, welcome to the club, pal.    """
    def __init__(self, x_vector=[0,0], calculated_f_x=0.0):    
        self.x_values = []
        self.x_values = list(x_vector).copy()
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
        self.HMCR = 0.80 # (0,1) decyduje czy wybieramy historyczny czy losowy wektor
        self.PAR = 0.6 # to mielismy zmieniac, prawdopodobienstwo pitch adjustingu -> x=x+rand*bw
        self.bw = 1/10 # distance bound wide, liczone w step3
        #NI= 0 #liczba generacji wektora rozwiazan, ile razy powtórzy się algorytm
        self.accuracy = 2 # how many digits are considered 0.XXXX

        
        # Step 2: Initialize HM:
        self.HM = []
        self.HM_dict = {}
        HM_i = [] # vector that stores randomized x values
        # generuje losowe wektory rozwiazan
        for i in range(self.HMS):
            for j in range(self.N):
                # wylosuj x_j = rand(x_j_min, x_j_max):
                x_j = round(uniform(self.xRanges[j][0], self.xRanges[j][1]), self.accuracy)
                HM_i.append(x_j) # dodaj do HM_i wszystkie losowe wartości x_1...x_N
            # Calculate solution value for randomized vector HM_i
            score_f_x = self.calculate_f_x(HM_i)
            
            # Save decision vector and solution as an ADT class and append to HM
            self.HM.append(SolutionVector(HM_i, score_f_x))

            # just in case:
            if score_f_x in self.HM_dict:
                print("\n OVERWRITING VALUE!!! \n")

            self.HM_dict[score_f_x] = HM_i.copy()
            # print(self.HM_dict[score_f_x]) # for debug

            # self.HM[-1].display_data() # for debug
            
            
            HM_i.clear() # clear buffer after each vector in HMS


    def calculate_f_x(self, x_vector):       
        x = x_vector       # something for eval() to work on
        return round(eval(self.f_x), self.accuracy)


    def displayParameters(self):
        """ Simply prints anything interesting"""
        print('Improved Harmony Search z parametrami:')
        print('HMS: ', self.HMS)
        print('HMCR: ', self.HMCR)
        print('PAR: ', self.PAR)
        print('bw: ', self.bw)
        print('Obecne HM: ')
        # for solution_vector in self.HM:
        #     solution_vector.display_data()
        print(self.HM_dict)
        print('Najlepszy wynik: ', self.Return_best_f_x())
        print()
        print('Równanie funkcji: ')
        print('      ', self.f_x)
        i = 0
        for x_i_Range in self.xRanges:
            print('Zakres x[', i, ']: ', '[', x_i_Range[0], x_i_Range[1],']')
            i = i+1
        
    # Step 3: Improvise New Harmony
    def improvise_new(self): 
        NHV = [None] * self.N # "New Harmony Vector" - Stores decision variables values

        for i in range(self.N): # iterate over each dec. var. x
            # TODO - is PAR and bw common, or separate for each x?
            # self.PAR = PAR(gn) #gn = dana generacja numer
            # self.bw = bw(gn)
            # PAR = self.PAR #gn = dana generacja numer
            # bw = self.bw

            PVB_lower = self.xRanges[i][0]
            PVB_upper = self.xRanges[i][1]

            if random() < self.HMCR:    # (1) memory consideration
                # choose a vector from current Harmony Memory
                D_1 = int(uniform(0, self.HMS-1))  # Raczej iterujemy 0..HMS
                # From chosen vector(HM[D_1]), access x_i value
                
                # D_2 = self.HM[D_1].x_values[i]
                # Acces [i] variable from [d_1] list of variables in HM
                D_2 = list(self.HM_dict.values())[D_1][i]

                NHV[i] = D_2

                if random() < self.PAR: # (2) pitch adjustment
                    if random() < 0.5:
                        D_3 = NHV[i] - random()*self.bw
                        if PVB_lower <= D_3: # is D_3 within PVB?
                            NHV[i] = round(D_3, self.accuracy)
                    else:
                        D_3 = NHV[i] + random()*self.bw
                        if PVB_upper >= D_3: # is D_3 within PVB?
                            NHV[i] = round(D_3, self.accuracy)
            else:   # (3) random selection
                # generate any rand float, within Possible Value Bond
                NHV[i] = round(uniform(PVB_lower, PVB_upper), self.accuracy)
       
            # finished iterating over decision variables & filling up NHV
        return NHV

    def Return_best_f_x(self):     
            Sorted_f_x = sorted(self.HM_dict)
            return Sorted_f_x[0]

    def update_HM(self, NHV):     
        new_solution = self.calculate_f_x(NHV)
        # print("\n New vector")
        print('Nowy wynik z wektorem: ', new_solution, '   ', NHV)
        Sorted_f_x = sorted(self.HM_dict)
        if new_solution < Sorted_f_x[-1] and new_solution not in self.HM_dict:
            del self.HM_dict[Sorted_f_x[-1]]
            self.HM_dict[new_solution] = NHV
        print(self.HM_dict)


        # self.HM.append(SolutionVector((NHV, new_solution)))
        
        # self.HM_dict.update({new_solution, NHV})

        # HM_list = sorted(self.HM_dict)
        # print(HM_list)
        # del HM_list[-1]
        # print(HM_list)
        # self.HM_dict = dict(HM_list)

        # generate list of f_x from current HM
        # current_solutions = [x.f_x for x in self.HM] 
        # dict(sorted(d.items()))
        # current_solutions, self.HM = zip(*sorted(zip(current_solutions, self.HM)))
        # Debug
        # print("HM: ")
        # print(self.HM)
        # print(type(self.HM))
        # print("curr sol: ")
        # # print(current_solutions)
        # print(type(current_solutions))
        
        # worst case(largest f_x) has index [-1]
        # print("HM[-1].f_x: ")
        # print(self.HM[-1].f_x)
        
        # return 
       