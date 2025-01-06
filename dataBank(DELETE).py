import sqlite3

try: 
    banco = sqlite3.connect('dataBank.db') # Cria e conecta o banco de dados

    cursor = banco.cursor()

    cursor.execute("DELETE FROM pessoas WHERE age = '23'") #Aqui cria a tabela
    print('Verifique se o valor foi deletado corretamente!')

    banco.commit() #Aqui salva as alterações

except sqlite3.Error as erro:
    print('Erro ao deletar os valores:', erro)