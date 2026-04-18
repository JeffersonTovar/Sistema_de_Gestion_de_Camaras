#!/bin/sh

echo "Esperando base de datos..."
while ! nc -z db 3306; do
  sleep 1
done

echo "DB lista!"

echo "Creando tablas..."
python -c "from app.db.init_db import init_db; init_db()"

echo "Ejecutando seed..."
python -m seed.run_seed

echo "Iniciando servidor..."
uvicorn main:app --host 0.0.0.0 --port 8000
