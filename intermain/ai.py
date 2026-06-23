import json
import os
import time
import requests

filedir = os.path.dirname(os.path.abspath(__file__))
#np C:\Users\ok\Desktop\github\llama.cpp\build\bin\Release\llama-server.exe
path2 = r"PathToLlama.cpp"
worse = r"PathLocalWorse"
better = r"PathLocalBetter"
client = None
def run(liczba1:int, tekst:str, liczba2=1):
    while True:
        if liczba1 == 1:
            k = is_local_ai_running()
            if not k:
                if liczba2 == 1:
                    path = worse
                elif liczba2 == 2:
                    path = better
                else:
                    wiadomosc = "wybierz 1 albo 2"
                    return wiadomosc
                start_server(path)
                #4 minuty starcza by server wstal
                for i in range(60):
                    if is_local_ai_running():break
                    else:time.sleep(2)
            odpowiedz = chat_local_ai(message=tekst)
            return odpowiedz
        elif liczba1 == 2:
            from google import genai
            # Prefer environment variable for the API key, fall back to apikey.json
            key = load_key()
            # Some client implementations also read env var, set it as a fallback
            os.environ.setdefault("GOOGLE_API_KEY", key)
            client = genai.Client(api_key=key)
            return ask(tekst, client)

def is_local_ai_running():
    try:
        r = requests.get("http://localhost:8080/v1/models", timeout=2)
        return r.status_code == 200
    except:
        return False

def chat_local_ai(
    message=None,
    messages=None,
    temperature=0.7,
    max_tokens=512,
    top_p=1.0,
    stream=False,
    raw=False,
    timeout=400
):
    url = "http://localhost:8080/v1/chat/completions"
    if messages is None:
        messages = [{"role": "user", "content": message}]
    data = {
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "top_p": top_p,
        "stream": stream
    }
    try:
        response = requests.post(url, json=data, timeout=timeout)
        response.raise_for_status()

        if raw:
            return response.json()

        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Błąd: {e}"

def load_key():
    # 1) Try environment variables (recommended)
    for var in ("GEMINI_API_KEY", "GOOGLE_API_KEY", "GENAI_API_KEY"):
        val = os.environ.get(var)
        if val:
            return val

    # 2) Fallback to local apikey.json (NOT recommended)
    api_key_path = os.path.join(filedir, "apikey.json")
    try:
        with open(api_key_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if "gemini" in data:
                return data["gemini"]
            raise RuntimeError("apikey.json nie zawiera klucza 'gemini'")
    except FileNotFoundError:
        raise RuntimeError(
            "Brak klucza API. Ustaw zmienną środowiskową GEMINI_API_KEY lub utwórz apikey.json lokalnie.\n"
            "Nie dodawaj pliku z kluczem do repozytorium — dodaj go do .gitignore i rotuj klucz jeśli już został ujawniony."
        )

def start_server(model_path):
    cmd = f'start "" "{path2}" -m "{model_path}" -c 2048 --port 8080 --host 0.0.0.0'
    os.system(cmd)

def ask(prompt,client):
    r = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return r.text
