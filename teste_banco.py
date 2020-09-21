from models.cliente import Cliente
from models.conta import Conta

felicity: Cliente = Cliente('Felicity Jones', 'felicity@gmail.com', '123.456.789-10', '02/09/1987')
angelina: Cliente = Cliente('Angelina Jolie', 'angelinajolie@gmail.com', '987.654.321-01', '31/12/1978')

#print(felicity)
#print(angelina)

contaf : Conta = Conta(felicity)
contaa : Conta = Conta(angelina)

#print(contaf)
#print(contaa)