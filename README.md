# SocialNetworkAnalysis-Service
Сервис для профориентации молодёжи и выстраивания карьерного пути. 

### Технологии
 - <b>Frontend:</b> html, css, js
 - <b>Backend:</b> fastapi, flask, flask_admin, sqlalchemy, postgresql, alembic, docker, nginx.
 - <b>Parsing:</b> vk_api, sqlite3
 - <b>Data-Science:</b> pandas, numpy, pymorphy2, navec, sikit-learn, nltk, catboost
 - Обучанная ML модель на основе спарсенных данных пользователей соц. сети VK

### Сервисы
 - API (api сайта)
 - Admin-Panel (admin панель для просмотра базы данных)
 - Postgresql-container (докер контейнер базы данных)
 - Chat-Bot (телеграм бот для консультации по карьерному росту) https://t.me/Career_assistant_bot
 - MonitoringServerBot (телеграм бот для мониторинга сервера) https://t.me/dayanadesign_inline_bot

### Прицип работы сервиса
- Аутентификая/Регистрация по номеру телефона (flash call)
- Профиль пользователя
- Выстраивание карьерного пути на основе информации VK страницы пользователя (парсинг данных)
- Тестирование для определения приверженности к определенным типам профессиий

### Спарсенные данные




### Дерево проекта
```main-services/
├── docker-compose.yaml
├── documents
├── pyproject.toml
└── services
    ├── admin_panel
    │   ├── Dockerfile
    │   ├── main.py
    │   ├── requirements.txt
    │   └── src
    │       ├── config.py
    │       ├── db
    │       │   └── database.py
    │       └── models
    │           ├── users
    │           │   ├── admin.py
    │           │   └── model.py
    │           └── verification_codes
    │               ├── admin.py
    │               └── model.py
    ├── chat_bot
    │   ├── Dockerfile
    │   ├── main.py
    │   └── requirements.txt
    └── site_api
        ├── alembic.ini
        ├── Dockerfile
        ├── main.py
        ├── migrations
        │   ├── env.py
        │   ├── README
        │   ├── script.py.mako
        │   └── versions
        │       └── 6ed24cdc0081_database_creation.py
        ├── requirements.txt
        └── src
            ├── config_reader.py
            ├── db
            │   ├── database.py
            │   └── repository.py
            ├── dependencies.py
            ├── essence
            │   ├── operations
            │   │   └── router.py
            │   ├── users
            │   │   ├── models.py
            │   │   ├── repository.py
            │   │   ├── router.py
            │   │   ├── schemas.py
            │   │   └── service.py
            │   └── verification_codes
            │       ├── models.py
            │       ├── repository.py
            │       ├── schemas.py
            │       └── service.py
            ├── models.py
            ├── security.py
            └── utils
                ├── config.json
                ├── ml_model.py
                ├── navec_hudlit_v1_12B_500K_300d_100q.tar
                ├── sms_api.py
                └── vk_parser.py
```

### Схема Базы Данных
![SayraxPrint (1)](https://github.com/SocialNetworkAnalysis-Service/main-services/assets/65904112/90f4db55-b42d-4689-9423-d5ada9a7a97d)


### Запуск API, Admin_Panel, ChatBot (карьерный бот) на локалке
```bash
git clone https://github.com/SocialNetworkAnalysis-Service/main-services.git
cd main-services/
docker-compose up -d
```
<img width="1002" alt="image" src="https://github.com/SocialNetworkAnalysis-Service/main-services/assets/65904112/112ae62b-d4fd-47f3-9879-3fbe12db6d48">



