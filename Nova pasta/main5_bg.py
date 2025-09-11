import pygame
import os

# Inicializando o Pygame
pygame.init()

# Definindo o tamanho da janela padrão
WIDTH, HEIGHT = 1020, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)  # Janela redimensionável
pygame.display.set_caption("Mover Imagem com Setas")

# Definindo a cor de fundo (usada se não houver imagem de fundo)
BG_COLOR = (193, 0, 40)  # cor de fundo (um tom escuro)

# Carregar a imagem do personagem
image_file = "GAME\\player.png"  # Coloque o nome correto da sua imagem aqui
if os.path.exists(image_file):
    img = pygame.image.load(image_file).convert_alpha()  # Carregar a imagem
    img_rect = img.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Centraliza a imagem
else:
    print("Imagem do personagem não encontrada!")
    img = None
    img_rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, 50, 50)  # Retângulo padrão para evitar erro

# Carregar a imagem de fundo (original)
background_file = "GAME\\background.png"  # Caminho para sua imagem de fundo
if os.path.exists(background_file):
    background_orig = pygame.image.load(background_file).convert()
    background = pygame.transform.scale(background_orig, (WIDTH, HEIGHT))
else:
    background_orig = None
    background = None
    print("Imagem de fundo não encontrada!")

# Velocidade de movimento
SPEED = 15  # pixels por movimento
JUMP_STRENGTH = 30  # Força do pulo (quanto maior, mais alto o pulo)
GRAVITY = 0.9  # Gravidade, fazendo o personagem cair
JUMPING = False  # Indica se o personagem está no ar
VELOCITY_Y = 0  # Velocidade no eixo Y (inicialmente sem velocidade de pulo)

# Função para centralizar a imagem conforme o tamanho da tela
def centralize_image():
    global img_rect, WIDTH, HEIGHT
    img_rect.center = (WIDTH // 2, HEIGHT // 2)  # Centraliza a imagem no centro da tela

# Variáveis para controle de redimensionamento
last_width, last_height = WIDTH, HEIGHT

# Limite de movimento para que o personagem não saia da tela
def limit_movement():
    global img_rect, WIDTH, HEIGHT
    # Limita a posição da imagem para não sair da tela
    if img_rect.left < 0:
        img_rect.left = 0
    if img_rect.right > WIDTH:
        img_rect.right = WIDTH
    if img_rect.top < 0:
        img_rect.top = 0
    if img_rect.bottom > HEIGHT:
        img_rect.bottom = HEIGHT

# Função para realizar o pulo
def jump():
    global VELOCITY_Y, JUMPING
    if not JUMPING:
        VELOCITY_Y = -JUMP_STRENGTH  # Inicia o pulo para cima
        JUMPING = True

# Função para atualizar o movimento do pulo
def update_jump():
    global VELOCITY_Y, JUMPING, img_rect
    if JUMPING:
        VELOCITY_Y += GRAVITY  # Simula a gravidade
        img_rect.y += VELOCITY_Y  # Atualiza a posição Y do personagem

        # Se o personagem estiver tocando o chão novamente, para o pulo
        if img_rect.bottom >= HEIGHT:
            img_rect.bottom = HEIGHT  # Garante que o personagem não passe do chão
            JUMPING = False
            VELOCITY_Y = 0  # Reseta a velocidade no eixo Y

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Verifica se o tamanho da janela foi alterado
    current_width, current_height = screen.get_size()

    # Se a janela foi redimensionada, atualiza variáveis e redimensiona fundo e personagem
    if current_width != last_width or current_height != last_height:
        WIDTH, HEIGHT = current_width, current_height
        centralize_image()  # Centraliza a imagem quando a janela mudar de tamanho
        if background_orig:
            background = pygame.transform.scale(background_orig, (WIDTH, HEIGHT))  # Redimensiona fundo a partir da original
        last_width, last_height = current_width, current_height

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

    # Pulo (tecla Space)
    if keys[pygame.K_SPACE]:
        jump()  # Ativa o pulo

    # Limita o movimento para não sair da tela
    limit_movement()

    # Atualiza a física do pulo
    update_jump()

    # Desenha o fundo
    if background:
        screen.blit(background, (0, 0))
    else:
        screen.fill(BG_COLOR)  # Caso não tenha fundo, mantém a cor de fundo

    # Desenhar a imagem na tela
    if img:
        screen.blit(img, img_rect.topleft)

    # Atualizar a tela
    pygame.display.flip()

# Finalizar o Pygame
pygame.quit()