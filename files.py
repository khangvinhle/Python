f = open('1k.txt', 'w')
for index in range(1000):
    f.write(str(index + 1) + '\n')
f.close()
