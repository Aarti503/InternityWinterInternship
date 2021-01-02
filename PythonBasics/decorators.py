def one():
    print("I'm first function")

def two(func):
    print("I'm with parameter,now I'll call one")
    func()

two(one)

#decoratrs
def another_example(func):
    def inner(x,y):
        if y==0:
            return "Invalid Input"
        return func(x,y)
    return inner
#Telling it is a decorator calling
@another_example
def div(a,b):
    return a/b
print(div(9,0))

