# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 14:13:25 2018

@author: User
"""

import json
import os

a = open('estoque.json', 'a')
a.close()




with open('estoque.json', 'r') as f:
    if os.stat('estoque.json').st_size == 0:
        estoque = {}
    else:
        conteudo = f.read()
        estoque = json.loads(conteudo)
        
escolha = -1

loja = input("Escolha uma loja")
estoque[loja] = loja

print ('\nCONTROLE DE ESTOQUE ABERTO')

while escolha != 0:
    print ('\n0 - sair ')
    print ('1 - adicionar item')
    print ('2 - remover item')
    print ('3 - alterar item')
    print ('4 - imprimir estoque')
    escolha = int(input('Escolha um comando: '))
    
    
    if escolha == 1:
        produto = input('Nome do produto: ')
        if produto in estoque:
            print('\nEste produto já existe no estoque!')
        else:
            quantidade = int(input('Quantidade inicial: '))
            preco = float(input('Preço do produto: R$ '))
            if preco >= 0:
                estoque[produto] = {'quantidade': quantidade,'valor' : preco,\
                       'z.total': quantidade * preco}
                print ('\nItem adicionado com sucesso!')
            else:
                print('\nValor inválido!')
            
            
    elif escolha == 2:
        produto = input('Nome do produto: ')
        if produto in estoque:
            del estoque[produto]
            print ('\nO item foi removido com sucesso!')
        else:
            print ('\nO produto não foi encontrado no estoque!')
            
    
    elif escolha == 3:
        produto = input('Nome do produto: ')    
        if produto in estoque:
            comando = -1
            print(' ')
            print ('\nA atual quantidade deste produto no estoque é: {0}'\
                   .format(estoque[produto]['quantidade']))
            print ('\nO atual preço deste produto é: R${0}'\
                   .format(estoque[produto]['valor']))
            print(' ')
            print('\n5 - Alterar quantidade do produto no estoque')
            print('6 - Alterar preço do produto')
            print('7 - Alterar preço e quantidade do produto')
            comando = int(input('\nEscolha um comando: '))
            if comando ==5:
                quantidade = int(input('\nQuantidade a ser adicionada: '))
                estoque[produto]['quantidade'] += quantidade
                print('\nA nova quantidade deste produto no estoque é: {0}'\
                  .format(estoque[produto]['quantidade']))
            elif comando == 6:
                novo_preco = float(input('\nNovo preço do produto: R$ '))
                if novo_preco >= 0:
                    estoque[produto]['valor'] = novo_preco
                    print('\nO novo preço deste produto é: R${0}'\
                          .format(estoque[produto]['valor']))
                else:
                    print('\nValor inválido')
            
            elif comando == 7:
                quantidade = int(input('\nQuantidade a ser adicionada: '))
                novo_preco = float(input('\nNovo preço do produto: R$ '))
                estoque[produto]['quantidade'] += quantidade
                if novo_preco >= 0:
                    estoque[produto]['valor'] = novo_preco
                    print('\nA nova quantidade deste produto no estoque é: {0}'\
                          .format(estoque[produto]['quantidade']))
                    print('\nO novo preço deste produto é: R${0}'\
                          .format(estoque[produto]['valor']))
                else:
                    print('\nValor inválido')
        else:
            print ('\nO produto não foi encontrado no estoque!')
    
    
    elif escolha == 4:
        print ('\n8 - Imprimir estoque completo')
        print ('9 - Listar produtos com quantidade negativa')
        print ('10 - Exibir valor monetário total')
        comando = int(input('\nEscolha um comando: '))
       
        if comando == 8:
            print(' ')
            for i in estoque:
                print('{0}: quantidade = {1}; valor = {2}; total = {3}'\
                      .format(i, estoque[i]['quantidade'], estoque[i]['valor'],\
                              estoque[i]['z.total']))
            if i not in estoque:
                print('Estoque vazio')
        
        elif comando == 9:
           estoque_negativo = {}
           for i in estoque:
               if estoque[i]['quantidade'] < 0:
                   estoque_negativo[i] = estoque[i]['quantidade']
                   print ('\n{0}: {1}' .format(i, estoque[i]['quantidade']))

        
        elif comando == 10:
            monetario = 0
            for i in estoque:
                monetario += estoque[i]['quantidade'] * estoque [i]['valor']
            print ('\nO valor monetario total do seu estoque é: R${0}'\
                   .format(monetario))
        
    
    elif escolha != 0:
        print('\nComando inválido!')
        
            
if escolha == 0:
    print ('\nCONTROLE DE ESTOQUE ENCERRADO')
    print ('\nATÉ MAIS!')   
    novo_estoque = json.dumps(estoque, sort_keys = True, indent = 0)
    with open ('estoque.json', 'w') as f:
        novo_conteudo = f.write(novo_estoque)