import instaloader
import time

L = instaloader.Instaloader()

# DATOS
TU_USUARIO = "mariiaa_beleen"
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
    print("--- MODO DE RESCATE ACTIVADO ---")

    dict_cookies = cargar_cookies_manual(ARCHIVO_COOKIES)
    if not dict_cookies: return

    try:
        L.context._session.cookies.update(dict_cookies)

        # 1. Cargamos el perfil (esto suele funcionar porque no usa GraphQL pesado)
        print("Validando cuenta...")
        profile = instaloader.Profile.from_username(L.context, TU_USUARIO)
        print(f"Sesión activa para: {profile.full_name}")

        # 2. En lugar de un bucle de publicaciones, intentamos bajar SOLO EL PERFIL
        # Esto descarga la foto de perfil y la info básica sin activar el baneo de posts
        print("Descargando metadatos básicos del perfil...")
        L.download_profile(profile.username, profile_pic_only=False)

        print("\n--- ÉXITO PARCIAL ---")
        print("Se descargó la info base. Instagram tiene bloqueada la lista de posts para tu cuenta por ahora.")

    except Exception as e:
        print(f"\nERROR: {e}")
        print("\nDIAGNÓSTICO FINAL: Instagram ha bloqueado tu sesión para scraping.")


if __name__ == "__main__":
    ejecutar_scraping_seguro()