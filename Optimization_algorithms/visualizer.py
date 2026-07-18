import plotly.graph_objects as go
import numpy as np
from algos import Optimizers

class Visualizer:
    def __init__(self, x, y, funcZ):
        x = np.linspace(x[0], x[1], x[2])
        y = np.linspace( y[0],  y[1],  y[2])
        self.X, self.Y = np.meshgrid(x, y)
        self.funcZ = funcZ
        self.opt = Optimizers()
    
    # def change
    
    def show_graph(self):
        self.Z = self.funcZ(self.X, self.Y)

        fig = go.Figure(data=[go.Surface(
            x=self.X,
            y=self.Y,
            z=self.Z,
            colorscale='Viridis',
            opacity=1.0
        )])
        self.set_pointer(fig)


    
    def set_pointer(self, fig):
        # Define the point
        point_x, point_y = 8, 14
        point_z = self.funcZ(point_x, point_y)

        # Add the center point (optional)
        fig.add_trace(go.Scatter3d(
            x=[point_x],
            y=[point_y],
            z=[point_z],
            mode='markers',
            marker=dict(
                size=6,
                color='red',
                symbol='circle',
                opacity=1.0
            ),
            name='Point'
        ))
        self.animation(fig, point_x, point_y, point_z)

        
    def animation(self, fig, px, py, pz):
        opt = Optimizers()
        n = len(self.X)
        frames = []
        frame = go.Frame(
            data=[go.Scatter3d(
                x=[px],
                y=[py],
                z=[pz],
                mode='markers',
                marker=dict(
                    size=6,
                    color='red',
                    symbol='circle',
                    opacity=1.0
                )
            )],
            traces=[1],
            name=f'frame{0}'
        )
        frames.append(frame)
        for i in range(1000):
            lx = frames[-1].data[0].x[0]
            ly = frames[-1].data[0].y[0]
            lx, ly = self.opt.SGDM(lx,ly)
            lz = self.funcZ(lx, ly)
            frame = go.Frame(
                data=[go.Scatter3d(
                    x=[lx],
                    y=[ly],
                    z=[lz],
                    mode='markers',
                    marker=dict(
                        size=6,
                        color='red',
                        symbol='circle',
                        opacity=1.0
                    )
                )],
                traces=[1],
                name=f'frame{i+1}'
            )
            frames.append(frame)
        fig.frames = frames

        # Add animation slider - sample every 5 frames
        slider_steps = []
        for i in range(0, 1000, 5):
            step = dict(
                method='animate',
                args=[
                    [f'frame{i}'],
                    dict(mode='immediate', frame=dict(duration=0, redraw=True))
                ],
                label=f'{i:.1f}'
            )
            slider_steps.append(step)
        fig.update_layout(
            title='Ball Moving Along y = x Curve',
            scene=dict(
                xaxis_title='X',
                yaxis_title='Y',
                zaxis_title='Z',
                xaxis_range=[-5, 10],
                yaxis_range=[0, 15],
                zaxis_range=[0, 300]
            ),
            sliders=[dict(
                active=0,
                steps=slider_steps,
                currentvalue=dict(prefix='Position t = '),
                pad=dict(t=50)
            )],
            updatemenus=[dict(
                type='buttons',
                buttons=[
                    dict(
                        label='▶ Play',
                        method='animate',
                        args=[None, dict(
                            frame=dict(duration=50, redraw=True),
                            fromcurrent=True,
                            transition=dict(duration=0)
                        )]
                    ),
                    dict(
                        label='⏸ Pause',
                        method='animate',
                        args=[[None], dict(
                            frame=dict(duration=0, redraw=False),
                            mode='immediate',
                            transition=dict(duration=0)
                        )]
                    ),
                    dict(
                        label='⟳ Loop',
                        method='animate',
                        args=[None, dict(
                            frame=dict(duration=100, redraw=True),
                            fromcurrent=True,
                            loop=True
                        )]
                    )
                ],
                x=0,
                y=0.3,
                bgcolor='rgba(255,255,255,0.8)'
            )]
        )

        fig.show()