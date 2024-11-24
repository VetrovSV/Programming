# `.env` - файл конфигурации
`.env` файл используется для хранения переменных окружения, которые можно загружать в приложение во время выполнения. Это помогает разделить код и конфигурацию, улучшая переносимость и безопасность приложения.

**Принцип разделения кода и конфигурации**
- **Код** должен содержать логику работы программы, а не фиксированные значения конфигурации.
- **Конфигурация** — это изменяемые параметры, которые варьируются в зависимости от среды (разработка, тестирование, продакшн).

Например, адреса серверов, ключи для доступа к API и режимы работы удобно передавать через такие файлы.

## Использование `.env` файлов

### Установка и использование `dotenv`
**Установка пакета dotenv**:
   ```bash
   pip install python-dotenv
   ```

**Пример файла `.env`**:
   ```env
   SERVER_URL=https://api.example.com
   DEBUG=True
   API_KEY=your-api-key
   ```
**Загрузка файла в программе**:
   ```python
   from dotenv import load_dotenv
   import os

   load_dotenv()        # имя файла не указывается

   server_url = os.getenv("SERVER_URL")
   debug_mode = os.getenv("DEBUG", "False") == "True"
   print(server_url, debug_mode)
   ```

---

## Правила создания `.env` файлов
- Файл имеет расширение **`.env`**.
- Каждая строка содержит пару `ключ=значение`.
- Для значений с пробелами используйте кавычки.
- Файлы поддерживают пустые строки, которые можно использовать для визуального разделения данных
- Можно добавлять комментарии, начиная строку с #, чтобы пояснить назначение переменных. 
- Пробелы до и после `=` не ставятся.
Например:
  ```env
  # База данных для разработки
  DATABASE_URL=postgresql://user:password@localhost:5432/dev_db
 
  # Токен API
  API_TOKEN="example-token"

  SECRET_KEY="my-secret-key"
  DEBUG=True
  DATABASE_URL=postgresql://user:password@localhost:5432/mydb
  ```

---

## Работа с чувствительными данными
1. Создайте файл `.env.secret` для токенов и паролей.
2. Добавьте его в `.gitignore`:
   ```bash
   echo ".env.secret" >> .gitignore
   ```
3. Загружайте оба файла в коде:
   ```python
   load_dotenv(".env")
   load_dotenv(".env.secret")
   ```

---

## Лучшие практики
1. **Не добавляйте чувствительные данные в контроль версий!**
2. Разделяйте конфигурации:
   - `.env` — для общих параметров.
   - `.env.secret` — для токенов, паролей и других секретов.
3. Используйте файл-шаблон (`env.example`):
   ```env
   # env.example
   SERVER_URL=
   DEBUG=
   API_KEY=
   ```
4. Проверяйте наличие обязательных переменных:
   ```python
   required_vars = ["SERVER_URL", "API_KEY"]
   for var in required_vars:
       if not os.getenv(var):
           raise EnvironmentError(f"Missing required environment variable: {var}")
   ```

---

## Управление `.env` в разных окружениях
1. Создавайте отдельные `.env` файлы:
   - `.env.development`
   - `.env.production`
2. Выбирайте файл в зависимости от окружения:
   ```python
   env_file = ".env.development" if os.getenv("ENV") == "development" else ".env.production"
   load_dotenv(env_file)
   ```

---

## Использование `.env` в Docker
1. Передача `.env` в контейнер через `docker-compose`:
   ```yaml
   services:
     app:
       env_file:
         - .env
   ```
2. Передача через командную строку:
   ```bash
   docker run --env-file .env my-container
   ```

---

## Отладка и тестирование
- Проверьте, какие переменные окружения загружены:
  ```python
  print(os.environ)
  ```
- Отобразите отсутствующие переменные:
  ```python
  required_vars = ["SERVER_URL", "API_KEY"]
  for var in required_vars:
      if not os.getenv(var):
          print(f"Missing: {var}")
  ```

---

## Автоматизация работы с `.env` файлами
1. **Скрипт для генерации `.env` на основе шаблона**:
   ```python
   import os

   def generate_env(template_file, output_file):
       with open(template_file) as template, open(output_file, "w") as env_file:
           for line in template:
               key = line.split("=")[0].strip()
               value = os.getenv(key, "")
               env_file.write(f"{key}={value}\n")

   generate_env("env.example", ".env")
   ```
2. **Проверка соответствия `.env` и `env.example`**:
   ```python
   def check_env(template_file, env_file):
       with open(template_file) as template:
           template_keys = {line.split("=")[0].strip() for line in template}

       with open(env_file) as env:
           env_keys = {line.split("=")[0].strip() for line in env}

       missing_keys = template_keys - env_keys
       if missing_keys:
           print("Missing keys:", missing_keys)

   check_env("env.example", ".env")
   ```

---

## Частые ошибки
2. Пробелы вокруг знака `=` в `.env` файле.
3. Необработанные отсутствующие переменные в коде.

---

Теперь ты можешь использовать `.env` файлы эффективно и безопасно!

