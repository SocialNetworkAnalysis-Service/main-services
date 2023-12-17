# SocialNetworkAnalysis-Service
Сервис для профориентации молодёжи и выстраивания карьерного пути. 

### Технологии
 - Frontend: html, css, js
 - Backend: fastapi, flask, flask_admin, sqlalchemy, postgresql, alembic, docker, nginx.
 - Parsing: vk_api, sqlite3
 - Data-Science: pandas, numpy, pymorphy2, navec, sikit-learn, nltk, catboost
 - Обучанная ML модель на основе спарсенных данных пользователей соц. сети VK

### Сервисы
 - API (api сайта)
 - Admin-Panel (admin панель для просмотра базы данных)
 - Chat-Bot (телеграм бот для консультации по карьерному росту) https://t.me/Career_assistant_bot
 - Postgresql-container (докер контейнер базы данных)
   
### Прицип работы сервиса
- Аутентификая/Регистрация по номеру телефона (flash call)
- Профиль пользователя
- Выстраивание карьерного пути на основе информации vk страницы пользователя (парсинг данных)



### Запуск API, Admin_Panel на локалке
```bash
git clone https://github.com/SocialNetworkAnalysis-Service/main-services.git
cd main-services/
docker-compose up -d
```
<img width="1002" alt="image" src="https://github.com/SocialNetworkAnalysis-Service/main-services/assets/65904112/112ae62b-d4fd-47f3-9879-3fbe12db6d48">
