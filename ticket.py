# ticket class
import user 
import trip

class Ticket:

    def __init__(self, id, user, trip):
        self.id = id
        self.user = user
        self.trip = trip
        self.amount = float(user.count) * float(trip.cost)

    def showDetails(self):
        print(self.id) 
        print("user details : ", self.user.showDetails())
        print("trip details : ")
        self.trip.showDetails()
        print("Total Amount", self.amount)



trip_1 = trip.Trip("Shatabdi", "Delhi", "Bangluru", "2 Days", "2500")

# trip_1.showDetails()

user_1 = user.User("kanishk", "debnath", 23, "male", "8130692843", 4)

print("start of program")

# print(user_1.showDetails())
# print(user_1.fullname())
# print(user_1.age)

ticket_1 = Ticket(101, user_1, trip_1)

ticket_1.showDetails()

print("end of program")