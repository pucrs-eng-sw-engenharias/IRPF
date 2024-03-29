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


Catalogo = []

continuar = 1
while continuar != 0:
    
    print ("S para cadastro simples e C para cadastro completo")

    x = input()
    
    if x.upper() == 'S':
        
        pessoa = Simples()
        pessoa.nome = input("Digite seu nome: ")
        print ("")
        while 1:
                pessoa.cpf = (input("Digite seu CPF: "))
                if pessoa.cpf.isdigit() and len(pessoa.cpf) == 11 : 
                    break
                print ("CPF inválido!")
        print ("")
        
        while 1:
            try:
                pessoa.contribuicao = float(input("Digite sua contribuicao: "))
                break
            except ValueError:
                print ("Contribuicao invalida!")
        print ("")
        
        while 1:
            try:
                pessoa.renda = float(input("Digite sua renda: "))
                break
            except ValueError:
                print ("Renda invalida!")
        print ("")
    
        Catalogo.append(pessoa)
    
        BaseCalculo = (pessoa.renda - pessoa.contribuicao) - ((pessoa.renda - pessoa.contribuicao)*0.05)
    
        if BaseCalculo <= 12000 :
            print ('Isento de imposto de renda')
    
        elif BaseCalculo > 12000 :
            Imposto = (BaseCalculo - 12000)*0.15
            if BaseCalculo >= 24000 :
                Imposto = Imposto + (BaseCalculo - 24000) * 0.275
        
            print ('Cálculo Imposto de Renda: R$',round(Imposto,2))

    if x.upper() == 'C':
    
        pessoa = Completo()
        pessoa.nome = input("Digite seu nome: ")
        print ("")
        while 1:
                pessoa.cpf = (input("Digite seu CPF: "))
                if pessoa.cpf.isdigit() and len(pessoa.cpf) == 11 : 
                    break
                print ("CPF inválido!")
        print ("")
        
        while 1:
            try:
                pessoa.contribuicao = float(input("Digite sua contribuicao: "))
                break
            except ValueError:
                print ("Contribuicao invalida!")
        print ("")
        
        while 1:
            try:
                pessoa.renda = float(input("Digite sua renda: "))
                break
            except ValueError:
                print ("Renda invalida!")
        
        print ("")
        while 1:
            try:
                pessoa.idade = int(input("Digite sua idade: "))
                break
            except ValueError:
                print ("Idade inválida!")

        print ("")
        
        while 1:
            try:
                pessoa.dependentes = int(input("Digite numero de dependentes: "))
                break
            except ValueError:
                print ("Numero de dependentes inválido!")

        print ("")
    
        Catalogo.append(pessoa)
    
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
            
            print ('Cálculo Imposto de Renda: R$',"%.2f" % Imposto)
    
    print ("Continuar?")
    print ("  0 --> ENCERRAR")
    print ("  1 --> CONTINUAR CADASTRAMENTO")
    continuar = int(input ())
