'''
Valor Total da Folha Salarial -> Qual foi o gasto total com salários de funcionários pela empresa?

Qual foi o faturamento da empresa?

Qual o % de funcionários que já fechou algum contrato?

Calcule o total de contratos que cada área da empresa já fechou

Calcule o total de funcionários por área

Qual o ticket médio mensal (faturamento médio mensal) dos contratos?

'''
import pandas as pd

#   ENTRADA DAS BASES DE DADOS
servicos_prestados = pd.read_excel('BaseServiçosPrestados_MiniProjeto.xlsx')
cadastro_clientes = pd.read_csv('CadastroClientes_MiniProjeto.csv', sep=';', decimal=',')
cadastro_funcionarios = pd.read_csv('CadastroFuncionarios_MiniProjeto.csv', sep=';', decimal=',')

#   1- VALOR TOTAL DA FOLHA SALARIAL
total_SalarioBase = cadastro_funcionarios['Salario Base'].sum()
total_Impostos = cadastro_funcionarios['Impostos'].sum()
total_Beneficios = cadastro_funcionarios['Beneficios'].sum()
total_VT = cadastro_funcionarios['VT'].sum()
total_VR = cadastro_funcionarios['VR'].sum()

total_Geral = total_SalarioBase + total_Impostos + total_Beneficios + total_VT + total_VR
print('=-' * 40)
print('================ 1 - FOLHA SALARIAL TOTAL ================')
print(f''
      f'O Total gasto com Salário Base foi de:      R${total_SalarioBase:.2f}\n'
      f'O Total gasto com Impostos foi de:          R${total_Impostos:.2f}\n'
      f'O Total gasto com Beneficios foi de:        R${total_Beneficios:.2f}\n'
      f'O Total gasto com Vale Transporte foi de:   R${total_VT:.2f}\n'
      f'O Total gasto com Vale Refeição foi de:     R${total_VR:.2f}\n\n'
      f'O Total gasto na Folha Salarial foi de:     R${total_Geral:.2f}')

#     2- FATURAMENTO DA EMPRESA
faturamentos_df = servicos_prestados[['ID Cliente', 'Tempo Total de Contrato (Meses)']].merge(cadastro_clientes[['ID Cliente', 'Valor Contrato Mensal']], on='ID Cliente')
faturamentos_df['Faturamento Total'] = faturamentos_df['Tempo Total de Contrato (Meses)'] * faturamentos_df['Valor Contrato Mensal']

print('================ 2 - FATURAMENTO DA EMPRESA ================')
print(f"O Faturamento Total foi de:                 R${sum(faturamentos_df['Faturamento Total']):.2f}")

#     3- CONTRATOS FECHADOS (%)
qtd_contratos_fechados = len(servicos_prestados['ID Funcionário'].unique())
qtd_funcionarios_total = len(cadastro_funcionarios['ID Funcionário'])

print('================ 3 - CONTRATOS FECHADOS (%) ================')
print(f'A porcentagem de funcionários que fecharam contratos foi de: {qtd_contratos_fechados/qtd_funcionarios_total:.2%}')

#     4- CONTRATOS POR ÁREA
contratos_area = servicos_prestados[['ID Funcionário']].merge(cadastro_funcionarios[['ID Funcionário', 'Area']], on='ID Funcionário')
qtd_contratos_area = contratos_area['Area'].value_counts()

print('================ 4 - CONTRATOS POR ÁREA ================')
print(qtd_contratos_area)

#     5- FUNCIONÁRIOS POR ÁREA
funcionarios_area = cadastro_funcionarios['Area'].value_counts()

print('================ 5 - FUNCIONÁRIOS POR ÁREA ================')
print(funcionarios_area)

#     6- TICKET MÉDIO
ticket_medio = cadastro_clientes['Valor Contrato Mensal'].mean()

print('================ 6 - TICKET MÉDIO ================')
print(f'O Ticket médio mensal dos contratos é de:   R${ticket_medio:.2f}')
print('=-' * 40)
print('oi')
print('oi git')