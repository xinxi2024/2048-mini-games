const audio = {
    sounds: {
        merge: new Audio('/assets/sounds/merge.mp3'),
        move: new Audio('/assets/sounds/move.mp3'),
        gameOver: new Audio('/assets/sounds/game_over.mp3')
    },

    playSound(name) {
        if (this.sounds[name]) {
            this.sounds[name].currentTime = 0;
            this.sounds[name].play();
        }
    }
}; 