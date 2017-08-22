from datetime import date
estudante = input('Estudante?:').lower().capitalize()
if estudante == 'True' or estudante == 'Yes':
    if date.today().day <= 10:
        print('Mensalidade = 200$')
    else:
        print('Mensalidade = 200$ + 10$(multa)')
else:
    if date.today().day <= 10:
        print('Mensalidade = 300$')
    else:
        print('Mensalidade = 300$ + 10$(multa)')


