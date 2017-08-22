c = 0
while c == 0:
    r = int(input('O que deseja fazer?:\n -[0]Inscrição\n -[1]Pagar Mensalidade\n -[2]Entrar/Sair\n -[3]Sair.\nDigite um valor:'))
    if r == 0:
        import inscricao
    elif r == 1:
        import pagarMensalidade
    elif r == 2:
        import in_Out
    elif r == 3:
        c = 1
    else:
        print('---------------')
        print('Valor invalido.')
        print('---------------')
print('Até a proxima!')
