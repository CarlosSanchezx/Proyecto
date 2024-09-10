using UnityEngine;
using UnityEngine.SceneManagement; // Necesario para gestionar escenas

public class GameManager : MonoBehaviour
{
    public static GameManager Instance;

    // Enum para los diferentes estados del juego
    public enum GameState
    {
        MainMenu,
        Playing,
        GameOver,
        Win
    }

    public GameState currentState;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject);
        }
        else
        {
            Destroy(gameObject);
        }
    }

    private void Start()
    {
        // Iniciar en el menú principal
        LoadScene("MenuPrincipal");
    }

    private void Update()
    {
        // Puedes manejar el estado del juego aquí si es necesario
        switch (currentState)
        {
            case GameState.MainMenu:
                // Lógica del menú principal
                break;
            case GameState.Playing:
                // Lógica del juego en curso
                break;
            case GameState.GameOver:
                // Lógica de fin de juego
                break;
            case GameState.Win:
                // Lógica de victoria
                break;
        }
    }

    public void LoadScene(string sceneName)
    {
        SceneManager.LoadScene(sceneName);
    }

    public void StartGame()
    {
        currentState = GameState.Playing;
        LoadScene("Nivel1");
    }

    public void EndGame(bool won)
    {
        currentState = won ? GameState.Win : GameState.GameOver;
        LoadScene(won ? "WinScene" : "GameOverScene");
    }

    public void RestartGame()
    {
        currentState = GameState.Playing;
        LoadScene("Nivel1");
    }

    public void GoToMainMenu()
    {
        currentState = GameState.MainMenu;
        LoadScene("MenuPrincipal");
    }
}