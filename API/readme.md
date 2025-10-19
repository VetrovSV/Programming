# OpenAPI — кратко

**OpenAPI** — спецификация (формат YAML/JSON) для описания HTTP/REST API. Позволяет описать пути (paths), операции (operations — методы HTTP), параметры, схемы данных, ответы, коды ошибок, механизмы безопасности и метаданные API. OpenAPI широко используется для генерации интерактивной документации, mock-серверов, клиентских SDK и тестов.

**Версии:** OpenAPI **3.0** и **3.1**. Версия 3.1 привела совместимость со стандартом JSON Schema 2020-12.

**Инструменты:** Swagger UI, ReDoc, Swagger Editor, OpenAPI Generator, Spectral (линтер), Stoplight, Postman, Insomnia.

## Аналоги и связанные спецификации

* **RAML**, **API Blueprint** — альтернативы для документирования REST.
* **GraphQL** — иной подход к API (не «альтернатива описанию OpenAPI», а другая парадигма).
* **AsyncAPI** — предназначен для событийно-ориентированных и двунаправленных коммуникаций (WebSocket, MQTT, Kafka и т.д.). OpenAPI не покрывает такие протоколы полноценно.




## Формат и машинная обработка

* Документы в YAML/JSON читаемы машинами → генерация документации, кода, тестов.
* В OpenAPI 3.1 используется полноценный JSON Schema, это упрощает валидацию и переиспользование схем.

---

## Хорошие практики

* **Single Source of Truth:** согласовывать, откуда генерируется спецификация — код → спецификация (code-first) или спецификация → код (design-first).
* **Версионирование API:** укажите версию (обычно в `info.version` и/или в пути `/v1/`). Рекомендация: указывать major-версию в URL (`/api/v1`) для явного управления несовместимыми изменениями.
* **Components & $ref:** переиспользуйте схемы и ответы через `components/schemas` и `$ref` чтобы избежать дублирования.
* **Линтинг и CI:** запускать Spectral или другие проверки схем в CI.
* **Документируйте ошибки и примеры:** добавляйте `examples` в `responses` и `requestBody` — это облегчает понимание и тестирование.
* **Security:** явно описывайте механизмы авторизации (например, `securitySchemes` + `security`).
* **Документация в окружении:** размещайте интерактивную документацию (Swagger UI / ReDoc) в рамках dev/staging/production по соглашению команды.

---

## Быстрые примеры

**Пример `info` (в спецификации):**

```yaml
openapi: "3.1.0"
info:
  title: RAG API
  description: API для работы с RAG-системой (Retrieval-Augmented Generation)
  version: "1.0.0"
  contact:
    name: Иван Иванов
    email: ivan@example.com
  license:
    name: MIT
```

**Пример `servers`:**

```yaml
servers:
  - url: https://api.example.com/v1
    description: Продакшн
  - url: https://staging.example.com/v1
    description: Стадия
```

**Путь с параметрами и ответом:**

```yaml
paths:
  /users/{userId}:
    get:
      summary: Получить пользователя по ID
      parameters:
        - name: userId
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Успешный ответ
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '404':
          description: Пользователь не найден
```

**Security (Bearer):**

```yaml
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

security:
  - BearerAuth: []
```

---

## FastAPI — что важно знать (коррекции и акценты)

* FastAPI автоматически генерирует OpenAPI-документ и UI (по умолчанию `/docs` → Swagger UI, `/redoc` → ReDoc, и `/openapi.json`), но это — **фреймворк-специфичная реализация** документации, а не часть спецификации OpenAPI как таковой.
* **Uvicorn** — это ASGI-сервер (не просто «веб-сервер для WebSocket»). ASGI — интерфейс между сервером и приложением, он поддерживает HTTP и WebSocket.
* FastAPI использует **Pydantic** для валидации и сериализации данных (на основе аннотаций типов).
* Для форм: используйте `Form`, для файлов — `File` / `UploadFile`. Для более точной документации параметров можно применять `Annotated` + `Query`/`Path`/`Header` и т. п.
* Фоновые задачи: `BackgroundTasks` (встроенный) или внешние решения (Celery) для сложных фоновых рабочих процессов.
