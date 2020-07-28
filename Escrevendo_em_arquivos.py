"""
Escrevendo em Arquivos

#OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas ler,
Da mesma forma, se abrirmos um arquivo para escrita, não podemo le-lo, somente escrever nele.

# Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional

Para escrevermos dados em um arquivo, após abrir o arquivo utrilizamos a função write().
Está função recebe uma string como parâmetro. Caso contrario teremos um TypeError

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir será criado,
caso ele já exista, o anterior sera apagado e um novo será criado. Dessa forma, todo
o conteudo no arquivo anterior é perdido.

# Exemplo de escrita - modo 'w' - write (escrita)

#Forma Tradicional
arquivo = open('mais.txt', 'w')

arquivo.write('Um texto qualquer.\n')
arquivo.write('Mais um texto')

arquivo.close()


#Forma Pythônica
with open('novo.txt', 'w') as arquivo:
    arquivo.write('Novos dados.\n')
    arquivo.write('Podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Esta é a ultima linha.')

with open('geek.txt', 'w') as arquivo:
    arquivo.write('Geek ' * 1000)
"""
with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break



