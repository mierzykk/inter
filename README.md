Krótkie repo z narzędziami pomocniczymi i integracjami AI.

Główne katalogi:

- `inter/` — narzędzia interaktywne i moduły pomocnicze (`intermain/`).

Ważne pliki:
- [inter.py](inter.py)
- [intermain/ai.py](intermain/ai.py)
- [intermain/id.py](intermain/id.py)

Wymagania
----------

- Python 3.8+
- `requests` (używane przez `api.py`)

Instalacja (szybko)
-------------------

1. Utwórz virtualenv i zainstaluj zależności:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install requests
```

2. (Opcjonalnie) skonfiguruj lokalny serwer LLM i ścieżki w `intermain/ai.py` jeśli chcesz korzystać z lokalnych modeli.

Bezpieczeństwo kluczy (ważne)
----------------------------
preferuje zmienne środowiskowe w tej kolejności: `GEMINI_API_KEY`, `GOOGLE_API_KEY`, `GENAI_API_KEY`. Jeśli żaden z nich nie istnieje, skrypt próbuje odczytać lokalny `apikey.json` (tylko jako fallback). (apikey.json nie istnieje jezeli chcesz  by wczytywalo z apikey.apikey.json wpisz
{
"gemini":"twoj api key"
}
)

Ustawienie klucza w PowerShell (bieząca sesja):

```powershell
$env:GEMINI_API_KEY = "twoj klucz"
```

Ustawienie klucza trwale (PowerShell):

```powershell
setx GEMINI_API_KEY "twoj klucz"
```


Uruchamianie przykładowe
------------------------


- Szybki test `generete_id()` z `inter`:

```powershell
python -c print(generete_id())"
```

