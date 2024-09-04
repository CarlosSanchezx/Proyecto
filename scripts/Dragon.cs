using UnityEngine;
using TMPro;

public class TextController : MonoBehaviour
{
    public TextMeshProUGUI textMeshPro;
    public TMP_FontAsset newFont;

    private void Start()
    {
        if (textMeshPro != null)
        {
            textMeshPro.text = "Nuevo Texto";
            textMeshPro.font = newFont;
        }
    }
}