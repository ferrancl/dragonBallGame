import pygame

from spritea import Animacio

class Animacio(pygame.sprite.Sprite):

    (A1, A2, A3, A4,A5,A6,C1D,M1D,PUNY1D,PUNY2D,PATADA1D,PATADA2D,PATADA3D,PATADA4D,MORTD,DEFENSAD,KOD,C1E,M1E,PUNY1E,PUNY2E,PATADA1E,PATADA2E,PATADA3E,PATADA4E,MORTE,DEFENSAE,KAOE) = list(range(28))

    def __init__(self, spritesheet, pos, nfils, ncols):
        super(Animacio, self).__init__()
        self.spritesheet = pygame.mask.from_surface(spritesheet)
        self.estat = Animacio.C1D
        self.count = 0
        self.nframes = ncols
        self.llista_im = crea_matriu_imatges(spritesheet, nfils, ncols)
        self.image = self.llista_im[0][1] 
        self.rect = self.image.get_rect().move(pos)
        self.vel=(0,0)
        self.mon = pygame.display.get_surface().get_rect()

    def update(self,personatge2):
        self.count = self.count + 1
        if self.count == self.nframes * 10:
            self.count = 0

            
        if self.rect.left <= 0:
            self.vel=(0,0)
            if self.estat==Animacio.M1D:
                self.vel=(2,0)

        if self.rect.right >= self.mon.width:
            self.vel=(0,0)
            if self.estat==Animacio.M1E:
                self.vel=(-2,0)

        if self.rect.top <= 0:
            self.vel=(0,0)
            if self.estat==Animacio.M1E:
                self.vel=(-2,0)
            if self.estat==Animacio.M1D:
                self.vel=(2,0)

        if self.rect.bottom >= self.mon.height:
            self.vel=(0,0)
            if self.estat==Animacio.M1E:
                self.vel=(-2,0)
            if self.estat==Animacio.M1D:
                self.vel=(2,0)

        if pygame.sprite.collide_mask(self,personatge2)!=None:
            self.vel=(0,0)
            if self.estat==Animacio.M1E:
                if self.rect.right<personatge2.rect.right:
                    self.vel=(-2,0)
            if self.estat==Animacio.M1D:
                if self.rect.right>personatge2.rect.right:
                    self.vel=(2,0)
            if personatge2.estat==Animacio.PUNY1D or personatge2.estat==Animacio.PATADA2D:
                if personatge2.rect.right<self.rect.right:
                    self.estat=Animacio.MORTE
                    self.vel=(5,0)
            
            if personatge2.estat==Animacio.PUNY1E or personatge2.estat==Animacio.PATADA2E:
                if personatge2.rect.right>self.rect.right:
                    self.estat=Animacio.MORTD
                    self.vel=(-5,0)
            
                
        
        if self.vel==(5,0) and abs(self.rect.right-personatge2.rect.right)>=100:
            self.vel=(0,0)
        
        if self.vel==(-5,0) and abs(self.rect.right-personatge2.rect.right)>=100:
            self.vel=(0,0)
        
    
                
            
            
        self.rect=self.rect.move(self.vel)

        if self.estat==Animacio.M1D:
            self.vel=(2,0)
            fila=1
            columna=0
            
        elif self.estat==Animacio.M1E:
            self.vel=(-2,0)
            fila=1
            columna=5
        
        elif self.estat==Animacio.MORTD:
            fila=0
            columna=0
            self.count=0

        elif self.estat==Animacio.MORTE:
            fila=0
            columna=5

        elif self.estat==Animacio.C1E:
            fila=0
            columna=4

        elif self.estat==Animacio.C1D:
            fila=0
            columna=1
        
        elif self.estat==Animacio.PUNY1D:
            fila=1
            columna=1
        
        elif self.estat==Animacio.PUNY2D:
            fila=2
            columna=0
        
        elif self.estat==Animacio.PATADA1D:
            fila=0
            columna=2
        
        elif self.estat==Animacio.PATADA2D:
            fila=1
            columna=2
        
        elif self.estat==Animacio.PUNY1E:
            fila=1
            columna=4
        
        elif self.estat==Animacio.PUNY2E:
            fila=2
            columna=5
        
        elif self.estat==Animacio.PATADA1E:
            fila=0
            columna=3
        
        elif self.estat==Animacio.PATADA2E:
            fila=1
            columna=3
        
	
        else:
            fila = self.estat
            columna = self.count // 10
        self.image = self.llista_im[fila][columna]


    

    def canvi(self):
        if self.rect.right+100<self.mon.width:
            self.rect=self.rect.move(100,0)
        else:
            self.rect=self.rect.move(-100,0)

    
    def ves_dreta(self):
        self.estat = Animacio.M1D

    
    def ves_esquerra(self):
        self.estat = Animacio.M1E
    

    def aturat(self):
        self.estat=Animacio.QUIET
        self.vel=(0,0)

    def aturat1(self):
        if self.rect.right<personatge2.rect.right:
            self.estat=Animacio.C1D
            self.vel=(0,0)
        else:
            self.estat=Animacio.C1E
            self.vel=(0,0)
            

    def aturat2(self,personatge2):
        if self.rect.right<personatge2.rect.right:
            self.estat=Animacio.C1D
            self.vel=(0,0)
        else:
            self.estat=Animacio.C1E
            self.vel=(0,0)

    def coppuny1(self,personatge2):
        if self.rect.right<personatge2.rect.right:
            self.estat=Animacio.PUNY1D
            self.vel=(0,0)
        else:
            self.estat=Animacio.PUNY1E
            self.vel=(0,0)
            
    def patada1(self,personatge2):
        if self.rect.right<personatge2.rect.right:
            self.estat=Animacio.PATADA2D
            self.vel=(0,0)
        else:
            self.estat=Animacio.PATADA2E
            self.vel=(0,0)
    
    def coppuny2(self):
        self.estat=Animacio.PUNY1E
        self.vel=(0,0)
    
    def patada2(self):
        self.estat=Animacio.PATADA2E
        self.vel=(0,0)

def crea_matriu_imatges(spritesheet, nfils, ncols):
        mides = ( spritesheet.get_width() // ncols,
                  spritesheet.get_height() // nfils )
        matriu = [[] for i in range(nfils)]
        for fila in range(nfils):
            for columna in range(ncols):
                tros = pygame.Rect( (mides[0] * columna, mides[1] * fila), mides )
                matriu[fila].append(spritesheet.subsurface(tros))
        return matriu


