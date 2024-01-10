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





