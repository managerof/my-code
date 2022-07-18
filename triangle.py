#angle
aa = input('A angle ')
ab = input('B angle ')
ac = input('C angle ')
#side
sa = input('AB side ')
sb = input('BC side ')
sc = input('CA side ')
#formulas

#variable

#code
tra = (aa, ab, ac)

if str('90') in tra:
    print('Треугольник прямой')
    
elif aa == ab in tra:
    print('Треугольник равносторонний')
    
elif ab == ac in tra:
    print('Треугольник равносторонний')
    
elif ac == aa in tra:
    print('Треугольник равносторонний')
    
else:
    print('Vash trikutnik hernia')