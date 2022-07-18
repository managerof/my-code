#Hello!

file = open("AtlantBaby.txt", "w+", encoding='utf-8')

file.write('Hello!')

file.close()

def c(name, listt):
    file = open(name+'.txt', "w+", encoding='utf-8')
    file.write('Hello!')
    file.close()