# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 14:13:25 2018

@author: User
"""
from firebase import firebase

base_de_dados = firebase.FirebaseApplication(\
                        'https://estoque-7f000.firebaseio.com/', None)

estoque = base_de_dados.get('/Estoque/lojas', None)

if estoque == None:
    estoque = {}


loja = input('\nESCOLHA UMA LOJA PARA EDITAR: ')
if loja not in estoque:
    estoque[loja] = {}
    
else:
    estoque[loja] = estoque[loja]
    
escolha = -1

print ('\nCONTROLE DE ESTOQUE ABERTO')

while escolha != 0:
    
    print ('\n0 - sair ')
    print ('1 - adicionar item')
    print ('2 - remover item')
    print ('3 - alterar item')
    print ('4 - imprimir estoque')
    print ('5 - Selecionar nova loja')
    
    escolha = int(input('Escolha um comando: '))
    
    
    if escolha == 1:
        produto = input('Nome do produto: ')
        if produto in estoque[loja]:
            print('\nEste produto já existe no estoque!')
        else:
            quantidade = int(input('Quantidade inicial: '))
            preco = float(input('Preço do produto: R$ '))
            if preco >= 0:
                estoque[loja][produto] = {'quantidade': quantidade,\
                       'valor' : preco, 'vlr_total': quantidade * preco}
                print ('\nItem adicionado com sucesso!')
            else:
                print('\nValor inválido!')
            
            
    elif escolha == 2:
        produto = input('Nome do produto: ')
        if produto in estoque[loja]:
            del estoque[loja][produto]
            print ('\nO item foi removido com sucesso!')
        else:
            print ('\nO produto não foi encontrado no estoque!')
            
    
    elif escolha == 3:
        produto = input('Nome do produto: ')    
        if produto in estoque[loja]:
            comando = -1
            print(' ')
            print ('\nA atual quantidade deste produto no estoque é: {0}'\
                   .format(estoque[loja][produto]['quantidade']))
            print ('\nO atual preço deste produto é: R${0}'\
                   .format(estoque[loja][produto]['valor']))
            print(' ')
            print('\n1 - Alterar quantidade do produto no estoque')
            print('2 - Alterar preço do produto')
            print('3 - Alterar preço e quantidade do produto')
            
            comando = int(input('\nEscolha um comando: '))
            
            if comando ==1:
                quantidade = int(input('\nQuantidade a ser adicionada: '))
                estoque[loja][produto]['quantidade'] += quantidade
                estoque[loja][produto]['vlr_total'] = \
                estoque[loja][produto]['quantidade'] * estoque[loja][produto]['valor']
                print('\nA nova quantidade deste produto no estoque é: {0}'\
                  .format(estoque[loja][produto]['quantidade']))
            
            elif comando == 2:
                novo_preco = float(input('\nNovo preço do produto: R$ '))
                if novo_preco >= 0:
                    estoque[loja][produto]['valor'] = novo_preco
                    estoque[loja][produto]['vlr_total'] =\
                    novo_preco * estoque[loja][produto]['quantidade']
                    print('\nO novo preço deste produto é: R${0}'\
                          .format(estoque[loja][produto]['valor']))
                else:
                    print('\nValor inválido')
            
            elif comando == 3:
                quantidade = int(input('\nQuantidade a ser adicionada: '))
                novo_preco = float(input('\nNovo preço do produto: R$ '))
                if novo_preco >= 0:
                    estoque[loja][produto]['valor'] = novo_preco
                    estoque[loja][produto]['quantidade'] += quantidade
                    estoque[loja][produto]['vlr_total'] =\
                    novo_preco * estoque[loja][produto]['quantidade']
                    print('\nA nova quantidade deste produto no estoque é: {0}'\
                          .format(estoque[loja][produto]['quantidade']))
                    print('\nO novo preço deste produto é: R${0}'\
                          .format(estoque[loja][produto]['valor']))
                else:
                    print('\nValor inválido')
        else:
            print ('\nO produto não foi encontrado no estoque!')
    
    
    elif escolha == 4:
        print ('\n1 - Imprimir estoque da loja')
        print ('2 - Listar produtos com quantidade negativa')
        print ('3 - Exibir valor monetário total da loja')
        print ('4 - Imprimir estoque completo')
        comando = int(input('\nEscolha um comando: '))
       
        if comando == 1:
            print(' ')
           
            for i in estoque[loja]:
                print('{0}: quantidade = {1}; valor = {2}; total = {3}'\
                      .format(i, estoque[loja][i]['quantidade'],\
                              estoque[loja][i]['valor'],
                              estoque[loja][i]['vlr_total']))
            
            if i not in estoque[loja]:
                print('Estoque vazio')
        
        elif comando == 2:
           estoque_negativo = {}
           for i in estoque[loja]:
               if estoque[loja][i]['quantidade'] < 0:
                   estoque_negativo[i] = estoque[loja][i]['quantidade']
                   print ('\n{0}: {1}' .format(i, estoque[loja][i]['quantidade']))

        
        elif comando == 3:
            monetario = 0
            for i in estoque[loja]:
                monetario +=\
                estoque[loja][i]['quantidade'] * estoque[loja] [i]['valor']
            print ('\nO valor monetario total desta loja é: R${0}'\
                   .format(monetario))
            
            
        elif comando == 4:
            for e in estoque:
                print ('\n{0}'.format(e))
                for i in estoque[e]:
                    print('{0} : quantidade = {1}, valor = {2}, vlr_total = {3}'\
                          .format(i, estoque [e][i]['quantidade'], estoque [e][i]['valor'],\
                                  estoque[e][i]['vlr_total']))

                
    elif escolha == 5:
        loja = input('\nEscolha uma loja: ')
        if loja not in estoque:
            estoque[loja] = {}
    
        else:
            estoque[loja] = estoque[loja]    
    
        
        
    elif escolha != 0:
        print('\nComando inválido!')
        
if escolha == 0:
    print ('\nCONTROLE DE ESTOQUE ENCERRADO')
    print ('\nATÉ MAIS!')   
    novo_estoque = base_de_dados.patch('/Estoque/lojas', estoque)