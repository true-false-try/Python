file_f = open('f.txt', 'r')
file_g = open('g.txt', 'r')
file_h = open('h.txt', 'w')

file_h.write(file_f.read() + ' ' + file_g.read())

file_f.close()
file_g.close()
file_h.close()
