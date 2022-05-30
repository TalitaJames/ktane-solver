import bomb

def count(word, letter):
    count = 0
    for c in word:
        if c == letter:
            count += 1
    return count

def lastValue(word, letter):
    letterList = []
    for c in range(len(word)):
        if word[c] == letter:
            letterList.append(c)
    return max(letterList)+1 # +1 because of zero indexing

def simpleWires(input):
    # wires can be 3-6
    #cut one
    #order from top

    cutWire=0
    #colours: yellow (Y), red (R), blue (B), black (X), or white (W)

    if len(input)==3:
        # If there are no red wires, cut the second wire.
        if "R" not in input:
            cutWire=2
        
        # Otherwise, if the last wire is white, cut the last wire.
        elif input[2]=="W":
            cutWire=len(input)
        
        # Otherwise, if there is more than one blue wire, cut the last blue wire.
        elif count(input, "B")>=1:
            cutWire=lastValue(input, "B")
            
        else:  # Otherwise, cut the last wire.
            cutWire=len(input)
    elif len(input)==4:
        # If there is more than one red wire and the last digit of the serial number is odd, cut the last red wire.     
        if count(input, "R")>1 and not bomb.lastDigit():
            cutWire=lastValue(input, "R")

        # Otherwise, if the last wire is yellow and there are no red wires, cut the first wire.
        elif input[-1]=="Y" and "R" not in input:
            cutWire=1

        # Otherwise, if there is exactly one blue wire, cut the first wire.
        elif count(input, "B")==1:
            cutWire=1

        # Otherwise, if there is more than one yellow wire, cut the last wire.
        elif count(input, "Y")>1:
            cutWire=len(input)

        else: # Otherwise, cut the second wire.
            cutWire=2
    elif len(input)==5:
        # If the last wire is black and the last digit of the serial number is odd, cut the fourth wire.
        if input[-1]=="X" and not bomb.lastDigit():
            cutWire=4

        # Otherwise, if there is exactly one red wire and there is more than one yellow wire, cut the first wire.
        elif count(input, "R")==1 and count(input, "Y")>1:
            cutWire=1
        
        # Otherwise, if there are no black wires, cut the second wire.
        elif "X" not in input:
            cutWire=2
        
        else: # Otherwise, cut the first wire.
            cutWire=1      
    elif len(input)==6:
        # If there are no yellow wires and the last digit of the serial number is odd, cut the third wire.
        if "Y" not in input and not bomb.lastDigit():
            cutWire=3

        # Otherwise, if there is exactly one yellow wire and there is more than one white wire, cut the fourth wire.
        elif count(input, "Y")==1 and count(input, "W")>1:
            cutWire=4

        # Otherwise, if there are no red wires, cut the last wire.
        elif "R" not in input:
            cutWire=len(input)

        # Otherwise, cut the fourth wire
        else:
            cutWire=4
        
    else:
        print("Error: input must be 3-6 wires")
    
    return "Cut wire number " + cutWire

def theButton(colour, text):
    hold=False
    # If the button is blue and the button says "Abort", hold the button and refer to "Releasing a Held Button".
    if colour=="B" and text=="Abort":
        hold=True
    
    # If there is more than 1 battery on the bomb and the button says "Detonate", press and immediately release the button.
    elif bomb.batteryCount()>1 and text=="Detonate":
        return "press and immediately release"
    
    # If the button is white and there is a lit indicator with label CAR, hold the button and refer to "Releasing a Held Button".
    elif colour=="W" and bomb.Lit=="CAR":
        hold=True

    # If there are more than 2 batteries on the bomb and there is a lit indicator with label FRK, press and immediately release the button.
    elif bomb.batteryCount()>2 and bomb.Lit=="FRK":
        return "press and immediately release"

    # If the button is yellow, hold the button and refer to "Releasing a Held Button".
    elif colour=="Y":
        hold=True

    # If the button is red and the button says "Hold", press and immediately release the button.
    elif colour=="R" and text=="Hold":
        return "press and immediately release"
    
    # If none of the above apply, hold the button and refer to "Releasing a Held Button".
    
    if hold==True:
        colouredStrip=input("What is the colored strip?", end=" ")
        if colouredStrip=="B":
            return "Release when timer has: 4"
        elif colouredStrip=="W":
            return "Release when timer has: 1"
        elif colouredStrip=="Y":
            return "Release when timer has: 5"
        else:
            return "Release when timer has: 1"

def keypads()

