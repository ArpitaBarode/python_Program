#operator overloading
class test:
    def __init__(self,subject1,subject2):
        self.subject1=subject1
        self.subject2=subject2

    def show(self):
        print(self.subject1)
        print(self.subject2)
    def __add__(self,other):
        subject1=self.subject1+other.subject1
        subject2=self.subject2+other.subject2
        return test(subject1,subject2)
t1=test(21,17)
print("marks of sub1")
t1.show()
t2=test(18,17)
print("marks of sub2")
t2.show()
t3=t1+t2
print("total marks")
t3.show()
    
