from words import word_list
import random
#import  pygame
#pygame.init()

'''
size=(640,480)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("L'impiccato")
color=(255,255,120)
cornici_colore=(0,0,0)
screen.fill(color)
rettangolo1=(10,10,250,460)
pygame.draw.rect(screen,cornici_colore,rettangolo1)

rettangolo2=(300,10,330,320)
pygame.draw.rect(screen,cornici_colore,rettangolo2)

rettangolo3=(300,370,330,80)
r3=pygame.draw.rect(screen,cornici_colore,rettangolo3)

my_font=pygame.font.SysFont("verdana", 24, True)
'''




#def get_word():
word = random.choice(word_list)
word.upper()
#word = "uva"
#word.upper()
word_completion = []

for index in range(0,len(word)):
    word_completion.append(" _ ")

#def play(word): #fa partire il programma
#word_completion = " _ " * len(word)
guessed = False 
guessed_letters = []
impiccato = 0
lettera=""
lettera_trovata = False
input_lettera = True
print(word_completion)
separatore=" "

#parola=separatore.join(word_completion)#trasforma da lista in stringa
'''
text_box=my_font.render(parola, False, color)
screen.blit(text_box,(300,370))
pygame.display.update()
'''

while (guessed==False) and (impiccato < 9): 
    input_lettera = True
    while input_lettera==True:
        lettera_trovata =False
        lettera=input("Inserisci una lettera ").upper()
        #for event in pygame.event.get():
        #while event.type == pygame.KEYDOWN:
        #lettera=event.KEY
        #break
        if lettera in guessed_letters: 
            print("La lettera è già stata inserita")
            input_lettera = True
        else:
            input_lettera = False

    # Controllo TUTTE le lettere della parola nascosta
    for indice in range(0, len(word)):
        if lettera == word[indice]:
            lettera_trovata = True
            word_completion[indice]= lettera
            print(word_completion)
            guessed_letters.append(lettera)
            if len(guessed_letters)== len(word):
                print("Hai vinto")
                guessed=True
                break

    if lettera_trovata == False:
        impiccato=impiccato+1
        tentativi_rimasti=9-impiccato
        print("Riprova. Ti rimangono ", tentativi_rimasti," tentativi" )
        ''''if tentativi_rimasti==8:
            pygame.draw.line(screen, color, (30,430), (180,430),3)
            pygame.display.flip()
            pygame.display.update()
        if tentativi_rimasti==7:
            pygame.draw.line(screen, color, (105,430), (105,230),3)
            pygame.display.flip()
            pygame.display.update()'''

        if impiccato == 9:
            print("hai perso")
            print("La parola è ",word)