# Créé par Utilisateur, le 01/03/2022 en Python 3.7

import pygame
import pygame.base
from random import *
import shelve
from sys import exit

niveau1 = shelve.open('score/score1.txt')
niveau1v1 = shelve.open('score/score1-1.txt')
niveau1v2 = shelve.open('score/score1-2.txt')
niveau2 = shelve.open('score/score2.txt')
niveau2v1 = shelve.open('score/score2-1.txt')
niveau2v2 = shelve.open('score/score2-2.txt')
niveau3 = shelve.open('score/score3.txt')
niveau3v1 = shelve.open('score/score3-1.txt')
niveau3v2 = shelve.open('score/score3-2.txt')
pygame.init()
surface = pygame.image.load("images/Snakeivo.png")
pygame.display.set_icon(surface)
# quelques couleurs au cas ou
white = (255, 255, 255)
black = (0, 255, 0)
red = (255, 0, 0)

meilleurscorenv1 = niveau1['score']
meilleurscorenv1v1 = niveau1v1['score1']
meilleurscorenv1v2 = niveau1v2['score2']
meilleurscorenv2 = niveau2['score3']
meilleurscorenv2v1 = niveau2v1['score4']
meilleurscorenv2v2 = niveau2v2['score5']
meilleurscorenv3 = niveau3['score6']
meilleurscorenv3v1 = niveau3v1['score7']
meilleurscorenv3v2 = niveau3v2['score8']

dis = pygame.display.set_mode((1, 1))


def button(screen, position, text):
    font = pygame.font.SysFont("Arial", 15)
    text_render = font.render(text, 1, (255, 0, 0))
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (0, 0, 0), (x, y), (x + w, y), 5)
    pygame.draw.line(screen, (0, 0, 0), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (0, 0, 0), (x, y + h), (x + w, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w, y+h), [x + w, y], 5)
    pygame.draw.rect(screen, (255, 255, 255), (x, y, w, h))
    return screen.blit(text_render, (x, y))


