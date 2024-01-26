## list comprehension

lst_1=[i for i in range(0,100)]
print(lst_1)
lst_2=[i for i in range(0,100) if i%2==0]
print(lst_2)
lst_3=[i%2 for i in range(0,100)]
print(lst_3)
lst_4=[0 if i%2==0 else 1 for i in range(0,100)]
print(lst_4)
lst_5=[[i for i in range(5)] for i in range(5)]
print(lst_5)

##Generator and Iterator
def gen(x):
    for i in range(x):
        yield i

gen_itr=gen(10)

print(next(gen_itr))
print(next(gen_itr))
print(next(gen_itr))
print(next(gen_itr))
print(next(gen_itr))
print(next(gen_itr))


## Lambda function

sqr=lambda x: x**2
print(sqr(5))

summ=lambda x,y: x+y
print(summ(5,6))

print(type(summ))

## map & filter
##map by itself returns an iterable object so we need to use next()

init_list=[1,2,3,4,5]
lam=lambda x:x*2
mapped=map(lam,init_list)
print(next(mapped))
print(next(mapped))
print(next(mapped))

##another approach

init_list2=[1,2,3,4,5]
lam2=lambda x:x*2
mapped2=map(lam2,init_list2)
print(list(mapped2))


init_list3=[1,2,3,4,5]
lam3=lambda x:x%2==0
filtered=filter(lam3,init_list3)
print(list(filtered))


##Closures
#A closure is a function inside another function that remembers the values from the outer function



def greet(text):
    def print_greet():
        print(text)

    return print_greet

say_hi=greet('Hello')
print(say_hi())

##File handling
##Need to connect to a stream which opens the file and need to ensure we close it

try:
    stream=open('README.md')
    stream.close()
except Exception as e:
    print("An error occurred:",str(e))


try:
    stream=open('module_1.py')
    print(stream.read(10)) #read bytes/characters at a time, based on the parameter defined. !0 in this case
    print(stream.read(10))
    print(stream.read(20))
    stream.close() 
except Exception as e:
    print("An error occurred:",e)

# No issue in printing more than the # of characters will have
try:
    stream=open('module_1.py')
    print(stream.read()) #with no input parameter, it will read the whole file. THis might be a risk if you are reading a huge file (TBs in size)
    stream.close() 
except Exception as e:
    print("An error occurred:",e)


print('Trying readline now')

try:
    stream=open('module_1.py')
    print(stream.readline()) #will read 1 line at a time
    print(stream.readline()) 
    stream.close()
except Exception as e:
    print("An error occurred:",e)

## We can also use readlines to read atleast the specified number of charaters
print('Trying readlines now')

try:
    stream=open('module_1.py')
    lines=stream.readlines() ##return list of strings
    print('the number of lines in the file:',len(lines)) 
    for line in lines:
        print(line)
    stream.close()
except Exception as e:
    print("An error occurred:",e)


try:
    stream=open('module_1.py')
    lines=stream.readlines(5)
    print('the number of lines in the file:',len(lines)) 
    for line in lines:
        print(line)
    stream.close()
except Exception as e:
    print("An error occurred:",e)


####We can even open streams for reading without the need to explicitly close it if we use the below syntax/method:
print('Reading directly from stream')

try:
    stream=open('module_1.py')
    for line in stream:
        print(line, end=' ')
except Exception as e:
    print("An error occurred:",e)   

### writing data into files

try:
    stream=open('write_test.txt','w')
    stream.write("The 1st line in the file")
    stream.close()
except Exception as e:
    print("An error occurred:",e)  

##Binary files
    
data =bytearray(100)
#range of number from 0-255
data[0]=100 #cant store anything bigger than 255
data[1]=120

try:
    stream=open('file.bin','wb')
    stream.write(data)
    stream.close()
except Exception as e:
    print("An error occurred:",e) 

#### Uisng readinto to read in into a bytearray vs bytes object. Bytes objects is immutable
    
data = bytearray(10)
try:
    bf = open('file.bin', 'rb')
    bf.readinto(data)
    bf.close()
except Exception as e:
    print('An error occured:', e)

#### file handling arguments/modes
### + for both read and write (update)
    
## Predefined streams
    
#sys.stdin ## reads user input from keyboard
    #quits when we enter q

#sys.stdout very simialr to print but less useful
    
#sys.stderr


##errno prints the error number associated with an error

    
    
