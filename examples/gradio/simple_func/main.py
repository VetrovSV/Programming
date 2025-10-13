import gradio as gr


# пример функции бизнес-логики. Стоит приводить в отдельном модуле
def BMI(mass:float, heigh:float):
    """Вычисляет индекс массы тела. mass - кг, height - метры"""
    return mass/ heigh**2


# функция обработчик
def on_submit(mass:float, heigh:float):
    """Обработчик для кнопки отправки формы"""
    if mass <= 0 or heigh <= 0:
        raise gr.Error("Неправильные масса и\или рост!", duration=10)
    return round(BMI(mass, heigh), 1)


# Построение интерфейса
form = gr.Interface(fn = on_submit, inputs=["number", gr.Number()], outputs="label")
# запуск веб-сервера и веб-приложения.
form.launch()
# Адрес по умолчанию: http://localhost:7860