def jeu_debut():
    global gamefun, niveau, speedblock

    speed = 5
    niveau = 1
    speedblock = 1
    meilleurscore = ''

    # lance l'interface de jeu
    meilleurscoretxt = str(meilleurscorenv1)
    coordonneex, coordonneey = 610, 318

    dis = pygame.display.set_mode((800, 450))
    game_over = False
    pygame.display.set_caption('Snake Game')

    image_fond = pygame.image.load("images/SNAKE_pagecli.png")
    dis.blit(image_fond, (0, 0))

    myfont12 = pygame.font.SysFont('Retro Gaming', 40)

    textsurface = myfont12.render("Niveau 1", False, white)

    b1 = button(dis, (0, 0), "Bouton fun")

    SPEED_text = myfont12.render("SLOW", False, white)
    best = myfont12.render(meilleurscoretxt, False, white)
    hight = myfont12.render("Best score :", False, white)

    dis.blit(SPEED_text, (610, 318))
    dis.blit(textsurface, (353, 322))
    dis.blit(best, (480, 295))
    dis.blit(hight, (315, 295))

    pygame.display.update()
    gamefun = False

    while not game_over:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_over = True
            # si on appuie sur le bouton alors game fun = true ce qui fait que la pomme disparait
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    gamefun = True
            # si une touche et appuye alors :
            if event.type == pygame.KEYDOWN:
                # choix des niveaux avec les flèches qui fait +1 ou -1 à niveau et speedblock
                if event.key == pygame.K_LEFT or event.key == pygame.K_q:
                    niveau -= 1

                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    niveau += 1

                if event.key == pygame.K_UP or event.key == pygame.K_z:
                    speedblock += 1

                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    speedblock -= 1

                # comme on rajoute 1 ou on enlève 1 aux variables niveaux et vitesse il faut pouvoir les remèttre à un cran en dessous ou au dessus
                # car sinon elle vont a 4 5 6 7 ... et la selection des niveau et plus compliqué
                # comme le niveau max est 3 quand niveau est a 4 on le remet a 3
                if niveau > 3:
                    niveau = 3

                if niveau < 1:
                    niveau = 1

                # pareille mais avec la vitesse
                if speedblock > 3:
                    speedblock = 3

                if speedblock < 1:
                    speedblock = 1

                # choix de la vitesse du niveau
                if speedblock == 1:

                    b1 = button(dis, (0, 0), "Bouton fun")

                    coordonneex = 610

                    SPEED_text = myfont12.render("SLOW", False, white)

                    dis.blit(SPEED_text, (coordonneex, coordonneey))
                    dis.blit(textsurface, (353, 322))
                    pygame.display.update()

                    speed = 5

                if speedblock == 2:

                    b1 = button(dis, (0, 0), "Bouton fun")

                    SPEED_text = myfont12.render("MEDIUM", False, white)

                    coordonneex = 597

                    dis.blit(SPEED_text, (coordonneex, coordonneey))
                    dis.blit(textsurface, (353, 322))
                    pygame.display.update()

                    speed = 7

                if speedblock == 3:
                    b1 = button(dis, (0, 0), "Bouton fun")

                    SPEED_text = myfont12.render("FAST", False, white)

                    coordonneex = 615

                    dis.blit(SPEED_text, (coordonneex, coordonneey))
                    dis.blit(textsurface, (353, 322))
                    pygame.display.update()

                    speed = 10

                # choix de chaque niveaux
                if niveau == 1:
                    dis.blit(image_fond, (0, 0))
                    textsurface = myfont12.render("Niveau 1", False, white)
                    if speedblock == 1:
                        meilleurscoretxt = str(meilleurscorenv1)
                        best = myfont12.render(meilleurscoretxt, False, white)
                        hight = myfont12.render("Best score :", False, white)
                        dis.blit(best, (480, 295))
                        dis.blit(hight, (315, 295))
                        dis.blit(textsurface, (353, 322))
                    if speedblock == 2:
                        meilleurscoretxt = str(meilleurscorenv1v1)
                        best = myfont12.render(meilleurscoretxt, False, white)
                        hight = myfont12.render("Best score :", False, white)
                        dis.blit(best, (480, 295))
                        dis.blit(hight, (315, 295))
                        dis.blit(textsurface, (353, 322))
                    if speedblock == 3:
                        meilleurscoretxt = str(meilleurscorenv1v2)
                        best = myfont12.render(meilleurscoretxt, False, white)
                        hight = myfont12.render("Best score :", False, white)
                        dis.blit(best, (480, 295))
                        dis.blit(hight, (315, 295))
                        dis.blit(textsurface, (353, 322))
                    dis.blit(SPEED_text, (coordonneex, coordonneey))
                    b1 = button(dis, (0, 0), "Bouton fun")
                    pygame.display.update()

                if niveau == 2:
                    dis.blit(image_fond, (0, 0))
                    textsurface = myfont12.render("Niveau 2", False, white)
                    if speedblock == 1:
                        meilleurscoretxt = str(meilleurscorenv2)
                        best = myfont12.render(meilleurscoretxt, False, white)
                        hight = myfont12.render("Best score :", False, white)
                        dis.blit(best, (480, 295))
                        dis.blit(hight, (315, 295))
                        dis.blit(textsurface, (353, 322))
                    if speedblock == 2:
                        meilleurscoretxt = str(meilleurscorenv2v1)
                        best = myfont12.render(meilleurscoretxt, False, white)
                        hight = myfont12.render("Best score :", False, white)
                        dis.blit(best, (480, 295))
                        dis.blit(hight, (315, 295))
                        dis.blit(textsurface, (353, 322))
                    if speedblock == 3:
                        meilleurscoretxt = str(meilleurscorenv2v2)
                        best = myfont12.render(meilleurscoretxt, False, white)
                        hight = myfont12.render("Best score :", False, white)
                        dis.blit(best, (480, 295))
                        dis.blit(hight, (315, 295))
                        dis.blit(textsurface, (353, 322))
                    dis.blit(SPEED_text, (coordonneex, coordonneey))
                    b1 = button(dis, (0, 0), "Bouton fun")
                    pygame.display.update()

                if niveau == 3:
                    dis.blit(image_fond, (0, 0))
                    textsurface = myfont12.render("Niveau 3", False, white)
                    if speedblock == 1:
                        meilleurscoretxt = str(meilleurscorenv3)
                        best = myfont12.render(meilleurscoretxt, False, white)
                        hight = myfont12.render("Best score :", False, white)
                        dis.blit(best, (480, 295))
                        dis.blit(hight, (315, 295))
                        dis.blit(textsurface, (353, 322))
                    if speedblock == 2:
                        meilleurscoretxt = str(meilleurscorenv3v1)
                        best = myfont12.render(meilleurscoretxt, False, white)
                        hight = myfont12.render("Best score :", False, white)
                        dis.blit(best, (480, 295))
                        dis.blit(hight, (315, 295))
                        dis.blit(textsurface, (353, 322))
                    if speedblock == 3:
                        meilleurscoretxt = str(meilleurscorenv3v2)
                        best = myfont12.render(meilleurscoretxt, False, white)
                        hight = myfont12.render("Best score :", False, white)
                        dis.blit(best, (480, 295))
                        dis.blit(hight, (315, 295))
                        dis.blit(textsurface, (353, 322))
                    dis.blit(SPEED_text, (coordonneex, coordonneey))
                    b1 = button(dis, (0, 0), "Bouton fun")
                    pygame.display.update()

                # quand la touche entre est appuiyé si
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    if niveau == 1:
                        a = 80
                        MainLoop("images/cases12.png", a, speed)
                    if niveau == 2:
                        a = 50
                        MainLoop("images/cases13.png", a, speed)
                    if niveau == 3:
                        a = 40
                        MainLoop("images/cases.png", a, speed)

                # si
                if event.key == pygame.K_ESCAPE:
                    fermer()

