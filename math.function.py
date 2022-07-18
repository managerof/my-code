#p1pearony

def qb(par):
    ## возводит введеное число в квадрат
    return par**2

def qb3(par):
    ## возводит введеное число в куб
    return par**3

def qb0(par):
    ## извлекает корень из числа
    return par**0.5

def dgr(par,degree):
    ## возводит число в степень 'par' - число,'deegre' - степень
    return par**degree

def D(a,b,c):
    ## выводит значение дискриминанта
    D = b*b+4*a*c
    return D

def dx(a,b,c):
    ## выводит значение дискиминанта и двух его корней
    D = b*b+4*a*c
    x1 = -b+pow(D, 0.5)
    x2 = -b-pow(D, 0.5)
    return D, x1, x2

#print(dx(2,4,0))