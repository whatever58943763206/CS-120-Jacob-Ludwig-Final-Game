import simpleGE, pygame, random
from pygame import mixer


class star(simpleGE.Sprite):
    def __init__(self, item):
        super().__init__(item)
        self.setImage("star.png")
        self.setSize(45, 45)
        self.minSpeed = 4
        self.maxSpeed = 6
        self.reset()
        
    def reset(self):
        self.y = 5
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
        
        
class meteor(simpleGE.Sprite):
    def __init__(self, item):
        super().__init__(item)
        self.setImage("meteor.png")
        self.setSize(60, 60)
        self.minSpeed = 2
        self.maxSpeed = 6
        self.reset()
    
    def reset(self):
        self.y = 5
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
            
            
class speed_boost(simpleGE.Sprite):
    def __init__(self, item):
        super().__init__(item)
        self.setImage("plus.png")
        self.setSize(27, 27)
        self.minSpeed_neg = (-3)
        self.maxSpeed_neg = (-5)
        self.minSpeed_pos = 3
        self.maxSpeed_pos = 5
        self.reset()
        
    def reset(self):
        self.randnum = random.randint(1, 2)
        if self.randnum == 1:
            self.y = 15
            self.x = random.randint(0, self.screenWidth)
            self.dy = random.randint(self.minSpeed_pos, self.maxSpeed_pos)
        if self.randnum == 2:
            self.y = 465
            self.x = random.randint(0, self.screenWidth)
            self.dy = random.randint(self.maxSpeed_neg, self.minSpeed_neg)


class speed_loss_1(simpleGE.Sprite):
    def __init__(self, item):
        super().__init__(item)
        self.setImage("minus.png")
        self.setSize(27, 27)
        self.minSpeed_neg = (-3)
        self.maxSpeed_neg = (-5)
        self.minSpeed_pos = 3
        self.maxSpeed_pos = 5
        self.reset()
        
    def reset(self):
        self.randnum = random.randint(1, 2)
        if self.randnum == 1:
            self.y = 15
            self.x = random.randint(0, self.screenWidth)
            self.dy = random.randint(self.minSpeed_pos, self.maxSpeed_pos)
        if self.randnum == 2:
            self.y = 465
            self.x = random.randint(0, self.screenWidth)
            self.dy = random.randint(self.maxSpeed_neg, self.minSpeed_neg)

    def checkBounds(self):
        if self.y < 5:
            self.reset()
        if self.y > 475:
            self.reset()
            
            
class speed_loss_2(simpleGE.Sprite):
    def __init__(self, item):
        super().__init__(item)
        self.setImage("minus.png")
        self.setSize(27, 27)
        self.minSpeed_neg = (-3)
        self.maxSpeed_neg = (-5)
        self.minSpeed_pos = 3
        self.maxSpeed_pos = 5
        self.reset()
        
    def reset(self):
        self.randnum = random.randint(1, 2)
        if self.randnum == 1:
            self.y = 15
            self.x = random.randint(0, self.screenWidth)
            self.dy = random.randint(self.minSpeed_pos, self.maxSpeed_pos)
        if self.randnum == 2:
            self.y = 465
            self.x = random.randint(0, self.screenWidth)
            self.dy = random.randint(self.maxSpeed_neg, self.minSpeed_neg)

    def checkBounds(self):
        if self.y < 5:
            self.reset()
        if self.y > 475:
            self.reset()


class spaceship(simpleGE.Sprite):
    def __init__(self, item):
        super().__init__(item)
        self.setImage("spaceship.png")
        self.setSize(50, 50)
        self.position = (320, 375)
        self.moveSpeed = 7
        
    def process(self):
        if (self.isKeyPressed(pygame.K_LEFT)) and (self.x > 15):
            self.x -= self.moveSpeed
        if (self.isKeyPressed(pygame.K_RIGHT)) and (self.x < 625):
            self.x += self.moveSpeed
        if (self.isKeyPressed(pygame.K_UP)) and (self.y > 20):
            self.y -= self.moveSpeed
        if (self.isKeyPressed(pygame.K_DOWN)) and (self.y < 465):
            self.y += self.moveSpeed
        
           
