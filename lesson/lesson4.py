





#Пример простого декоратора
def my_decorator(func): #2
    
    def wrapper():
        print("Перед выполнением функции") #4
        func() #5
        print("После выполнением функции") #6
        
    return wrapper #3


@my_decorator
def hello():
    print("Hello world!")
    

#  hello() #1 


#Декораторы с аргументами
         # n = 3
def repeat(n):   # step 2   
                   # func = greet()
    def decorator(func): # step 3
        
        def wrapper(*args, **kwargs):
            for i in range(n):   #step 5
                func(*args, **kwargs)   #step 5
                
        return wrapper  # step 4
    return decorator


@repeat(3)  
def greet():
    print("Hello")
    
greet()  #step 1


# Декораторы для классов
                    #MyClass
def class_decorator(cls):
                   #MyClass
    class NewClass(cls):
        
        def new_method(self):
            return print("Новый метод")
        
    return NewClass

@class_decorator
class MyClass:
    
    def old_method(self):
        return print("Old method")
    

#obj = MyClass() # NewClass()
#obj.old_method()
#obj.new_method()









class Person:
    
    
    # Магический метод
    def __init__(self, name, age):
       self.name = name
       self.age = age 
       
    def __str__(self):
        return f"bla bla bla" 
     
     
obj = Person("Pavel", 25)

print(obj)


class Money:
    
    def __init__(self, amount):
        self.amount = amount
        
    def __add__(self, other):
        print(f"{self.amount}-----{other.amount}")
        return f'pass'
    
    def __str__(self):
        return f"{self.amount} som"
    
    def __len__(self):
        return f"pass"
    
m1 = Money(100)
m2 = Money(400)
m3 = m1 + m2
len(m3)



# Встроенные в класс декораторы

class Math:
    
    @staticmethod
    def add(a, b):
        return a + b
    

print(Math.add(1,2))


class Person:
    count = 0
    password = "Def"
    
    def __init__(self, name):
        self.name = name
        Person.count += 1
        
    @classmethod
    def get_population(cls):
        return cls.count
    
    @classmethod    # Person
    def create_person(cls, name):
        return cls(name)
                #Person(John)
    
    person1 = Person("Alice")
    person2 = Person("Bob")
    person3 = Person("Jack")
    print(Person.get_population())
    person4 = Person.create_person("John")
    print(person4.name)