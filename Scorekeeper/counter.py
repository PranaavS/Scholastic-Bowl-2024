team_one_name = "Red"
team_two_name = "Blue"
round = 1
set = 1

import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
dt = 0
wait_constant = 200 # in milliseconds

pygame.font.init() # you have to call this at the start, if you want to use this module.
heading = pygame.font.SysFont('Helvetica', 70, bold=True)
text = pygame.font.SysFont('Helvetica', 70)
team_font = pygame.font.SysFont('Helvetica', 30, bold=True)
round_set_font = pygame.font.SysFont('Helvetica', 50, bold=True)



player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


class team:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

team_one = team(team_one_name)
team_two = team(team_two_name)
question_count = 1
vertical_offset = 330

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # check for the fullscreen toggle event
        if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            # Toggle fullscreen mode
            pygame.display.toggle_fullscreen()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # render "SCHOLASTIC BOWL 2024" in gold above both team names
    title_text = heading.render("SCHOLASTIC BOWL 2024", True, (212, 175, 55))
    title_rect = title_text.get_rect(center=(screen.get_width() / 2, vertical_offset - 200))
    screen.blit(title_text, title_rect)

    # render round and set numbers
    title_text = round_set_font.render(f"Round {round} — Set {set}", True, (0, 0, 0))
    title_rect = title_text.get_rect(center=(screen.get_width() / 2, vertical_offset - 100))
    screen.blit(title_text, title_rect)

    # render "TEAM" in gold above both team names
    team_text = team_font.render("TEAM", True, (255, 0, 0))
    team_rect = team_text.get_rect(center=(screen.get_width() / 4, vertical_offset))
    screen.blit(team_text, team_rect)

    team_text = team_font.render("TEAM", True, (0, 0, 255))
    team_rect = team_text.get_rect(center=(screen.get_width() / 4 * 3, vertical_offset))
    screen.blit(team_text, team_rect)

    # render headings (team names)
    team_one_name_text = heading.render(team_one.name, True, (0, 0, 0))
    team_one_text_rect = team_one_name_text.get_rect(center=(screen.get_width() / 4, vertical_offset + 60))
    screen.blit(team_one_name_text, team_one_text_rect)

    team_two_name_text = heading.render(team_two.name, True, (0, 0, 0))
    team_two_text_rect = team_two_name_text.get_rect(center=(screen.get_width() / 4 * 3, vertical_offset + 60))
    screen.blit(team_two_name_text, team_two_text_rect)


    # render scores
    team_one_score_text = text.render(str(team_one.score), True, (0, 0, 0))
    team_one_score_rect = team_one_score_text.get_rect(center=(screen.get_width() / 4, vertical_offset + 210))
    screen.blit(team_one_score_text, team_one_score_rect)

    team_two_score_text = text.render(str(team_two.score), True, (0, 0, 0))
    team_two_score_rect = team_two_score_text.get_rect(center=(screen.get_width() / 4 * 3, vertical_offset + 210))
    screen.blit(team_two_score_text, team_two_score_rect)

    # render question count
    question_count_text = text.render("Question " + str(question_count) + " of 10", True, (0, 0, 0))
    question_count_rect = question_count_text.get_rect(center=(screen.get_width() / 2, screen.get_height() - 70))
    screen.blit(question_count_text, question_count_rect)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        team_one.score += 10
        pygame.time.wait(wait_constant)
    if keys[pygame.K_z]:
        team_one.score -= 10
        pygame.time.wait(wait_constant)
    if keys[pygame.K_d]:
        team_two.score += 10
        pygame.time.wait(wait_constant)
    if keys[pygame.K_c]:
        team_two.score -= 10
        pygame.time.wait(wait_constant)
    if keys[pygame.K_SPACE]:
        question_count += 1
        pygame.time.wait(wait_constant)
    if keys[pygame.K_DOWN]:
        question_count -= 1
        pygame.time.wait(wait_constant)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()