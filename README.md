📸 ScreenshotApp

Um utilitário leve em Python que monitora a tecla Print Screen e salva automaticamente capturas de tela em uma pasta organizada, exibindo notificações modernas do Windows a cada captura.

🚀 Novidades da Versão Atual
🧠 1. Execução paralela (multithreading)

Cada captura é executada em uma thread separada, permitindo tirar várias capturas rapidamente sem travar o programa.

Antes, o programa esperava terminar a primeira captura para aceitar outra.

⚡ 2. Notificações nativas modernas

Agora usa a biblioteca winotify

📁 3. Salvamento automático organizado

As imagens são salvas automaticamente na pasta:

C:\Users\<seu_nome>\Pictures\Capturas\


Cada arquivo recebe o nome no formato:
2025-11-06_14-00-35.png

🧩 4. Código mais robusto

Tratamento de exceções aprimorado

Continua funcionando mesmo se a notificação falhar

Compatível com o modo Ctrl+C para encerrar de forma limpa

Sem travamentos ou lentidão após várias capturas

🔔 5. Feedback visual e auditivo (opcional)

O código já está preparado para adicionar:

Som de clique de câmera 🎵

Flash visual breve 💡

Esses efeitos podem ser ativados facilmente para melhorar a experiência do usuário.

🪄 6. Execução rápida sem VSCode

Agora você pode:

Criar um atalho .bat para iniciar com duplo clique

Ou gerar um .exe com pyinstaller:

pyinstaller --onefile main.py

E até definir uma tecla de atalho global, como Ctrl + Alt + P, para iniciar o monitoramento sem abrir o editor.


⚙️ Instalação

Clone o projeto ou baixe os arquivos.

Instale as dependências:

pip install pillow keyboard winotify

Execute:

python main.py


🧱 Estrutura de pastas
📁 ScreenshotApp/
│
├── main.py                 # Lógica principal (monitoramento da tecla Print)
├── config.py               # Configurações gerais (ex: tempo entre capturas)
├── 📁 utils/
│   └── screenshot.py       # Função de captura e salvamento



💡 Uso

Execute o programa (python main.py ou pelo atalho .bat).

Pressione Print Screen a qualquer momento.

A captura será salva automaticamente e você verá uma notificação 📢.

Pressione Ctrl + C para encerrar.


🧰 Tecnologias utilizadas

🐍 Python 3.10+

🖼️ Pillow (PIL) — captura da área de transferência

⌨️ Keyboard — monitoramento da tecla Print Screen

🔔 Winotify — notificações nativas do Windows


🧩 Próximas melhorias sugeridas

🔊 Adicionar som de “click de câmera”

💡 Efeito de flash breve na tela ao capturar

🧠 Interface gráfica simples (PyQt / Tkinter)

☁️ Opção para enviar capturas direto ao Google Drive ou Dropbox

👨‍💻 Autor

Pedro Vinícius Silva Magalhães

Projeto pessoal de automação e produtividade em Python.