import pygame
import random
import time
import pygame.mixer

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 4
CELL_SIZE = WIDTH // GRID_SIZE
FONT_SIZE = 36
SCORE_FONT_SIZE = 24
TIME_FONT_SIZE = 24

# Colors
BACKGROUND_COLOR = (187, 173, 160)
EMPTY_CELL_COLOR = (205, 193, 180)
CELL_COLORS = {
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

# Font
font = pygame.font.Font(None, FONT_SIZE)

class Game2048:
    def __init__(self):
        self.grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.add_new_tile()
        self.add_new_tile()
        self.score = 0
        self.start_time = time.time()
        self.game_mode = "normal"  # normal, time_challenge
        self.time_limit = None
        self.current_skin = "default"
        
        # 初始化音效
        pygame.mixer.init()
        self.merge_sound = pygame.mixer.Sound('sounds/merge.wav')
        self.move_sound = pygame.mixer.Sound('sounds/move.wav')
        self.game_over_sound = pygame.mixer.Sound('sounds/game_over.wav')

    def add_new_tile(self):
        empty_cells = [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if self.grid[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.grid[i][j] = 2 if random.random() < 0.9 else 4

    def move(self, direction):
        moved = False
        if direction in ["up", "down"]:
            for j in range(GRID_SIZE):
                column = [self.grid[i][j] for i in range(GRID_SIZE)]
                if direction == "up":
                    new_column = self.merge(column)
                else:
                    new_column = self.merge(column[::-1])[::-1]
                for i in range(GRID_SIZE):
                    if self.grid[i][j] != new_column[i]:
                        moved = True
                    self.grid[i][j] = new_column[i]
        else:  # left or right
            for i in range(GRID_SIZE):
                row = self.grid[i]
                if direction == "left":
                    new_row = self.merge(row)
                else:
                    new_row = self.merge(row[::-1])[::-1]
                if self.grid[i] != new_row:
                    moved = True
                self.grid[i] = new_row
        if moved:
            self.add_new_tile()
            self.move_sound.play()  # 播放移动音效
        return moved

    def merge(self, line):
        new_line = [x for x in line if x != 0]
        for i in range(len(new_line) - 1):
            if new_line[i] == new_line[i + 1]:
                new_line[i] *= 2
                self.score += new_line[i]  # 增加分数
                self.merge_sound.play()    # 播放合并音效
                new_line[i + 1] = 0
        new_line = [x for x in new_line if x != 0]
        return new_line + [0] * (GRID_SIZE - len(new_line))

    def draw(self):
        screen.fill(BACKGROUND_COLOR)
        
        # 绘制分数
        score_text = font.render(f"分数: {self.score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))
        
        # 绘制时间
        elapsed_time = int(time.time() - self.start_time)
        if self.game_mode == "time_challenge" and self.time_limit:
            remaining_time = max(0, self.time_limit - elapsed_time)
            time_text = font.render(f"剩余时间: {remaining_time}秒", True, (0, 0, 0))
        else:
            time_text = font.render(f"时间: {elapsed_time}秒", True, (0, 0, 0))
        screen.blit(time_text, (WIDTH - 150, 10))
        
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                value = self.grid[i][j]
                cell_rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, EMPTY_CELL_COLOR if value == 0 else CELL_COLORS.get(value, (237, 194, 46)), cell_rect, border_radius=8)
                if value != 0:
                    text_surface = font.render(str(value), True, (0, 0, 0))
                    text_rect = text_surface.get_rect(center=cell_rect.center)
                    screen.blit(text_surface, text_rect)
        pygame.display.flip()

    def is_game_over(self):
        if any(0 in row for row in self.grid):
            return False
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                value = self.grid[i][j]
                if (i < GRID_SIZE - 1 and value == self.grid[i + 1][j]) or \
                   (j < GRID_SIZE - 1 and value == self.grid[i][j + 1]):
                    return False
        return True

def main():
    game = Game2048()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.move("up")
                elif event.key == pygame.K_DOWN:
                    game.move("down")
                elif event.key == pygame.K_LEFT:
                    game.move("left")
                elif event.key == pygame.K_RIGHT:
                    game.move("right")
                
                if game.is_game_over():
                    print("Game Over!")
                    running = False
        
        game.draw()
    
    pygame.quit()

if __name__ == "__main__":
    main()

print("2048 game implementation complete!")

