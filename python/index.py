def multi_print(string):
    print("""{}
    looping
    function
    object oriented programming
    """.format(string))

def run_multi_print():
    multi_print("python")

def print_type(param):
    print(type(param))

def run_print_type():
    print_type("hello")
    print_type(5)
    print_type(5.5)
    print_type(True)


def run_list_operations():
    fruits=["apple","banana","cherry"]

    fruits.append("orange")
    fruits.insert(1,"mango")
    fruits.remove("banana")
    fruits.pop()
    print(fruits)

    print(fruits[0:2])
    print(fruits[-1])

    tuple=("apple","banana","cherry")
    print(tuple)
    print(tuple[0:2])

    tuple=3,"hello",5.5  #packing
    print(tuple)

    a,b,c=tuple
    print(a)

    for i in tuple:
        print(i)

    print(tuple[0:2])

    set={1,2,3,4,5,6,7,8,9,10}
    print(set)

    set.add(11) #add()=add element in set
    set.remove(3) #remove()=remove element from set
    print(set)

    setb={1,2,3,4,5,6,7,8,9,10}

    print(set.intersection(setb)) #intersection()=return common elements
    print(setb.intersection(set))

    print(setb.symmetric_difference(set)) #symmetric_difference()=return uncommon elements

    a={1,2,3,0,5}
    print(all(a)) #all()=return true if all elements are true


    list=[10,6,2,9,1,5,3,7,8,4]
    print(sorted(list,reverse=True)); #sorted()=sort the list

def run_person_class():
    class Person:
        def __init__(self,name,age):
            self.name=name
            self.age=age

        def myfunc(self):
            print("Hello my name is "+self.name)

    p1=Person("John",36)
    print(p1.name)
    print(p1.age)
    p1.myfunc()

def run_dict_operations():
    dict={
        "name":"John",
        "age":36,
        "country":"Norway"
    }

    print(dict)
    print(dict["name"])

    new_dict=dict([('name','John'),('age',36)]) #dict()=create dictionary from list of tuples
    print(new_dict)

def run_math_operations():
    print(5//2)  #// = floor division
    print(5**2)  #** = exponentiation
    print(5%2)   #% = modulus
    print(5*2)   #* = multiplication
    print(5+2)   #+ = addition


def operators():
    # comparison operators
    print(5==2)  #== = equal to
    print(5!=2)  #!= = not equal to
    print(5>2)   #> = greater than
    print(5<2)   #< = less than
    print(5>=2)  #>= = greater than or equal to
    print(5<=2)  #<= = less than or equal to

    # logical operators
    print(5>2 and 5<10) #and = returns true if both statements are true
    print(5>2 or 5<10)  #or = returns true if one of the statements is true
    print(not(5>2 and 5<10)) #not = reverse the result,returns false if the result is true

    # identity operators
    # print(5 is 5) #is = returns true if both variables are the same object
    # print(5 is not 5) #is not = returns true if both variables are not the same object

    # membership operators
    list=[1,2,3,4,5]
    print(5 in list) #in = returns true if a sequence with the specified value is present in the object
    print(5 not in list) #not in = returns true if a sequence with the specified value is not present in the object


def check_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True

def print_primes():
    for i in range(2,101):
        if check_prime(i):
            print(i)

def print_triangle1():
    for i in range(1,5):
        for j in range(1,i+1):
            print(j,end=" ")
        print()

def print_triangle2():
    for i in range(1,5):
        for j in range(1,i+1):
            print(i,end=" ")
        print()

def print_triangle3():
    for i in range(1,5):
        for j in range(1,5):
            if(j<i):
                print(" ",end=" ")
            else:
                print("*",end=" ")
        print()

def greater(a, b):
    if a > b:
        return "a is greater than b"
    elif a < b:
        return "a is less than b"
    else:
        return "a is equal to b"
    
def check_prime(n):
    
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True