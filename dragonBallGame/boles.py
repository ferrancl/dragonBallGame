import pygame
from energia import Energia
from spritea import Animacio
from vida3 import Vida
class Boles(pygame.sprite.Sprite):

    (A1, A2,B1,B2,B3,B4) = list(range(6))

    def __init__(self, spritesheet, pos, nfils, ncols):
        super(Boles, self).__init__()
        self.spritesheet = pygame.mask.from_surface(spritesheet)
        self.estat = Boles.B1
        self.count = 0
        self.nframes = ncols
        self.llista_im = crea_matriu_imatges(spritesheet, nfils, ncols)
        self.image = self.llista_im[0][0] 
        self.rect = self.image.get_rect().move(pos)
        self.vel=(0,0)
        self.mon = pygame.display.get_surface().get_rect()

    def update(self,personatge2,ola,bola2):

        l=[Vida.VIDA1,Vida.VIDA2,Vida.VIDA3,Vida.VIDA4,Vida.VIDA5,Vida.VIDA6,Vida.VIDA7,Vida.VIDA8,Vida.VIDA9,Vida.VIDA10,Vida.VIDA11,Vida.VIDA12,Vida.VIDA13,Vida.VIDA14,Vida.VIDA15,Vida.VIDA16]
        
        if ola.estat==Vida.VIDA1:
            n=0
        elif ola.estat==Vida.VIDA2:
            n=1
        elif ola.estat==Vida.VIDA3:
            n=2
        elif ola.estat==Vida.VIDA4:
            n=3
        elif ola.estat==Vida.VIDA5:
            n=4
        elif ola.estat==Vida.VIDA6:
            n=5
        elif ola.estat==Vida.VIDA7:
            n=6
        elif ola.estat==Vida.VIDA8:
            n=7
        elif ola.estat==Vida.VIDA9:
            n=8
        elif ola.estat==Vida.VIDA10:
            n=9
        elif ola.estat==Vida.VIDA11:
            n=10
        elif ola.estat==Vida.VIDA12:
            n=11
        elif ola.estat==Vida.VIDA13:
            n=12
        elif ola.estat==Vida.VIDA14:
            n=13
        elif ola.estat==Vida.VIDA15:
            n=14
        elif ola.estat==Vida.VIDA16:
            n=15
        self.count = self.count + 1
        if self.count == self.nframes * 10:
            self.count = 0

        if self.rect.left <= 0:
            self.vel=(0,0)
            self.image = self.llista_im[0][0]
            self.estat=Boles.B1
            self.rect.right=300
            self.rect.top=150

        if self.rect.right >= self.mon.width:
            self.vel=(0,0)
            self.image = self.llista_im[0][0]
            self.rect.right=300
            self.rect.top=150
            self.estat=Boles.B1

        if pygame.sprite.collide_mask(self,personatge2)!=None:
            self.estat=Boles.B1
            if self.rect.right>personatge2.rect.right:
                if personatge2.estat==Animacio.DEFENSAE or personatge2.estat==Animacio.DEFENSAD:
                    personatge2.rect.right=personatge2.rect.right-60
                    if n<=13:
                        n=n+2
                        ola.estat=l[n]
                else:
                   self.image = self.llista_im[0][0]
                   personatge2.estat=personatge2.MORTD
                   personatge2.vel=(-3,0)
                   if n<=11:
                       n=n+4
                       ola.estat=l[n]
                   else:
                       ola.estat=l[15]
               
            else:
                if personatge2.estat==Animacio.DEFENSAE or personatge2.estat==Animacio.DEFENSAD:
                    personatge2.rect.right=personatge2.rect.right+60
                    if n<=13:
                        n=n+2
                        ola.estat=l[n]
                    else:
                        ola.estat=l[15]
                    
                else:
                    self.image = self.llista_im[0][0]
                    personatge2.estat=personatge2.MORTE
                    personatge2.vel=(3,0)
                    if n<=11:
                        n=n+4
                        ola.estat=l[n]
                    else:
                        ola.estat=l[15]
                    
                
        if pygame.sprite.collide_mask(self,bola2)!=None:
            self.estat=Boles.B1
            bola2.estat=Boles.B1
            
                    


        if self.estat==Boles.B1:
            self.image = self.llista_im[0][0]

        elif self.estat==Boles.B2:
            self.image = self.llista_im[0][1]
            
        elif self.estat==Boles.B4:
            self.image = self.llista_im[1][1]
            
        self.rect=self.rect.move(self.vel)
        
    def apareix(self,p1,p2,ola):
        if ola.estat!=Energia.VIDA16 and  ola.estat!=Energia.VIDA15 and  ola.estat!=Energia.VIDA14  and ola.estat!=Energia.VIDA13 and  ola.estat!=Energia.VIDA12:
            if p1.rect.right>p2.rect.right:
                self.rect.right=p1.rect.right-70
                self.rect.top=p1.rect.top
            else:
                self.rect.right=p1.rect.right+70
                self.rect.top=p1.rect.top
            
            self.estat=Boles.B2
            self.image = self.llista_im[0][1]
            c=pygame.mixer.Sound('Kamehameha.wav')
            pygame.mixer.Sound.play(c)
           
        

    def dispara(self,p2):
        if self.image==self.llista_im[0][1]:
            if self.rect.right>p2.rect.right:
                self.vel=( 5,0)
            else:
                self.vel=(-5,0)
            pygame.mixer.stop()
            c=pygame.mixer.Sound('Kamehameha1.wav')
            pygame.mixer.Sound.play(c)
        
        

def crea_matriu_imatges(spritesheet, nfils, ncols):
        mides = ( spritesheet.get_width() // ncols,
                  spritesheet.get_height() // nfils )
        matriu = [[] for i in range(nfils)]
        for fila in range(nfils):
            for columna in range(ncols):
                tros = pygame.Rect( (mides[0] * columna, mides[1] * fila), mides )
                matriu[fila].append(spritesheet.subsurface(tros))
        return matriu

