sudo apt-get -y install libgmp3-dev
cd ~
mkdir rsa
cd rsa
virtualenv venv
source venv/bin/activate
git clone https://github.com/Ganapati/RsaCtfTool.git
cd RsaCtfTool
git clone https://github.com/hellman/libnum.git
cd libnum
python setup.py install
cd ..
pip install -r requirements.txt
cd ..
git clone https://github.com/ius/rsatool.git
cd rsatool
python setup.py install
cd ..
pip install sympy
git clone https://github.com/rk700/attackrsa.git
cd attackrsa
python setup.py install
cd ..
deactivate

# Download Yafu
echo Make sure to download Yafu!
echo https://sourceforge.net/projects/yafu/
