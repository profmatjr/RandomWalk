#!/usr/bin/env python
import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, FigureCanvasAgg
from matplotlib.figure import Figure
import numpy as np 
import pylab 
import random 

def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def randwalk(n):
	x = np.zeros(n) # x and y are arrays which store the coordinates of the position 
	y = np.zeros(n) 
	direction=["Up","Down","Right","Left"] # Assuming the four directions of movement.
	for i in range(1, n): 
		step = random.choice(direction) #Randomly choosing the direction of movement. 
		if step == "Right": #updating the direction with respect to the direction of motion choosen.
			x[i] = x[i - 1] + 1
			y[i] = y[i - 1] 
		elif step == "Left": 
			x[i] = x[i - 1] - 1
			y[i] = y[i - 1] 
		elif step == "Up": 
			x[i] = x[i - 1] 
			y[i] = y[i - 1] + 1
		else: 
			x[i] = x[i - 1] 
			y[i] = y[i - 1] - 1
	return x, y

def main():

    NUM_DATAPOINTS = 10000
    # define the form layout
    layout = [[sg.Text('Animated 2D Random Walk', size=(40, 1),
                justification='center', font='Helvetica 16')],
              [sg.Canvas(size=(640, 640), key='-CANVAS-')],
              [sg.Button('Exit', size=(10, 1), pad=((280, 0), 3), font='Helvetica 12')]]

    # create the form and show it without the plot
    window = sg.Window('Animated RandomWalk In PySimpleGUI',
                layout, finalize=True)

    canvas_elem = window['-CANVAS-']
    canvas = canvas_elem.TKCanvas

    # draw the initial plot in the window
    x=[]
    y=[]
    fig = Figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    fig_agg = draw_figure(canvas, fig)
    # make two vectors of random walk data points
    x, y = randwalk(NUM_DATAPOINTS)

    for i in range(len(y)):

        event, values = window.read(timeout=10)
        if event in ('Exit', None):
            exit(1)
        ax.cla() # clear the subplot
        ax.plot(x[0:i], y[0:i],  color='red')
        ax.set_title(r'step:%d'%i)
        fig_agg.draw()

    window.close()

if __name__ == '__main__':
    main()
