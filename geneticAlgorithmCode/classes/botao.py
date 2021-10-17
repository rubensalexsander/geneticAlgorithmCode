#from utils import *

class Botao:
    def __init__(self, lugar=[0,0], texto='', cor=(150,150,150), corTexto=(255,255,255), tamanho=[20,20], tamanhoTexto=0.1, comando=None, codigo=None):
        self.texto = texto
        self.lugar = lugar
        self.tamanho = tamanho
        self.cor = cor
        self.corTexto = corTexto
        self.tamanhoTexto = tamanhoTexto
        self.comando = comando
        self.codigo = codigo

    def getArea(self):
        return [
            [self.lugar[0], self.lugar[1]],
            [self.lugar[0] + self.tamanho[0], self.lugar[1] + self.tamanho[1]]
        ]
