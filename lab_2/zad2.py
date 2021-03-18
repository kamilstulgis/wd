import sys

print('Podaj pierwsza liczbe: \n')
x = sys.stdin.readline()
print('Podaj druga liczbe: \n')
y = sys.stdin.readline()
z = int(x)*int(y)
sys.stdout.write(str(z))