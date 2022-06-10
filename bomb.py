class Bomb:
    def __init__(self, serialNum, parrallelPort, battery, Lit):
        self.serialNum = serialNum
        self.parrallelPort = parrallelPort
        self.battery = battery
        self.Lit = Lit
        self.strikeCount = 0
    
    def __str__(self):
        return "Bomb: serialNum: {}, parrallelPort: {}, Lit: {}".format(self.serialNum, self.parrallelPort, self.Lit)

    def __repr__(self):
        return self.__str__()
    
    def serialLastDigit(self):
        #True if last digit is even
        return self.serialNum[-1] % 2 ==0
    
    def serialContainsVowel(self):
        vowelCount = False
        for letter in self.serialNum:
            if letter in "aeiou":
                vowelCount = True
        return vowelCount
    
    def batteryCount(self):
        return self.battery
    
    def addStrike(self):
        self.strikeCount += 1
    
    def returnStrike(self):
        return self.strikeCount