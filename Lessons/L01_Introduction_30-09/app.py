a = 5
print(a)

print(id(a)) # id(a) returns the memory address of a
b = 6

a= 4

print(id(a)) # now a references something else in memory --> some objects are immutable 
# once created won't change and a new object will be instead created, losing the old one 

print(a)

a = None

print(type(a))

# Tuples 
print((a, "4.2", 4, b, 5, 4))

a = range(100)

def item(x):
    return x%2

b = list(filter(item, a))

print(b)
print(list(map(lambda x:x**2, a)))

c = [{"name":"giovanni", "age":25}, {"name":"luca", "age":29}, {"name":"pippo", "age":42}]

print(sorted(c, key=lambda x:x['age'], reverse=True))
print(list(filter(lambda x:x['age']<30, c)))

# Dictionary comprension

print({el: el**2 for el in b if el < 10})
x=[1,2,3]
y=[1,4,9]

print(sum(list(map(lambda w: (w[0]- w[1])**2, zip(a,b))))**0.5)

class Triangle:
    __x = 5
    
    def __init__(self):
        self.__init__(1,2,3)
        
    def __init__(self, l1:float, l2:float, l3:float)->None:
        self.l1=l1
        self.l2=l2
        self.l3=l3
        self.__per = l1+l2+l3
    
    def returnEdges(self)->list[float]:
        return [self.l1, self.l2, self.l3]
    
    def perimeter(self)->float:
        return self.l1+self.l2+self.l3
    
    def __prova(self):
        return 6
    
    

t1 = Triangle(3,4,5)
print(t1.perimeter())
# Both errors
#print(t1.__x)
#print(t1.__prova())

# when we import a module, we first run the init file inside the package containing the module
# then the code inside the module called is executed (or the single function if import only one)
# we can then use function, classes and methods of said module

# this if statement controls if the file is run by terminal or play (true)
# or run inside another file which will be false
if __name__ == '__main__':
    print("Hello")