# Capitains: local use
* cd <PATH>
* pip install -r requirements.txt
* pip install flask_nemo
* python3 app.py

# Validation
* [Validator](https://capitains-validator.herokuapp.com/)
* [HookTest](https://github.com/Capitains/HookTest)
```
cd ~/Documents/github/mnemosyne/
pip3 install -r requirements.txt
pip3 install HookTest
cd ~/Documents/github/mnemosyne/corpora
hooktest ./ --console --scheme epidoc --workers 3 --verbose 10 --countwords
hooktest ./ --console --scheme epidoc --workers 3 --verbose 10 --countwords --filter tlg0019.tlg001
```
