import os

# Caminho onde os prints serão salvos
SAVE_PATH = os.path.join(os.path.expanduser("~"), "Pictures", "Prints_Automaticos")

# Tempo de espera entre capturas para evitar duplicados
SLEEP_TIME = 1.0  # segundos

# Formato do nome do arquivo (usa data e hora)
FILENAME_FORMAT = "print_{timestamp}.png"
