# class Slider(UIElement):
#     pass
#     def __init__(self, name, val, maxi, mini, pos):
#         self.val = val  # start value
#         self.maxi = maxi  # maximum at slider position right
#         self.mini = mini  # minimum at slider position left
#         self.xpos = pos  # x-location on screen
#         self.ypos = 550
#         self.surf = pygame.surface.Surface((100, 50))
#         self.hit = False  # the hit attribute indicates slider movement due to mouse interaction
#
#         # Static graphics - slider background #
#         self.surf.fill((100, 100, 100))
#         pygame.draw.rect(self.surf, GREY, [0, 0, 100, 50], 3)
#         pygame.draw.rect(self.surf, ORANGE, [10, 10, 80, 10], 0)
#         pygame.draw.rect(self.surf, WHITE, [10, 30, 80, 5], 0)
#
#     def draw(self):
#
#         # static
#         surf = self.surf.copy()
#
#     # screen
#     screen.blit(surf, (self.xpos, self.ypos))
