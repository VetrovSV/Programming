import gradio as gr

def BMI(mass:float, heigh:float):
    """Вычисляет индекс массы тела. mass - кг, height - метры"""
    return mass/ heigh**2


form = gr.Interface(fn = BMI, inputs=[gr.Number(), gr.Number()])


