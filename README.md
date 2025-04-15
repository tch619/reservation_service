# API-сервис для бронирования столиков в ресторане 

Проект для управления бронированием столов в ресторане с использованием FastAPI и SQLAlchemy. 
Пользователи могут создавать, обновлять, удалять и просматривать брони столов через API. 
В проекте реализована работа с базой данных, а также возможность тестирования через Postman или Pytest.

## Стуртура проекта
- **app**: основная дириктория
- **.env**: Файл переменных окружения для настройки приложения. 
- **tests**: Каталог с тестами для проверки функционала.
- **alembic**: Конфигурация для миграций 

## Требования

- Docker (и Docker Compose)
- Python 3.10 или выше (если не используется Docker)
- Создание файла .env

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/tch619/reservation_service.git

cd tables-reservation
```

### 2. Настройка виртуального окружения

```bash
python3 -m venv venv
source venv/bin/activate  # Для Linux/Mac
venv\Scripts\activate     # Для Windows
```

### 3. Установка зависимостей 
```bash
pip install -r requirements.txt
```

### 4. Создание .env

```
example:

DB_USER=db_user
DB_PASSWORD=db_pass
DB_HOST=db_host
DB_PORT=db_port
DB_NAME=db_name

DATABASE_URL=postgresql://db_user:db_pass@db_host:db_port/db_name

ENV=test # оcтавить так же для pytest

```

### 5. Docker

```bash
docker-compose up --build # поднять контейнер 
docker-compose down # остановить 
```

### 6. Запуск тестов
```bash
pytest
```

## Заключение

Это тестовое задание продемонстрировало мои навыки в разработке API с использованием FastAPI, взаимодействии с базой данных через SQLAlchemy, а также в использовании Docker для удобства развертывания и запуска проекта. Я реализовал основные функции для бронирования столов, такие как создание, удаление и просмотр информации о бронированиях, а также добавил тесты для проверки корректности работы этих функций.

**Включенные функции:**
- Создание, удаление и получение информации о бронированиях столов.
- Работа с базой данных через SQLAlchemy.
- Использование Docker для упрощенного развертывания.

**Дальнейшие улучшения, которые могут быть полезны:**
- Реализация дополнительных функций, таких как обновление бронирования или фильтрация бронирований по времени.
- Подключение системы аутентификации и авторизации для обеспечения безопасности API.
- Разработка более сложной схемы взаимодействия с пользователями и администраторами.

Я открыт для предложений по улучшению проекта и готов внести необходимые изменения. Спасибо за возможность выполнить это задание!

---

**Контакты:**
- Email: [timurchikeev@gmail.com]
- Telegram: [@veek1h]
