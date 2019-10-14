# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 18:14:37 2019

@author: 13106827
"""

class Simples:
    def _init_(self,nome,cpf,contribuicao,renda):
        self.nome = nome
        self.cpf = cpf
        self.contribuicao = contribuicao
        self.renda = renda
        
    def setNome (self, nome):
        self.nome = nome
        
    def setCPF (self, cpf):
        self.cpf = cpf
        
    def setContribuicao (self, contribuicao):
        self.contribuicao = contribuicao
    
    def setRenda (self, renda):
        self.renda = renda
    
    def getNome (self):
        return self.nome
    
    def getCPF (self):
        return self.cpf
    
    def getContribuicao (self):
        return self.contribuicao
    
    def getRenda (self):
        return self.renda

class Completo (Simples):
    
    def _init_(self,nome,cpf,idade,dependentes,contribuicao,renda):
        super()._init_(nome,cpf,contribuicao,renda)
        self.idade = idade
        self.dependentes = dependentes
        
    def setIdade (self,idade):
        self.idade = idade
            
    def setDependentes (self,dependentes):
        self.dependentes = dependentes
        
    def getIdade (self):
        return self.idade
        
    def getDependentes (self):
        return self.dependentes


ListaSimples = []
ListaCompleta = []

print ("S para cadastro simples e C para cadastro completo")

x = input()

if x.upper() == 'S':
    
    pessoa = Simples()
    pessoa.nome = input("Digite seu nome: ")
    print ("")
    pessoa.cpf = int(input("Digite seu CPF: "))
    print ("")
    pessoa.contribuicao = float(input("Digite sua contribuicao: "))
    print ("")
    pessoa.renda = float(input("Digite sua renda: "))
    print ("")
    
    ListaSimples.append(pessoa)
    
    BaseCalculo = (pessoa.renda - pessoa.contribuicao) - ((pessoa.renda - pessoa.contribuicao)*0.05)
    
    if BaseCalculo <= 12000 :
        print ('Isento de imposto de renda')
    
    elif BaseCalculo > 12000 :
        Imposto = (BaseCalculo - 12000)*0.15
        
        if BaseCalculo >= 24000 :
            Imposto = Imposto + (BaseCalculo - 24000) * 0.275
        
        print ('Cálculo Imposto de Renda: R$',Imposto)

if x.upper() == 'C':
    
    pessoa = Completo()
    pessoa.nome = input("Digite seu nome: ")
    print ("")
    pessoa.cpf = int(input("Digite seu CPF: "))
    print ("")
    pessoa.contribuicao = float(input("Digite sua contribuicao: "))
    print ("")
    pessoa.renda = float(input("Digite sua renda: "))
    print ("")
    pessoa.idade = int(input("Digite sua idade: "))
    print ("")
    pessoa.dependentes = int(input("Digite numero de dependentes: "))
    print ("")
    
    ListaCompleta.append(pessoa)
    
    BaseCalculo = (pessoa.renda - pessoa.contribuicao)

    if pessoa.idade < 65 :
        if pessoa.dependentes <= 2 :
            BaseCalculo = BaseCalculo - (BaseCalculo * 0.02)
        elif pessoa.dependentes >= 3 and pessoa.dependentes <=5 :
            BaseCalculo = BaseCalculo - (BaseCalculo * 0.035)
        elif pessoa.dependentes > 5 :
            BaseCalculo = BaseCalculo - (BaseCalculo * 0.05)
    elif pessoa.idade >= 65 :
        if pessoa.dependentes <=2 :
            BaseCalculo = BaseCalculo - (BaseCalculo * 0.03)
        elif pessoa.dependentes >= 3 and pessoa.dependentes <=5 :
            BaseCalculo = BaseCalculo - (BaseCalculo * 0.045)
        elif pessoa.dependentes > 5 :
            BaseCalculo = BaseCalculo - (BaseCalculo * 0.06)
    
    if BaseCalculo <= 12000 :
        print ('Isento de imposto de renda')
    
    elif BaseCalculo > 12000 :
        Imposto = (BaseCalculo - 12000)*0.15
        
        if BaseCalculo >= 24000 :
            Imposto = Imposto + (BaseCalculo - 24000) * 0.275
        
        print ('Cálculo Imposto de Renda: R$',Imposto)


# adicionar ListaSimples[] e ListaComlpleta a uma ListaComum[]
# fazer loop de cadastramento
# arredondar ou cortar resultado final do imposto de renda