import pygame
import math
from datetime import datetime as dt
import sys as sys
def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    screen.fill((255, 255, 255))

    start_point = (250, 250) #centrum af displayet
    end_point = (400, 250) #koordinat som flytter sig under beregningerne, 150 pixels linje
    length = 150
    angle = 0
    for i in range(60): #beregner radiating lines for hver sekund/minut split (6 grader)
        end_x = start_point[0] + length * math.cos(math.radians(angle)) #beregner x og y koordinat en linje på 150 pixels ud fra centrum
        end_y = start_point[1] + length * math.sin(math.radians(angle))
        end_point = (end_x, end_y)
        angle = angle + 6 #fortæller størrelsen på vinklen, "angle = 0"
        pygame.draw.line(screen, (0, 0, 0), start_point, end_point , 1) #tegner radiating lines hvert 6 grad
    pygame.draw.circle(screen, (255, 255, 255), start_point, length-10) #sætter en hvid cirkel over linjerne ud fra centrum som giver sekund stregerne den rette længde
                                                                    
    

    for i in range(12): #beregner radiatin lines for hver time split (30 grader)
        end_x = start_point[0] + length * math.cos(math.radians(angle)) #beregner x og y koordinat en linje på 150 pixels ud fra centrum, ud fra vinkel og længde
        end_y = start_point[1] + length * math.sin(math.radians(angle))
        end_point = (end_x, end_y)
        angle = angle + 30 #fortæller størrelsen på vinklen, "angle = 0"
        pygame.draw.line(screen, (0, 0, 0), start_point, end_point , 3)

    pygame.draw.circle(screen, (0, 0, 0), start_point, length, 3)# tegner radiating lines hvert 30 grad
    pygame.draw.circle(screen, (0, 0, 0), start_point, 3)#sætter en hvid cirkel over linjerne ud fra centrum som giver time stregerne den rette længde

    while True:
        ur(screen, start_point, 130)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


def tid(center, radius, angle, time): #definerer funktionen tid med 4 parametre, til at bestemme klokkeslettet
    radiant = math.radians((time-15)*angle) #variablen bestemmer vinklen
    end_x = center[0] + radius * math.cos(radiant) #beregner x og y koordiant for en linje ud fra centrum af urskiven, ud fra radias og vinkel
    end_y = center[1] + radius * math.sin(radiant)
    return (end_x, end_y)
    

def ur(screen, center, radius): #definerer urskiven ud fra 3 parametre
    pygame.draw.circle(screen, (255, 255, 255), center, 130) #sætter en hvid cirkel over linjerne ud fra centrum som giver timestregerne den rette længde
    nutid = dt.now() #variabel for at bestemme tiden 
    timer = nutid.hour #variabel for at bestiime klokkeslettet i timer ud fra "nutid" som er baseret på datetime
    minutter = nutid.minute #variabel for at bestiime klokkeslettet i minutter ud fra "nutid" som er baseret på datetime
    sekunder = nutid.second #variabel for at bestiime klokkeslettet i sekunder ud fra "nutid" som er baseret på datetime
    pygame.draw.line(screen, (0, 0, 0), center, tid(center, radius-35, 30, timer), 3) #tegner timeviseren ud fra "ur" og "tid" beregningerne
    pygame.draw.line(screen, (0, 0, 0), center, tid(center, radius-10, 6, minutter), 3) #radius-"x" bestmmer længden på ur viserne
    pygame.draw.line(screen, (0, 255, 0), center, tid(center, radius-10, 6, sekunder), 2)
    pygame.draw.line(screen, (0, 255, 0), center, tid(center, radius-165, 6, sekunder), 2)
    pygame.draw.circle(screen, (0, 0, 0), center,3)
    
main()