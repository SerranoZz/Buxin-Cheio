from pygame import draw
from pygame.mouse import set_pos
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.gameobject import *
from PPlay.collision import *
from PPlay.animation import *
import modos


class Jogador(object):
    def __init__(self, janela):
        self.janela = janela
        self.player = Sprite("Player/dir.png", 3)
        self.playercima = Sprite("Player/cima.png", 3)
        self.playerbaixo = Sprite("Player/baixo.png", 3)
        self.playerdir = Sprite("Player/dir.png", 3)
        self.playeresq = Sprite("Player/esq.png", 3)
        self.teclado = self.janela.get_keyboard()
        self.vidas = 3
        self.cronometrocorrida = 0
        self.velocidadeplayer = 0
        self.velocidadeplayer2 = 0
        self.duration()
        self.set_pos()

    def duration(self):
        self.playercima.set_total_duration(modos.duraçao)
        self.playerbaixo.set_total_duration(modos.duraçao)
        self.playerdir.set_total_duration(modos.duraçao)
        self.playeresq.set_total_duration(modos.duraçao)
    
    def _draw(self):
        self.player.draw()
    
    def set_pos(self):
        self.player.set_position(self.janela.width - 200 ,self.janela.height - self.player.height)
        self.playerdir.set_position(self.player.x,self.player.y)
        self.playercima.set_position(self.player.x,self.player.y)
        self.playerbaixo.set_position(self.player.x,self.player.y)
        self.playeresq.set_position(self.player.x,self.player.y)

    def andar(self):         
        #Andar
        if(self.teclado.key_pressed("LEFT")):
            if self.teclado.key_pressed("LEFT") == (self.teclado.key_pressed("RIGHT") or self.teclado.key_pressed("UP") or self.teclado.key_pressed("DOWN")):
                pass
            else:
                if(self.player.x >= 0):
                    self.player = self.playeresq
                    self.playeresq.update()
                    self.velocidadeplayer = self.player.x - modos.velplayer * self.janela.delta_time()
                    self.playeresq.x = self.velocidadeplayer
                    self.playerdir.x = self.velocidadeplayer
                    self.playercima.x = self.velocidadeplayer
                    self.playerbaixo.x = self.velocidadeplayer
                    modos.velplayer = 200
                
        
        if(self.teclado.key_pressed("RIGHT")):
            if self.teclado.key_pressed("RIGHT") == (self.teclado.key_pressed("LEFT") or self.teclado.key_pressed("UP") or self.teclado.key_pressed("DOWN")):
                pass
            else:
                if((self.player.x + self.player.width) <= self.janela.width):
                    self.player = self.playerdir
                    self.playerdir.update()
                    self.velocidadeplayer = self.player.x + modos.velplayer * self.janela.delta_time()
                    self.playeresq.x = self.velocidadeplayer
                    self.playerdir.x = self.velocidadeplayer
                    self.playerbaixo.x = self.velocidadeplayer
                    self.playercima.x = self.velocidadeplayer
                    modos.velplayer = 200


        if(self.teclado.key_pressed("UP")):
            if(self.player.y >= 0):
                self.player = self.playercima
                self.playercima.update()
                self.velocidadeplayer2 = self.player.y - modos.velplayer * self.janela.delta_time()
                self.playercima.y = self.velocidadeplayer2
                self.playerbaixo.y = self.velocidadeplayer2
                self.playeresq.y = self.velocidadeplayer2
                self.playerdir.y = self.velocidadeplayer2
                modos.velplayer = 200
        
        if(self.teclado.key_pressed("DOWN")):
            if((self.player.y + self.player.height) <= self.janela.height):
                self.player = self.playerbaixo
                self.playerbaixo.update()
                self.velocidadeplayer2 = self.player.y + modos.velplayer * self.janela.delta_time()
                self.playerbaixo.y = self.velocidadeplayer2
                self.playercima.y = self.velocidadeplayer2
                self.playerdir.y = self.velocidadeplayer2
                self.playeresq.y = self.velocidadeplayer2
                modos.velplayer = 200
        

    def run(self):        
        self._draw()     
        #Andar
        if(self.teclado.key_pressed("LEFT")):
            if self.teclado.key_pressed("LEFT") == (self.teclado.key_pressed("RIGHT") or self.teclado.key_pressed("UP") or self.teclado.key_pressed("DOWN")):
                pass
            else:
                if(self.player.x >= 0):
                    self.player = self.playeresq
                    self.playeresq.update()
                    self.velocidadeplayer = self.player.x - modos.velplayer * self.janela.delta_time()
                    self.playeresq.x = self.velocidadeplayer
                    self.playerdir.x = self.velocidadeplayer
                    self.playercima.x = self.velocidadeplayer
                    self.playerbaixo.x = self.velocidadeplayer
                    modos.velplayer = 200
                
        
        if(self.teclado.key_pressed("RIGHT")):
            if self.teclado.key_pressed("RIGHT") == (self.teclado.key_pressed("LEFT") or self.teclado.key_pressed("UP") or self.teclado.key_pressed("DOWN")):
                pass
            else:
                if((self.player.x + self.player.width) <= self.janela.width):
                    self.player = self.playerdir
                    self.playerdir.update()
                    self.velocidadeplayer = self.player.x + modos.velplayer * self.janela.delta_time()
                    self.playeresq.x = self.velocidadeplayer
                    self.playerdir.x = self.velocidadeplayer
                    self.playerbaixo.x = self.velocidadeplayer
                    self.playercima.x = self.velocidadeplayer
                    modos.velplayer = 200


        if(self.teclado.key_pressed("UP")):
            if(self.player.y >= 0):
                self.player = self.playercima
                self.playercima.update()
                self.velocidadeplayer2 = self.player.y - modos.velplayer * self.janela.delta_time()
                self.playercima.y = self.velocidadeplayer2
                self.playerbaixo.y = self.velocidadeplayer2
                self.playeresq.y = self.velocidadeplayer2
                self.playerdir.y = self.velocidadeplayer2
                modos.velplayer = 200
        
        if(self.teclado.key_pressed("DOWN")):
            if((self.player.y + self.player.height) <= self.janela.height):
                self.player = self.playerbaixo
                self.playerbaixo.update()
                self.velocidadeplayer2 = self.player.y + modos.velplayer * self.janela.delta_time()
                self.playerbaixo.y = self.velocidadeplayer2
                self.playercima.y = self.velocidadeplayer2
                self.playerdir.y = self.velocidadeplayer2
                self.playeresq.y = self.velocidadeplayer2
                modos.velplayer = 200
        
        
        self._draw()
        

