
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")



class Trainer(Employee):
    def __init__(self, name, role, specialization):
        super().__init__(name, role)
        self.specialization = specialization

    def display(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Specialization: {self.specialization}")



class YogaInstructor(Employee):
    def __init__(self, name, role, yoga_style):
        super().__init__(name, role)
        self.yoga_style = yoga_style

    def display(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Yoga Style: {self.yoga_style}")



class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name, role, specialization, yoga_style):
        # Use super() to ensure proper initialization order
        super().__init__(name, role, specialization)
        self.yoga_style = yoga_style

    def display(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Specialization: {self.specialization}")
        print(f"Yoga Style: {self.yoga_style}")





emp = Employee("John Doe", "Receptionist")

trainer = Trainer("Alice Smith", "Trainer", "Weight Training")

yoga_instructor = YogaInstructor("Raj Kumar", "Yoga Instructor", "Hatha Yoga")

multi_trainer = MultiTrainer("Sara Lee", "Multi Trainer", "CrossFit", "Vinyasa Yoga")


print("=== Employee ===")
emp.display()
print("\n=== Trainer ===")
trainer.display()
print("\n=== Yoga Instructor ===")
yoga_instructor.display()
print("\n=== Multi Trainer ===")
multi_trainer.display()
