from PIL import ImageGrab
import os
import time

def save_screenshot_from_clipboard():
    image = ImageGrab.grabclipboard()
    if image:
        # Caminho da pasta "Imagens/Capturas" do usuário
        pictures_folder = os.path.join(os.path.expanduser("~"), "Pictures", "Capturas")
        os.makedirs(pictures_folder, exist_ok=True)

        # Nome do arquivo com data e hora
        filename = time.strftime("%Y-%m-%d_%H-%M-%S.png")
        path = os.path.join(pictures_folder, filename)

        # Salva a imagem
        image.save(path)
        print(f"✅ Captura salva em: {path}")
    else:
        print("⚠️ Nenhuma imagem encontrada na área de transferência.")
