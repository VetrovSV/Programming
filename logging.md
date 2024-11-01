# Логирование в Python

## Что такое логирование?

**Логирование** — это процесс регистрации сообщений о работе программы. Сообщения могут включать:
- информацию о выполнении ключевых этапов,
- диагностические данные для отладки,
- сообщения об ошибках и критических сбоях.

## Зачем нужно логирование?

- **Отслеживание работы программы**: позволяет понимать, какие этапы были выполнены, и видеть подробности выполнения.
- **Диагностика ошибок**: помогает быстро найти и устранить ошибки, предоставляя полные сообщения об ошибках.
- **Мониторинг в продакшене**: отслеживание состояния приложения в реальном времени и выявление аномалий.
- **Упрощение отладки**: детализация действий программы помогает разработчикам видеть ход выполнения кода и выявлять узкие места.

## Пакет logging

Для небольших программ логирование можно организовать с помощью простого использования библиотеки `logging`:
```python
import logging

# Устанавливаем базовую конфигурацию
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
# логировать сообщения уровня INFO и выше
# %(levelname)s: подставляется уровень логирования (INFO, WARNING, ERROR, и т.д.).
# %(message)s: подставляется само сообщение, которое передано в лог

# Пример логов, приведены в порядке возрастания уровня
logging.debug("Это сообщение для отладки (DEBUG)")
logging.info("Программа начала выполнение (INFO)")
logging.warning("Предупреждение: низкий объем памяти (WARNING)")
logging.error("Ошибка загрузки данных (ERROR)")
logging.critical("Критическая ошибка: завершение программы (CRITICAL)")
```