# Ejemplo de uso

player_name = "Jugador1"
coins_gained = 100
current_level = 2

# Guardar el progreso del jugador
save_player_progress(player_name, coins_gained, current_level)

# Recuperar el progreso del jugador
coins, level = get_player_progress(player_name)
print(f"{player_name} tiene {coins} monedas y está en el nivel {level}.")
