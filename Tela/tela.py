import PySimpleGUI as sg
import conexaomysql
import mysql.connector

class TelaPython:
    def __init__(self):
        #layout
        layout = [
        [sg.Text('Cliente:',), sg.Input(key='cliente')],
        [sg.Text('Problema Apresentado:'), sg.Input(key='problema')],
        [sg.Text('Solução:'), sg.Input(key='solucao')],
        [sg.Text('Data de Recebimento:'), sg.Input(key='datareceb')],
        [sg.Text('Data de Entrega:'), sg.Input(key='dataentreg')],
        [sg.Text('Status do Atendimento:'), sg.Combo(['Resolvido','Pendente', 'Aguardando Cliente', 'Aguardando Compra'], key='statusatend')],
        [sg.Text('Valor do Serviço:'), sg.Input(key='valor')],
        [sg.Text('Desconto:'), sg.Input(key='desconto')],
        [sg.Text('Total a receber:'), sg.Input(key='total')],
        [sg.Text('Data do Pagamento:'), sg.Input(key='diadopag')],
        [sg.Text('Status do Pagamento:'), sg.Combo(['Pago','Pendente','Em atraso'], key='statuspag')],
        [sg.Button('Salvar'), sg.Button('Voltar')]
        
        ]

        #janela
        self.janela = sg.Window("Atendimento").layout(layout)
        
        #extrairosdados
        #self.button, self.values = self.janela.Read()

    def Iniciar(self):
        while True:    
            
            self.button, self.values = self.janela.Read()
            cliente = self.values['cliente']
            problema = self.values['problema']
            solucao = self.values['solucao']
            datareceb = self.values['datareceb']
            dataentreg = self.values['dataentreg']
            statusatend = self.values['statusatend']
            valor = self.values['valor']
            desconto = self.values['desconto']
            total = self.values['total']
            diadopag = self.values['diadopag']
            statuspag = self.values['statuspag']
            #print(self.values)
            #Query
            #INSERT INTO `ATENDIMENTOS`(`id_atendimento`, `cliente`, `problema`, `solucao`, `dataatend`, `dataentrega`, `statusatend`, `valor`, `desconto`, `total`, `datapag`, `statuspag`) 
            #VALUES ('', 'Liane', 'DNS não responde', 'Retirar o IP de DNS',   '25/01/2022', '25/01/2022',  'Resolvido',  '30',  '',   '', '',  'Pendente' );
            query = "INSERT INTO `ATENDIMENTOS`(`id_atendimento`, `cliente`, `problema`, `solucao`, `dataatend`, `dataentrega`, `statusatend`, `valor`, `desconto`, `total`, `datapag`, `statuspag`) VALUES ('', '"+cliente+"', '"+problema+"', '"+solucao+"', '"+datareceb+"', '"+dataentreg+"', '"+statusatend+"', '"+valor+"', '"+desconto+"', '"+total+"', '"+diadopag+"','"+statuspag+"')"
            print(query)
            conexaomysql.query_sql(query)

tela = TelaPython()
tela.Iniciar()