import mysql.connector

def query_sql(query):
    con = mysql.connector.connect(host='151.106.96.1', database='u588158726_RomuloTech', user='u588158726_romulo', password='Rb17571946735@')


    if con.is_connected():
        print("Foi!")
        cursor = con.cursor()
        
        cursor.execute(query)
        #linha = cursor.fetchone()
        #print(linha)
        print("Gravado com sucesso!")
        con.commit()


