testCase = int(input())

def getResult(speedOftheCars,numberOfCars):
    carsAtMaximumSpeedCounter = 1
    MaximumSpeed = speedOftheCars[0]
    for i in range(1,numberOfCars):
        if(MaximumSpeed>=speedOftheCars[i]):
            carsAtMaximumSpeedCounter +=1
            MaximumSpeed = speedOftheCars[i]
    
    print(carsAtMaximumSpeedCounter)




for i in range(testCase):
    numberOfCars = int(input())
    speedOftheCars = [int(x) for x in input().split()]

    getResult(speedOftheCars,numberOfCars)