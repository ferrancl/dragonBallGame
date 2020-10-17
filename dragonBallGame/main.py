import pygame
import spritea
import spritea3
import vida3
import fons
import boles
import energia
import goku1
import boles1



def ini_sprites():
    im =pygame.image.load("SG.png").convert_alpha()
    im2=pygame.image.load("freezer.png").convert_alpha()
    im3=pygame.image.load("ola.png").convert_alpha()
    im4=pygame.image.load("ola.png").convert_alpha()
    im5=pygame.image.load("fons1.png").convert_alpha()
    im6=pygame.image.load("bolesdefoc.png").convert_alpha()
    im7=pygame.image.load("energia.png").convert_alpha()
    im8=pygame.image.load("freezern2.png").convert_alpha()
    im9=pygame.image.load("gokuss.png").convert_alpha()
    
    grup = pygame.sprite.LayeredUpdates() # grup de Sprites
    c1=spritea.Animacio( im, (500, 300), 6, 6)
    c2=spritea.Animacio( im2, (100,300), 6,6)
    c3=vida3.Vida( im3, (125,0), 4,4)
    c4=vida3.Vida( im4, (640,0), 4,4)
    c5=fons.fons(im5)
    c6=boles.Boles(im6, (300,100),2,2)
    c9=boles.Boles(im6, (300,100),2,2)
    c7=energia.Energia(im7, (125,50), 4, 4)
    c8=energia.Energia(im7, (640,50), 4, 4)
    c10=goku1.goku1(im8, (15,10))
    c11=goku1.goku1(im9, (537,11))
    c12=boles1.Boles(im6, (300,100),2,2)
    c13=boles1.Boles(im6, (300,100),2,2)

    grup.add(c1,layer=1)
    grup.add(c2,layer=1)
    grup.add(c3,layer=1)
    grup.add(c4,layer=1)
    grup.add(c5, layer=0)
    grup.add(c6, layer=1)
    grup.add(c9, layer=1)
    grup.add(c7, layer=1)
    grup.add(c8, layer=1)
    grup.add(c10, layer=1)
    grup.add(c11, layer=1)
    grup.add(c12, layer=1)
    grup.add(c13, layer=1)
    return c5,c1,c2,c3,c4,c6,c9,c7,c8,c12,c13,grup
 

def tracta_events(heroi,heroi2,vida1,vida2,bola1,bola2,energia1,energia2,bola11,bola22):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            return True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return True
            
            elif event.key == pygame.K_RIGHT:
                heroi.ves_dreta()
            elif event.key == pygame.K_LEFT:
                heroi.ves_esquerra()
            elif event.key== pygame.K_o:
                energia2.carrega_energia()
            elif event.key==pygame.K_q:
                energia1.carrega_energia()
            elif event.key== pygame.K_i:
                heroi.coppuny1(heroi2)
                bola1.apareix(heroi,heroi2,energia2)
                energia2.baixa_energia()
            elif event.key==pygame.K_u:
                heroi.coppuny1(heroi2)
                bola11.apareix1(heroi,heroi2,energia2)
                energia2.baixa_energia()
            elif event.key== pygame.K_r:
                heroi2.coppuny1(heroi)
                bola2.apareix(heroi2,heroi,energia1)
                energia1.baixa_energia()
            elif event.key==pygame.K_e:
                heroi2.coppuny1(heroi)
                bola22.apareix1(heroi2,heroi,energia1)
                energia1.baixa_energia()
            elif event.key==pygame.K_z:
                heroi2.proteccio(heroi)
            elif event.key==pygame.K_f:
                heroi2.canvi(heroi)
            elif event.key==pygame.K_UP:
                heroi.salt(heroi2)
            elif event.key==pygame.K_l:
                heroi.coppuny1(heroi2)
            elif event.key==pygame.K_k:
                heroi.patada2(heroi2)
            elif event.key==pygame.K_m:
                heroi.proteccio(heroi2)
            elif event.key==pygame.K_c:
                heroi2.coppuny1(heroi)
            elif event.key==pygame.K_v:
                heroi2.patada2(heroi)
            elif event.key==pygame.K_j:
                heroi.patada1(heroi2)
            elif event.key==pygame.K_p:
                heroi.canvi(heroi2)
            elif event.key==pygame.K_x:
                heroi2.patada1(heroi)
            elif event.key == pygame.K_d:
                heroi2.ves_dreta()
            elif event.key == pygame.K_a:
                heroi2.ves_esquerra()
            
        elif event.type == pygame.KEYUP:
            
            if event.key==pygame.K_RIGHT:
                heroi.aturat2()
            elif event.key==pygame.K_LEFT:
                heroi.aturat1()
            elif event.key == pygame.K_d:
                heroi2.aturat2()
            elif event.key== pygame.K_m:
                heroi.aturat3(heroi2)
            elif event.key== pygame.K_z:
                heroi2.aturat3(heroi)
            elif event.key == pygame.K_a:
                heroi2.aturat1()
            elif event.key==pygame.K_i:
                bola1.dispara(heroi)
            elif event.key==pygame.K_u:
                bola11.dispara1(heroi)
            elif event.key==pygame.K_r:
                bola2.dispara(heroi2)
            elif event.key==pygame.K_e:
                bola22.dispara1(heroi2)
            elif event.key==pygame.K_l:
                heroi.aturat3(heroi2)
            elif event.key==pygame.K_k:
                heroi.aturat3(heroi2)
            elif event.key==pygame.K_j:
                heroi.aturat3(heroi2)
            elif event.key==pygame.K_c:
                heroi2.aturat3(heroi)
            elif event.key==pygame.K_x:
                heroi2.aturat3(heroi)
            elif event.key==pygame.K_v:
                heroi2.aturat3(heroi)
            elif event.key==pygame.K_o:
                pass
               
            
    return False


            
def main():
    pygame.init()
    # pygame.mixer.music.load('DBZFB.mp3')
    # pygame.mixer.music.play(-1,1.5)
    colorFons = (255, 255, 255)
    pantalla = pygame.display.set_mode( (770, 415) )
    crono = pygame.time.Clock()
    a,heroi,heroi2,vida1,vida2,bola1,bola2,energia1,energia2,bola11,bola22,sprites = ini_sprites()
    final = False
    while not final:
        final= tracta_events(heroi,heroi2,vida1,vida2,bola1,bola2,energia1,energia2,bola11,bola22) 
        heroi.update(heroi2)
        heroi2.update(heroi)
        bola1.update(heroi2,vida1,bola2)
        bola2.update(heroi,vida2,bola1)
        vida1.update(heroi,heroi2)
        vida2.update(heroi2,heroi)
        bola11.update(heroi2,vida1,bola2)
        bola22.update(heroi,vida2,bola1)
        energia1.update()
        energia2.update()
        pantalla.fill(colorFons)  # pinta el fons de la pantalla
        sprites.draw(pantalla)    # pinta sprites
        pygame.display.flip()
        crono.tick(60)
        if vida1.estat==vida3.Vida.VIDA16:
            print ("Goku superguerrer guanya")
            final=True
        if vida2.estat==vida3.Vida.VIDA16:
            print ("Goku guanya")
            final=True
            
    pygame.quit()   
 
 
if __name__=='__main__' :
    main()
