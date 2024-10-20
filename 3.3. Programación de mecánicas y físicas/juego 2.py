var jump_force = -400
var is_on_ground = false

func _physics_process(delta):
    if is_on_ground and Input.is_action_just_pressed("jump"):
        velocity.y = jump_force
        is_on_ground = false
    
    # Añadir gravedad
    velocity.y += gravity * delta
    move_and_slide(velocity, Vector2.UP)
