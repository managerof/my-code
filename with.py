r = open('file.txt', 'a')
r.write('something' + '\n')
r.write('something')
r.close()

print('all good')