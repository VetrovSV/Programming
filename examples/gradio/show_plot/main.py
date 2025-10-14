import gradio as gr
import seaborn
import matplotlib.pyplot as plt
import pandas as pd

def plot_seaborn_scatter(data):
    fig = plt.figure(figsize=(6,4))
    seaborn.scatterplot(data=data, x="x", y="y")
    # fig = plt.gcf()  # получить текущую фигуру
    return fig


gr.Interface(
    fn=plot_seaborn_scatter, 
    inputs=gr.Dataframe(headers=["x", "y"]), 
    outputs=gr.Plot()
).launch()
