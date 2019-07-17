# Scrollable Graph in Bokeh library using CustomJS
**Bokeh** library in python is a very powerful library for creating interactive graphs. But, while exporting graphs with large amount of data to html, it creates very clustered graphs making it hard to understand. Consider the following example:

    # Import the required libraries
    from bokeh.plotting import figure, show, output_file
    from bokeh.transform import dodge
    # Define the output HTML file         
    output_file('vbar.html')
    # Define x-axis values
    x=['1996-11-01','1996-11-02','1996-11-03','1996-11-04','1996-11-05','1996-11-06',
    '1996-11-07','1996-11-08','1996-11-09','1996-11-10','1996-11-11']
    # Define the top of each bar
    top=[1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,10.1,11.2]
    # Create a figure object
    p = figure(x_range=x,plot_width=500, plot_height=400)
    # Create a bar graph
    p.vbar(x=x, width=0.5, bottom=0, top=top, color="firebrick")
    # Show the graph
    show(p)
	
This gives a very clustered graph:

![](/media/clusteredGraph.png)

One solution to this is create a scrollable graph using the sliders provided by Bokeh library and CustomJS.  This involves displaying a subset of data initially on the graph and then using the slider to display the next subsequent subset of data.  The slider can be used to move back and forth through tha data.

First,  we modify the figure object to display only 5 bars on the graph initially.

    p = figure(x_range=x[:5],plot_width=500, plot_height=400)

Then we define callable function as :

    callback = CustomJS(args=dict(fig=p, xr=renderers.data_source.data['x']), code="""
    	    var A = slider.value;
    	    fig.x_range.factors = [];
    	    for (i = A; i < A+5; i++) {
    	    	if (i>xr.length)
    	    		break;
    	      fig.x_range.factors.push(xr[i]);
    	    }
    	""")
		
It updates the current subset of data displayed according to the slider value.

At last, we create the slider object and show the graph and slider as columns.

    p.x_range.js_on_change('factors', callback)
    slider = Slider(start=0, end=1 + (len(x)-6)  , value=0, callback=callback)
    callback.args["slider"] = slider
    show(column(p,slider))
	
This gives the final result as:

![](/media/scrollableGraph.gif)

For the full code please refer here.
