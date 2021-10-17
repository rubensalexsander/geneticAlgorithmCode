from time import time
import pygame
from utils import *
from classes.botao import Botao
from classes.mouse import Mouse

#Configurações----
tamanhoTela = [600,450]
FPS_rate=120
show_fps_screen = True
rgbIdeal = (0, 0, 0) #Cor (RGB) idel (selecionada pelo ambiente)
quantidadeDaspopulacoes = 100
geracoes = 500 #Mínimo 100
corTexto = (50, 255, 50)
font = 'ARIAL'
tamanhoTexto = 0.1
#-----------------
#Variáveis--------
fps = 0
FPS = None
atualizar = True
#-----------------
#Funções----------
def criaBotoes():
    botoes = []
    botoes.append(Botao(lugar=[int(tamanhoTela[0]*0.925), int(tamanhoTela[1]*0.025)], texto='x',tamanho=[int(tamanhoTela[0]*0.05), int(tamanhoTela[0]*0.05)],cor=(20,20,20), corTexto=(255,0,0), tamanhoTexto=tamanhoTexto, codigo=0))
    
    return botoes
#-----------------

#Definições--------
pygame.init()
screen = pygame.display
screen.set_caption('Genetic algorithm')
screen = screen.set_mode(tamanhoTela)
clock = pygame.time.Clock()
resultsList, geracoesList = [], []
mouse = Mouse()
botoes = criaBotoes()
#-----------------
#Times------------
tempo_inicio = time()
timeContoufps = time()
#-----------------

new_population = createFirstpopulation(quantidadeDaspopulacoes)

running = True
while running:

    # Executa comandos do usuário
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            changeCenter = None
            changeZoom = None
        if event.type == pygame.MOUSEBUTTONDOWN:
            areaClique = pygame.mouse.get_pos()
            for botao in botoes:
                if hasColision(botao.getArea(), mouse.getArea(areaClique)):
                    codigo = botao.codigo
                    if codigo == None:
                        print('Botão sem comando definido.')
                    elif codigo == 0:
                        running = False
                    break
    
    if FPS:
        # Updates dentro do tempo (dt=1/FPS)
        #Fases do algoritmo genético:
        # Verifica se atingiu o número de gerações
        if len(geracoesList) < geracoes:
            pais = populationCheckandSelect(new_population, rgbIdeal)
            filho = crossOverandMutation(pais)
            ponts_filho = getPontuacao(rgbIdeal, filho)
            new_population = defineNewgeneration(quantidadeDaspopulacoes, pais, filho)
            
            # Imprime resultados
            print(f'\nGeração: {len(geracoesList)}')
            print(f'Filho: RGB - {filho}, Pts - {ponts_filho}')

            geracoesList.append(new_population)
            resultsList.append(ponts_filho)
        
        # Atualiza o display
        pygame.draw.rect(screen, rgbIdeal, (0,0,int(tamanhoTela[0]/2),tamanhoTela[1]))
        pygame.draw.rect(screen, filho, (int(tamanhoTela[0]/2),0,int(tamanhoTela[0]/2),tamanhoTela[1]))

    # Escreve botões
    for botao in botoes:
        pygame.draw.rect(screen, botao.cor, (botao.lugar[0],botao.lugar[1],botao.tamanho[0],botao.tamanho[1]))
        myfont = pygame.font.SysFont(font, int((tamanhoTela[0] / 2) * tamanhoTexto))
        textsurface = myfont.render(botao.texto, True, botao.corTexto)
        screen.blit(textsurface, (int((botao.lugar[0])+botao.tamanho[0]*0.3), int((botao.lugar[1])-botao.tamanho[1]*0.2)))

    #Escreve informações na tela
    myfont = pygame.font.SysFont(font, int((tamanhoTela[0] * 0.25) * tamanhoTexto))
    if show_fps_screen:
        textsurface = myfont.render(f"FPS: {str(FPS)}", True, corTexto)
        screen.blit(textsurface, (int(tamanhoTela[0] * 0.025), 5))
        textsurface = myfont.render(f"Geração: {str(len(geracoesList))} de {geracoes}", True, corTexto)
        screen.blit(textsurface, (int(tamanhoTela[0] * 0.025), 25))
    
    textsurface = myfont.render(f"COR IDEAL", True, corTexto)
    screen.blit(textsurface, (int(tamanhoTela[0] * 0.2), int(tamanhoTela[1] * 0.5)))
    textsurface = myfont.render(f"COR DO MELHOR INDIVIDUO", True, corTexto)
    screen.blit(textsurface, (int(tamanhoTela[0] * 0.6), int(tamanhoTela[1] * 0.5)))

    # Atualiza valor FPS
    if (time() - timeContoufps) >= 1:
        FPS = fps
        timeContoufps = time()
        fps = 0
    fps += 1

    # Atualiza janela Pygame e define FPS
    pygame.display.flip()
    clock.tick(FPS_rate)

pygame.quit()
