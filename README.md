📸 Auto Screenshot Saver

Um programa em Python que monitora a tecla Print Screen e salva automaticamente a captura de tela como imagem em uma pasta organizada.
Ideal para quem tira muitos prints e quer evitar o trabalho manual de colar e salvar.

✅ Funcionalidades

Captura automaticamente qualquer print enviado ao clipboard após pressionar Print Screen.

Salva a imagem em uma pasta específica (ex.: Pictures/Prints_Automaticos).

Cria nomes de arquivo com data e hora para evitar duplicados.

Roda em segundo plano e exibe logs no terminal.

Código organizado usando boas práticas (módulos, separação de responsabilidades, config centralizada).

📁 Estrutura do Projeto
auto_screenshot/
│
├── main.py                 # Loop principal que monitora Print Screen
├── config.py               # Configurações globais
├── utils/
│   ├── __init__.py
│   ├── file_manager.py     # Manipulação de pastas e nomes de arquivo
│   └── screenshot.py       # Lógica de captura e salvamento da imagem
└── requirements.txt        # Dependências do projeto

🧩 Instalação
1️⃣ Clone o repositório
git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
cd NOME_DO_REPOSITORIO

Crie um ambiente virtual (opcional, recomendado)
python -m venv .venv

Ativar:

Windows
.venv\Scripts\activate

Linux/Mac
source .venv/bin/activate

3️⃣ Instale as dependências
pip install -r requirements.txt

▶️ Como usar

Execute o programa:
python main.py

A partir disso:

✅ toda vez que você pressionar Print Screen,
✅ o conteúdo do clipboard será salvo automaticamente em:
Pictures/Prints_Automaticos

O programa cria o diretório automaticamente se ele não existir.

⚙️ Configurações

Você pode ajustar as opções no arquivo config.py:
SAVE_PATH = r"Caminho onde os prints serão salvos"
SLEEP_TIME = 1.0  # Intervalo para evitar duplicações
FILENAME_FORMAT = "print_{timestamp}.png"

Modifique livremente conforme sua necessidade.

🧱 Tecnologias utilizadas

Python 3.x

Pillow (manipulação de imagens)

Keyboard (monitoramento de tecla)

Estrutura organizada em módulos

🚀 Melhorias futuras (opcionais)

Executável .exe para Windows (PyInstaller)

Notificações no sistema ao salvar prints

Interface gráfica para configurar o programa

Upload automático para: Google Drive, Dropbox ou Telegram

Modo “minimizado para bandeja” (system tray)

📄 Licença

Você pode definir a licença que preferir (MIT, Apache, GPL etc).
Exemplo:
Este projeto está licenciado sob a licença MIT — sinta-se livre para usar, modificar e distribuir.

🤝 Contribuições

Contribuições são bem-vindas!
Caso queira sugerir melhorias, abrir issues ou enviar pull requests — fique à vontade.

⭐ Se gostou do projeto...

Deixe uma estrela no GitHub ⭐ para apoiar!
