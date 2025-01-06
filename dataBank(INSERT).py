import sqlite3

name = ''
age = 0      #Aqui você pode colocar os valores que deseja inserir no banco de dados
email = ''

banco = sqlite3.connect('dataBank.db') # Cria e conecta o banco de dados

cursor = banco.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS pessoas (name TEXT, age INTEGER, email TEXT)") #Aqui cria a tabela

cursor.execute("INSERT INTO pessoas VALUES ('"+name+"', "+str(age)+", '"+email+"')") #Aqui insere os valores na tabela
print('Valores inseridos com sucesso!')

banco.commit() #Aqui salva as alterações