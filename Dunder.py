"""
Dunder Name e Dunder Main

Dunder -> Double Under

Dunder Name -> __name__

Dunder Main -> __main__

dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']

Em Python, são utilizados dunder para criar funções, atributos, propriedades e etc utilizando
Double Under para não gerar conflito com os nomes destes elementos na programação.

# Na linguagem C, temos um programa da seguinte forma:

int main(){
    return 0;
}

# Na linguagem Java, temos um programa da seguinte forma:

public static void main(String[] args){

}

# Em Python, se executarmos um modulo Python diretamente na linha de comando, internamente o Python atribuirá a
variável __name__ o valor __main__ indicando que este módulo é o módulo de execução principal.

Main -> Significa Principal

print(__name__)
__main__

if __name__ == '__main__': # Fazer isso na funcoes_com_paramemtrps.py

"""

import primeiro
import segundo

