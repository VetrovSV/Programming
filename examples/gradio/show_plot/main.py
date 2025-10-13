import gradio as gr
import seaborn
import matplotlib.pyplot as plt
import pandas as pd

def plot_seaborn_scatter(data):
    plt.figure(figsize=(6,4))
    seaborn.scatterplot(data=data, x="x_column", y="y_column")
    fig = plt.gcf()  # получить текущую фигуру
    return fig

df = pd.DataFrame({
    "x_column": [1, 2, 3, 4],
    "y_column": [10, 15, 13, 17]
})

gr.Interface(
    fn=plot_seaborn_scatter, 
    inputs=gr.Dataframe(headers=["x_column", "y_column"]), 
    outputs=gr.Plot()
).launch()
