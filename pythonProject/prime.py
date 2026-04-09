'''class Character:
    def __init__(self, health):
        self.__health = health

    def drop(self, amount):
        self.__health -= amount
        if self.__health <= 0:
            self.__health = 0
        print("Health after damage:", self.__health)

    def status(self):
        if self.__health <= 0:
            print("Character is dead")
        else:
            print("Character is alive")

    def get_health(self):
        return self.__health

o1 = Character(damage=20, heal=10, health=100)

o1.drop(50)
o1.status()
print("Current Health:", o1.get_health())'''

'''class Person:
    def __init__(self,name):
        self.name=name
    def learning(self):
        print("person studying")
class Student(Person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll = roll
    def learning(self):
        print("student studying")
class CvCorpStudent(Student):
    def __int__(self,name,roll):
        super().__init__(name)
        self.roll=roll
    def learning(self):
        super().learning()
p1=CvCorpStudent('xyz',20)
p1.learning(True)'''

from abc import ABC,abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self):
        pass
class EmailNotification(Notification, ABC):
    def send(self):
        print("email sending")
class SMSNotification(Notification, ABC):
    def send(self):
        print("sms sending")
class PushNotification(Notification, ABC):
    def send(self):
        print("Push sending")

e=EmailNotification()
p=PushNotification()
l=(e,p)
for i in l:
    i.send()









