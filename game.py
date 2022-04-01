from PPlay.collision import *
from PPlay.collision import*
from PPlay.gameimage import *
from PPlay.gameobject import *
from PPlay.sprite import *
from PPlay.window import *
from player_and_enemy import*
from PPlay.sound import *
from os import path
from modos import*
from tilemap import *
import modos


class Game(object):
    def __init__(self, janela):
        self.janela = janela
        self.screen = pg.display.set_mode((1625, 914))
        self.teclado = janela.get_keyboard()
        self.jogador = Jogador(self.janela)
        self.inimigo = Inimigo1(self.janela)
        self.inimigo2 = Inimigo1(self.janela)
        self.inimigo3 = Inimigo1(self.janela)
        self.arvore = Sprite("Imagens/arvoreplay.png")
        self.placa = Sprite("Imagens/placa.png")
        self.life1 = Sprite("Imagens/vidas.png") 
        self.life21 = Sprite("Imagens/lives1.png")
        self.life22 = Sprite("Imagens/lives2.png")
        self.life23 = Sprite("Imagens/lives3.png")
        self.life4 = Sprite("Imagens/lives3.png")
        self.coin = Sound('musicas/coin.mp3')
        self.coin2 = Sound('musicas/yeah.mp3')
        self.pontuacao = 0
        self.pontos = 0
        self.pontos2 = 0
        self.tempo = 0
        self.load_data()
        self.barabim = False
        self.espeto = Sprite("Imagens/espeto.png")
        self.espeto2 = Sprite("Imagens/paodealho.png")
        self.espeto3 = Sprite("Imagens/comida2.png")
        self.espeto4 = Sprite("Imagens/bebida1.png")
        self.espeto5 = Sprite("Imagens/salmao2.png")
        self.espeto6 = Sprite("Imagens/salmao.png")
        self.espeto7 = Sprite("Imagens/copo.png")
        self.espeto8 = Sprite("Imagens/salsichao.png")
        self.espeto9 = Sprite("Imagens/arroz.png")
        self.espeto10 = Sprite("Imagens/comida1.png")
        self.espeto11 = Sprite("Imagens/bebida2.png")
        self.espeto12 = Sprite("Imagens/comida3.png")
        self.espeto13 = Sprite("Imagens/arroz.png")
        self.espeto14 = Sprite("Imagens/bebida2.png")
        self.espeto15 = Sprite("Imagens/copo22132.png")
        self.setpos()
        self.setpos2()

    def _draw(self):
        self.espeto.draw()
        self.espeto2.draw()
        self.espeto3.draw()
        self.espeto4.draw()
        self.espeto5.draw()
        self.espeto6.draw()
        self.espeto7.draw()
        self.espeto8.draw()
        self.espeto9.draw()
        self.espeto10.draw()
        self.espeto11.draw()
        self.espeto12.draw()
        self.espeto13.draw()
        self.espeto14.draw()
        self.espeto15.draw()
        self.arvore.draw()
        self.placa.draw()
        self.life1.draw()
        self.life4.draw()
    
    def setpos(self):
        self.espeto.set_position(645, 760)
        self.espeto2.set_position(0, 765)
        self.espeto3.set_position(260, 570)
        self.espeto4.set_position(0, 55)
        self.espeto5.set_position(65, 90)
        self.espeto6.set_position(260, 60)
        self.espeto7.set_position(340, 40)
        self.espeto8.set_position(440, 60)
        self.espeto9.set_position(455, 0)
        self.espeto10.set_position(830, 260)
        self.espeto11.set_position(830, 315)
        self.espeto12.set_position(900, 320)
        self.espeto13.set_position(640, 500)
        self.espeto14.set_position(900, 5)
        self.espeto15.set_position(1520, 430)
        self.arvore.set_position(1480, 660)
        self.placa.set_position(1350, 660)
        self.life1.set_position(0,self.life21.height/2)
        self.life21.set_position(self.life1.width + 5, 12)
        self.life22.set_position(self.life1.width + 5, 12)
        self.life23.set_position(self.life1.width + 5, 12)
        self.life4.set_position(self.life1.width + 5, 12)
    
    def setpos2(self):
        if modos.dificuldade == 1:
            self.inimigo.set_pos(1154,124)
            self.inimigo2.set_pos(10000,10000)
            self.inimigo3.set_pos(10000,10000)
        if modos.dificuldade == 2:
            self.inimigo.set_pos(1154,124)
            self.inimigo2.set_pos(865,694)
            self.inimigo3.set_pos(10000,10000)
        if modos.dificuldade == 3:
            self.inimigo.set_pos(1154,124)
            self.inimigo2.set_pos(865,694)
            self.inimigo3.set_pos(94,464)

    def comidas(self,coisa):
        self.comidinha = coisa 
        if self.jogador.player.collided(self.comidinha):
            if(self.teclado.key_pressed("E")):
                self.coin.set_volume(100)
                self.coin.play()
                self.comidinha.set_position(self.janela.width-1000, self.janela.height-1000)
                self.pontuacao += 20
                self.veloadicional = self.pontuacao/10
                modos.velplayer -= self.veloadicional

        if self.jogador.player.collided(self.arvore):
            if(self.teclado.key_pressed("E")):
                if self.pontuacao > 0: 
                    self.coin2.set_volume(100)
                    self.coin2.play()
                    self.pontos = self.pontuacao - self.tempo/10
                    self.pontos2 += self.pontos
                    self.pontuacao = 0
                    self.veloadicional2 = self.pontos2/100
                    modos.velocidadeInimigos += self.veloadicional2
                    self.tempo = 0
                self.setpos()
    
    def comidas2(self):
        self.comidas(self.espeto)
        self.comidas(self.espeto2)
        self.comidas(self.espeto3)
        self.comidas(self.espeto4)
        self.comidas(self.espeto5)
        self.comidas(self.espeto6)
        self.comidas(self.espeto7)
        self.comidas(self.espeto8)
        self.comidas(self.espeto9)
        self.comidas(self.espeto10)
        self.comidas(self.espeto11)
        self.comidas(self.espeto12)
        self.comidas(self.espeto13)
        self.comidas(self.espeto14)
        self.comidas(self.espeto15)

    def musica(self):
        pygame.init()
        pygame.mixer.music.load('musicas/jogo.mp3')
        pygame.mixer.music.play()
        pygame.event.wait()


    def load_data(self):
        game_folder = path.dirname(__file__)
        map_folder = path.join(game_folder, 'maps')
        self.mapa = TiledMap(path.join(map_folder, 'level.tmx'))
        self.mapa_img = self.mapa.make_map()
        self.mapa_rect = self.mapa_img.get_rect()
        self.camera = Camera(self.mapa.width, self.mapa.height)
               
    def colisoes_player(self, coiso):
        self.coisa = coiso
        if(self.teclado.key_pressed("UP")):
            if self.jogador.player.collided(self.coisa):
                if self.jogador.player.y > self.coisa.y:
                    self.jogador.player.y += 2.5
                    self.velplayer = 0
        if(self.teclado.key_pressed("DOWN")):
            if self.jogador.player.collided(self.coisa):
                if self.jogador.player.y < self.coisa.y:
                    self.jogador.player.y -= 2.5
                    self.velplayer = 0
        if(self.teclado.key_pressed("RIGHT")):
            if self.jogador.player.collided(self.coisa):
                if self.jogador.player.x < self.coisa.x:
                    self.jogador.player.x -= 2.5
                    self.velplayer = 0
        if(self.teclado.key_pressed("LEFT")):
            if self.jogador.player.collided(self.coisa):
                if self.jogador.player.x > self.coisa.x:
                    self.jogador.player.x += 2.5
                    self.velplayer = 0

    def colisoes_inimigo(self, coiso):
        self.coisa = coiso
        if self.inimigo.inimigo1.collided(self.coisa):
            if self.inimigo.inimigo1.y > self.coisa.y:
                self.inimigo.inimigo1.y += 2.5
        if self.inimigo.inimigo1.collided(self.coisa):
            if self.inimigo.inimigo1.y < self.coisa.y:
                self.inimigo.inimigo1.y -= 2.5
        if self.inimigo.inimigo1.collided(self.coisa):
            if self.inimigo.inimigo1.x < self.coisa.x:
                self.inimigo.inimigo1.x -= 2.5
        if self.inimigo.inimigo1.collided(self.coisa):
            if self.inimigo.inimigo1.x > self.coisa.x:
                self.inimigo.inimigo1.x += 2.5
        
        if self.inimigo2.inimigo1.collided(self.coisa):
            if self.inimigo2.inimigo1.y > self.coisa.y:
                self.inimigo2.inimigo1.y += 2.5
        if self.inimigo2.inimigo1.collided(self.coisa):
            if self.inimigo2.inimigo1.y < self.coisa.y:
                self.inimigo2.inimigo1.y -= 2.5
        if self.inimigo2.inimigo1.collided(self.coisa):
            if self.inimigo2.inimigo1.x < self.coisa.x:
                self.inimigo2.inimigo1.x -= 2.5
        if self.inimigo2.inimigo1.collided(self.coisa):
            if self.inimigo2.inimigo1.x > self.coisa.x:
                self.inimigo2.inimigo1.x += 2.5
        
        if self.inimigo3.inimigo1.collided(self.coisa):
            if self.inimigo3.inimigo1.y > self.coisa.y:
                self.inimigo3.inimigo1.y += 2.5
        if self.inimigo3.inimigo1.collided(self.coisa):
            if self.inimigo3.inimigo1.y < self.coisa.y:
                self.inimigo3.inimigo1.y -= 2.5
        if self.inimigo3.inimigo1.collided(self.coisa):
            if self.inimigo3.inimigo1.x < self.coisa.x:
                self.inimigo3.inimigo1.x -= 2.5
        if self.inimigo3.inimigo1.collided(self.coisa):
            if self.inimigo3.inimigo1.x > self.coisa.x:
                self.inimigo3.inimigo1.x += 2.5
        
    def colisoes2(self):
        for tile_object in self.mapa.tmxdata.objects:
            if tile_object.name == 'wall':
                self.colisoes_player(tile_object)
                self.colisoes_inimigo(tile_object)
            
            if tile_object.name == 'safe_zone':
                if self.jogador.player.x > tile_object.x and self.jogador.player.y > tile_object.y:
                    modos.velocidadeInimigos = 0
                else:
                    modos.velocidadeInimigos = 80
       
    def reset(self):
        self.inimigo = Inimigo1(self.janela)
        self.inimigo2 = Inimigo1(self.janela)
        self.inimigo3 = Inimigo1(self.janela)
        self.jogador = Jogador(self.janela)
        self.pontos2 = 0
        self.setpos()
        self.setpos2()
        modos.velocidadeInimigos = 80
        modos.dificuldade = 1

    def gameOver(self):    
        self.janela.draw_text("GAME OVER", self.janela.width/2 , self.janela.height/2, size=500, color=(255,255,255), font_name="Minecraft")    
        arq = open('ranking.txt','r')
        conteudo = arq.readlines()
        nome = input("Enter your name (6 LETTERS!): ")
        linha = nome + '/' + str(modos.texto) + '/' + str(int(self.pontos2)) + '\n'
        conteudo.append(linha)
        arq.close()
        arq = open('ranking.txt', 'w')
        arq.writelines(conteudo)
        arq.close()
        print('Ranking atualizado com sucesso')
        self.reset()
        self.barabim = False
        modos.modo = 3
        modos.dificuldade = 1
    
    def run(self):
        self.tempo = self.tempo + self.janela.delta_time()
        if modos.modo == 1:
            if self.barabim == False:
                self.musica()
                self.barabim = True
        
        self.screen.blit(self.mapa_img, self.camera.apply_rect(self.mapa_rect))
        
        if modos.dificuldade == 1:
            self.jogador.run()
            self.inimigo.run()
        
        if modos.dificuldade == 2:
            self.jogador.run()
            self.inimigo.run()
            self.inimigo2.run()
        if modos.dificuldade == 3:
            self.jogador.run()
            self.inimigo.run()
            self.inimigo2.run()
            self.inimigo3.run()
    

        self.colisoes2()
        self._draw()

        self.janela.draw_text(str(int(self.pontos2)), self.placa.x + 15, self.placa.y + 15, size=35, color=(51,39,15), font_name="Segoe Print")
        self.comidas2()
        
        if self.jogador.player.collided(self.inimigo.inimigo1) or self.jogador.player.collided(self.inimigo2.inimigo1) or self.jogador.player.collided(self.inimigo3.inimigo1):
            self.jogador.vidas -= 1
            self.pontuacao = 0
            self.inimigo = Inimigo1(self.janela)
            self.inimigo2 = Inimigo1(self.janela)
            self.inimigo3 = Inimigo1(self.janela)
            self.jogador.set_pos()
            self.setpos()
            self.setpos2()
            if self.jogador.vidas == 0:
                self.gameOver()
                

        if self.jogador.vidas == 3:
            self.life4 = self.life23
        if self.jogador.vidas == 2:
            self.life4 = self.life22
        if self.jogador.vidas == 1:
            self.life4 = self.life21

        if(self.teclado.key_pressed("ESC")):
            modos.modo = 0
            self.barabim = False
            self.reset()