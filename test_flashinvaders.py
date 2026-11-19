import json
import urllib.request

URL = "https://www.space-invaders.com/flashinvaders/flashes/"

print("Connexion à FlashInvaders...")

request = urllib.request.Request(
    URL,
    headers={
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json,text/plain,*/*"
    }
)

with urllib.request.urlopen(request, timeout=30) as response:
    content = response.read().decode("utf-8")
    print("HTTP Status :", response.status)

data = json.loads(content)
events = data.get("without_paris", [])

print("Taille de la réponse :", len(content))
print("Nombre d'événements :", len(events))

if len(events) != 300:
    raise ValueError("Nombre d'événements inattendu")

with open("flashes.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False)

print("RESULTAT : SUCCES")
print("Fichier flashes.json créé")
