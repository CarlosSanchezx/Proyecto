using UnityEngine;

public class GameController : MonoBehaviour
{
    public void WinGame()
    {
        GameManager.Instance.EndGame(true);
    }

    public void LoseGame()
    {
        GameManager.Instance.EndGame(false);
    }
}