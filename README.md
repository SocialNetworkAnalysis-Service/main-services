# SocialNetworkAnalysis-Service
Сервис для профориентации молодёжи и выстраивания карьерного пути. 

### Технологии
 - <b>Frontend:</b> html, css, js
 - <b>Backend:</b> fastapi, flask, flask_admin, sqlalchemy, postgresql, alembic, docker, nginx.
 - <b>Parsing:</b> vk_api, sqlite3
 - <b>Data-Science:</b> pandas, numpy, pymorphy2, navec, sikit-learn, nltk, catboost
 - Обучанная ML модель на основе спарсенных данных пользователей соц. сети VK (https://colab.research.google.com/drive/140vBm5aFKM8veqIRp49eY_m5cAxSUN_h?usp=sharing)

### Сервисы
 - API (api сайта)
 - Admin-Panel (admin панель для просмотра базы данных)
 - Postgresql-container (докер контейнер базы данных)
 - Chat-Bot (телеграм бот для консультации по карьерному росту) https://t.me/Career_assistant_bot
 - MonitoringServerBot (телеграм бот для мониторинга сервера) https://t.me/dayanadesign_inline_bot https://disk.yandex.ru/d/RK0LQJh4r1GQFQ

### Github репозитории дополнительные
 - https://github.com/SocialNetworkAnalysis-Service/vk-parser-draft
 - https://github.com/SocialNetworkAnalysis-Service/ml-model-draft
### Прицип работы сервиса
- Сайт https://dayanadesign.ru
- Аутентификая/Регистрация по номеру телефона (flash call)
- Профиль пользователя https://dayanadesign.ru/profile.html
- Выстраивание карьерного пути на основе информации VK страницы пользователя (парсинг данных)
- Тестирование в виде игры для определения приверженности к определенным типам профессиий https://dayanadesign.ru/profile.html

### Спарсенные данные
Характеристики пользователей ВК подписанные на сообщества определенной профессии
https://github.com/SocialNetworkAnalysis-Service/vk-parser-draft/tree/main/parsed_data


### Запущенные сервисы на данный момент
 - Сайт https://dayanadesign.ru
 - API http://88.210.3.130:8000/docs
   логин: user
   пароль: password

 - AdminPanel http://88.210.3.130:777/admin
   логин: user
   пароль: password

 - Chat-Bot (телеграм бот для консультации по карьерному росту) https://t.me/Career_assistant_bot
 - MonitoringServerBot (телеграм бот для мониторинга сервера) https://t.me/dayanadesign_inline_bot

   
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
- Нужно создат файл с конфигом services/admin_panel/src/.env
```# Admin panel secrets
FLASK_ADMIN_SWATCH=cosmo
BASIC_AUTH_USERNAME=user
BASIC_AUTH_PASSWORD=password
BASIC_AUTH_FORCE=True

# Database secrets
DB_HOST=localhost
DB_PORT=5432
DB_NAME=social_network
DB_USER=postgres
DB_PASSWORD=fWBuv1
```

- Нужно создат файл с конфигом services/site_api/src/.env
```
# Database secrets
DB_HOST=localhost
DB_PORT=5432
DB_NAME=social_network
DB_USER=postgres
DB_PASSWORD=fWBuv1


## SMS agent secrets
SMS_AGENT_LOGIN=sayraxfc
SMS_AGENT_PASSWORD=7RECj7MJ
SMS_AGENT_API_URL=https://api3.sms-agent.ru/v2.0/json/send/



## Nats
NATS_SERVER_URL=nats://nats:4222
``` 
```bash
git clone https://github.com/SocialNetworkAnalysis-Service/main-services.git
cd main-services/
docker-compose up -d
```
<img width="1002" alt="image" src="https://github.com/SocialNetworkAnalysis-Service/main-services/assets/65904112/112ae62b-d4fd-47f3-9879-3fbe12db6d48">


