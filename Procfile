web: gunicorn base.wsgi --log-file -
python manage.py collectstatic --noinput
manage.py migrate
