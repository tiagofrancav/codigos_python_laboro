"""
for(etapa1, etapa2, etapa3):{

}

"""

## Exemplo 1 - Contador de 1 a 10, não conta o valor final 10 vai até 9.
for contador in range(1, 11):
    print(contador, end=' ') 

print("\n")
print('-' * 20)

## Exemplo 2 - Contador de 10 a 1, não conta o valor final 1 vai até 2.
for contador in range(10, 0, -1):
    print(contador, end=' ')
# end=' ' -> Imprime na mesma linha, inicialmente o padrão é '\n' que pula a linha.

print("\n")
print('-' * 20)


## Exemplo 3 - Contador de 1 a 10, pulando de 2 em 2.
for contador in range(0, 22, 2):
    print(contador, end=', ')

print("\n")
print("-" * 20)

## Atividade 1 - Contador de 10 a 500, pulando de 10 em 10.
for contador in range(10, 501, 10):
    print(contador, end=', ')