Technical Guide
===============

There is one and only one main program called BodePlotFilter that is composed with a main programming structure that do the call for the particular libraries used and the functions.

Composition
-----------

BodePlotFilter Code structure and partial description:
	* Libraries:
		- Visa Library => this library managed the external instrumentation functionalities such as, recognition, read, write, etc.
		- Time Library => this library give us access to certain function used. In particular we used Sleep to give time while visa communicate with peripherals.
		- Tkinter Library => this library give us access to the GUI design and its different functionalities.
		- Matplotlib Library => this library was used to do the graphical representation of Bode plot.
		
	* Functions:
		- get_values => this functions collects all the information entered by the user in order of control the Function Generator.
		- send_cmds => this is the principal function where everything happens. It is in charge of manipulating the GUI and the peripheral elements. It managed Read and Write functions, buttons and graphs' plots. Only Pause and Close buttons are managed apart.
		- Pause => managed the button in charge of stopping the swept of frequencies used in Bode Plot.
		- Close => simple executes quit of the program and closes the window.
	
	* Main program:
		- Declaration/Initialization => this is where the generic variables are managed.
		- Window composition => establishment of the titles, fonts and window parameters.
		- GUI creation => structure of the window itself. How can we managed to manipulate the elements into the window.
		- Window elements creation => creation of buttons, radio buttons, text labels, and graph plot areas.
		- Window elements location => once elements are created we need to assign them around the window.

	