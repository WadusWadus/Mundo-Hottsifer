=== crear enviroment ===

python3 -m venv .venv

=== activar ===
source .venv/bin/activate

=== python install (pip) ===

python -m pip install --upgrade pip

=== crear programa ===
django-admin startproject dianapp .
python manage.py startapp accounts
python manage.py startapp characters
