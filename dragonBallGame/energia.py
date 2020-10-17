import pygame


class Energia(pygame.sprite.Sprite):

     (A1,A2,A3,A4,VIDA1,VIDA2,VIDA3,VIDA4,VIDA5,VIDA6,VIDA7,VIDA8,VIDA9,VIDA10,VIDA11,VIDA12,VIDA13,VIDA14,VIDA15,VIDA16)=list(range(20))

     def __init__(self, spritesheet, pos, nfils, ncols):
        super(Energia, self).__init__()
        self.spritesheet = spritesheet
        self.estat = Energia.VIDA1
        self.count = 0
        self.nframes = ncols
        self.llista_im = crea_matriu_imatges(spritesheet, nfils, ncols)
        self.image = self.llista_im[0][0] 
        self.rect = self.image.get_rect().move(pos)
        self.a=pygame.time.get_ticks()
        self.n=0
        self.l=[Energia.VIDA1,Energia.VIDA2,Energia.VIDA3,Energia.VIDA4,Energia.VIDA5,Energia.VIDA6,Energia.VIDA7,Energia.VIDA8,Energia.VIDA9,Energia.VIDA10,Energia.VIDA11,Energia.VIDA12,Energia.VIDA13,Energia.VIDA14,Energia.VIDA15,Energia.VIDA16]

     def update(self):

          l=[Energia.VIDA1,Energia.VIDA2,Energia.VIDA3,Energia.VIDA4,Energia.VIDA5,Energia.VIDA6,Energia.VIDA7,Energia.VIDA8,Energia.VIDA9,Energia.VIDA10,Energia.VIDA11,Energia.VIDA12,Energia.VIDA13,Energia.VIDA14,Energia.VIDA15,Energia.VIDA16]


          if self.estat==Energia.VIDA1:
               self.image=self.llista_im[0][0]
               self.n=0
          if self.estat==Energia.VIDA2:
               self.image=self.llista_im[0][1]
          if self.estat==Energia.VIDA3:
               self.image=self.llista_im[0][2]
          if self.estat==Energia.VIDA4:
               self.image=self.llista_im[0][3]
          if self.estat==Energia.VIDA5:
               self.image=self.llista_im[1][0]
          if self.estat==Energia.VIDA6:
               self.image=self.llista_im[1][1]
          if self.estat==Energia.VIDA7:
               self.image=self.llista_im[1][2]
          if self.estat==Energia.VIDA8:
               self.image=self.llista_im[1][3]
          if self.estat==Energia.VIDA9:
               self.image=self.llista_im[2][0]
          if self.estat==Energia.VIDA10:
               self.image=self.llista_im[2][1]
          if self.estat==Energia.VIDA11:
               self.image=self.llista_im[2][2]
          if self.estat==Energia.VIDA12:
               self.image=self.llista_im[2][3]
          if self.estat==Energia.VIDA13:
               self.image=self.llista_im[3][0]
          if self.estat==Energia.VIDA14:
               self.image=self.llista_im[3][1]
          if self.estat==Energia.VIDA15:
               self.image=self.llista_im[3][2]
          if self.estat==Energia.VIDA16:
               self.image=self.llista_im[3][3]
          

     def baixa_energia(self):
          a=pygame.time.get_ticks()
          b=a
          if 0<=self.n<=10:
               self.n=self.n+5
               self.estat=self.l[self.n]
               b=a+100
          else:
               pass
          
     def carrega_energia(self):
          if self.n>1:
               self.n=self.n-2
               self.estat=self.l[self.n]
          else:
               self.n=0
               self.estat=self.l[self.n]

def crea_matriu_imatges(spritesheet, nfils, ncols):
    mides = ( spritesheet.get_width() // ncols,
                  spritesheet.get_height() // nfils )
    matriu = [[] for i in range(nfils)]

    for fila in range(nfils):
        for columna in range(ncols):
            tros = pygame.Rect( (mides[0] * columna, mides[1] * fila), mides )
            matriu[fila].append(spritesheet.subsurface(tros))
    return matriu

