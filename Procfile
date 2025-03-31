web: gunicorn  virtual_pet.wsgi:application
celery -A virtual_pet worker --loglevel=info
celery -A virtual_pet beat --loglevel=info