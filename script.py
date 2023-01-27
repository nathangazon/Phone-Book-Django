from datetime import datetime
from random import randint
from faker import Faker
"""
SCRIPT PARA GERAR REGISTROS ALEATÓRIOS NA AGENDA.
"""


fake = Faker(locale='pt-br')

arquivo = open("sqlsInserts.txt", "a", encoding='UTF-8')
sqls = list()

for i in range(2, 205):  # considerando que vc já possui um contato na agenda
    id = i
    nome = fake.first_name()
    sobrenome = fake.last_name()
    nome1 = nome.split()
    email = nome1[0].lower() + '@email.com'
    num_registro = str(i).zfill(3)
    data_criacao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    categoria_id = randint(1, 3)
    telefone = fake.phone_number()
    descricao = fake.sentence()

    valores = (f"INSERT INTO contatos_contato"
               f" (id, nome, sobrenome, telefone, email, data_criacao, descricao, categoria_id)"
               f" VALUES ('{id}', '{nome}', '{sobrenome}', '{telefone}', '{email}',"
               f" '{data_criacao}', 'descricao{num_registro}', '{categoria_id}'); \n")

    sqls.append(str(valores))

arquivo.writelines(sqls)
arquivo.close()
print(f"Feito, foram inseridos {len(sqls)} no arquivo txt!")
