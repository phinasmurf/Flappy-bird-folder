
current_time = (pygame.time.get_ticks() / 1000) - start_time

     #score surface
     score_font = pygame.font.Font('font/Pixeltype.ttf', 50)
     score_surface = font.render(str(current_time), False,(64, 64, 64))
     score_rect = score_surface.get_rect(center = (400, 50))
     screen.blit(score_surface, score_rect)