# fonction pour fermer la fenetter


def fermer():
    niveau1.close()
    niveau1v1.close()
    niveau1v2.close()
    niveau2.close()
    niveau2v1.close()
    niveau2v2.close()
    niveau3v1.close()
    niveau3v2.close()
    niveau3.close()
    pygame.display.quit()
    pygame.quit()
    exit()


def MainLoop(Image, tailleblock, Speed):
    global snake_liste_parties, score, snake_block, meilleurscore, score11
    # def la taille de l'interface

    dis = pygame.display.set_mode((800, 800))
    # et le nom de l'interface
    pygame.display.set_caption('Snake Game')

    # charge l'image de fond avec la grille
    image_fond = pygame.image.load(Image)
    game_over = False

    # place la snake a un endroit random dans le jeu
    x = randrange(tailleblock, 790-tailleblock, tailleblock)
    y = randrange(tailleblock, 790-tailleblock, tailleblock)
    x_change = 0
    y_change = 0

    clock = pygame.time.Clock()

    # def de vers ou vas le snake au début
    vas_haut = False
    vas_droite = False
    vas_gauche = False
    vas_bas = False

    # liste des coordonée de chaque morceau du snak
    snake_liste_parties = []

    # vitesse du snake
    tic = Speed

    # Coordonée de la pomme
    pommex = randrange(tailleblock, 790-tailleblock, tailleblock)
    pommey = randrange(tailleblock, 790-tailleblock, tailleblock)

    # nombre de pomme mangé mais aussi la taille du snake
    score = 0
    score11 = ""

    # taille du block snack
    snake_block = tailleblock

    # temps que le jeu est pas fini on regarde si une des flèche a été activé et si c'est le cas on avance dans la direction
    while not game_over:
        score11 = str(score)
        dis.blit(image_fond, (0, 0))

        if score == 0:
            pygame.draw.rect(
                dis, red, [pommex, pommey, snake_block, snake_block])
        myfont12 = pygame.font.SysFont('Retro Gaming', 60)
        textsurface = myfont12.render(score11, False, red)
        dis.blit(textsurface, (10, 0))

        for event in pygame.event.get():
            pygame.display.update()
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT or event.key == pygame.K_q:
                    # si une flèche auposé à la direction du snake est appuyer alors il ne se passe rien ex : il va vers la droite il ne peut pas aller vers la gauche
                    if vas_droite == False:
                        vas_haut = False
                        vas_bas = False
                        vas_droite = False
                        vas_gauche = True
                        # bouge le snake dans la bonne direction
                        x_change = -snake_block
                        # quand il change de direction on remet a 0 le changement du snake pour plus qu'il bouge dans la direction précedente
                        y_change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if vas_gauche == False:
                        vas_haut = False
                        vas_bas = False
                        vas_gauche = False
                        vas_droite = True
                        x_change = snake_block
                        y_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_z:
                    if vas_bas == False:
                        vas_bas = False
                        vas_droite = False
                        vas_gauche = False
                        vas_haut = True
                        y_change = -snake_block
                        x_change = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if vas_haut == False:
                        vas_haut = False
                        vas_droite = False
                        vas_gauche = False
                        vas_bas = True
                        y_change = snake_block
                        x_change = 0
                if event.key == pygame.K_ESCAPE:
                    fermer()

        # replace la pomme si elle est dans le snake
        POMMExy = []
        POMMExy = [[pommex, pommey]]
        for coordo1 in range(len(snake_liste_parties)):
            if snake_liste_parties[coordo1][0] == pommex and snake_liste_parties[coordo1][1] == pommey:
                pommex = randrange(tailleblock, 790-tailleblock, tailleblock)
                pommey = randrange(tailleblock, 790-tailleblock, tailleblock)
                pygame.draw.rect(
                    dis, red, [pommex, pommey, snake_block, snake_block])
                pygame.display.update()

        # print(x,y,x_change,y_change)
        # change les coordonée du snake dans le direction voulu
        x += x_change
        y += y_change

        # place la pomme de façon aleatoire sur le jeu
        if gamefun == False:
            pygame.draw.rect(
                dis, red, [pommex, pommey, snake_block, snake_block])

        # fait une liste des éléments de la liste
        Tete_snake = []
        # ajoute/acctualise a la liste les coordonées du snake
        Tete_snake.append(x)
        Tete_snake.append(y)
        # on ajoute a la liste comprenant toutes les coordonées les coordonées de la tête
        snake_liste_parties.append(Tete_snake)

        # si la position de snake est la même que la pomme alors on augmante le score et on replace la pomme à un autre endroit
        if x == pommex and y == pommey:
            pommex = randrange(tailleblock, 790-tailleblock, tailleblock)
            pommey = randrange(tailleblock, 790-tailleblock, tailleblock)
            pygame.draw.rect(
                dis, red, [pommex, pommey, snake_block, snake_block])
            pygame.display.update()
            score += 1

        prog_qui_gere_la_longueur_du_snake(snake_block, snake_liste_parties)
        pygame.draw.rect(dis, (20, 255, 255), [x, y, snake_block, snake_block])
        pygame.display.update()

        # verifie que la longueur du snake ne soit pas plus long que le score et si c'est le cas suprime le dernier element
        # sans cette ligne le snake ne retrecie pas
        if len(snake_liste_parties) > score:
            del snake_liste_parties[0]

        if x <= tailleblock-20 or y <= tailleblock-20 or x >= 790-tailleblock or y >= 790-tailleblock:
            ecran_fin()

        xyinter = []
        xyinter = [[x, y]]
        for coordo in range(len(snake_liste_parties)-1):
            if snake_liste_parties[coordo][0] == xyinter[0][0] and snake_liste_parties[coordo][1] == xyinter[0][1]:
                ecran_fin()

        clock.tick(tic)

    fermer()

