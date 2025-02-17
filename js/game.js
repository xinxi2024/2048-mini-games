class Game2048 {
    constructor() {
        this.grid = Array(4).fill().map(() => Array(4).fill(0));
        this.score = 0;
        this.startTime = Date.now();
        this.gameMode = "normal";
        this.timeLimit = null;
        
        this.init();
    }

    init() {
        this.addNewTile();
        this.addNewTile();
        this.draw();
    }

    addNewTile() {
        const emptyCells = [];
        for (let i = 0; i < 4; i++) {
            for (let j = 0; j < 4; j++) {
                if (this.grid[i][j] === 0) {
                    emptyCells.push([i, j]);
                }
            }
        }
        if (emptyCells.length) {
            const [i, j] = emptyCells[Math.floor(Math.random() * emptyCells.length)];
            this.grid[i][j] = Math.random() < 0.9 ? 2 : 4;
        }
    }

    move(direction) {
        // 移动逻辑保持不变
        const moved = false;
        // ...移动代码
        if (moved) {
            audio.playSound('move');
            this.addNewTile();
        }
        this.draw();
        return moved;
    }

    // ... 其他游戏逻辑方法
}

const game = new Game2048(); 