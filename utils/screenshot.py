from PIL import ImageGrab
from utils.file_manager import ensure_directory_exists, generate_filename


def save_screenshot_from_clipboard():
    """Captura imagem do clipboard (Print Screen) e salva automaticamente."""
    ensure_directory_exists()
    img = ImageGrab.grabclipboard()
    if img:
        filename = generate_filename()
        img.save(filename)
        print(f"[✅] Print salvo em: {filename}")
        return True
    else:
        print("[⚠️] Nenhuma imagem encontrada no clipboard.")
        return False
