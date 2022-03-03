import shutil
import os
import os.path
import datetime
from datetime import datetime
from datetime import date

def move_arq(arquivo,dir,de,para):
    try:
        status='OK'
        dir_ori=os.path.join(dir,de)
        dir_des=os.path.join(dir,para)
        if len(arquivo)>0:
            file_name=arquivo
            shutil.move(os.path.join(dir_ori, file_name), dir_des)
        else:
            file_names = os.listdir(dir_ori)
            for file_name in file_names:
                shutil.move(os.path.join(dir_ori, file_name), dir_des)
    except Exception as e:
        status='NOK' 
    return status

data_hoje = datetime.now().strftime('%Y%m%d')

directory = 'C:\\00Producao\\09BBNexidia\\'

de = '00Entrada\\'

para = '02ArqDiario\\'

#arquivo = data_hoje+'date.txt'
#print(directory+de+arquivo)
#print(data_hoje)
move_arq('CTR_20210930.xls',directory,de,para)
os.remove('C:\\00Producao\\09BBNexidia\\00Entrada\\bb_nexidia.xlsx')
os.remove('C:\\00Producao\\09BBNexidia\\00Entrada\\bb_nexidia.xlsx')
os.startfile('C:\\00Producao\\09BBNexidia\\01ETL\\0000J_CargaAutomatica.bat')