# cette def va prendre en compte la liste des partie du snake et va faire en sorte que le snake entier soit affiché
# il parcoure la liste et affiche un block vert au bonne coordonné


def prog_qui_gere_la_longueur_du_snake(snake_block, snake_list_parties):
    for x1 in snake_list_parties:
        pygame.draw.rect(dis, (0, 255, 0), [
                         x1[0], x1[1], snake_block, snake_block])


def ecran_fin():
    global meilleurscorenv1, meilleurscorenv2, meilleurscorenv3, meilleurscorenv1v1, meilleurscorenv1v2, meilleurscorenv2v1, meilleurscorenv2v2, meilleurscorenv3v1, meilleurscorenv3v2
    meilleuraffichage = ""
    if niveau == 1:
        if speedblock == 1:
            if meilleurscorenv1 < score:
                meilleurscorenv1 = score
            meilleuraffichage = str(meilleurscorenv1)
            niveau1['score'] = meilleurscorenv1
            myfont11 = pygame.font.SysFont('Retro Gaming', 90)
            bestone = myfont11.render(meilleuraffichage, False, (0, 0, 0))
            bestonetxt = myfont11.render("Best score :", False, (0, 0, 0))
            dis.blit(bestone, (560, 500))
            dis.blit(bestonetxt, (200, 500))
        if speedblock == 2:
            if meilleurscorenv1v1 < score:
                meilleurscorenv1v1 = score
            meilleuraffichage = str(meilleurscorenv1v1)
            niveau1v1['score1'] = meilleurscorenv1v1
            myfont11 = pygame.font.SysFont('Retro Gaming', 90)
            bestone = myfont11.render(meilleuraffichage, False, (0, 0, 0))
            bestonetxt = myfont11.render("Best score :", False, (0, 0, 0))
            dis.blit(bestone, (560, 500))
            dis.blit(bestonetxt, (200, 500))
        if speedblock == 3:
            if meilleurscorenv1v2 < score:
                meilleurscorenv1v2 = score
            meilleuraffichage = str(meilleurscorenv1v2)
            niveau1v2['score2'] = meilleurscorenv1v2
            myfont11 = pygame.font.SysFont('Retro Gaming', 90)
            bestone = myfont11.render(meilleuraffichage, False, (0, 0, 0))
            bestonetxt = myfont11.render("Best score :", False, (0, 0, 0))
            dis.blit(bestone, (560, 500))
            dis.blit(bestonetxt, (200, 500))

    if niveau == 2:
        if speedblock == 1:
            if meilleurscorenv2 < score:
                meilleurscorenv2 = score
            meilleuraffichage = str(meilleurscorenv2)
            niveau2['score3'] = meilleurscorenv1
            myfont11 = pygame.font.SysFont('Retro Gaming', 90)
            bestone = myfont11.render(meilleuraffichage, False, (0, 0, 0))
            bestonetxt = myfont11.render("Best score :", False, (0, 0, 0))
            dis.blit(bestone, (560, 500))
            dis.blit(bestonetxt, (200, 500))
        if speedblock == 2:
            if meilleurscorenv2v1 < score:
                meilleurscorenv2v1 = score
            meilleuraffichage = str(meilleurscorenv2v1)
            niveau2v1['score4'] = meilleurscorenv2v1
            myfont11 = pygame.font.SysFont('Retro Gaming', 90)
            bestone = myfont11.render(meilleuraffichage, False, (0, 0, 0))
            bestonetxt = myfont11.render("Best score :", False, (0, 0, 0))
            dis.blit(bestone, (560, 500))
            dis.blit(bestonetxt, (200, 500))
        if speedblock == 3:
            if meilleurscorenv2v2 < score:
                meilleurscorenv2v2 = score
            meilleuraffichage = str(meilleurscorenv2v2)
            niveau2v2['score5'] = meilleurscorenv2v2
            myfont11 = pygame.font.SysFont('Retro Gaming', 90)
            bestone = myfont11.render(meilleuraffichage, False, (0, 0, 0))
            bestonetxt = myfont11.render("Best score :", False, (0, 0, 0))
            dis.blit(bestone, (560, 500))
            dis.blit(bestonetxt, (200, 500))

    if niveau == 3:
        if speedblock == 1:
            if meilleurscorenv3 < score:
                meilleurscorenv3 = score
            meilleuraffichage = str(meilleurscorenv3)
            niveau3['score6'] = meilleurscorenv3
            myfont11 = pygame.font.SysFont('Retro Gaming', 90)
            bestone = myfont11.render(meilleuraffichage, False, (0, 0, 0))
            bestonetxt = myfont11.render("Best score :", False, (0, 0, 0))
            dis.blit(bestone, (560, 500))
            dis.blit(bestonetxt, (200, 500))
        if speedblock == 2:
            if meilleurscorenv3v1 < score:
                meilleurscorenv3v1 = score
            meilleuraffichage = str(meilleurscorenv3v1)
            niveau3v1['score7'] = meilleurscorenv3v1
            myfont11 = pygame.font.SysFont('Retro Gaming', 90)
            bestone = myfont11.render(meilleuraffichage, False, (0, 0, 0))
            bestonetxt = myfont11.render("Best score :", False, (0, 0, 0))
            dis.blit(bestone, (560, 500))
            dis.blit(bestonetxt, (200, 500))
        if speedblock == 3:
            if meilleurscorenv3v2 < score:
                meilleurscorenv3v2 = score
            meilleuraffichage = str(meilleurscorenv3v2)
            niveau3v2['score8'] = meilleurscorenv3v2
            myfont11 = pygame.font.SysFont('Retro Gaming', 90)
            bestone = myfont11.render(meilleuraffichage, False, (0, 0, 0))
            bestonetxt = myfont11.render("Best score :", False, (0, 0, 0))
            dis.blit(bestone, (560, 500))
            dis.blit(bestonetxt, (200, 500))

    pygame.display.update()
    myfont12 = pygame.font.SysFont('Retro Gaming', 130)
    myfont11 = pygame.font.SysFont('Retro Gaming', 90)
    Gameover = myfont12.render("GAME-OVER", False, red)
    dis.blit(Gameover, (130, 310))
    score1 = myfont11.render("Votre score :", False, red)
    score13 = myfont11.render(score11, False, red)
    Enter = myfont11.render("Press enter", False, red)
    dis.blit(score1, (190, 230))
    dis.blit(score13, (575, 230))
    dis.blit(Enter, (230, 400))
    Fin = False
    while not Fin:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    jeu_debut()
                if event.key == pygame.K_ESCAPE:
                    fermer()


jeu_debut()
