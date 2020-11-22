# User class
# use of abstraction and encapsulation

class User:

    def __init__(self, firstname, lastname, age, gender, contact, count):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.contact = contact
        self.count = count

    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

    def showDetails(self):
        return '{} {} of age {} of gender {} has contact {} booked {} seats'.format(self.firstname, self.lastname, self.age, self.gender, self.contact, self.count)
    
# user_1 = User("kanishk", "debnath", 23, "male", "8130692843", 4)

# print(user_1.showDetails())
# print(user_1.fullname())
# print(user_1.age)
