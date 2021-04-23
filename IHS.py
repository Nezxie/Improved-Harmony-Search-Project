from task_function import TaskFunction 
import random
class IHS:
    """ """
    
    def __init__(self, TaskFunction):
        print('init')
        self.f_x=TaskFunction.fnc#funkcja - czy to tak po prostu zadziala?
        self.x=[]#zmienna decyzyjna, czy to sie tak inicjalizuje, nie wiem xd
        self.N=len(TaskFunction.x) #ilosc zmiennych decyzyjnych CZY TO JEST WEKTOR Z TYMI WARTOSCIAMI CZY COS JESZCZE, JAKIES SPACJE I SMIECI?? BO NIE UMIEM TEGO DOBRZE ZPRINTOWAC I ZOBACZYC I NWM
        self.HMS= 2#ilosc wektorow rozwiazan w HM
        self.HMCR=0 #idk (0,1) decyduje czy wybieramy historyczny czy losowy wektor
        self.PAR=0 #to mielismy zmieniac, prawdopodobienstwo pitch adjustingu -> x=x+rand*bw
        self.bw=0 #distance bound wide, liczone w step3
        #NI=#liczba generacji wektora rozwiazan, ile razy powtórzy się algorytm TO CHYBA W MAINIE JEST JUZ WLASNIE

    def init_HM(self):
        a=0
        b=0
        HM=[]
        HM_i=[]
        f=[]
        # generuje losowe wektory rozwiazan
        for i in range(self.HMS):
            k=0
            for j in range(self.N):
                a = TaskFunction.xRanges[k]
                b = TaskFunction.xRanges[k+1]
                HM[i][j]=random.randint(a, b)
                HM_i[j]=HM[i][j] #mam nadzieje ze to bedzie sie nadpisywac bo nie wiem jak przekazac do calculate HM
                k=k+2
            f[i]=IHS.calculate_f(self,HM_i)


    # Methods
    def calculate_f(self,HM_i):
       #for i in range(len(HM_i))
       self.x=HM_i
       return eval(self.f_x)

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
                if ran<self.PAR
                    if ran<0.5:
                        D_3=NHV[i]-ran*self.bw
                        if PVB[0]<=D_3:
                            NHV[i]=D_3
                    else:
                        D_3=NHV[i]+ran*self.bw
                        if PVB[0]>=D_3:
                            NHV[i]=D_3
            else:
                NHV[i]=random.randint(PVB[0],PVB[1]) #co to pvb?
        return NHV

    def update_HM(self,x, f_x):
        calculate_f(self,)
        #czy lepszy?
        #dodaj nowa, usun najgorsza
        #work still in progress :/