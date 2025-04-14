#!/bin/bash
/wait-for-it.sh db:5432 --strict --timeout=30 -- \
    alembic upgrade head

echo "Применение миграций Alembic..."
alembic current
alembic upgrade head && echo "Alembic миграции успешно применены!" || {
  echo "Ошибка применения миграций"
  exit 1
}

exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
