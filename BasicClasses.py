
class Person:

    def __init__(self, name):
        self.name = name
        age = 0
        self.age = age
        self.names = []
        import random
        self.height_of_person = random.randint (17,21)/1
    def get_older(self):
        self.age += 1
        if self.age < 21:
            self.height_of_person += 3
            return self.height_of_person
    def about_me(self):
        return ("Hello! I'm " + self.name +  " I am " + str(self.age) +" years old and " + str(self.height_of_person) + " inches tall.")

    def make_friend(self, name):
        self.names.append (name)

    def talk_about_friends(self):
        print (self.name + "'s friends: ----------")
        if self.names == []:
            print ("I don't have any friends yet.")
        else:
            for name in self.names:
                print (name + " is a friend of mine.")
    def walk_far(self):
        distance_walked = self.height_of_person + 1
        print (self.name + " has walked " + str(distance_walked) + " miles so far. Wow!")


# LEAVE THIS CODE AS IS ---------
person1 = Person('Dale')
person2 = Person('Stacey')
person3 = Person('Johnny')
print(person1.about_me())
print(person2.about_me())
print()

person1.get_older()
print(person1.about_me())
person1.talk_about_friends()
person1.make_friend('Rita')
person1.make_friend('Sen')
person1.talk_about_friends()
person1.get_older()
print(person1.about_me())
print()

for i in range(10):
    person2.get_older()
print(person2.about_me())
person2.make_friend('Johanis')
person2.talk_about_friends()
for i in range(15):
    person3.get_older()
print (person3.about_me())
person3.walk_far()
