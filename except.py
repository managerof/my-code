while True:
    try:
        enter = float(input('Write number '))
        print(100/enter)
    
    except ValueError:
        print('You didn`t wrote a number')
        
    except ZeroDivisionError:
        print('Division by zero')
        
    else:
        print('User is cool!!!')
        
    finally:
        print('Return finally')
        
print('All good!')