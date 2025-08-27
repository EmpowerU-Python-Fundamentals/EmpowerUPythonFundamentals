import pygame
import random
import sys
import os
import colors
import threading
import queue
import sounddevice as sd
import json
from vosk import Model, KaldiRecognizer
from gtts import gTTS

pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=512)
pygame.init()
pygame.mixer.init()

WIDTH = 800
HEIGHT = 600


PLAYER_SPEED = 350  # швидкість
INITIAL_SPAWN_MS = 900  #  час між появою астероїдів у мілісекундах

gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("Space Game")
big_font = pygame.font.SysFont('Calibri', 90, True, False)
font = pygame.font.SysFont('Calibri', 40, True, False)
small_font = pygame.font.SysFont('Calibri', 20, True, False)

running = True
TRIGGERS = ["блін", "берлін", "блідий", "бля", "для", "капець", "бляха" ]
voice_triggered = False

clock = pygame.time.Clock()
FPS = 60

# =====================Створення відносних шляхів==========================

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


background_image = pygame.image.load(resource_path("mini_projects\yuliaklimchuk\Space_project\img/bg.jpg"))
background_image= pygame.transform.scale(background_image, (WIDTH, HEIGHT)) 

highscore_file = resource_path("mini_projects\yuliaklimchuk\Space_project\highscore.txt")

with open (highscore_file, 'r', encoding="utf-8") as file:
    highscore = int(file.read() or 0)

