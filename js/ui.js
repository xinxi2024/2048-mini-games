const ui = {
    init() {
        document.addEventListener('keydown', this.handleKeyPress.bind(this));
        document.getElementById('new-game-btn').addEventListener('click', () => game.init());
        
        // 加载保存的皮肤
        const savedSkin = localStorage.getItem('2048-skin');
        if (savedSkin) {
            document.querySelector('.skin-select').value = savedSkin;
            this.changeSkin(savedSkin);
        }
    },

    changeSkin(skin) {
        document.body.setAttribute('data-theme', skin);
        localStorage.setItem('2048-skin', skin);
        game.draw();
    },

    handleKeyPress(event) {
        const keyActions = {
            'ArrowUp': 'up',
            'ArrowDown': 'down',
            'ArrowLeft': 'left',
            'ArrowRight': 'right'
        };
        
        if (keyActions[event.key]) {
            event.preventDefault();
            game.move(keyActions[event.key]);
        }
    },

    updateScore(score) {
        document.getElementById('score').textContent = `分数: ${score}`;
    },

    updateTimer() {
        // 计时器更新逻辑
    }
};

// 初始化 UI
ui.init(); 