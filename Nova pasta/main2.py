import pygame
import os

# Inicializando o Pygame
pygame.init()

# Definindo o tamanho da janela
WIDTH, HEIGHT = 1000, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Janela com Imagem")

# Definindo a cor de fundo
BG_COLOR = (30, 30, 40)  # cor de fundo (um tom escuro)

# Carregar a imagem
image_file = "GAME\player.png"  # coloque o nome da sua imagem aqui
if os.path.exists(image_file):
    img = pygame.image.load(image_file).convert_alpha()  # Carregar a imagem
    img_rect = img.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Centraliza a imagem
else:
    print("Imagem não encontrada!")

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preencher o fundo
    screen.fill(BG_COLOR)

    # Desenhar a imagem na tela
    screen.blit(img, img_rect.topleft)

    # Atualizar a tela
    pygame.display.flip()

# Finalizar o Pygame
pygame.quit()