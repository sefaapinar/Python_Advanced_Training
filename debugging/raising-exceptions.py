# x = 10

# if x >5:
#     raise ValueError('x 5 den büyük olamaz.')


def colorize(text,color):
    colors = ("blue","red","black","orange")
    if type(text) is not str:
        raise TypeError("renk str tipinde olmalıdır.")
    if type(color) is not str:
        raise TypeError("Renk str tipinde olmalıdır.")
colorize("Merhaba","red")
colorize("Selam","blue")