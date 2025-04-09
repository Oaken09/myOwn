import holoviews as hv
import pandas as pd
hv.extension('bokeh')  # Используем Bokeh для интерактивности
data = {
    'Дата': pd.date_range(start='2023-01-01', periods=30, freq='D'),
    'Баллы': [133, 10, 930, 86, 132, 188, 254, 230, 190, 222,
                211, 243, 276, 280, 300, 320, 2223, 255, 279, 252,
                2476, 230, 843, 266, 200, 150, 180, 170, 160, 111],
    'Секция': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C',
             'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C', 'B',
             'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A']
}
df = pd.DataFrame(data)
# Точечный график (Scatter)
scatter = hv.Scatter(df, 'Дата', 'Баллы', label='Баллы по дням')
scatter.opts(width=800, size=8, color='green', tools=['hover'])

# Линейный график (Curve)
curve = hv.Curve(df, 'Дата', 'Баллы').opts(line_color='blue', line_width=2)

# Объединяем графики
combined = (scatter * curve).opts(title='Баллы за январь 2023')

# Или сохранить в HTML
hv.save(combined, 'sales_plot.html')