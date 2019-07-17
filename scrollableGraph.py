# Import the required libraries
from bokeh.plotting import figure, show, output_file
from bokeh.transform import dodge
from bokeh.models import Slider, CustomJS
from bokeh.layouts import column
# Define the output HTML file         
output_file('vbar.html')
# Define x-axis values
x=['1996-11-01','1996-11-02','1996-11-03','1996-11-04',
'1996-11-05','1996-11-06','1996-11-07','1996-11-08','1996-11-09','1996-11-10','1996-11-11']
# Define the top of each bar
top=[1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,10.1,11.2]
# Create a figure object
p = figure(x_range=x[:5],plot_width=500, plot_height=400)
# Create a bar graph
renderers = p.vbar(x=x, width=0.5, bottom=0, top=top, color="firebrick")
callback = CustomJS(args=dict(fig=p, xr=renderers.data_source.data['x']), code="""
	    var A = slider.value;
	    fig.x_range.factors = [];
	    for (i = A; i < A+5; i++) {
	    	if (i>xr.length)
	    		break;
	      fig.x_range.factors.push(xr[i]);
	    }
	""")
p.x_range.js_on_change('factors', callback)
slider = Slider(start=0, end=1 + (len(x)-6)  , value=0, callback=callback)
callback.args["slider"] = slider
# Show the graph
show(column(p,slider))
