import matplotlib.pyplot as plt
import numpy as np
from abc import ABC, abstractmethod

class DataSet:
    """
    Class representing a dataset to be plotted
    """
    def __init__(self, x_values, y_values, label=None, color=None, style=None):
        self.x_values = x_values
        self.y_values = y_values
        self.label = label
        self.color = color
        self.style = style or '-'  # Default line style
        
    def get_plot_args(self):
        """Returns the arguments for plotting this dataset"""
        args = {'linestyle': self.style}
        if self.color:
            args['color'] = self.color
        if self.label:
            args['label'] = self.label
        return args


class PlotStrategy(ABC):
    """Abstract base class for different plotting strategies"""
    @abstractmethod
    def plot(self, ax, dataset):
        pass


class LinePlotStrategy(PlotStrategy):
    """Strategy for line plots"""
    def plot(self, ax, dataset):
        return ax.plot(dataset.x_values, dataset.y_values, **dataset.get_plot_args())


class ScatterPlotStrategy(PlotStrategy):
    """Strategy for scatter plots"""
    def plot(self, ax, dataset):
        return ax.scatter(dataset.x_values, dataset.y_values, **dataset.get_plot_args())


class Canvas:
    """
    Canvas class for plotting multiple datasets with different styles
    Follows the Factory Design Pattern to create different types of plots
    """
    def __init__(self, title=None, xlabel=None, ylabel=None, figsize=(10, 6)):
        """
        Initialize the canvas with optional title and axis labels
        
        Parameters:
        -----------
        title : str, optional
            Title of the plot
        xlabel : str, optional
            Label for x-axis
        ylabel : str, optional
            Label for y-axis
        figsize : tuple, optional
            Figure size as (width, height) in inches
        """
        self.fig, self.ax = plt.subplots(figsize=figsize)
        self.datasets = []
        self.plot_strategies = {
            'line': LinePlotStrategy(),
            'scatter': ScatterPlotStrategy()
        }
        
        if title:
            self.ax.set_title(title)
        if xlabel:
            self.ax.set_xlabel(xlabel)
        if ylabel:
            self.ax.set_ylabel(ylabel)
    
    def add_dataset(self, x_values, y_values, label=None, color=None, style=None, plot_type='line'):
        """
        Factory method to add a dataset to the canvas
        
        Parameters:
        -----------
        x_values : array-like
            x coordinates of the data points
        y_values : array-like
            y coordinates of the data points
        label : str, optional
            Label for the dataset in the legend
        color : str, optional
            Color of the plot
        style : str, optional
            Line style or marker style
        plot_type : str, optional
            Type of plot ('line' or 'scatter')
        
        Returns:
        --------
        int
            Index of the added dataset
        """
        dataset = DataSet(x_values, y_values, label, color, style)
        self.datasets.append((dataset, plot_type))
        return len(self.datasets) - 1
    
    def remove_dataset(self, index):
        """Remove a dataset by its index"""
        if 0 <= index < len(self.datasets):
            self.datasets.pop(index)
            return True
        return False
    
    def clear(self):
        """Clear all datasets and reset the canvas"""
        self.datasets = []
        self.ax.clear()
    
    def plot(self):
        """Plot all datasets on the canvas"""
        for dataset, plot_type in self.datasets:
            if plot_type in self.plot_strategies:
                self.plot_strategies[plot_type].plot(self.ax, dataset)
        
        if any(dataset.label for dataset, _ in self.datasets):
            self.ax.legend()
        
        self.fig.tight_layout()
    
    def show(self):
        """Display the plot"""
        self.plot()
        plt.show()
    
    def save(self, filename, dpi=300):
        """Save the plot to a file"""
        self.plot()
        self.fig.savefig(filename, dpi=dpi, bbox_inches='tight')
        return filename