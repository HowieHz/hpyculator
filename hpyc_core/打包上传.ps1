chcp 65001

del .\dist\*.gz
python setup.py sdist
python -m twine upload dist/* --verbose