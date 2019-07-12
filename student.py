class Student:
    def __int__(self, name, ID, GPA):
        self.Name = name
        self.id = ID
        self.gpa = GPA
    def displayInfo(self):
        print(self.Name)
        print(self.id)
        print(self.gpa)
    def gradWithHonors(self):
        if self.gpa >= 3.85:
            return True
        else:
            return False

        
