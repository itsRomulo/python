from turtle import color
import matplotlib.pyplot as plt

def gstackedbar(values,title,filename):
    
    #Valores da Linha X do gráfico
    label1 = ['Trabalhados'] #Valor de X da Coluna 1
    trabalhados = values[0] #coluna1
    alo = values[1]   #Recebendo parâmetros
    label2 = ['Trabalhados x Alô'] #Valor de X da Coluna 2
    cpc = values[2]  #Recebendo parâmetros
    label3 = ['Alô x CPC'] #Valor de X da Coluna 3
    agendados = values[3] #Recebendo parâmetros
    label4 = ['CPC x Agendados'] #Valor de X da Coluna 4
    width = 0.35       # the width of the bars: can also be len(x) sequence
    
    fig, ax = plt.subplots(1, figsize=(12,6)) #Define o tamanho do gráfico de acordo com o figsize
    
    
    coluna2 = trabalhados - alo  #Cálculo da Coluna 2
    coluna3 = alo - cpc #Cálculo da Coluna 3
    coluna4 = cpc - agendados #Cálculo da Coluna 4
   
    #Monta o gráfico
    p1=ax.bar(label1, trabalhados, width,  label='Trabalhados', color='#689ff7')
    p2=ax.bar(label2, alo, width,   label='Alô', color='#3ddb9a')
    p3=ax.bar(label2, coluna2, width, bottom=alo,  color='#689ff7')
    p4=ax.bar(label3, cpc, width,   label='CPC', color='#e68d75')
    p5=ax.bar(label3, coluna3, width, bottom=cpc, color='#3ddb9a')
    p6=ax.bar(label4, agendados, width, label='Agendados', color='#dade73')
    p7=ax.bar(label4, coluna4, width,  bottom=agendados, color='#e68d75')

    #Define parâmentros dos valores de X e Y
    ax.tick_params(axis='x', labelsize=18)
    ax.tick_params(axis='y', labelsize=14)

    #Calcula o valor de cada % e junta em uma string
    pColuna1 = str(values[0]) + '\n(100%%)' #Valor Fixo de 100% da coluna 1
    pAloxTrab = str(values[1]) + '\n' + '(' + str(round((alo*100)/trabalhados)) + '%%)' #String do % de Alo x Trabalhados
    pTrabxAlo = str(coluna2) + '\n' + '(' + str(100 - round((alo*100)/trabalhados)) + '%%)' #String do inverso de Alo x Trabalhados
    pCPCxAlo = str(values[2]) + '\n' + '(' +  str(round((cpc*100)/alo))  + '%%)' #String do % de CPC x Alo
    pAloxCPC = str(coluna3) + '\n' + '(' +  str(100 - round((cpc*100)/alo))  + '%%)' #String do inverso de CPC x Alo
    pAgendadosxCPC = str(values[3]) + '\n' +  '(' + str(round((agendados*100)/cpc))  + '%%)' #String do % de Agendados x CPC
    pCPCxAgendados = str(coluna3) + '\n' +  '(' + str(100 - round((agendados*100)/cpc))  + '%%)' #String do inverso de Agendados x CPC

    #Formata as labels da tabela
    ax.bar_label(p1, fmt=pColuna1, label_type='center', fontsize=14)
    ax.bar_label(p2, fmt=pAloxTrab, label_type='center', fontsize=14)
    ax.bar_label(p3, fmt=pTrabxAlo, label_type='center', fontsize=14)
    ax.bar_label(p4, fmt=pCPCxAlo, label_type='center', fontsize=14)
    ax.bar_label(p5, fmt=pAloxCPC, label_type='center', fontsize=14)
    ax.bar_label(p6, fmt=pAgendadosxCPC, label_type='center', fontsize=14)
    ax.bar_label(p7, fmt=pCPCxAgendados, label_type='center', fontsize=14)

    
    ax.set_title(title, fontsize=18, color='#444') #Tamanho do título da tabela
    ax.legend(fontsize=14) #Tamanho do título da tabela

    plt.show()
    #plt.savefig(filename, dpi=300)

values = [400,250,170,50]
title = "Resultado de 28/02/2022"
perc = ['\n(5%%)', '10%', '20%', 'teste']
gstackedbar(values, title, "filename")
