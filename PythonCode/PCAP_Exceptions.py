print("My name is "+str(123))

try:
    print("My name is "+str((0.07)))  #SyntaxError in try blocks cannot be caught
except ValueError:
    print("There is a value error")
except TypeError:
    print("Looks like there is a Type Error")
except:  #The regualr except block must always be last!!!
    print("Looks like there is an unknown error")  
else:
    print("No error was raised")
finally:
    print("I am always printed")

my_dict={"Abhimanyu":"Father", "Archana":"Mother"}

for keys,values in my_dict.items():
    print("Name is "+keys+" And the relationship is "+values)

print(my_dict.items())


def calculate(number):
    assert (number!=0),'Got 0 an input!'
    print(1/number)

calculate(1)

def return_bigger(a,b):
    if not isinstance(a, int) or not isinstance(b,int):
        raise ValueError
    if b>a:
        return b
    else:
        return a

print(return_bigger(2,1))

def return_reverse(x):
    try:
        return 1/x
    except:
        print("Something went wrong!")
        #raise   #Will raise the error based on what error was encountered

print(return_reverse(0))

try:
    print("My name is "+int(('0.07a')))  #SyntaxError in try blocks cannot be caught
except Exception as e:   ##creating an object for an exception class
    print(type(e).__name__+" : "+str(e))

print(ValueError.__bases__)

print(ValueError.__name__)

print(ZeroDivisionError.__bases__)


### We can also make our own exception classes

class AnimalValueError(ValueError):
    pass

print(AnimalValueError.__name__)

anerr=AnimalValueError()

print(type(ZeroDivisionError))


#print(anerr.__bases__)

s = "test string"
try:
    s = s[:100]
except Exception as exc:
    print(exc)

print(type(()))