# ==============================================Оголошення класів===========================================================
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(resource_path("mini_projects\yuliaklimchuk\Space_project\img/ship.png")).convert_alpha()  # PNG з прозорістю
        self.image = pygame.transform.scale(self.image, (120, 120)) 
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 4
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # межі екрану
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(resource_path("mini_projects\yuliaklimchuk\Space_project\img/asteroid.png")).convert_alpha()  # PNG з прозорістю
        self.image = pygame.transform.scale(self.image, (80, 80)) 
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = random.randint(1,2)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if (self.rect.y <= HEIGHT):
            self.rect.y += self.speed 
        else:
            self.kill()  

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__()
        self.image = pygame.image.load(resource_path("mini_projects\yuliaklimchuk\Space_project\img/explosion.png") if img == "ship" else resource_path("mini_projects\yuliaklimchuk\Space_project\img/asteroid_explosion.png")).convert_alpha()  # PNG з прозорістю
        self.image = pygame.transform.scale(self.image, (110, 110)) 
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        # час життя вибуху (в мілісекундах)
        self.lifetime = 1000  
        self.spawn_time = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.spawn_time > self.lifetime:
            self.kill()  

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.color = colors.Gray
        self.radius = 5
        self.speed = 10
        self.image = pygame.Surface((self.radius*2, self.radius*2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.y -= self.speed   
        if self.rect.bottom < 0:    
            self.kill()


# ===========================================Налаштування Vosk для слухання======================================
q = queue.Queue()
def callback(indata, frames, time, status):
    if status:
        print("STATUS:", status)
    q.put(bytes(indata))
# 1. Підбираємо частоту саме з мікрофона
device_info = sd.query_devices(kind='input')
SAMPLE_RATE = int(device_info['default_samplerate'])

# 2. Завантажуємо модель
model = Model(resource_path("mini_projects\yuliaklimchuk\Space_project\model"))  
recognizer = KaldiRecognizer(model, SAMPLE_RATE)

# ============================================= Слухання голосу ===============================
def listen_voice():
    global voice_triggered
    last_said = ""
    with sd.RawInputStream(samplerate=SAMPLE_RATE, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        while True:
            try:
                data = q.get(timeout=0.1)  #не блокує, якщо даних немає
            except queue.Empty:
                continue  # просто продовжуємо цикл

            if recognizer.AcceptWaveform(data):
                res = json.loads(recognizer.Result())
                if isinstance(res, dict):
                    said = res.get("text", "")
            else:
                pres = json.loads(recognizer.PartialResult())
                if isinstance(pres, dict):
                    said = pres.get("partial", "")

            for trigger in TRIGGERS:
                if trigger in said and said != last_said:
                    voice_triggered = True
                    last_said = said
                    break

# запускаємо слухання в окремому потоці
threading.Thread(target=listen_voice, daemon=True).start()

# ===========================================Підготовка голосів для мовлення============================
voices = {
    "censor": "voice_censor.mp3",
    "welcome": "voice_welcome.mp3",
    "game_over": "voice_game_over.mp3"
}

# Генеруємо файли, якщо їх ще немає
if not os.path.exists(resource_path(voices["censor"])):
    tts = gTTS(text="Тихше, тихше! Тут цензура!", lang="uk")
    voice_path = resource_path(voices["censor"])
    tts.save(voice_path)

if not os.path.exists(resource_path(voices["welcome"])):
    tts = gTTS(text="Ну давай покажи на що ти здатен!", lang="uk")
    voice_path = resource_path(voices["welcome"])
    tts.save(voice_path)

if not os.path.exists(resource_path(voices["game_over"])):
    tts = gTTS(text="Пу-пу-пу... Не фортанУло! Може вийде іншого разу", lang="uk")
    voice_path = resource_path(voices["game_over"])
    tts.save(voice_path)
# Завантажуємо у pygame
censor_sound = pygame.mixer.Sound(resource_path(voices["censor"]))
welcome_sound = pygame.mixer.Sound(resource_path(voices["welcome"]))
game_over_sound = pygame.mixer.Sound(resource_path(voices["game_over"]))

ch_welcome = pygame.mixer.Channel(0)
ch_censor = pygame.mixer.Channel(1)
ch_game_over = pygame.mixer.Channel(2)

# ===================================================Екран Game over=====================================================
def game_over_screen(score, highscore):

    waiting = True
    if score > highscore:
            highscore = score
            with open (highscore_file, 'w', encoding="utf-8") as file:
                file.write(str(highscore))
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:   # перезапуск гри
                    waiting = False
                elif event.key == pygame.K_ESCAPE: 
                    pygame.quit()
                    sys.exit()

        gameDisplay.blit(background_image, (0, 0))

        game_over_text = big_font.render("GAME OVER", True, colors.Aqua)
        gameDisplay.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//3))

        score_text = font.render(f"Score: {score}", True, colors.Black)
        gameDisplay.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2))

        highscore_text = font.render(f"HIGHSCORE: {highscore}", True, colors.Black)
        gameDisplay.blit(highscore_text, (WIDTH//2 - highscore_text.get_width()//2, HEIGHT//2+50))

        restart_text = font.render("Press R to Restart or ESC to Quit", True, colors.Silver)
        gameDisplay.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//1.5))

        pygame.display.update()

# ============================================Основний цикл гри============================================================

def game_loop():
    global highscore, voice_triggered
    
    while True:
        score = 0
        player_shoot_delay = 200   # мілісекунди між пострілами
        last_shot = 0
        player = Player(WIDTH // 2, HEIGHT - 100)
        asteroids = pygame.sprite.Group()
        explosions = pygame.sprite.Group() 
        bullets = pygame.sprite.Group()
        all_sprites = pygame.sprite.Group()
        all_sprites.add(player)

        running = True
        game_over = False

        # Для вітального звуку
        if not ch_welcome.get_busy():
            ch_welcome.play(welcome_sound)

        # Для зміни швидкості  астероїдів
        asteroid_speed_multiplier = 1.0  
        speed_increase_interval = 10000
        last_speed_increase = pygame.time.get_ticks()
        round = 1
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if score > int(highscore):
                        highscore = score
                        with open (highscore_file, 'w', encoding="utf-8") as file:
                            file.write(str(highscore))
                    running = False
                    pygame.quit()
                    sys.exit()

            #=========Поява астероїдів================
            if random.random() < 0.01:  # ймовірність появи в кожному кадрі
                asteroid = Asteroid(random.randint(40, WIDTH-10), -40)
                asteroid.speed = int(asteroid.speed * asteroid_speed_multiplier)
                all_sprites.add(asteroid)
                asteroids.add(asteroid)
            
            #=========Збільшення швидкості астероїдів з часом=========
            now = pygame.time.get_ticks()  
            if now - last_speed_increase > speed_increase_interval:
                asteroid_speed_multiplier += 0.5
                round +=1
                last_speed_increase = now

            #=========Постріли================
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                now = pygame.time.get_ticks()  
                if now - last_shot > player_shoot_delay:
                    bullet = Bullet(player.rect.centerx, player.rect.top)
                    all_sprites.add(bullet)
                    bullets.add(bullet)
                    last_shot = now
            #===================================
            if not game_over:
                all_sprites.update()
                player.update()
            else:
                explosions.update() 
            #==================Зіткнення астероїда з кораблем======================
            for asteroid in asteroids:
                offset = (asteroid.rect.x - player.rect.x, asteroid.rect.y - player.rect.y)
                collision_point = player.mask.overlap(asteroid.mask, offset)
                if collision_point and not game_over:
                    global_x = player.rect.x + collision_point[0]
                    global_y = player.rect.y + collision_point[1]
                    explosion = Explosion(global_x, global_y, "ship")
                    all_sprites.add(explosion)
                    explosions.add(explosion)  
                    ch_game_over.stop()  
                    ch_game_over.play(game_over_sound)
                    game_over = True
                    break 
                if game_over and len(explosions) == 0:
                    game_over_screen(score, highscore)
                    pygame.event.clear()
                    running = False
                    break
            #==================Влучання кулі в астероїд======================
            for bullet in bullets:
                for asteroid in asteroids:
                    offset = ((bullet.rect.centerx+bullet.radius) -  asteroid.rect.x, (bullet.rect.bottom+2*bullet.radius) -asteroid.rect.y)
                    collision_point = asteroid.mask.overlap(bullet.mask, offset)
                    if collision_point:
                        global_x = asteroid.rect.x + collision_point[0]
                        global_y = asteroid.rect.y + collision_point[1]
                        explosion = Explosion(global_x, global_y, "asteroid")
                        all_sprites.add(explosion)
                        explosions.add(explosion)  
                        score +=100
                        asteroid.kill()

            #====================== Реагування на слова-тригери=========================
            if voice_triggered:
                voice_triggered = False
                if not ch_censor.get_busy():
                    ch_censor.play(censor_sound)
                
            #====================== Малювання=========================
            gameDisplay.blit(background_image, (0, 0))  

            #===========================Score display=================
            score_display = pygame.Surface((WIDTH/6, HEIGHT/6), pygame.SRCALPHA)  
            pygame.draw.rect(score_display, (255, 255, 255, 100), (0, 0, WIDTH/6, HEIGHT/6))  
            gameDisplay.blit(score_display, (WIDTH-WIDTH/6, 0))

            raund_text = small_font.render(f"Round {round}", True, colors.Black)
            score_text = small_font.render(f"Score {score}", True, colors.Black)
            gameDisplay.blit(raund_text, (WIDTH-WIDTH/6+20, 30))
            gameDisplay.blit(score_text, (WIDTH-WIDTH/6+20, 60))
            #=====================================================
            all_sprites.draw(gameDisplay)
            pygame.display.update()
            clock.tick(FPS)
        
    
game_loop()


