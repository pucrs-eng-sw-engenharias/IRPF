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

print ("S para cadastro simples e C para cadastro completo")

x = input()

if x == 'S':
    













