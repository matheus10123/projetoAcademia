mensalidade = int
inscricao = 50
nome = input('Digite nome e sobrenome.')
endereco = input('Digite endereço.')
telefone = input('Digite seu numero de telefone.')
telefone2 = input('Digite um numero reserva.')
estudante = input('Estudante? [True/False]').lower().capitalize()
if (estudante == 'True' or estudante == 'Yes'):
    mensalidade = 200
    instituicao_ensino = input('Instituição de ensino:')
    print('Taxa de inscrição + Mensalidade:{}'.format(mensalidade + 50))
else:
    mensalidade = 300
    print('Taxa de inscrição + Mensalidade:{}'.format(mensalidade + 50))
email = input('Digite seu Email:')
experiencia = input('Experiência com academia ou primeira vez?:')
saude = input('Problemas de saude ou lesões?[True/False]').lower().capitalize()
if saude == 'True' or saude == 'Yes':
    situacao = input('Situação:')
    print('Inscrição finalizada')
else:
    print('Inscrição finalizada')
print('-----------------------------------------------')
print(' Informações inseridas:\n Nome: {}\n Endereço: {}\n Telefone: {}\n Telefone reserva: {}\n Estudante?: {}\n'.format(nome, endereco, telefone, telefone2, estudante),
      "Instituição de ensino: {}\n".format(instituicao_ensino) if (estudante == 'Sim' or estudante == 'True') else 'Não estudante\n',
      'Email: {}\n Experiencia: {}\n Problemas de saúde?: {}\n'.format(email, experiencia, saude),
      'Situação: {}'.format(situacao) if saude == 'sim' or saude == 'True' else 'Saudavel :)\n', 'Mensalidade:{}'.format(mensalidade))
print('-----------------------------------------------')

