from datetime import *
n = input('Digite seu nome:')
dtn2 = datetime.now()
dtn = int(datetime.now().hour)
if dtn < 12 and dtn >= 6:
    s = 'Bom dia!'
elif dtn >= 12 and dtn < 18:
    s = 'Boa tarde!'
else:
    s = 'Boa noite!'

print('Olá {}, {} '.format(n, s))
print('Entrada: {}'.format(dtn2.strftime(' %d/%m/%Y %H:%M:%S')))
print('Saida: {}'.format(dtn2.strftime(' %d/%m/%Y {}:%M:%S'.format(dtn + 1))))
