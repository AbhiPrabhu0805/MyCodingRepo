### Object Oriented Programming from the PCAP course

def test_func(tst):
    test_attr=1
    tst+=test_attr
    return tst

test_func.test_attr=2

print(test_func(1))
print(test_func.test_attr)

##Class variable exists even if the class has o object cretaed


class Dog:
    counter=0
    def __init__(self, name, age):
        self.__name=name
        self.age=age
    
my_pet=Dog("Jenny",1)

print("Pets name is:",my_pet._Dog__name,"and the age of the pet is:", my_pet.age)

print(my_pet.__dict__)

print(Dog.__dict__)

print(hasattr(my_pet,'_Dog__name'))
print(hasattr(my_pet,'__name'))
print(hasattr(my_pet,'age'))

print(hasattr(Dog,'_Dog__name'))

print(hasattr(Dog,'counter'))

print(hasattr(Dog,'age'))

print(Dog.__name__)

print(type(my_pet).__name__)

print(type(2).__name__)

print(type(my_pet))

print(type(2))

print(Dog.__module__)


## We cannot use return statements in a constructor method in a class (__init__)

#we can even make a method inside a class private by using __

class Cat:
    counter=0
    def __init__(self, name, age):
        self.__name=name
        self.age=age
        #self.__private_method()
    
    def __private_method(self):
        print('I am private')

kitty=Cat("Mewtwo",1)
print(kitty._Cat__name)
kitty._Cat__private_method()

class Cub:
    counter=0
    def __init__(self):
        self.__name="Cubby"
        self.age=10
        #self.__private_method()

Simba=Cub()

print(Simba.counter)

def empty_strings(user_object):
    for prop_name in user_object.__dict__.keys():
        prop_value=getattr(user_object, prop_name)
        if isinstance(prop_value, str):
            setattr(user_object,prop_name,'')


print(Simba._Cub__name)
empty_strings(Simba)

print(Simba._Cub__name)

##Inheritence

class Vehicle:
    def __init__(self,speed):
        self.speed=speed

class Landvehicle(Vehicle):
    def __init__(self,speed,wheel_count):
        #Vehicle.__init__(self,speed)
        super().__init__(speed)
        self.wheel_count=wheel_count



class Car(Landvehicle):
    pass

print(issubclass(Landvehicle, Vehicle))

print(issubclass(Car, Landvehicle))

print(issubclass(Car, Car))

print(issubclass(Vehicle, Car))

CRV=Car(60,4)

print(Car.__dict__)

print(CRV.__dict__)

## __bases__ returns a tuple with all the base classes that the class inherits from


print(Car.__bases__)

print(Landvehicle.__bases__)

print(Vehicle.__bases__)

class Upper:
    def __init__(self):
        return 1
        #return False #will fail as we cannot return boolean, onlu None in constructor

#up=Upper()

class Diamond:
    pass

class Adamant(Diamond):
    pass

class Gem(Diamond):
    cnt=1
    def __init__(self):
        self.names="A"

g=Gem()

print(Gem.__bases__)
print(Gem.__name__)
print(Gem.__module__)
print(Gem.__dict__)
print(g.__dict__)
print(hasattr(g,"names"))
print(hasattr(Gem,"names"))
print(getattr(g,"names"))
print(g.__dict__)
print(type(g).__name__)

class A:
    class_variable = 1

    def __init__(self):
        self.instance_variable_init = 2

    def do(self):
        self.instance_variable = 2

class B(A):
    pass


o = B()
o.do()
print(o.class_variable, o.instance_variable)
print(A.__dict__)
print(o.__dict__)

print(A.__module__)
print(o.__module__)
print(Gem.__bases__)
print(Gem.__name__)

a=1
b=2
c=1+1
print(a is b)
print(c is b)