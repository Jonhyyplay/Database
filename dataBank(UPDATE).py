import sqlite3

try:
    banco = sqlite3.connect('dataBank.db') # Conecta o banco de dados

    cursor = banco.cursor() 

    cursor.execute("UPDATE pessoas SET *** = '' WHERE *** = ''") #Aqui atualiza os valores na tabela
    print('Valores atualizados com sucesso!')

    banco.commit() #Aqui salva as alterações

except sqlite3.Error as erro:
    print('Erro ao atualizar os valores:', erro)