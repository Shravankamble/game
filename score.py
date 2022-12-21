import pygame

reset = 0
high_score = ""
clicks = 0

def score(screen):
    global reset
    global high_score
    global clicks
    clicks = (int)(pygame.time.get_ticks() / 150) - reset
    surface = pygame.font.Font(None, 35)
    score_grd = surface.render(f'{clicks}', False, 'black')
    score_rect = score_grd.get_rect(center = (615, 20))
    screen.blit(score_grd, score_rect)
    high_score = clicks
    
def hello(name) -> str
    return f"hello {name}
