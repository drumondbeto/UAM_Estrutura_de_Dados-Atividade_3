def Main():
    lista5 = []
    pilha = []
    lista10 = []

    # Passo 1: Insira os numeros [1, 2, 3, 4 e 5] em uma lista - com 5 celulas;
    lista5 = [1,2,3,4,5]
    
    # Passo 2: Remova todos os dados da lista e insira-os em uma Pilha - com 5 celulas.
    # Deve-se sempre remover os dados da celula inicial da lista;
    while len(lista5) > 0:
        pilha.append(lista5[0])
        del lista5[0]


    # Passo 3: Remova os dados da Pilha e insira-os em uma Fila - com 10 celulas);
    while len(pilha) > 0:
        lista10.append(pilha[-1])
        pilha.pop()

    
    # Passo 4: Insira os numeros [6, 7, 8, 9 e 10] na lista;
    lista5 = [6,7,8,9,10]

    # Passo 5: Repita os passos 2 e 3.
    while len(lista5) > 0:
        pilha.append(lista5[0])
        del lista5[0]

    while len(pilha) > 0:
        lista10.append(pilha[-1])
        pilha.pop()

    # Passo 6: Exiba todos os numeros que foram inseridos na fila.
    print(lista10)


Main()

# Ao rodar este script o resultado obtido no Console é:
# [5, 4, 3, 2, 1, 10, 9, 8, 7, 6]
