# trip class

class Trip:

    def __init__(self, trainName, fromDestination, toDestination, duration, cost):
        self.trainName = trainName
        self.fromDestination = fromDestination
        self.toDestination = toDestination
        self.duration = duration
        self.cost = cost

    def showDetails(self):
        print("++++++++++++++++++++++++++++++++++")
        print("Name of train : ", self.trainName)
        print("From : ", self.fromDestination)
        print("To : ", self.toDestination)
        print("Duration : ", self.duration)
        print("Cost per person : ", self.cost, " Rs")
        print("++++++++++++++++++++++++++++++++++")
    
# trip_1 = Trip("Shatabdi", "Delhi", "Bangluru", "2 Days", "2500")

# trip_1.showDetails()
    
