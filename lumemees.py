import pygame
pygame.init()
ekraani_pind=pygame.display.set_mode((300,300)) 
ekraani_pind.fill((204,229,255)) 
pygame.display.set_caption("Esimene aken")
hat=pygame.Rect(105,20,60,80)
pygame.draw.ellipse(ekraani_pind,(102,0,204), hat)

lumemees=pygame.Rect(105,50,60,60)
pygame.draw.ellipse(ekraani_pind,(255,255,250), lumemees)
hat2=pygame.Rect(90,40,90,35)
pygame.draw.ellipse(ekraani_pind,(102,0,204), hat2)
lumemees1=pygame.Rect(95,110,80,80)
pygame.draw.ellipse(ekraani_pind,(255,255,250), lumemees1)
lumemees2=pygame.Rect(85,190,110,110)
pygame.draw.ellipse(ekraani_pind,(255,255,250), lumemees2)
nupp=pygame.Rect(130,120,7,7)
pygame.draw.ellipse(ekraani_pind,(0,0,0), nupp)
nupp2=pygame.Rect(130,140,7,7)
pygame.draw.ellipse(ekraani_pind,(0,0,0), nupp2)
nupp3=pygame.Rect(130,160,7,7)
pygame.draw.ellipse(ekraani_pind,(0,0,0), nupp3)
silmad=pygame.Rect(120,75,7,7)
nupp4=pygame.Rect(130,180,7,7)
pygame.draw.ellipse(ekraani_pind,(0,0,0), nupp4)
pygame.draw.ellipse(ekraani_pind,(0,0,0), silmad)
silmad2=pygame.Rect(140,75,7,7)
pygame.draw.ellipse(ekraani_pind,(0,0,0), silmad2)
silmad2=pygame.Rect(130,85,8,12)
pygame.draw.ellipse(ekraani_pind,(255,0,0), silmad2)
white=(255,255,255)
black=(0,0,0)
prun=(102,51,0)
pygame.draw.line(ekraani_pind, white,(100,140) , (30,200),5)
pygame.draw.line(ekraani_pind, white,(250,140) , (135,120),5)
pygame.draw.line(ekraani_pind, black,(135,103) , (133,100),7)
pygame.draw.line(ekraani_pind, prun,(50,150) , (50,300),5)
lopp_x=50
lopp_y=0
for i in range(30):
    pygame.draw.line(ekraani_pind,prun,(50,150),(lopp_x,lopp_y),3)
    lopp_x-=10
    lopp_y+=12


"""arm1=pygame.Rect(2,4)
pygame.draw.line(ekraani_pind, (255, 255, 255), (95, 60), (20))"""

pygame.display.flip() #отображает поэтому должна находиться в конце рисунков

while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
pygame.quit()