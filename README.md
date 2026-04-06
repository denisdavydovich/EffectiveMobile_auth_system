# EffectiveMobile_auth_system
📌 Auth System (Django + DRF)
📖 Описание проекта
Данный проект представляет собой backend-приложение с кастомной системой аутентификации и авторизации.
Реализовано:
* регистрация и логин пользователей
* JWT-аутентификация
* RBAC (Role-Based Access Control)
* разграничение доступа к ресурсам
* mock бизнес-логика

🧠 Архитектура
🔐 Аутентификация
Используется:
* JWT токены
* Middleware для определения пользователя
🔄 Процесс:
1. Пользователь логинится (/api/login/)
2. Получает JWT токен
3. Передаёт токен в заголовке:

Authorization: Bearer <token>

1. Middleware извлекает пользователя и кладёт в:

request.custom_user


🛡️ Авторизация (RBAC)
Основные сущности:
* User — пользователь
* Role — роль (admin, user)
* BusinessElement — ресурс (products)
* AccessRule — правила доступа

🗄️ Структура БД
User
Поле	Тип
id	int
email	string
password	string
role_id	FK
is_active	bool
Role
Поле	Тип
id	int
name	string
BusinessElement
Поле	Тип
id	int
name	string
AccessRule
Поле	Тип
role_id	FK
element_id	FK
read	bool
read_all	bool
create	bool
update	bool
update_all	bool
delete	bool
delete_all	bool
🔐 Логика прав доступа
Проверка происходит через:

check_permission(user, element, action)

Пример:

check_permission(user, "products", "read_all")


🚀 Установка и запуск
1. Клонировать проект

git clone <repo_url>
cd auth_system


2. Создать виртуальное окружение

python -m venv .venv
source .venv/bin/activate  # Mac/Linux


3. Установить зависимости

pip install django djangorestframework pyjwt bcrypt


4. Применить миграции

python manage.py makemigrations
python manage.py migrate


5. Создать суперпользователя (для admin)

python manage.py createsuperuser


6. Запустить сервер

python manage.py runserver


🔗 API Эндпоинты
👤 Пользователи
Регистрация

POST /api/register/


{
  "email": "user@mail.com",
  "password": "123456"
}


Логин

POST /api/login/


{
  "email": "user@mail.com",
  "password": "123456"
}

Ответ:

{
  "token": "jwt_token"
}


Logout

POST /api/logout/


📦 Бизнес-логика
Получить список продуктов

GET /api/products/

Headers:

Authorization: Bearer <token>


👑 Управление правами (admin only)
Получить правила

GET /api/rules/


Создать правило

POST /api/rules/


⚠️ Возможные ошибки
401 Unauthorized
Пользователь не авторизован

{
  "error": "Unauthorized"
}


403 Forbidden
Нет прав доступа

{
  "error": "Forbidden"
}


🧪 Тестовые данные
Пример ролей:
* admin — полный доступ
* user — только чтение

📌 Особенности реализации
* ❌ Не используется стандартная auth система Django
* ✅ Полностью кастомная логика
* ✅ JWT + middleware
* ✅ Гибкая система прав (RBAC)

