#global scope

x = 'global x'

def function():
    #x = 'local x'
    print(x)

function()
print(x)

################

name = 'Sefa'

def changeName(new_name):
    name = new_name
    print(name)

changeName('Merve')
print(name)

#############3

name = 'global string'

def greeting():
    name ='Sefa'

    def hello():
        print('Hello' + name)

    hello()
greeting()

#### 
x=50
def test(x):
    print(f'x: {x}')
    x = 100
    print(f'changed x to {x}' )

test(x)