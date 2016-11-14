# G.E-Downloader
## Faça o download de doujinshis e mangás do g.e-hentai!

### Descrição:
#### Este é um simples programa em Python que possui a função de fazer o download dos álbuns do g.e-hentai escolhidos pelo usuário.

#### Ao executar o programa sem utilizar argumentos pela linha de comando, o programa irá pedir ao usuário a URL do álbum desejado. Ele então irá carregar todas as informações do álbum para que o download das imagens possa ser realizado.

#### Após carregar as informações, o programa irá criar uma pasta no diretório atual do programa com o nome do álbum escolhido e dentro dela irá fazer o download das imagens.

![G.E-Downloader](http://i.imgur.com/gv6MLnH.png)

## [Verifique o CHANGELOG para maiores informações sobre novas versões](https://raw.github.com/Wolfterro/G.E-Downloader/master/CHANGELOG.txt)

### Opções (CLI):

#### Aqui estão algumas opções disponíveis e que podem ser inseridas como argumentos pela linha de comando:

    Uso: ./GEDownloader.py [URL / OPÇÕES]
    -------------------------------------
    
    Opções:
    -------
    -h || --help       Mostra o menu de ajuda.

#### É possível inserir a URL do álbum diretamente pela linha de comando. Caso contrário, o programa irá pedir pela URL.

### Requerimentos (CLI):
 - Python 2.x
 - BeautifulSoup4

#### Para instalar o BeautifulSoup4, basta utilizar o pip para fazer o download:

    sudo pip install beautifulsoup4

### Requerimentos (GUI):
- ***Linux:*** 
- (x86): Pode ser executado diretamente, sem qualquer requisito ou dependência.
- (x64): Pode ser executado diretamente, sem qualquer requisito ou dependência. Requer bibliotecas de compatibilidade caso escolha a versão em x86.
- ***Windows:*** 
- (x86 & x64): Requer o Microsoft Visual C++ 2010 Redistributable instalado (provavelmente já vem instalado em sistemas atualizados).

### Compilando (GUI):
- Python 2.7
- PyQt4 para Python 2.7
- BeautifulSoup4
- PyInstaller
- Microsoft Visual C++ 2010 Redistributable (Windows apenas)

#### Execute o PyInstaller para compilar o programa:

      - Linux:
      pyinstaller --noconsole --onefile GEDownloader.py
      
      - Windows
      pyinstaller --icon="Icon.ico" --noconsole --onefile GEDownloader.py

### Download (CLI):

#### Você poderá baixar o programa utilizando o git:

    git clone https://github.com/Wolfterro/G.E-Downloader.git
    cd G.E-Downloader/
    ./GEDownloader.py [URL / OPÇÕES]

#### Você também poderá utilizar o wget para baixar o programa:

    wget "https://raw.github.com/Wolfterro/G.E-Downloader/master/GEDownloader.py"
    chmod +x GEDownloader.py
    ./GEDownloader.py [URL / OPÇÕES]

### Download (GUI):

#### Linux: https://github.com/Wolfterro/G.E-Downloader/releases/tag/v1.0.2-Linux

#### Windows: https://github.com/Wolfterro/G.E-Downloader/releases/tag/v1.0.2-Windows

#### Caso não possua o git e queira também baixar o repositório por completo, baixe através deste [Link](https://github.com/Wolfterro/G.E-Downloader/archive/master.zip) ou clique em "Clone or Download", no topo da página.
