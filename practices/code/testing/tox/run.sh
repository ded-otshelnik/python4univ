# если tox надо запустить в текущей Python-среде (venv, conda),
# то перед этим требуется установить плагин tox-current-env 
# pip install tox-current-env
# tox --current-env ...
tox run -v > output.txt