import xlrd
import pandas as pd

dir_local = 'C:\\00Trabalho\\09BBNexidia\\01FormatadorPlanilha\\00Entrada\\'
nome_arq = 'CTR202174210791_Nexidia_BB ( Sep 16, 2021 08_00 AM ).xls'

#arquivo = xlrd.open_workbook(nome_arq)
#
#planilha = arquivo.sheet_by_name('Tabular Reports')
#
#coluna = planilha.col_values(0)
#coluna = planilha.col_values(1)

df = pd.read_excel(dir_local+nome_arq, sheet_name='Tabular Reports', usecols="A:K", skiprows=8)
df.rename(columns={' ':'request_id',
                   'CLASSIFICAÇÃO':'classificacao',
                   'CLIENTE SITE':'cliente_site',
                   'Prioridade':'prioridade',
                   'Hora de criação':'hora_criacao',
                   'Solicitante':'solicitante',
                   'Hora da Solução':'hora_solucao',
                   'Tempo decorrido':'tempo_decorrido',
                   'Tempo gasto':'tempo_gasto',
                   'Unnamed: 10':'total_gasto'}, inplace=True)
df.drop(columns='Unnamed: 1', inplace=True)
print(df)