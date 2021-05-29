
import math
from math import sin, cos, exp, sqrt, pi, log  
from os import system, listdir
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from hashlib import new
from random import randint, random, uniform
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

class App:
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("Improved harmony search")
        self.started=True

        self.frame_1=tk.Frame()
        self.frame_1.pack(fill=tk.X)
        self.function_lb=tk.Label(self.frame_1,text="Funkcja:",width=16)
        self.function_lb.pack(side=tk.LEFT,padx=5,pady=5)
        self.function_box=tk.Entry(self.frame_1)
        self.function_box.insert(0,'x[0]*x[1]')
        self.function_box.pack(fill=tk.X,padx=5)

        self.frame_2=tk.Frame()
        self.frame_2.pack(fill=tk.X)
        self.range_lb=tk.Label(self.frame_2,text="Zakres (a_i < x_i < b_i) :",width=16)
        self.range_lb.pack(side=tk.LEFT,padx=10,pady=5)
        
 
        #ramka matka
        
        self.mother=tk.Frame()
        self.mother.pack(side=tk.LEFT,fill=tk.Y)
        
        
        #1
        self.frame_3=tk.Frame(self.mother)
        #self.frame_3.config(bg="#ccccff")
        self.frame_3.pack(fill=tk.X)
        self.rangex1_lb=tk.Label(self.frame_3,text="x_1",width=16)
        self.rangex1_lb.config(bg="#ccccff")
        self.rangex1_lb.pack(side=tk.LEFT,padx=5,pady=5)

        

        self.rangex1_box1=tk.Entry(self.frame_3)
        self.rangex1_box1.insert(0,'-5')
        self.rangex1_box1.pack(fill=tk.X,padx=5)
        self.rangex1_box1.config(bg="#ccccff")

        self.rangex1_box2=tk.Entry(self.frame_3)
        self.rangex1_box2.insert(0,'5')
        self.rangex1_box2.pack(fill=tk.X,padx=5,pady=10)
        self.rangex1_box2.config(bg="#ccccff")

        #2
        self.frame_4=tk.Frame(self.mother)
        self.frame_4.pack(fill=tk.X)
        self.rangex2_lb=tk.Label(self.frame_4,text="x_2",width=16)
        self.rangex2_lb.pack(side=tk.LEFT,padx=5,pady=5)

        self.rangex2_box1=tk.Entry(self.frame_4)
        self.rangex2_box1.insert(0,'-5')
        self.rangex2_box1.pack(fill=tk.X,padx=5)

        self.rangex2_box2=tk.Entry(self.frame_4)
        self.rangex2_box2.insert(0,'5')
        self.rangex2_box2.pack(fill=tk.X,padx=5,pady=10)
        #3
        self.frame_5=tk.Frame(self.mother)
        #self.frame_5.config(bg="#ccccff")
        self.frame_5.pack(fill=tk.X)
        self.rangex3_lb=tk.Label(self.frame_5,text="x_3",width=16)
        self.rangex3_lb.config(bg="#ccccff")
        self.rangex3_lb.pack(side=tk.LEFT,padx=5,pady=5)

        self.rangex3_box1=tk.Entry(self.frame_5)
        self.rangex3_box1.insert(0,'null')
        self.rangex3_box1.pack(fill=tk.X,padx=5)
        self.rangex3_box1.config(bg="#ccccff")

        self.rangex3_box2=tk.Entry(self.frame_5)
        self.rangex3_box2.insert(0,'null')
        self.rangex3_box2.pack(fill=tk.X,padx=5,pady=10)
        self.rangex3_box2.config(bg="#ccccff")
        #4
        self.frame_6=tk.Frame(self.mother)
        self.frame_6.pack(fill=tk.X)
        self.rangex4_lb=tk.Label(self.frame_6,text="x_4",width=16)
        self.rangex4_lb.pack(side=tk.LEFT,padx=5,pady=5)

        self.rangex4_box1=tk.Entry(self.frame_6)
        self.rangex4_box1.insert(0,'null')
        self.rangex4_box1.pack(fill=tk.X,padx=5)

        self.rangex4_box2=tk.Entry(self.frame_6)
        self.rangex4_box2.insert(0,'null')
        self.rangex4_box2.pack(fill=tk.X,padx=5,pady=10)
        #5
        self.frame_7=tk.Frame(self.mother)
        #self.frame_7.config(bg="#ccccff")
        self.frame_7.pack(fill=tk.X)
        self.rangex5_lb=tk.Label(self.frame_7,text="x_5",width=16)
        self.rangex5_lb.config(bg="#ccccff")
        self.rangex5_lb.pack(side=tk.LEFT,padx=5,pady=5)

        self.rangex5_box1=tk.Entry(self.frame_7)
        self.rangex5_box1.insert(0,'null')
        self.rangex5_box1.pack(fill=tk.X,padx=5)
        self.rangex5_box1.config(bg="#ccccff")

        self.rangex5_box2=tk.Entry(self.frame_7)
        self.rangex5_box2.insert(0,'null')
        self.rangex5_box2.pack(fill=tk.X,padx=5,pady=10)
        self.rangex5_box2.config(bg="#ccccff")

         #druga ramka ojciec
        self.father=tk.Frame()
        self.father.pack(side=tk.RIGHT,fill=tk.Y)
          #boxy do wyświetlania/wpisywania zakresów
        self.peniz=tk.Frame(self.father)
        self.peniz.pack(fill=tk.X)
        self.peniz1=tk.Label(self.peniz,text="uuuuuuuu",width=16)
        self.peniz1.pack(side=tk.LEFT,padx=5,pady=5)

         
        #wpisywanie parametrów algorytmu
        #PAR
        self.frame_8=tk.Frame(self.mother)
        self.frame_8.pack(fill=tk.X)
        self.par1_lb=tk.Label(self.frame_8,text="PAR",width=16)
        self.par1_lb.pack(side=tk.LEFT,padx=5,pady=5)

        self.par1_lb1=tk.Label(self.frame_8,text="górna granica (<1)",width=16)
        self.par1_lb1.pack(fill=tk.X,padx=5)
        self.par1_box1=tk.Entry(self.frame_8)
        self.par1_box1.insert(0,'0.99')
        self.par1_box1.pack(fill=tk.X,padx=5)

        self.par1_lb2=tk.Label(self.frame_8,text="dolna granica (>0)",width=16)
        self.par1_lb2.pack(fill=tk.X,padx=5)
        self.par1_box2=tk.Entry(self.frame_8)
        self.par1_box2.insert(0,'0.35')
        self.par1_box2.pack(fill=tk.X,padx=5,pady=5)

        #HMCR
        self.frame_9=tk.Frame(self.mother)
        self.frame_9.pack(fill=tk.X)
        
        self.hmcr_lb=tk.Label(self.frame_9,text="HMCR",width=16)
        self.hmcr_lb.pack(side=tk.LEFT,padx=5,pady=5)
        self.hmcr_lb.config(bg="#A8A8A8")

        self.hmcr_box1=tk.Entry(self.frame_9)
        self.hmcr_box1.insert(0,'0.95')
        self.hmcr_box1.pack(fill=tk.X,padx=5)
        self.hmcr_box1.config(bg="#A8A8A8")
        #HMS
        self.frame_10=tk.Frame(self.mother)
        self.frame_10.pack(fill=tk.X)
        self.hms_lb=tk.Label(self.frame_10,text="HMS",width=16)
        self.hms_lb.pack(side=tk.LEFT,padx=5,pady=5)

        self.hms_box1=tk.Entry(self.frame_10)
        self.hms_box1.insert(0,'6')
        self.hms_box1.pack(fill=tk.X,padx=5)

        #PAR
        self.frame_12=tk.Frame(self.mother)
        self.frame_12.pack(fill=tk.X)
        self.bw1_lb=tk.Label(self.frame_12,text="bandwidth",width=16)
        self.bw1_lb.pack(side=tk.LEFT,padx=5,pady=5)
        self.bw1_lb.config(bg="#A8A8A8")

        self.bw1_lb1=tk.Label(self.frame_12,text="górna granica",width=16)
        self.bw1_lb1.pack(fill=tk.X,padx=5)
        self.bw1_box1=tk.Entry(self.frame_12)
        self.bw1_box1.insert(0,'3')
        self.bw1_box1.pack(fill=tk.X,padx=5)
        self.bw1_box1.config(bg="#A8A8A8")

        self.bw1_lb2=tk.Label(self.frame_12,text="dolna granica (>0)",width=16)
        self.bw1_lb2.pack(fill=tk.X,padx=5)
        self.bw1_box2=tk.Entry(self.frame_12)
        self.bw1_box2.insert(0,'0.0001')
        self.bw1_box2.pack(fill=tk.X,padx=5,pady=5)
        self.bw1_box2.config(bg="#A8A8A8")

        #zmiana ilości lini na wykresach
        self.ilewarstwic=tk.Frame(self.mother)
        self.ilewarstwic.pack(fill=tk.X)
        self.ilewarstwic_lb=tk.Label(self.ilewarstwic,text="Liczba warstwic",width=16)
        self.ilewarstwic_lb.pack(side=tk.LEFT,padx=5,pady=5)

        self.ilewarstwic_box1=tk.Entry(self.ilewarstwic)
        self.ilewarstwic_box1.insert(0,'20')
        self.ilewarstwic_box1.pack(fill=tk.X,padx=5)

        #przycisk start
        self.frame_11=tk.Frame(self.mother)
        self.frame_11.pack(fill=tk.X)
        self.button=ttk.Button(self.frame_11,text="START",command=self.start)#,command=funkcja ktora uruchamia ihs
        self.button.pack(side=tk.LEFT,padx=5,pady=5)

        #wykresy

        self.figure1 = plt.Figure(figsize=(5, 3), dpi=100)
        self.ax1 = self.figure1.add_subplot(111)
        self.bar1 = FigureCanvasTkAgg(self.figure1, self.root)
        self.bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        self.figure2 = plt.Figure(figsize=(4, 3), dpi=100)
        self.ax2 = self.figure2.add_subplot(111, projection='3d')
        self.bar2 = FigureCanvasTkAgg(self.figure2, self.root)
        self.bar2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        
       
        self.root.mainloop()

  #main który jest wywoływany przez przycisk start
    def start(self):
        max_iterations = 20000
        min_result_change=0.000001
        currentFunction=self.function_box.get()

        all_ranges=self.ranges_input()


        algo = IHS(currentFunction,all_ranges,max_iterations)  
        algo.HMS = float(self.hms_box1.get())
        algo.HMCR = float(self.hmcr_box1.get())
        algo.PAR_max=float(self.par1_box1.get())
        algo.PAR_min=float(self.par1_box2.get())
        algo.bw_max=float(self.bw1_box1.get())
        algo.bw_min=float(self.bw1_box2.get())
        #algo.PAR=self....get() itd
        iterations = 0
     
        while iterations < max_iterations: 
            result_change = round(algo.improvise_and_update(iterations), 3)
        
            if result_change < min_result_change:
                break
            iterations += 1

        if  self.is2dimension():
            point=algo.HM.get(algo.best_f_x()[0])
            delta = 0.1 #co ile krok, im mniejszy tym lepiej
            x=[0,0,0,0,0]
            Z=[]
            a = np.arange(float(self.rangex1_box1.get())-0.5, float(self.rangex1_box2.get())+0.5, delta)
            y = np.arange(float(self.rangex2_box1.get())-0.5, float(self.rangex2_box2.get())+0.5, delta)
            X, Y = np.meshgrid(a, y)
            for i in range(len(Y)): #po wszystich Y
               x[1]=Y[i,0]
               tmpZ=[]
               for j in range(len(X[0])):
                   x[0]=X[0,j]
                   tmpZ.append(eval(currentFunction))
               Z.append(tmpZ)

            self.ax1.clear()
            CS = self.ax1.contour(X, Y, Z,levels=int(self.ilewarstwic_box1.get())) #wyswietlanie, levels = ilosc lini
            self.ax1.clabel(CS, inline=True, fontsize=10, fmt='%1.1f')  #numerowanie warotsci warstwic
            self.ax1.xaxis.grid(True, zorder=0)
            self.ax1.yaxis.grid(True, zorder=0)
            self.ax1.set_title('Warstwice 2D')
            best_x = []
            best_y = []
            best_fx = []
            plot_best_x = []
            plot_best_y = []
            for k, v in algo.best_all().items():
                best_x.append(v[0])
                best_y.append(v[1])
                best_fx.append(k)
            # ax.plot(best_x,best_y,'o',color='red')
            best_len = len(best_fx)
            best_iterator = int(best_len*0.1)
            for xy in range(0,best_len,best_iterator):
                plot_best_x.append(best_x[xy])
                plot_best_y.append(best_y[xy])
                self.ax1.plot(best_x[xy],best_y[xy],'o',color='blue')
            self.ax1.plot(plot_best_x,plot_best_y,color='red')
            self.bar1.draw_idle()

            self.ax2.clear()
            self.ax2.contour3D(X,Y,Z, int(self.ilewarstwic_box1.get())) #50 - ilosc warstwic
            self.ax2.scatter(point[0],point[1],algo.best_f_x()[0],marker='o',color='red')
            self.bar2.draw_idle() 

    def is2dimension(self):
        fx=self.function_box.get()
        if fx.find("x[0]")!=-1 and fx.find("x[1]")!=-1 and fx.find("x[2]")==-1 and fx.find("x[3]")==-1 and fx.find("x[4]")==-1:
            return True
        return False
    def ranges_input(self):
        all_ranges=[]
        if self.rangex1_box1.get()!="null":
            all_ranges.append([float(self.rangex1_box1.get()), float(self.rangex1_box2.get())])

        if self.rangex2_box1.get()!="null":
            all_ranges.append([float(self.rangex2_box1.get()), float(self.rangex2_box2.get())])

        if self.rangex3_box1.get()!="null":
            all_ranges.append([float(self.rangex3_box1.get()), float(self.rangex3_box2.get())])

        if self.rangex4_box1.get()!="null":
            all_ranges.append([float(self.rangex4_box1.get()), float(self.rangex4_box2.get())])

        if self.rangex5_box1.get()!="null":
            all_ranges.append([float(self.rangex5_box1.get()), float(self.rangex5_box2.get())])

        return all_ranges



