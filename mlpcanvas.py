from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=4, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        self.axes.spines['top'].set_visible(False)
        self.axes.spines['right'].set_visible(False)
        self.axes.spines['left'].set_visible(False)
        self.axes.spines['bottom'].set_visible(False)
        self.axes.set_axisbelow(True)
        self.axes.yaxis.grid(True, color='#EEEEEE')
        self.axes.xaxis.grid(False)
        self.fig.tight_layout()
    
        super(MplCanvas, self).__init__(self.fig)