class score_label(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (520, 50)
            

class health_label(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Health amount:"
        self.center = (475, 100)
            

class heart_1(simpleGE.Sprite):
    def __init__(self, item):
        super().__init__(item)
        self.setImage("heart.png")
        self.setSize(18, 18)
        self.position = (566, 100)
        self.eliminate()
        
    def eliminate(self):
        self.kill()
        

class heart_2(simpleGE.Sprite):
    def __init__(self, item):
        super().__init__(item)
        self.setImage("heart.png")
        self.setSize(18, 18)
        self.position = (586, 100)
        self.eliminate()
        
    def eliminate(self):
        self.kill()


class heart_3(simpleGE.Sprite):
    def __init__(self, item):
        super().__init__(item)
        self.setImage("heart.png")
        self.setSize(18, 18)
        self.position = (606, 100)
        self.eliminate()
        
    def eliminate(self):
        self.kill()
        
        
class black(simpleGE.Sprite):
    def __init__(self, item):
        super().__init__(item)
        self.setImage("black.jpg")
        self.setSize(70, 30)
        self.position = (585, 100)
            

class game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("space_background_4.jpg")
        
        self.hitCount = 0
        self.score = 0
        
        self.score_label = score_label()
        self.health_label = health_label()
        
        self.spaceship = spaceship(self)
        self.star = star(self)
        self.meteors = []
        for i in range(7):
            self.meteors.append(meteor(self))
            
        self.speed_boost = speed_boost(self)
        self.speed_loss_1 = speed_loss_1(self)
        self.speed_loss_2 = speed_loss_2(self)       
            
        self.heart_1 = heart_1(self)
        self.heart_2 = heart_2(self)
        self.heart_3 = heart_3(self)
        self.black = black(self)
        
        self.sprites = [self.star,
                        self.meteors,
                        self.spaceship,
                        self.score_label,
                        self.health_label,
                        self.black, 
                        self.heart_1,
                        self.heart_2,
                        self.heart_3,
                        self.speed_boost,
                        self.speed_loss_1,
                        self.speed_loss_2]
        
    def process(self):
        for meteor in self.meteors:
            if meteor.collidesWith(self.spaceship):
                if self.hitCount == 2:
                    mixer.music.load("vine-boom.mp3")
                    mixer.music.play()
                    self.heart_1.eliminate()
                    self.stop()
                    print(f"Final score: {self.score}")
                elif self.hitCount == 0:
                    mixer.music.load("vine-boom.mp3")
                    mixer.music.play()
                    meteor.reset()
                    self.heart_3.eliminate()
                    self.hitCount += 1
                elif self.hitCount == 1:
                    mixer.music.load("vine-boom.mp3")
                    mixer.music.play()
                    meteor.reset()
                    self.heart_2.eliminate()
                    self.hitCount += 1
        
        if self.star.collidesWith(self.spaceship):
            mixer.music.load("lobotomy-sound-effect.mp3")
            mixer.music.play()
            self.star.reset()
            self.score += 1
            self.score_label.text = f"Score: {self.score}"
            
        if self.speed_boost.collidesWith(self.spaceship):
            mixer.music.load("pew_pew-dknight556-1379997159.mp3")
            mixer.music.play()
            self.spaceship.moveSpeed += 0.5
            self.speed_boost.reset()
        if self.speed_loss_1.collidesWith(self.spaceship):
            mixer.music.load("spongebob-boowomp.mp3")
            mixer.music.play()
            self.spaceship.moveSpeed -= 0.5
            self.speed_loss_1.reset()
        if self.speed_loss_2.collidesWith(self.spaceship):
            mixer.music.load("spongebob-boowomp.mp3")
            mixer.music.play()
            self.spaceship.moveSpeed -= 0.5
            self.speed_loss_2.reset()
        
      
class intro(simpleGE.Scene):
    def __init__(self):
        super().__init__()

        self.setImage("space_background.jpg")
        self.response = "Quit"
        
        self.directions = simpleGE.MultiLabel()
        self.directions.textLines = [
        "STAR CATCHER",
        "",
        "Move your spaceship around and",
        "catch as many stars as you can!",
        "Avoid falling asteroids,",
        "catch boosts to increase speed,",
        "and avoid negative boosts to",
        "keep from losing speed",
        ""]
        
        self.directions.center = (320, 160)
        self.directions.size = (500, 250)
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play"
        self.btnPlay.center = (100, 400)
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit"
        self.btnQuit.center = (540, 400)        
        
        self.sprites = [self.directions,
                        self.btnPlay,
                        self.btnQuit]
    
    def process(self):
        if self.btnPlay.clicked:
            self.response = "Play"
            self.stop()
        
        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()
    
    mixer.music.load("01 Title Theme.mp3")
    mixer.music.play()
       
       
def main():
    keepGoing = True
    
    while keepGoing:
        begin = intro()
        begin.start()
        
        if begin.response == "Play":
            gameplay = game()
            gameplay.start()
        
        else:
            keepGoing = False
        
      
if __name__ == "__main__":
    main()       