import mmap

f = open('reddy.txt')
s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
if s.find('what are you doing !') != -1:
    print('true')
else:
    print ('Fals')
