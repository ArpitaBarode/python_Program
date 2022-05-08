# instancemethod
class student:
    insitution="iips"
    def __init__(self ,a,b):
        self.a=a
        self.b=b

    def show(self):
        print("marks in pyrhon",self.a)
        print("marks in python lab",self.b)
#class method=for get the info about particular contain of class
    @classmethod
    def info(self):

      print("class belongs",self.insitution)
    @staticmethod  
    def about():
        print("this class hold the data of marks obtained by student")

s1=student(12,10)
s2=student(13,11)
s3=student(14,9)
s1.show()
s2.show()
s3.show()
student.info()
student.about()
#print(student.institution)
