class Bomb:
    def __init__(self, serialNum, parrallelPort, battery, Lit):
        self.serialNum = serialNum
        self.parrallelPort = parrallelPort
        self.battery = battery
        self.Lit = Lit
        self.strikeCount =0
    
    def __str__(self):
        return "Bomb: serialNum: {}, parrallelPort: {}, Lit: {}".format(self.serialNum, self.parrallelPort, self.Lit)

    def __repr__(self):
        return self.__str__()
    
    def lastDigit(self):
        #True if last digit is even
        return self.serialNum[-1] % 2 ==0
    
    def batteryCount(self):
        return self.battery


