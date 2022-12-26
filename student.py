class Student:
	def __init__(self):
		self.name="durga"
		self.rollno=202
		self.marks=100
	def talk(self):
		print("my name is :",self.name)
		print("my marks was :",self.marks)
		print("my rollno is :",self.rollno)


s=Student()
s.talk()
print(s.name,s.marks,s.rollno)
