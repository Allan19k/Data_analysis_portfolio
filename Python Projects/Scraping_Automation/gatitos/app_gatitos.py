import threading
import requests
import os

# Carpeta de salida
OUTPUT_DIR = "cats"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Lista de URLs de ejemplo 
urls = [
    "https://www.placecats.com/200/200",
    "https://www.placecats.com/300/300",
    "https://www.placecats.com/400/400",
    "https://www.placecats.com/500/500",
    "https://www.placecats.com/600/600",
]

def descargar_imagen(url, index):
    try:
        print(f"Descargando {url} ...")
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            filename = os.path.join(OUTPUT_DIR, f"gato_{index}.jpg")
            with open(filename, "wb") as f:
                f.write(r.content)
            print(f"Guardado: {filename}")
        else:
            print(f"Error {r.status_code} al descargar {url}")
    except Exception as e:
        print(f"Error descargando {url}: {e}")

if __name__ == "__main__":
    # Creamos un hilo por cada imagen
    hilos = []
    for i, url in enumerate(urls, 1):
        t = threading.Thread(target=descargar_imagen, args=(url, i))
        hilos.append(t)
        t.start()

    # Esperamos que terminen todos los hilos
    for t in hilos:
        t.join()

    print("Descargas finalizadas ✅")
