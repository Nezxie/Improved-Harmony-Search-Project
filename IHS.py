from hashlib import new
from task_function import TaskFunction 
from random import randint, random, uniform # uniform used in improvise_new
import math
from math import sin, cos, exp, sqrt, pi, log   # Instead of 'math.sin' -> 'sin'

class IHS:
    """ Handles the best algorithm in the whole galaxy. """
    
    def __init__(self, FncToCalculate, NI):
        ###################################
        # Step 1: Initialize Paramters:   
        ###################################
        self.f_x = FncToCalculate.fnc #funkcja - czy to tak po prostu zadziala? ~Raczej tak
        self.xRanges = FncToCalculate.x # 1:1 przepisz z TaskFunction danych
        self.N = len(self.xRanges) # ilosc zmiennych decyzyjnych 

        self.HMS = 6 # ilosc wektorow rozwiazan w HM
        self.HMCR = 0.95 # (0,1) decyduje czy wybieramy historyczny czy losowy wektor
        self.accuracy = 3 # how many digits are being considered 0.XXXX
        self.PAR_max=0.99
        self.PAR_min=0.35
        self.bw_max=4
        self.bw_min=1/1000000
        self.PAR = self.PAR_min # to mielismy zmieniac, prawdopodobienstwo pitch adjustingu -> x=x+rand*bw
        self.bw = self.bw_max # distance bound wide, liczone w step3
        self.NI=NI
        self.c = math.log(self.bw_min/self.bw_max)/self.NI
        self.PAR_CONST = (self.PAR_max-self.PAR_min)/self.NI # Used to calculate current PAR
        ###################################
        # Step 2: Initialize HM:
        ###################################

        self.HM = {} # f_x is key, variables vector is value,
        # e.g. f_x = 33; x = [2, 1, 3] -> {33: [2, 1, 3]}
        self.NewSolutions = {} # Stores proposed solutions, that are accepted

        HM_i = [] # vector that stores randomized x values
        # generuje losowe wektory rozwiazan
        for i in range(self.HMS):
            for j in range(self.N):
                # wylosuj x_j = rand(x_j_min, x_j_max):
                x_j = round(uniform(self.xRanges[j][0], self.xRanges[j][1]), self.accuracy)
                HM_i.append(x_j) # dodaj do HM_i wszystkie losowe wartości x_1...x_N
            # Calculate solution value for randomized vector HM_i
            score_f_x = self.calculate_f_x(HM_i)
            
            # Save decision vector and result, as value and key in HM
            
            # Warning, just in case newly generated result, key, would already be in HM
            # (A dictionary will overwrite value with the new one, len(HM) will be HMS-1)
            if score_f_x in self.HM: 
                print("\n OVERWRITING VALUE!!! \n")

            self.HM[score_f_x] = HM_i.copy() 
            
            HM_i.clear() # clear buffer after each vector in HMS


    def calculate_f_x(self, x_vector):       
        x = x_vector       # something for eval() to work on
        return round(eval(self.f_x), self.accuracy)


    def displayParameters(self):
        """ Simply prints anything interesting"""
        print('Równanie funkcji: ')
        print('      ', self.f_x)
        i = 0
        for x_i_Range in self.xRanges:
            print('Zakres x[', i, ']: ', '[', x_i_Range[0], x_i_Range[1],']')
            i = i+1
        print('Improved Harmony Search z parametrami:')
        print('HMS: {:^6}'.format(self.HMS))
        print('HMCR: {:^6}'.format(self.HMCR))
        print('PAR: {:^6}'.format(self.PAR))
        print('bw: {:^6}'.format(self.bw))
        print('Obecne HM: ')
        for k, v in self.HM.items():
            print('   f(x)= {:<7} x='.format(k), v)
        print()
        print('Najlepszy wynik: ')
        print('   f(x)= {:<7} x='.format(self.best_f_x()[0]), self.best_f_x()[1])
        print()
        
    
    def best_f_x(self):     
            # Sort dictionary keys, from lowest f_x to highest
            Sorted_f_x = sorted(self.HM) # Min is the first one
            Values = tuple((Sorted_f_x[0], self.HM[Sorted_f_x[0]])) # Get (f_x, x[])
            return Values 

    def best_all(self):
        return self.NewSolutions

    def improvise_and_update(self,gn): 
        """ First, improvise new harmony, then update the HM.
            Step 5, checking stop criteria is done outside! (watch out for PAR, bw values)"""
        ###################################
        # Step 3: Improvise New Harmony
        ###################################
        
        NHV = [None] * self.N # "New Harmony Vector" - Stores new decision variables values
        self.PAR = round(self.PAR_min+(self.PAR_CONST)*gn, 2)
        self.bw = round(self.bw_max*math.exp(self.c*gn), 6)
        for i in range(self.N): # iterate over each dec. var. x
            # TODO - is PAR and bw common, or separate for each x?
            # Narazie zakładam stałe, brane z "self."
            
            # self.PAR = PAR[i] #gn = dana generacja numer
            #self.bw = bw[i]
            # PAR = self.PAR #gn = dana generacja numer
            # bw = self.bw
            

            # Get Possible Value Bounds for given x[i]
            PVB_lower = self.xRanges[i][0]
            PVB_upper = self.xRanges[i][1]

            if random() < self.HMCR:    # (1) memory consideration
                # Choose a random vector from current Harmony Memory
                D_1 = int(uniform(0, self.HMS-1))  # we iterate over 0..HMS-1

                # Acces variable x[i] from vector list [D_1] of variables in HM
                D_2 = list(self.HM.values())[D_1][i]
                NHV[i] = D_2 # D_2 is value of x[i] in New Vector

                if random() < self.PAR: # (2) pitch adjustment
                    # Flip of coin for adding/substracting bw
                    if random() < 0.5:
                        D_3 = NHV[i] - random()*self.bw     # From D_2 substract a wee bit
                        if PVB_lower <= D_3:                # is D_3 within PVB?
                            NHV[i] = round(D_3, self.accuracy) # Update x[i] in New Vector
                    else:
                        D_3 = NHV[i] + random()*self.bw     # Add a wee bit to D_2
                        if PVB_upper >= D_3:                
                            NHV[i] = round(D_3, self.accuracy) # Update x[i] in New Vector
            else:   # (3) random selection
                # Generate any rand float, within Possible Value Bond
                NHV[i] = round(uniform(PVB_lower, PVB_upper), self.accuracy)
       
            # (Finished iterating over decision variables & filling up NHV)

        ###################################
        # Step 4: Update HM
        ###################################

        # Calculate result for the NHV
        result_change=1
        new_result = self.calculate_f_x(NHV)
        if new_result!=self.best_f_x()[0]:
            result_change=abs(new_result-self.best_f_x()[0]) #liczenie do przerwania jeśli zmiana za mała (w mainie)
        # print('Nowy wynik z wektorem: ', new_result, '   ', NHV) # For debug
        
        # Create a list of sorted dictionary keys, from lowest f_x to highest
        Sorted_f_x = sorted(self.HM)
        # Update HM, if new_result is better than the worst f_x key([-1] in a sorted list)
        # Also, new_result cannot already be in HM -> prevents edge case(I think)
        if new_result < Sorted_f_x[-1] and new_result not in self.HM:
            del self.HM[Sorted_f_x[-1]]     # Remove HM dict entry with key "Sorted_f_x[-1]"
            self.HM[new_result] = NHV       # Add new vector and result to HM

            self.NewSolutions[new_result] = NHV       # Add new vector and result to good solutions
        # print(self.HM) # for debug

        return result_change #new_result
    