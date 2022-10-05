import pygame
class character_models():
    def __init__(self, player, x, y, flip,  data, sprite_sheet, animation_frames, sound):
        self.player = player
        self.size = data[0]
        self.image_scale = data[1]
        self.offset = data[2]
        self.animation_list = self.load_images(sprite_sheet, animation_frames) # takes animation steps and adds it to a list.
        self.action = 0 # determines animations that will change, depending on what the character is doing.
        self.frame_index = 0 # starts animations at the first frame.
        self.image = self.animation_list[self.action][self.frame_index]
        self.update_time = pygame.time.get_ticks()
        self.flip = flip
        self.rect = pygame.Rect((x, y, 80, 180)) 
        self.vel_y = 0 # starting y (jump) velocity.
        self.running = False
        self.jump = False # defaults the character to not be in a jumping state.
        self.attacking = False # defualts character to not attack.
        self.attack_type = 0 # sets default attack type to 0.
        self.attack_cooldown = 0
        self.health = 100 # both characters start with 150 HP.
        self.damage = False
        self.alive = True
        self.attack_sound = sound

    def load_images(self, sprite_sheet, animation_frames):
        '''extracts images from the sprite sheets.'''
        animation_list = []

        for y, animations in enumerate(animation_frames):
            temporary_image_list = []

            for x in range(animations):
                temporary_image = sprite_sheet.subsurface(x * self.size, y * self.size, self.size, self.size) # extracts individual rows for sprite_sheets. # produces a finalized temporary image list. It will contain 1 rows worth of images.
                temporary_image_list.append(pygame.transform.scale(temporary_image, (self.size * self.image_scale, self.size * self.image_scale))) 
            animation_list.append(temporary_image_list) # adds to the master animation list and goes to the next row.
        return animation_list

    def character_movement(self, screen_width, screen_height, surface, target):

        SPEED = 7 # character's speed
        GRAVITY = 2 # character's gravity
        dx = 0 
        dy = 0
        self.attack_type = 0 # starts character without an attack.
        self.running = False # starts running animation as false, and resets to false when no longer running.

        '''characters x and y movements + key bindings.'''
        key = pygame.key.get_pressed() # gets a keypress 

        if self.attacking == False and self.alive == True: # the following can only be done if the character is not attacking.

            if self.player == 1:
                if key[pygame.K_a]: # if a on the keyboard is pressed.
                    dx = -SPEED # SPEED to the left.
                    self.running = True
                if key[pygame.K_d]: # if d on the keyboard is pressed.
                    dx = SPEED # SPEED to the right.
                    self.running = True

                '''character jump'''
                if key[pygame.K_w] and self.jump == False: # this will initiate a character jump, if they are not already jumping.
                    self.vel_y = -30 # negative value will move the character upwards.
                    self.jump = True

                '''character attack + key bindings.'''
                if key[pygame.K_SPACE] or key[pygame.K_r]: # assigns attacks to keys:

                    self.attacks(target)

                    if key[pygame.K_SPACE]:
                        self.attack_type = 1 # assigns attack 1 to the spacebar.
                    if key[pygame.K_r]:
                        self.attack_type = 2 # assigns attack 2 to the r key.

            if self.player == 2:
                if key[pygame.K_LEFT]: # if a on the keyboard is pressed.
                    dx = -SPEED # SPEED to the left.
                    self.running = True
                if key[pygame.K_RIGHT]: # if d on the keyboard is pressed.
                    dx = SPEED # SPEED to the right.
                    self.running = True

                '''character jump'''
                if key[pygame.K_UP] and self.jump == False: # this will initiate a character jump, if they are not already jumping.
                    self.vel_y = -30 # negative value will move the character upwards.
                    self.jump = True

                '''character attack + key bindings.'''
                if key[pygame.K_KP0] or key[pygame.K_KP3]: # assigns attacks to keys:
                    self.attacks(target)
                    if key[pygame.K_KP0]:
                        self.attack_type = 1 # assigns attack 1 to the spacebar.
                    if key[pygame.K_KP3]:
                        self.attack_type = 2



        '''character's y velocity will be 'brought down' by GRAVITY.'''
        self.vel_y += GRAVITY 
        dy += self.vel_y


        ''' ensures the character will stay on the screen.'''
        if self.rect.left + dx < 0: # 
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 30:
            self.vel_y = 0 # stops character
            self.jump = False # resets the jump to False when the character touches the ground.
            dy = screen_height - 30 - self.rect.bottom # the difference between the 'floor' and character (in pixels).

        '''ensures characters will face each other.'''
        if target.rect.centerx > self.rect.centerx: # flip stays False, as the characters are already facing each other.
            self.flip = False
        else:
            self.flip = True # faces character towards the target.

        '''attack animation cooldown'''
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
            
        '''updates the characters position.'''
        self.rect.x += dx # characters position is changed by dx variable
        self.rect.y += dy # characters position is changed by the dy variable.

    def update_animation(self):
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.update_actions(6) # death animation.
        elif self.damage == True:
            self.update_actions(5) # flinch animation.
        elif self.attacking == True:
            if self.attack_type == 1:
                self.update_actions(3) # 1st attack animation.
            elif self.attack_type == 2:
                self.update_actions(4) # 2nd attack animation.
        elif self.jump == True:
            self.update_actions(2) # jumping animation.
        elif self.running == True:
            self.update_actions(1) # running animation.
        else:
            self.update_actions(0) # idle animation.


        '''handles animation updates, and displays on screen.'''
        animation_cooldown = 50 # determines cooldown on frames.
        self.image = self.animation_list[self.action][self.frame_index] # increased frame index and allows animation to run.

        if pygame.time.get_ticks() - self.update_time > animation_cooldown: # checks if enough time has passed since the last animation.
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animation_list[self.action]): # loops animations
            if self.alive == False:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0
                if self.action == 3 or self.action == 4:
                    self.attacking = False
                    self.attack_cooldown = 27
            if self.action == 5: # returns character to idle animation after taking damage.
                self.hit == False 
                self.attacking = False # cancels out character attacks, if damaged.
                self.attack_cooldown = 27

    '''
    creates the hitbox for attacks. x and y coordinates are based on the character attacking. 
    centerx will throw the attack from the middle of the character model.
    2 * will make the attack 2 times as wide as the character currently is.
    '''
    def attacks(self, target):

        if self.attack_cooldown == 0:
            self.attacking = True
            self.attack_sound.play()
            attacking_hitbox = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height) # self.flip will offsets hitbox from the right, to the left.

            if attacking_hitbox.colliderect(target.rect): # checks for collision between two different 'rectangles.'
                target.health -= 13 # the target will lose 13 HP for every hit.
                target.hit = True
            

    def update_actions(self, new_animation):
        '''compares next animation to see if it is different than the previous one.'''
        if new_animation != self.action:
            self.action = new_animation

            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def display_character(self, surface):

        image = pygame.transform.flip(self.image, self.flip, False) # re-directs character to face the opponent.    
        surface.blit(image, (self.rect.x - (self.offset[0] * self.image_scale) , self.rect.y - (self.offset[1] * self.image_scale)))