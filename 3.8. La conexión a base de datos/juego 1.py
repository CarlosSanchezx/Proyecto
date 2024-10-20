def save_player_progress(player_name, coins, level):
    conn = sqlite3.connect('game_data.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO player_progress (player_name, coins, level)
        VALUES (?, ?, ?)
    ''', (player_name, coins, level))
    
    conn.commit()
    conn.close()

def get_player_progress(player_name):
    conn = sqlite3.connect('game_data.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT coins, level FROM player_progress WHERE player_name = ?
    ''', (player_name,))
    result = cursor.fetchone()
    
    conn.close()
    return result if result else (0, 0)  # Devuelve (0, 0) si no se encuentra el jugador
