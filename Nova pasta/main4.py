import pygame
import os

# Inicializando o Pygame
pygame.init()

# Definindo o tamanho da janela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mover Imagem com Setas e Pular com Espaço")

# Definindo a cor de fundo
BG_COLOR = (30, 30, 40)  # cor de fundo (um tom escuro)

# Carregar a imagem
image_file = "player.png"  # coloque o nome da sua imagem aqui
if os.path.exists(image_file):
    img = pygame.image.load(image_file).convert_alpha()  # Carregar a imagem
    img_rect = img.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Centraliza a imagem
else:
    print("Imagem não encontrada!")

# Velocidade de movimento
SPEED = 1  # pixels por movimento
JUMP_STRENGTH = 15  # Força do pulo
GRAVITY = 0.8  # Gravidade que puxa o personagem para baixo

# Variáveis de pulo
is_jumping = False
y_velocity = 0  # Velocidade no eixo Y (controle de gravidade)

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Pega as teclas pressionadas
    keys = pygame.key.get_pressed()

    # Movimentação da imagem
    if keys[pygame.K_LEFT]:
        img_rect.x -= SPEED  # Move para a esquerda
    if keys[pygame.K_RIGHT]:
        img_rect.x += SPEED  # Move para a direita
    if keys[pygame.K_UP]:
        img_rect.y -= SPEED  # Move para cima
    if keys[pygame.K_DOWN]:
        img_rect.y += SPEED  # Move para baixo

    # Pulo (pressionando espaço)
    if keys[pygame.K_SPACE] and not is_jumping:
        is_jumping = True
        y_velocity = -JUMP_STRENGTH  # Força inicial do pulo

    # Aplicar a gravidade
    if is_jumping:
        img_rect.y += y_velocity  # Movimenta o personagem para cima ou para baixo

        # Atualizar a velocidade do pulo
        y_velocity += GRAVITY

        # Quando o personagem atingir o "chão", ele para de cair
        if img_rect.bottom >= HEIGHT:
            img_rect.bottom = HEIGHT
            is_jumping = False
            y_velocity = 0

    # Preencher o fundo
    screen.fill(BG_COLOR)

    # Desenhar a imagem na tela
    screen.blit(img, img_rect.topleft)

    # Atualizar a tela
    pygame.display.flip()

# Finalizar o Pygame
pygame.quit()