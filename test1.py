#print ('START')

if 1 > 2:print('el primero es mayor')
elif 1>0:print('el numero 1')
else: print('el primero no es mayor')


a='numeros'
print('1234'+a)

def hi(name,saludo):

    if name=='Azu':print('Hi there!'+saludo)
    elif name=='Roberto':print('How are you?')



hi('Roberto','BETO')


def hi(name):
    print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']

for name in girls:
    hi(name)
    print('Next girl')


for i in range(1, 6):
    print(i)
