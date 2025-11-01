import os
import time
from config import SAVE_PATH, FILENAME_FORMAT


def ensure_directory_exists():
    """Cria a pasta de salvamento se ainda não existir."""
    os.makedirs(SAVE_PATH, exist_ok=True)

def generate_filename():
    """Gera nome do arquivo baseado na data/hora atual."""
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = FILENAME_FORMAT.format(timestamp=timestamp)
    return os.path.join(SAVE_PATH, filename)
