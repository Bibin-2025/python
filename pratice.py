class father:
    def skills(self):
        print("father:Gardening, Programming")
class mother:
    def skills(self):
        print("mother: Cooking, Art")
class child(father, mother):
    def skills(self):
        father.skills(self)
        mother.skills(self)
        print("child: Sports, Music")

     
c = child()
c.skills()




num_1 = 10
num_2 = 20
str_1 = "Python"
str_2 = "is Awesome."
print(num_1+num_2)
print(str_1+" "+str_2)



print(len("Mashup Stack"))
print(len(["Python", "Django", "Angular"]))
print(len({"Name": "Kevin", "Address": "India"}))
