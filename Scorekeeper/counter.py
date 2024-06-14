# variables that require immediate reassigning
team_one_name = "Moms"
team_two_name = "Pranaavs"
round = 3
set = 4

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
time_font = pygame.font.SysFont('Helvetica', 130)


class team:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score
        

# variables that don't need immediate reassigning
team_one = team(team_one_name)
team_two = team(team_two_name)
question_count = 1
vertical_offset = 330
buzz_noise = pygame.mixer.Sound("Scorekeeper/buzz.mp3")
noise_played = False
should_time = False

def countdown(duration, begin_time):
    global noise_played
    if duration + begin_time - pygame.time.get_ticks() / 1000 >= 0:
        return "{:.1f}".format(duration + begin_time - pygame.time.get_ticks() / 1000)
    else:
        if not noise_played:
            buzz_noise.play()
            noise_played = True
        return str(0)

# counter, display_time = 10, '10'.rjust(3)
# pygame.time.set_timer(pygame.USEREVENT, 1000)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        # if event.type == pygame.USEREVENT: 
        #     counter -= 1
        #     if counter > 0:
        #         display_time = str(counter)
        #     else:
        #         buzz_noise.play()

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
    question_count_rect = question_count_text.get_rect(center=(screen.get_width() / 2, screen.get_height() - 100))
    screen.blit(question_count_text, question_count_rect)

    if should_time:
        time_text = time_font.render(countdown(start_time, begin_time), True, (0, 0, 0))
        time_rect = time_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
        screen.blit(time_text, time_rect)


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
    if keys[pygame.K_r]: # reset timer to standard 10 seconds
        should_time = True
        start_time = 10
        noise_played = False
        begin_time = pygame.time.get_ticks() / 1000
        pygame.time.wait(wait_constant)
    if keys[pygame.K_m]: # reset timer to computation 30 seconds
        should_time = True
        start_time = 30
        noise_played = False
        begin_time = pygame.time.get_ticks() / 1000
    if keys[pygame.K_b]: # reset timer to bounce 5 seconds
        should_time = True
        start_time = 5
        noise_played = False
        begin_time = pygame.time.get_ticks() / 1000
    if keys[pygame.K_p]: # hides and clears timer
        should_time = False
        noise_played = True
        start_time = 0
        pygame.time.wait(wait_constant)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()