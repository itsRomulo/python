import matplotlib.pyplot as plt 



x = ['2', '4', '6', '8'] 
trabalhados = [673, 431, 599, 572] 
cpc = [255, 96, 213, 203] 
agendado = [106, 40, 87, 102] 
plt.bar(x, trabalhados, color='cornflowerblue') 
plt.bar(x, cpc,  bottom=trabalhados,  color='royalblue') 
plt.bar(x, agendado, bottom=[i+j for i,j in zip(trabalhados, cpc)], color='mediumseagreen')

for i in range(len(cpc)):
    
    plt.annotate(str(cpc[i]), xy=(x[i],cpc[i]), ha='center', va='bottom')

for i in range(len(trabalhados)):
    
    plt.annotate(str(trabalhados[i]), xy=(x[i],trabalhados[i]), ha='center', va='bottom')

for i in range(len(agendado)):
    
    plt.annotate(str(agendado[i]), xy=(x[i],agendado[i]), ha='center', va='bottom')

plt.legend(["Trabalhados", "CPC", "Agendado"]) 
plt.title("Trabalhados, CPC e Agendados") 
plt.show() 