import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def get_3d_vector_chart(jitter):
    """Visualizes the laser path with safety checks for negative scale."""
    # Safety Fix: NumPy normal scale must be positive
    safe_jitter = max(0.001, abs(jitter))
    
    x_val = np.random.normal(0, safe_jitter)
    y_val = np.random.normal(0, safe_jitter)
    
    fig = go.Figure(data=[go.Scatter3d(
        x=[0, x_val], y=[0, y_val], z=[0, 5],
        mode='lines+markers',
        line=dict(color='cyan', width=8),
        marker=dict(size=5, color='red')
    )])
    
    fig.update_layout(
        scene=dict(
            xaxis=dict(range=[-1, 1], title="X-Offset"),
            yaxis=dict(range=[-1, 1], title="Y-Offset"),
            zaxis=dict(range=[0, 5], title="Distance")
        ),
        margin=dict(l=0, r=0, b=0, t=0), height=400
    )
    return fig

def get_channel_chart(raw_data):
    df = pd.DataFrame(list(raw_data.items()), columns=['Channel', 'Signal'])
    fig = px.bar(df, x='Channel', y='Signal', color='Signal', color_continuous_scale='Plasma')
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=30), height=350, showlegend=False)
    return fig
