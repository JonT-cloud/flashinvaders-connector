import json
import urllib.request

URL = "https://www.space-invaders.com/flashinvaders/flashes/"

print("Test de connexion à FlashInvaders...")

request = urllib.request.Request(
    URL,
    headers={
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json,text/plain,*/*"
    }
)

try:
    with urllib.request.urlopen(request, timeout=30) as response:
        status = response.status
        content = response.read().decode("utf-8")

    print("HTTP Status :", status)
    print("Taille de la réponse :", len(content))

    data = json.loads(content)
    events = data.get("without_paris", [])

    print("Nombre d'événements without_paris :", len(events))

    if len(events) == 300:
        print("RESULTAT : SUCCES")
        print("Premier événement :", json.dumps(events[0], ensure_ascii=False))
    else:
        print("RESULTAT : ECHEC - nombre d'événements inattendu")

except Exception as error:
    print("RESULTAT : ECHEC")
    print("Erreur :", str(error))
