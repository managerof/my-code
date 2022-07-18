import os
import time

list = []

for adress, dirs, files in os.walk('D:\\py'):
    for file in files:
        full = os.path.join(adress, file)
        if '.png in list':
            list.append(full)
    
print(list)