#IHS kopia z projektu v0
class IHS:
       
    def __init__(self, FncToCalculate,all_ranges, NI):
        ###################################
        # Step 1: Initialize Paramters:   
        ###################################
        self.f_x = FncToCalculate 
        self.xRanges = all_ranges 
        self.N = len(self.xRanges) 

        self.HMS = 6 
        self.HMCR = 0.95 
        self.accuracy = 3 # how many digits are being considered 0.XXXX
        self.PAR_max=0.99
        self.PAR_min=0.35
        self.bw_max=3
        self.bw_min=1/10000
        self.PAR = self.PAR_min 
        self.bw = self.bw_max 
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

            self.HM[score_f_x] = HM_i.copy() 
            
            HM_i.clear() # clear buffer after each vector in HMS


    def calculate_f_x(self, x_vector):       
        x = x_vector       # something for eval() to work on
        return round(eval(self.f_x), self.accuracy)
             
    
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
        # # print('Nowy wynik z wektorem: ', new_result, '   ', NHV) # For debug
        
        # Create a list of sorted dictionary keys, from lowest f_x to highest
        Sorted_f_x = sorted(self.HM)
        # Update HM, if new_result is better than the worst f_x key([-1] in a sorted list)
        # Also, new_result cannot already be in HM -> prevents edge case(I think)
        if new_result < Sorted_f_x[-1] and new_result not in self.HM:
            del self.HM[Sorted_f_x[-1]]     # Remove HM dict entry with key "Sorted_f_x[-1]"
            self.HM[new_result] = NHV       # Add new vector and result to HM

            self.NewSolutions[new_result] = NHV       # Add new vector and result to good solutions

        # if new_result!=self.best_f_x()[0]:
        #     result_change=abs(new_result-self.best_f_x()[0]) #liczenie do przerwania jeśli zmiana za mała (w mainie)
        
        # print(self.HM) # for debug

        return result_change #new_result

  

app=App()