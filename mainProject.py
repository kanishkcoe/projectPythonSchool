import ticket
import user
import trip

# defining trips available for booking
trips = []
trip_1 = trip.Trip("Shatabdi", "Delhi", "Bangluru", "2 Days 7 hours", 2500)
trip_2 = trip.Trip("Gareeb Rath", "Patna", "Lucknow", "1 Days 3 hours", 500)


# append trips to the list called trips
trips.append(trip_1)
trips.append(trip_2)

def showTrip():
    count = 1
    for t in trips:
        print("Trip number : ", count)
        t.showDetails()
        count = count + 1

def bookTicket():
    showTrip()
    tripNumber = int(input("Enter the trip you want to select: "))
    passengerTrip = trips[tripNumber - 1]
    
    print("Enter Passenger details : ")
    firstname = input("Enter your first name :")
    lastname = input("Enter your last name :")
    age = input("Enter your age :")
    gender = input("Enter your gender :")
    contact = input("Enter your contact :")
    numberOfPassengers = int(input("Enter number of passengers :"))

    passenger = user.User(firstname, lastname, age, gender, contact, numberOfPassengers)

    passengerTicket = ticket.Ticket(101, passenger, passengerTrip)

    passengerTicket.showDetails()

def menu():
    print("Menu :")
    print("1. Show Trips Available") # normal print statements
    print("2. Book Ticket")    # insertion to a binary file
    print("3. Show Booking Status")    # search in a binary file
    print("4. Cancel Ticket")  # deletion from a binary file
    choice = int(input("Enter your choice : "))

    if choice == 1:
        #showTrip
        showTrip()
    elif choice == 2:
        #bookTicket
        print("option 2")
        bookTicket()
    elif choice == 3:
        #ShowStatus
        print("option 3")
    elif choice == 4:
        #CancelTicket
        print("option 4")
    else:
        print("Invalid choice")
    

# main flow of code
menu()