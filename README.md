[![Linter-check](https://github.com/VVtatarinoff/komtek/actions/workflows/lint.yml/badge.svg)](https://github.com/VVtatarinoff/komtek/actions/workflows/lint.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/987ef0ed04a7342363f0/maintainability)](https://codeclimate.com/github/VVtatarinoff/komtek/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/987ef0ed04a7342363f0/test_coverage)](https://codeclimate.com/github/VVtatarinoff/komtek/test_coverage)

# komtek
Тестовое задание. ТЗ в файле "Комтек ИЗ Python"

## Демо проект задеплоеен на https://komtektest.herokuapp.com/

Стэк использованных технологий:

    - django rest framework
    - postgres
    - flake8
    - poetry
    - pytest

Для запуска приложения необходимо создать БД и задать переменные окружения

    SECRET_KEY
    DATABASE_URL
    DEBUG=True  - если необходим 

#API entrypoints:
## /admin/ 

    административная панель БД

## /swagger/ 
    документация по доступным endpoints

## api/v1/references/

###GET:
    без параметров - получение списка справочников на текущую дату
    с параметром date (формат YYYY-MM-DD) - получение списка справочников на определенную дату, например:
        api/v1/references/?date=2022-03-29 - получение актуальных справочников на 29/03/2022
    
    Возвращается json в следующем формате. Пагинация по 10 элементов
    
    {"count": количество записей всего (число),
      "next": ссылка на следующую страницу,
      "previous": ссылка на текущую страницу,
      "results":
           [{"id": id справочника(число),
            "name": имя справочника (строка),
            "short_name": короткое наименование справочника (строка),
            "description": описание справочника (строка),
            "version_name": валидная версия справочника на указанную дату (строка),
            "version_id": id валидной версии справочника на указанную дату  (число),
            "valid_date": начало действия указанной версии справочника (строка в формате YYYY-DD-MM),
            },
            ...
           ]
   }

## api/v1/elements/<int>/

###GET:
    получение элементов справочника, указанного в параметре <int> - id справочника

    без параметров выборка выыполняется по текущей версии справочника
    с параметром ?version=<id> - из версии справочника с указанным id
    пример:
    api/v1/elements/12 - получение из справочника с id=12 текушей версии
    api/v1/elements/12/?version=1 - получение из справочника с id=12 версии с id=1

    Возвращается json в следующем формате. Пагинация по 10 элементов

    {"count": количество записей всего (число),
      "next": ссылка на следующую страницу,
      "previous": ссылка на текущую страницу,
      "results":
           [{"id": id элемента справочника(число),
            "code": код элемента справочника (строка),
            "value": значение элемента справочника (строка)},
            ...
           ]
   }
   
## api/v1/elements/<int>/

###POST:
    передаваемый формат - json, словарь в виде ключ-значение
    проверка переданных данных на соответсвие соответсвующим значениям справочоника
    индетификатор справочника - последний элемент <int> в url запроса
    опционально в параметрах запроса можно указать индентификатор версии справочника,
    без этого параметра проверяется текущая версия справочника.
    Пример:
        json данные: 
            {"code2" : "value1", "code2": "value2"} 
        api/v1/elements/10 - проверка справочника с id=10 (текущая версия)
        api/v1/elements/10/?version=2 - проверка справочника с id=10 (версия c id=2)

    Проверка происходит по всем парам ключ-значение. Соответствие должно быть полным:
        - все переданные ключи должны быть в справочнике
        - значение всех ключей соответствует значениям в справочнике
    
    возвращаемый результат - json словарь:
        {"result":"true"} в случае соответствия
        {"result":"true"} в случае наличия отклонения от значений (или при отсутствии данных для проверки)
