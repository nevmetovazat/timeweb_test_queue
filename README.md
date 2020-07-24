# Асинхронная очередь задач для web scraping

## Используемые технологии:
    Redis, Flask
    
Проект настроен для развертки на Heroku, нужно лишь указать переменные окружения.

# API пути
### - **POST** /scrape/
 
Принимает content-type:application/json. Формат:
  
```
{
    "url": "https://example.com"
}
```

Формат ответа: 
  
```
{
    "job_id": <uuid>
}
```

Также добавляется header Location с url, по которому можно получить ресурс.

### - **GET** /status/<job_id>
 
Принимает job_id как query parameter. Возвращает\:

```
{
    "status": "status",
    "result": {
        "headers": "headers",
        "content": "content"
    },
    "message": "if status == failed"
}
```

