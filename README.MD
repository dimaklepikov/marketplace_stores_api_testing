# Тестовое задание на работу с API от [QA/Testers](https://qatesters.ru/)
Привет! Приложение тестирует функциональность API-эндпоинтов данного [Store](stores-tests-api.herokuapp.com) API.
[Документация](https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/Item)

## Как запустить?
1. Клонируйте/Форкните репозиторий
2. Создайте виртуальное окружение c Python версии 3,9. Я использую anaconda:
```sh
conda create -n pytest_api python=3.9
```
3. Перейдите в директорию с проектом и установите зависимости:
```sh
pip install -r requirements.txt
```
4. Запустите тесты - выберете тэг api, укажите base url, дайте имя файлу с html отчетом:)
```sh
pytest -m api --url https://stores-tests-api.herokuapp.com --html=report.html
``` 

## Функционал проекта
1. **Функциональные тесты RESTful API [Flask-проекта](https://github.com/berpress/flask-restful-api) - 4 позитивных и 2 негативных**
2. **Кастомная фикстура, позволяющая задавать base url через CLI**
3. **Тесты запускаются по кастомному тегу 'api'**
4. **Генерируется отчет в виде html-файла**

