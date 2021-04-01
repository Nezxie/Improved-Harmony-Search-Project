class TaskFunction:
    """Stores optimization function/task data"""
    
    def __init__(self, filePath):
        taskData = [] # Collects data as strings
        
        try:    # ... opening the file
            with open(filePath) as f:
                for line in f:
                    taskData.append(line)
        except IOError:
            print('Error: File does not appear to exist: ', filePath)

        # Function/File name; use online middle of './Templates/XXX.txt' 
        self.fncName = filePath[12:-4] 
        # Funcja celu   
        self.fnc = taskData[0][0:-1] # [0:-1] removes \n at end of line
        # Zakresy wartości, as single integers
        xRanges = list(map(int, taskData[1].split()))
        self.x = []
        for i in range(0, len(xRanges), 2):   # get pairs of x[i] min and max values
            self.x.append([xRanges[i], xRanges[i+1]])   # x[i] = [x_imin, x_imax]
        # Any comment about fnc, it's opti score etc.
        self.scoreComment = taskData[2][0:-1] # [0:-1] removes \n at end of line
    
    # Methods
    def displayData(self):
        print('Nazwa pliku: ', self.fncName)
        print('Równanie funkcji: ')
        print('      ', self.fnc)
        print()
        for x_i in range(len(self.x)):
            print('Zakres x[', x_i, ']: ', self.x[x_i])
        print('Komentarz wyniku: ', self.scoreComment)
