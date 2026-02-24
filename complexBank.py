#Complex bank system using opp(poo)
from datetime import date, datetime

class Client: #Client class to associate an individual client to his related datas.
    def __init__(self, cliente_cpf, cliente_name, cliente_email, cliente_birthday):
        self.cpf = cliente_cpf
        self.name = cliente_name
        self.email = cliente_email
        self.birthday = cliente_birthday
        

def catching_data(): #Function used to catch client infomations
    client_cpf = input(int("Digite o seu cpf: "))
    client_name = input("Digite o seu nome completo: ")
    client_email = input("Digite seu email: ")

    while True: #Code block used to convert the string of de the date on a real date using datime classes methods
        cliente_birthday = input("Digite a sua data de nascimento (00/00/0000): ")
        try:
            cliente_birthday = datetime.strptime(cliente_birthday,"%d/%m/%Y").date()
            break
        except:
            print("Formato de data inválido.")

    client_data = [client_cpf, client_name, client_email,cliente_birthday]
    return client_data













