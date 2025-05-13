from User import User
class Manager(User):
    city=''
    def __init__(self,name,email,city):
        super().__init__(name,email)
        self.city=city
     # this fun is called when user print the object
    def __str__(self):
        return(f" the username is {self.name} and email is {self.email} and city is {self.city}")

manager= Manager('suresh','suresh@mail.com','mumbai')

print(manager.city, manager.name)
print(manager)
