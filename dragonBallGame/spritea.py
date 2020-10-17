
import pygame

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
                    if self.estat!=Animacio.DEFENSAE:
                        self.estat=Animacio.KAOE
                        self.vel=(10,0)
                    else:
                        self.vel=(5,0)
            
            if personatge2.estat==Animacio.PUNY1E or personatge2.estat==Animacio.PATADA2E:
                if personatge2.rect.right>self.rect.right:
                    if self.estat!=Animacio.DEFENSAD:
                        self.estat=Animacio.KOD
                        self.vel=(-10,0)
                    else:
                        self.vel=(-5,0)

            if personatge2.estat==Animacio.PATADA1E:
                if personatge2.rect.right>self.rect.right:
                    if self.estat!=Animacio.DEFENSAD:
                        self.estat=Animacio.A1
                        self.vel=(-5,0)
                    else:
                        self.vel=(-2.5,0)
            if personatge2.estat==Animacio.PATADA1D:
                if personatge2.rect.right<self.rect.right:
                    if self.estat!=Animacio.DEFENSAE:
                        self.estat=Animacio.A2
                        self.vel=(5,0)
                    else:
                        self.vel=(2.5,0)

        if self.vel==(10,0) and abs(self.rect.right-personatge2.rect.right)>=100:
            self.vel=(0,0)
        
        if self.vel==(-10,0) and abs(self.rect.right-personatge2.rect.right)>=100:
            self.vel=(0,0)

        if self.vel==(-5,0) and abs(self.rect.right-personatge2.rect.right)>=80:
            self.vel=(0,0)
        
        if self.vel==(5,0) and abs(self.rect.right-personatge2.rect.right)>=80:
            self.vel=(0,0)

        if self.vel==(2.5,0) and abs(self.rect.right-personatge2.rect.right)>=80:
            self.vel=(0,0)

        if self.vel==(-2.5,0) and abs(self.rect.right-personatge2.rect.right)>=80:
            self.vel=(0,0)
    

            
            
        self.rect=self.rect.move(self.vel)

        if self.estat==Animacio.M1D:
            self.vel=(3,0)
            fila=1
            columna=0
            
        elif self.estat==Animacio.M1E:
            self.vel=(-3,0)
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

        elif self.estat==Animacio.PUNY1E:
            fila=1
            columna=4

        elif self.estat==Animacio.PATADA1E:
            fila=0
            columna=3
            

        elif self.estat==Animacio.C1D:
            fila=0
            columna=1
        elif self.estat==Animacio.PUNY1D:
            fila=1
            columna=1
            
        elif self.estat==Animacio.PATADA1D:
            fila=0
            columna=2
        
        elif self.estat==Animacio.PUNY2D:
            fila=2
            columna=0
        
        
        
        elif self.estat==Animacio.PATADA2D:
            fila=1
            columna=2
        
        
        
        elif self.estat==Animacio.PUNY2E:
            fila=2
            columna=5
        
        
        
        elif self.estat==Animacio.PATADA2E:
            fila=1
            columna=3

        elif self.estat==Animacio.DEFENSAD:
            fila=3
            columna=2
        
        elif self.estat==Animacio.DEFENSAE:
            fila=3
            columna=3
        
        elif self.estat==Animacio.KOD:
            fila=2
            columna=2

        elif self.estat==Animacio.KAOE:
            fila=2
            columna=3
            
        elif self.estat==Animacio.A1:
            fila=5
            columna=1
            
        elif self.estat==Animacio.A2:
            fila=5
            columna=4
        else:
            fila = self.estat
            columna = self.count // 10
        self.image = self.llista_im[fila][columna]


    

    def canvi(self,personatge2):
        if self.rect.right+250<self.mon.width:
           if self.rect.move(250,0).colliderect(personatge2.rect)==False:
                self.rect=self.rect.move(250,0)
        else:
           if self.rect.move(-250,0).colliderect(personatge2.rect)==False:
                self.rect=self.rect.move(-250,0)
           

    
    def ves_dreta(self):
        self.estat = Animacio.M1D

    
    def ves_esquerra(self):
        self.estat = Animacio.M1E
    

    def aturat(self):
        self.estat=Animacio.QUIET
        self.vel=(0,0)

    def aturat1(self):
        self.estat=Animacio.C1E
        self.vel=(0,0)
            

    def aturat2(self):
        self.estat=Animacio.C1D
        self.vel=(0,0)

    def aturat3(self,personatge2):
        if self.rect.right<personatge2.rect.right:
            self.estat=Animacio.C1D
        else:
            self.estat=Animacio.C1E
        
            

    def coppuny1(self,personatge2):
        if self.rect.right<personatge2.rect.right:
            self.estat=Animacio.PUNY1D
            self.vel=(0,0)
        else:
            self.estat=Animacio.PUNY1E
            self.vel=(0,0)

    def patada1(self,personatge2):
        if self.rect.right<personatge2.rect.right:
            self.estat=Animacio.PATADA1D
            self.vel=(0,0)
        else:
            self.estat=Animacio.PATADA1E
            self.vel=(0,0)
            
    def patada2(self,personatge2):
        if self.rect.right<personatge2.rect.right:
            self.estat=Animacio.PATADA2D
            self.vel=(0,0)
        else:
            self.estat=Animacio.PATADA2E
            self.vel=(0,0)

    def bola_energia(self,personatge2):
        if self.rect.right<personatge2.rect.right:
            self.estat=Animacio.PUNY1D
            self.vel=(0,0)
        else:
            self.estat=Animacio.PUNY1E
            self.vel=(0,0)

    def proteccio(self, personatge2):
        if self.rect.right<personatge2.rect.right:
            self.estat=Animacio.DEFENSAD
            self.vel=(0,0)     
        else:
            self.estat=Animacio.DEFENSAE
            self.vel=(0,0)

    def salt(self,personatge2):
        pass
    
    def acabasalt(self,personatge2):
        pass
        

def crea_matriu_imatges(spritesheet, nfils, ncols):
        mides = ( spritesheet.get_width() // ncols,
                  spritesheet.get_height() // nfils )
        matriu = [[] for i in range(nfils)]
        for fila in range(nfils):
            for columna in range(ncols):
                tros = pygame.Rect( (mides[0] * columna, mides[1] * fila), mides )
                matriu[fila].append(spritesheet.subsurface(tros))
        return matriu

