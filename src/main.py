import subprocess
import threading
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Lancer FastAPI avec uvicorn
def run_fastapi():
    try:
        logging.info("Démarrage de FastAPI...")
        result = subprocess.run(
            ["uvicorn", "src.api:app", "--reload"],
            check=True
        )
    except subprocess.CalledProcessError as e:
        logging.error(f"Erreur lors du démarrage de FastAPI: {e}")


# Lancer Streamlit
def run_streamlit():
    try:
        logging.info("Démarrage de Streamlit...")
        subprocess.run(["streamlit", "run", "streamlit_app.py"], check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Erreur lors du démarrage de Streamlit: {e}")


if __name__ == "__main__":
    # On code deux threads pour exécuter les deux serveurs en parallèle
    fastapi_thread = threading.Thread(target=run_fastapi)
    streamlit_thread = threading.Thread(target=run_streamlit)

    # Démarrage dess threads
    fastapi_thread.start()
    streamlit_thread.start()

    # On attend que les threads se terminent
    fastapi_thread.join()
    streamlit_thread.join()

    logging.info("Les deux serveurs ont été démarrés avec succès.")