#  entradas (input) - cadastro  
#\n só para pular uma linha na hora de rodar o código
colaborador = input('\n  Digite o nome do colaborador ') 

salario = float(input('  Digite o valor do salário atual '))

aumento = float(input('  Digite a porcentagem de aumento do salário '))

#   cálculos - valor do aumento e novo salário
valor_do_aumento = salario * (aumento / 100)

novo_salario = salario + valor_do_aumento

# exibição (print) - saída
#\n para quebrar linha e \t para dar um recuo
print('\n\t\t Colaborador - ', colaborador, 
      f'\n\t\t Valor do aumento = {valor_do_aumento:,.2f} '
      f'\n\t\t O novo salário é de = {novo_salario:,.2f} ' )

