"""
Пример работы с талицей gr.Dataframe и компонентом gr.Plot для отображения графиков


gr.Plot способен отображать графики, представленные типом matplotlib.figure.Figure (см. fig в примере)
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn
import gradio as gr


# пример данных
rng = np.random.RandomState(0)
X = rng.normal(loc=5, scale=2, size=100)
Y = 2.0 * X + rng.normal(scale=3, size=100)


def plot_seaborn_scatter(data):
    # создание контейнера для всей картинки
    fig, ax = plt.subplots(figsize=(6,4))
    # fig: matplotlib.figure.Figure - контейнер» для всего рисунка (вся страница/холст)
    # ax: matplotlib.axes.Axes - полотно графика
    # добавляем на полотно (ax) данные, alpha - прозрачность, s - размер маркеров
    seaborn.scatterplot(x=X, y=Y, ax=ax, alpha=0.7, x="x", y="y")
    # поверх того же полотна дорисуем новые точки
    seaborn.scatterplot(data=data, ax=ax, s=50, x="x", y="y", 
                         marker='x', color='red',  # размер, тип, цвет маркера
                        label='new points', zorder=5)
    # если точка всего одна, то можно так:
    # seaborn.scatterplot(x = [координата_х], y = [координата_y], ...)
    # подписи к осям
    ax.set_xlabel("most important feature")     
    ax.set_ylabel("target")
    ax.legend()         # вкл. легенду

    plt.tight_layout()      # автоматически подбирает отступы (поля вокруг осей, расстояния между подграфиками), чтобы элементы рисунка (оси, подписи, тики, легенда) не перекрывались и не выходили за границы фигуры
    return fig


gr.Interface(
    fn=plot_seaborn_scatter, 
    inputs=gr.Dataframe(headers=["x", "y"]),            # таблица
    outputs=gr.Plot()                                   # компонент для отображения Figure (графиков matplotlib)
).launch()
