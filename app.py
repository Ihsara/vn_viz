# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

ROOT = 'C:/Users/longc/Documents/Plotly/'
teachers = 'Số giáo viên phổ thông thuộc các dân tộc ít người trực tiếp giảng dạy tại thời điểm 30_9 phân theo một số địa phương.xlsx'
students = 'Số học sinh phổ thông thuộc các dân tộc ít người tại thời điểm 30_9 phân theo địa phương.xlsx'

app = dash.Dash()

df_teachers = pd.ExcelFile( ROOT + teachers)
df_students = pd.ExcelFile( ROOT + students)

teachers = df_teachers.parse()
students = df_students.parse()

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


app = dash.Dash()

app.layout = html.Div(children=[
    html.H4(children='Số giáo viên phổ thông thuộc các dân tộc ít người trực tiếp giảng dạy tại thời điểm 30_9 phân theo một số địa phương'),
    generate_table(teachers),
    html.H4(children='Số học sinh phổ thông thuộc các dân tộc ít người tại thời điểm 30_9 phân theo địa phương'),
    generate_table(students)
])

if __name__ == '__main__':
    app.run_server(debug=True)
if __name__ == '__main__':
    app.run_server(debug=True)