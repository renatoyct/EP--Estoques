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

while escolha != 0:
    print ('\nControle de estoque')
    print ('0 - sair ')
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
            estoque[produto] = {'quantidade' : quantidade} 
            print ('\nItem adicionado com sucesso!')
            
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
            print ('\nA atual quantidade deste produto no estoque é: {0}'\
                   .format(estoque[produto]['quantidade']))
            quantidade = int(input('Quantidade a ser adicionada: '))
            estoque[produto]['quantidade'] += quantidade
            print('\nA nova quantidade deste produto no estoque é: {0}'\
                  .format(estoque[produto]['quantidade']))
        else:
            print ('\nO produto não foi encontrado no estoque!')
    
    elif escolha == 4:
        print (estoque)
    
    elif escolha != 0:
        print('\nComando inválido!')
        
            
if escolha == 0:
    print ('\nControle de estoque encerrado!')
    print ('\nAté mais!')   
    novo_estoque = json.dumps(estoque, sort_keys = True, indent = 0)
    with open ('estoque.json', 'w') as f:
        novo_conteudo = f.write(novo_estoque)