class Inimigo1(object):
    def __init__(self, janela):
        self.janela = janela
        self.jogador = Jogador(self.janela)
        self.inimigo1 = Sprite("inimigo/ini_baixo.png", 3)
        self.inimigocima1 = Sprite("inimigo/ini_cima.png", 3)
        self.inimigobaixo1 = Sprite("inimigo/ini_baixo.png", 3)
        self.inimigodir1 = Sprite("inimigo/ini_dir.png", 3)
        self.inimigoesq1 = Sprite("inimigo/ini_esq.png", 3)
        self.velocidadeInimigos = 0
        self.duration()
    

    def set_pos(self, x, y):
        self.inimigo1.set_position(x ,y)
        self.inimigocima1.set_position(self.inimigo1.x,self.inimigo1.y)
        self.inimigobaixo1.set_position(self.inimigo1.x,self.inimigo1.y)
        self.inimigoesq1.set_position(self.inimigo1.x,self.inimigo1.y)
        self.inimigodir1.set_position(self.inimigo1.x,self.inimigo1.y)
    
    def duration(self):
        self.inimigobaixo1.set_total_duration(modos.duraçao)
        self.inimigocima1.set_total_duration(modos.duraçao)
        self.inimigodir1.set_total_duration(modos.duraçao)
        self.inimigoesq1.set_total_duration(modos.duraçao)
    
    def perseguicao(self):
        if((self.inimigo1.x + self.inimigo1.width) <= self.janela.width):
            if self.jogador.player.x > self.inimigo1.x:
                self.inimigo1 = self.inimigodir1
                self.inimigodir1.update()
                self.velocidade_inimigo = self.inimigo1.x + modos.velocidadeInimigos * self.janela.delta_time()
                self.inimigocima1.x = self.velocidade_inimigo
                self.inimigobaixo1.x = self.velocidade_inimigo
                self.inimigoesq1.x = self.velocidade_inimigo
                self.inimigodir1.x = self.velocidade_inimigo
        
        if (self.inimigo1.x >= 0):
            if self.jogador.player.x < self.inimigo1.x:
                self.inimigo1 = self.inimigoesq1
                self.inimigoesq1.update()
                self.velocidade_inimigo = self.inimigo1.x - modos.velocidadeInimigos * self.janela.delta_time()
                self.inimigocima1.x = self.velocidade_inimigo
                self.inimigobaixo1.x = self.velocidade_inimigo
                self.inimigoesq1.x = self.velocidade_inimigo
                self.inimigodir1.x = self.velocidade_inimigo
        
        if((self.inimigo1.y + self.inimigo1.height) <= self.janela.height):
            if self.jogador.player.y > self.inimigo1.y:
                self.inimigo1 = self.inimigobaixo1
                self.inimigobaixo1.update()
                self.velocidade_inimigo2 = self.inimigo1.y + modos.velocidadeInimigos * self.janela.delta_time()
                self.inimigocima1.y = self.velocidade_inimigo2
                self.inimigobaixo1.y = self.velocidade_inimigo2
                self.inimigoesq1.y = self.velocidade_inimigo2
                self.inimigodir1.y = self.velocidade_inimigo2
        
        if(self.inimigo1.y >= 0):
            if self.jogador.player.y  < self.inimigo1.y:
                self.inimigo1 = self.inimigocima1
                self.inimigocima1.update()
                self.velocidade_inimigo2 = self.inimigo1.y - modos.velocidadeInimigos * self.janela.delta_time()
                self.inimigocima1.y = self.velocidade_inimigo2
                self.inimigobaixo1.y = self.velocidade_inimigo2
                self.inimigoesq1.y = self.velocidade_inimigo2
                self.inimigodir1.y = self.velocidade_inimigo2
    
    def drawe(self):
        self.inimigo1.draw()
    
    
    def run(self):
        self.drawe()
        self.jogador.andar()
        self.perseguicao()