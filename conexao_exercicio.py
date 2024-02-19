import sqlite3 

conexao = sqlite3.connect('exercicio.db')
cursor = conexao.cursor()

'''
cursor.execute('CREATE TABLE alunos(id Int, nome VARCHAR(100), idade Int, curso VARCHAR(100))')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(01,"Luiz",20,"Medicina")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(02,"Yasmim",28,"Engenharia")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(03,"Cezar",22,"Administração")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(04,"Junior",20,"Engenharia")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(05,"Gabriel",22,"Medicina")')

dados = cursor.execute('SELECT * FROM alunos')

dados = cursor.execute('SELECT nome,idade FROM alunos WHERE idade > 20 ')

dados = cursor.execute('SELECT nome FROM alunos WHERE curso="Engenharia" ORDER BY nome asc ')

dados = cursor.execute('SELECT count(*) FROM alunos')

for alunos in dados:
    print(alunos)

cursor.execute('UPDATE alunos SET idade = 27 WHERE idade = 28')

cursor.execute('DELETE FROM alunos WHERE id=05')

cursor.execute('CREATE TABLE clientes(id INTEGER PRIMARY KEY,nome VARCHAR(100),idade INTEGER,saldo FLOAT)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) Values(1, "João Silva", 30, 1000.00)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) Values(2, "Ana Maria", 32, 1200.00)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) Values(3, "Carlos Nunes", 30, 900.00)')   
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) Values(4, "Fabio Costa", 35, 1050.00)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) Values(5, "Marcia Ribeiro", 29, 850.00)')

dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')

dados = cursor.execute("SELECT AVG(saldo)FROM clientes").fetchone()[0]
print(dados)

dados = cursor.execute('SELECT * FROM clientes WHERE saldo=(SELECT MAX(saldo)FROM clientes)')

dados = cursor.execute('SELECT Count(*) FROM clientes WHERE saldo >1000')
for clientes in dados:
    print(clientes)

cursor.execute('UPDATE clientes SET saldo = 950 WHERE saldo = 850')

cursor.execute('DELETE FROM clientes WHERE id=3')

cursor.execute('CREATE TABLE compras (id INTEGER PRIMARY KEY, cliente_id INTEGER, produto VARCHAR(100), valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes(id));')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) Values(1, 4, "calça", 50.00)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) Values(2, 2, "vestido", 80.00)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) Values(3, 4, "camiseta", 65.00)')   
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) Values(4, 1, "calça", 50.00)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) Values(5, 5, "saia", 45.00)')

dados = cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM clientes JOIN compras ON clientes.id = compras.cliente_id')
for usuario in dados:
  print(usuario)
'''

conexao.commit()
conexao.close()

