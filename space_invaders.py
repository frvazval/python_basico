import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir los colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

# Tamaño de la ventana
ANCHO_VENTANA = 800
ALTO_VENTANA = 600

# Crear la ventana
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Space Invaders")

# FPS
FPS = 60
reloj = pygame.time.Clock()

# Definir la nave
class Nave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 30))
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO_VENTANA // 2
        self.rect.bottom = ALTO_VENTANA - 10
        self.velocidad = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocidad
        if keys[pygame.K_RIGHT] and self.rect.right < ANCHO_VENTANA:
            self.rect.x += self.velocidad

    def disparar(self):
        bala = Bala(self.rect.centerx, self.rect.top)
        todos_los_sprites.add(bala)
        balas.add(bala)

# Definir las balas
class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocidad = 7

    def update(self):
        self.rect.y -= self.velocidad
        if self.rect.bottom < 0:
            self.kill()

# Definir los enemigos
class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 30))
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, ANCHO_VENTANA - self.rect.width)
        self.rect.y = random.randint(50, 200)
        self.velocidad = random.randint(1, 3)

    def update(self):
        self.rect.y += self.velocidad
        if self.rect.top > ALTO_VENTANA:
            self.rect.x = random.randint(0, ANCHO_VENTANA - self.rect.width)
            self.rect.y = random.randint(-40, -10)
            self.velocidad = random.randint(1, 3)

# Crear los grupos de sprites
todos_los_sprites = pygame.sprite.Group()
enemigos = pygame.sprite.Group()
balas = pygame.sprite.Group()

# Crear la nave
nave = Nave()
todos_los_sprites.add(nave)

# Crear los enemigos
for i in range(10):
    enemigo = Enemigo()
    todos_los_sprites.add(enemigo)
    enemigos.add(enemigo)

# Bucle principal
jugando = True
while jugando:
    # Gestionar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                nave.disparar()

    # Actualizar los sprites
    todos_los_sprites.update()

    # Verificar colisiones
    colisiones = pygame.sprite.groupcollide(balas, enemigos, True, True)
    for colision in colisiones:
        enemigo = Enemigo()
        todos_los_sprites.add(enemigo)
        enemigos.add(enemigo)

    # Dibujar todo
    ventana.fill(NEGRO)
    todos_los_sprites.draw(ventana)

    # Actualizar la ventana
    pygame.display.flip()

    # Controlar los FPS
    reloj.tick(FPS)

# Salir del juego
pygame.quit()