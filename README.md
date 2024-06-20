Быков Фёдор Игнатьевич 215
Социальная сеть

# Примеры использования:

Скрипт `run.sh` запускает сервис через `docker-compose`, при этом снося старые `volume`ы, сбрасывая состояние СУБД после прошлых запусков

В папке `scripts` лежат скрипты, которые ходят в сервис через `curl`

Вот примеры использования для каждого из методов последовательно:

```
./signup Layton password
```

```
./login Layton password
```

`/api/login` возвращает нам сессию, её нужно передавать в заголовке в `/api/update` и `/api/profile`

```
./update example.json %SESSION_ID%
```

Файл `example.json` выглядит как-то так:

```
{
  "name" : "Hershel",
  "surname" : "Layton",
  "email" : "layton@google.com",
  "phone" : "88005553535",
  "birthdate" : "15 Feb 1923"
}
```

```
./profile %SESSION_ID%
```
