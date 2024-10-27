function startGame() {
    document.getElementById('mainMenu').style.display = 'none';
    document.getElementById('gameHUD').style.display = 'block';
}

function loadGame() {
    // Lógica para cargar una partida
}

function openSettings() {
    document.getElementById('mainMenu').style.display = 'none';
    document.getElementById('settingsMenu').style.display = 'block';
}

function exitGame() {
    // Lógica para salir del juego
}

function applySettings() {
    // Lógica para aplicar configuraciones
    closeSettings();
}

function closeSettings() {
    document.getElementById('settingsMenu').style.display = 'none';
    document.getElementById('mainMenu').style.display = 'block';
}

function pauseGame() {
    // Lógica para pausar el juego
}

function useItem() {
    // Lógica para usar un objeto del inventario
}

function closeInventory() {
    document.getElementById('inventory').style.display = 'none';
}
