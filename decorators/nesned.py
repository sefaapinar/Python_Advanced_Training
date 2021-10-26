# def greeting(name):
#     print('Hi',name)

# # print(greeting('Sefa'))


# sayHi = greeting

# print(sayHi)
# print(greeting)


# # print(greeting('Sefa'))
# # print(sayHi('Sefa'))


# #Bu işlem kapsülleme yani encapsulation
# def outer(num1):
#     print('outher')
#     def inner_increment(num1):
#         print('inner')
#         return num1 + 1
#     num2 = inner_increment(num1)
#     print(num1,num2)
# outer(10)

def factorial(number):
    if not isinstance(number,int):
        raise TypeError("number must be an integer")

    if not number >=0:
        raise ValueError("number must be zero or positive")
    def inner_factorial(number):
        if number <=1:
            return 1

        return number * inner_factorial(number -1)

    return inner_factorial(number)

print(factorial(-7))