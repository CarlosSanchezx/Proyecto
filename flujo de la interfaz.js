void Update() {
    float move = Input.GetAxis("Horizontal");
    transform.position += new Vector3(move, 0, 0) * speed * Time.deltaTime;
    if (Input.GetButtonDown("Jump")) {
        // Código para saltar
    }
}