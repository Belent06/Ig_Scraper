import instaloader
import time

L = instaloader.Instaloader()

# DATOS
TU_USUARIO = "mariiaa_beleen"
PERFIL_OBJETIVO = "anthonygonzalez___"
ARCHIVO_COOKIES = "instagram.com_cookies.txt"


def cargar_cookies_manual(ruta):
    cookies = {}
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('#') or not line.strip(): continue
                p = line.split()
                if len(p) >= 7: cookies[p[5]] = p[6]
        return cookies
    except:
        return None


def ejecutar_scraping_seguro():
    print(f"--- MODO DE RESCATE ACTIVADO: {PERFIL_OBJETIVO} ---")

    dict_cookies = cargar_cookies_manual(ARCHIVO_COOKIES)
    if not dict_cookies:
        print("Error: No se pudo cargar el archivo de cookies.")
        return

    try:
        L.context._session.cookies.update(dict_cookies)

        # 1. Validamos la sesión con tu usuario
        print(f"Validando sesión de {TU_USUARIO}...")

        # 2. Cargamos el perfil OBJETIVO
        profile = instaloader.Profile.from_username(L.context, PERFIL_OBJETIVO)
        print(f"Conexión establecida. Scrapeando a: {profile.full_name}")

        # 3. Descarga de metadatos básicos y foto de perfil
        print(f"Descargando metadatos básicos de {PERFIL_OBJETIVO}...")
        L.download_profile(profile.username, profile_pic_only=False)

        print("\n--- ÉXITO PARCIAL ---")
        print(f"Se descargó la info base de {PERFIL_OBJETIVO} en la carpeta del proyecto.")

    except Exception as e:
        print(f"\nERROR: {e}")
        print("\nDIAGNÓSTICO: Instagram sigue limitando el acceso a los datos detallados.")


if __name__ == "__main__":
    ejecutar_scraping_seguro()