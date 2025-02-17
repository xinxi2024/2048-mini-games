from flask import Flask, jsonify, request, render_template, send_from_directory
import random
import time

app = Flask(__name__)

class Game2048:
    def __init__(self):
        self.grid = [[0 for _ in range(4)] for _ in range(4)]
        self.add_new_tile()
        self.add_new_tile()
        self.score = 0
        self.start_time = time.time()
        self.game_mode = "normal"  # normal, time_challenge
        self.time_limit = None
        self.current_skin = "default"
        self.merged = False  # 添加合并标记

    def add_new_tile(self):
        empty_cells = [(i, j) for i in range(4) for j in range(4) if self.grid[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.grid[i][j] = 2 if random.random() < 0.9 else 4

    def move(self, direction):
        moved = False
        self.merged = False  # 重置合并标记
        
        if direction in ["up", "down"]:
            for j in range(4):
                column = [self.grid[i][j] for i in range(4)]
                if direction == "up":
                    new_column, merged = self.merge(column)
                else:
                    reversed_column, merged = self.merge(column[::-1])
                    new_column = reversed_column[::-1]
                self.merged = self.merged or merged
                for i in range(4):
                    if self.grid[i][j] != new_column[i]:
                        moved = True
                    self.grid[i][j] = new_column[i]
        else:  # left or right
            for i in range(4):
                row = self.grid[i]
                if direction == "left":
                    new_row, merged = self.merge(row)
                else:
                    reversed_row, merged = self.merge(row[::-1])
                    new_row = reversed_row[::-1]
                self.merged = self.merged or merged
                if self.grid[i] != new_row:
                    moved = True
                self.grid[i] = new_row
                
        if moved:
            self.add_new_tile()
        return moved

    def merge(self, line):
        merged = False
        new_line = [x for x in line if x != 0]
        for i in range(len(new_line) - 1):
            if new_line[i] == new_line[i + 1]:
                new_line[i] *= 2
                self.score += new_line[i]
                new_line[i + 1] = 0
                merged = True
        new_line = [x for x in new_line if x != 0]
        return new_line + [0] * (4 - len(new_line)), merged

    def is_game_over(self):
        if any(0 in row for row in self.grid):
            return False
        for i in range(4):
            for j in range(4):
                value = self.grid[i][j]
                if (i < 3 and value == self.grid[i + 1][j]) or \
                   (j < 3 and value == self.grid[i][j + 1]):
                    return False
        return True

game = Game2048()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_game', methods=['POST'])
def new_game():
    global game
    game = Game2048()
    return jsonify({
        "grid": game.grid,
        "score": game.score
    })

@app.route('/move', methods=['POST'])
def move():
    direction = request.json['direction']
    moved = game.move(direction)
    game_over = game.is_game_over()
    return jsonify({
        "grid": game.grid,
        "moved": moved,
        "merged": game.merged,
        "game_over": game_over,
        "score": game.score
    })

@app.route('/change_mode', methods=['POST'])
def change_mode():
    mode = request.json['mode']
    time_limit = request.json.get('time_limit', None)
    global game
    game = Game2048()
    game.game_mode = mode
    game.time_limit = time_limit
    return jsonify({"status": "success"})

@app.route('/change_skin', methods=['POST'])
def change_skin():
    skin = request.json['skin']
    game.current_skin = skin
    return jsonify({"status": "success"})

@app.route('/static/sounds/<filename>')
def serve_sound(filename):
    return send_from_directory('sounds', filename)

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

print("Flask backend for 2048 game is ready!")

