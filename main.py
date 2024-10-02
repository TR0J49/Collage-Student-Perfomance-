import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
import numpy as np

# Sample Data Creation (You can replace this with real-time data)
np.random.seed(42)
data = {
    "Student ID": [f"S{i}" for i in range(1, 101)],
    "Name": [f"Student {i}" for i in range(1, 101)],
    "Score": np.random.randint(50, 100, size=100),
    "Attendance": np.random.uniform(0.5, 1.0, size=100),
    "Assignments Submitted": np.random.randint(0, 10, size=100),
    "Projects Completed": np.random.randint(0, 5, size=100),
}
df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div(
    style={
        'background': 'linear-gradient(to right, #74ebd5, #ACB6E5)',
        'padding': '20px',
        'color': '#333'
    },
    children=[
        html.H1("Real-Time Analysis of College Student Performance", style={
            'text-align': 'center',
            'margin-bottom': '40px'
        }),

        # Creating a grid layout for the graphs
        html.Div(
            style={
                'display': 'grid',
                'grid-template-columns': 'repeat(auto-fit, minmax(300px, 1fr))',
                'gap': '20px',
                'margin': '0 auto',
                'max-width': '1200px'
            },
            children=[
                dcc.Graph(
                    id='score-distribution',
                    figure=px.histogram(df, x='Score', title='Score Distribution',
                                         color='Score',
                                         color_discrete_sequence=px.colors.sequential.Viridis).update_layout(height=250)
                ),
                dcc.Graph(
                    id='attendance-vs-score',
                    figure=px.scatter(df, x='Attendance', y='Score', title='Attendance vs Score',
                                      color='Score',
                                      color_continuous_scale=px.colors.sequential.Rainbow).update_layout(height=250)
                ),
                dcc.Graph(
                    id='assignments-distribution',
                    figure=px.histogram(df, x='Assignments Submitted', title='Assignments Submitted Distribution',
                                         color='Assignments Submitted',
                                         color_discrete_sequence=px.colors.sequential.Plasma).update_layout(height=250)
                ),
                dcc.Graph(
                    id='projects-completed',
                    figure=px.bar(df, x='Name', y='Projects Completed', title='Projects Completed by Students',
                                   color='Projects Completed',
                                   color_discrete_sequence=px.colors.sequential.Cividis).update_layout(height=250)
                ),
                dcc.Graph(
                    id='attendance-distribution',
                    figure=px.histogram(df, x='Attendance', title='Attendance Distribution',
                                         color='Attendance',
                                         color_discrete_sequence=px.colors.sequential.Magma).update_layout(height=250)
                ),
                dcc.Graph(
                    id='average-score-per-student',
                    figure=px.box(df, y='Score', title='Average Score Per Student',
                                  color='Score',
                                  color_discrete_sequence=px.colors.sequential.Oryel).update_layout(height=250)
                ),
                dcc.Graph(
                    id='score-heatmap',
                    figure=px.density_heatmap(df, x='Assignments Submitted', y='Score', title='Heatmap of Assignments vs Score',
                                               color_continuous_scale=px.colors.sequential.Blues).update_layout(height=250)
                ),
                dcc.Graph(
                    id='attendance-line-chart',
                    figure=px.line(df, x='Student ID', y='Attendance', title='Attendance Line Chart',
                                   markers=True,
                                   color='Attendance').update_layout(height=250)
                ),
                dcc.Graph(
                    id='score-pie-chart',
                    figure=px.pie(df, values='Score', names='Name', title='Score Distribution by Student',
                                   hole=0.3,
                                   color_discrete_sequence=px.colors.qualitative.Set2).update_layout(height=250)
                ),
                dcc.Graph(
                    id='attendance-bar-chart',
                    figure=px.bar(df, x='Name', y='Attendance', title='Attendance by Student',
                                   color='Attendance',
                                   color_discrete_sequence=px.colors.sequential.YlGn).update_layout(height=250)  # Changed to YlGn
                ),
            ]
        ),

        # Copyright Notice
        html.Div(
            children=[
                html.P("© 2024 Neuro Tech Enclave Pvt Ltd", style={
                    'text-align': 'center',
                    'margin-top': '40px',
                    'font-size': '14px'
                }),
            ],
            style={'text-align': 'center'}
        )
    ]
)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
