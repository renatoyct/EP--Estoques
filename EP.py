# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 16:21:49 2018

EP: Sistema de Grenciamento de Estoque

@author: Renato Tajima e Pedro Perri
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
                estoque[produto] = {'quantidade': quantidade,'valor' : preco}
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
            print ('\nA atual quantidade deste produto no estoque é: {0}'\
                   .format(estoque[produto]['quantidade']))
            print ('\nO atual preço deste produto é: R${0}'\
                   .format(estoque[produto]['valor']))
            print('\n7 - Alterar quantidade do produto no estoque')
            print('8 - Alterar preço do produto')
            print('9 - Alterar preço e quantidade do produto')
            comando = int(input('\nEscolha um comando: '))
            if comando ==7:
                quantidade = int(input('\nQuantidade a ser adicionada: '))
                estoque[produto]['quantidade'] += quantidade
                print('\nA nova quantidade deste produto no estoque é: {0}'\
                  .format(estoque[produto]['quantidade']))
            elif comando == 8:
                novo_preco = float(input('\nNovo preço do produto: R$ '))
                if novo_preco >= 0:
                    estoque[produto]['valor'] = novo_preco
                    print('\nO novo preço deste produto é: R${0}'\
                          .format(estoque[produto]['valor']))
                else:
                    print('\nValor inválido')
            
            elif comando == 9:
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
        print (estoque)
    
    
    elif escolha != 0:
        print('\nComando inválido!')
        
            
if escolha == 0:
    print ('\nCONTROLE DE ESTOQUE ENCERRADO')
    print ('\nATÉ MAIS!')   
    novo_estoque = json.dumps(estoque, sort_keys = True, indent = 0)
    with open ('estoque.json', 'w') as f:
        novo_conteudo = f.write(novo_estoque)
