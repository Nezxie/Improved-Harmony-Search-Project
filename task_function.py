class TaskFunction:
    'Stores optimization function, data'
    # This is our initializer method when a new object is created.
    def __init__(self, filePath):
        taskData = []

        try:
            with open(filePath) as f:
                for line in f:
                    taskData.append(line)
        except IOError:
            print('Error: File does not appear to exist: ', filePath)

        self.fncName = filePath[12:-4]     # use online middle of './Templates/XXX.txt' 
        self.fnc = taskData[0][0:-1] # [0:-1] removes \n at end of line 
        xRanges = list(map(int, taskData[1].split()))
        self.x = []
        for i in range(0, len(xRanges), 2):   # get pairs of x[i] min and max
            self.x.append([xRanges[i], xRanges[i+1]])   # x[i] = [x_imin, x_imax]
        self.scoreComment = taskData[2][0:-1] # [0:-1] removes \n at end of line
    
    # def __del__(self):
    #     print('some destructor')

    # Methods
    def displayData(self):
        print('Nazwa pliku: ', self.fncName)
        print('Równanie funkcji: ')
        print('      ', self.fnc)
        print()
        for x_i in range(len(self.x)):
            print('Zakres x[', x_i, ']: ', self.x[x_i])
        print('Komentarz wyniku: ', self.scoreComment)
    
    # def Get(self, amount):
    #     print('Kokos')
    #     # self.__Balance -= amount
