# Instalar o python na maquina Linux 
sudo apt-get install python

# Instalar o python no windows
https://www.python.org/ftp/python/3.12.8/python-3.12.8-amd64.exe

# Instalar o python no Mac
https://www.python.org/ftp/python/3.12.8/python-3.12.8-macos11.pkg

# Instalando dependencias no Windows
python3 -m venv venv
.venv/Scripts/activate
pip install -r requirements.txt

# Instalando dependencias no MAC/Linux
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt