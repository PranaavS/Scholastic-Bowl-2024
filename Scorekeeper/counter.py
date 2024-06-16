import pygame

# variables that require immediate reassigning
team_one_name = "ONE"
team_two_name = "TWO"
round = 1
set = 2

# pygame setup
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
dt = 0
wait_constant = 200  # in milliseconds

pygame.font.init()
heading = pygame.font.SysFont('Bahnschrift', 70, bold=False)
text = pygame.font.SysFont('Helvetica', 70)
team_font = pygame.font.SysFont('Helvetica', 30, bold=True)
round_set_font = pygame.font.SysFont('Helvetica', 50)
time_font = pygame.font.SysFont('Bahnschrift', 130)


class Team:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score


# variables that don't require immediate reassigning
team_one = Team(team_one_name)
team_two = Team(team_two_name)
question_count = 1
vertical_offset = 330
buzz_noise = pygame.mixer.Sound("Scorekeeper/buzz.mp3")
noise_played = False
should_time = False
timer = 0  # Initialize timer
is_paused = False  # Initialize pause state
paused_time = 0  # Store the time when paused

def countdown(duration, begin_time):
    global noise_played
    if duration + wait_constant / 1000 + begin_time - pygame.time.get_ticks() / 1000 >= 0:
        return "{:.1f}".format(duration + wait_constant / 1000 + begin_time - pygame.time.get_ticks() / 1000)
    else:
        if not noise_played:
            buzz_noise.play()
            noise_played = True
        return str(0)

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            pygame.display.toggle_fullscreen()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            is_paused = not is_paused
            if is_paused:
                paused_time = pygame.time.get_ticks() / 1000
            else:
                # Adjust begin_time to account for the pause duration
                begin_time += pygame.time.get_ticks() / 1000 - paused_time

    # update timer if should_time is True and not paused
    if should_time and not is_paused:
        timer = float(countdown(duration, begin_time))

    # fill the screen with a color to wipe away anything from last frame
    if should_time and timer < 3:
        screen.fill("firebrick1")
    else:
        screen.fill("white")

    # render "SCHOLASTIC BOWL 2024" in gold above both team names
    title_text = heading.render("SCHOLASTIC BOWL 2024", True, (212, 175, 55))
    title_rect = title_text.get_rect(center=(screen.get_width() / 2, vertical_offset - 200))
    screen.blit(title_text, title_rect)

    # render round and set numbers
    title_text = round_set_font.render(f"Round {round} — Set {set}", True, (0, 0, 0))
    title_rect = title_text.get_rect(center=(screen.get_width() / 2, vertical_offset - 100))
    screen.blit(title_text, title_rect)

    # render "TEAM" in purple and blue above both team names
    team_text = team_font.render("TEAM", True, "purple")
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
        time_text = time_font.render(str(timer) if timer > 0 else "0", True, (0, 0, 0))
        time_rect = time_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
        screen.blit(time_text, time_rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        team_one.score += 15
        pygame.time.wait(wait_constant)
    if keys[pygame.K_3]:
        team_two.score += 15
        pygame.time.wait(wait_constant)
    if keys[pygame.K_q]:
        team_one.score -= 15
        pygame.time.wait(wait_constant)
    if keys[pygame.K_e]:
        team_two.score -= 15
        pygame.time.wait(wait_constant)
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
    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        question_count += 1
        pygame.time.wait(wait_constant)
    if keys[pygame.K_DOWN]:
        if question_count > 0:
            question_count -= 1
        pygame.time.wait(wait_constant)
    if keys[pygame.K_r]:  # reset timer to standard 10 seconds
        should_time, is_paused = True, False
        duration = 10
        noise_played = False
        begin_time = pygame.time.get_ticks() / 1000
        pygame.time.wait(wait_constant)
    if keys[pygame.K_m]:  # reset timer to computation 30 seconds
        should_time, is_paused = True, False
        duration = 30
        noise_played = False
        begin_time = pygame.time.get_ticks() / 1000
        pygame.time.wait(wait_constant)
    if keys[pygame.K_b]:  # reset timer to bounce 5 seconds
        should_time, is_paused = True, False
        duration = 5
        noise_played = False
        begin_time = pygame.time.get_ticks() / 1000
        pygame.time.wait(wait_constant)
    if keys[pygame.K_p]:  # hides and clears timer
        should_time = False
        noise_played = True
        duration = 0
        pygame.time.wait(wait_constant)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
