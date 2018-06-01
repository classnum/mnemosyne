# Capitains: local use
* cd <PATH>
* pip install -r requirements.txt
* pip install flask_nemo
* python3 app.py

# Validation
* [Validator](https://capitains-validator.herokuapp.com/)
* [HookTest](https://github.com/Capitains/HookTest)
    * cd <PATH> [EXAMPLE: cd ~/Documents/github/mnemosyne/]
    * pip install -r requirements.txt
    * pip3 install HookTest
    * cd <PATH-TO-CORPORA> [EXAMPLE: cd ~/Documents/github/mnemosyne/corpora]
    * hooktest ./ --console table --scheme epidoc --workers 3 --verbose 10 --countwords
    * hooktest ./ --console table --scheme epidoc --workers 3 --verbose 10 --countwords --filter tlg0019.tlg001
