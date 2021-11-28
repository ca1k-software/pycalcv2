[Calculator developed by CA1K @ ca1k.xkotto.com] (3/2/2019) (Edited 10/26/21)

[2021]

*Statistical calculator added
	*Save/Load feature
		*merges the x and y plot arrays, and saves the raw array to a
		text file, ideally (.txt)
		*upon loading, the program splits the saved array in two via
		cloning said array and removing the contents on the first
		and midpoint
	*Mean/Median/Mode feature
	*Save directory feature
		*change save name and directory with the "File" button

*Graphing calculator modified
	*y graphing added
	*derivative function added
		*called df(func,var) or df(func,var,base) for functions needing a base
		*does NOT work with polynomials
	*log function fixed, returns 0 at negative inputs
	*graph plots 0 at any NaN values

*main menu modified
	*picture added

{New accepted inputs}
"+", "-", "*" (times), "/" (divided by), "**" (power to), "%" (modulus), "x", "sin()",
"cos()", "tan()", "arcsin()", "arccos()", "arctan()", "sinh()", "cosh()", "tanh()",
"floor()", "ceil()", "log()", "sqrt()", "fix()", "sinc()", "arcsinh()", "arccosh()"
"e" (= 2.718281828...), "PI" (= 3.14159...), "arctan()", "df()", "pow()", "y", "abs()"

*Don't input both x and y

As a word of advice, don't run this on a later python version than 3.9.0. As of right now,
the graphing library has not caught up. Speaking of the library, I've tried to find others
that could be compatible with tkinter and surprisingly, only matplotlib works.

For anyone looking to graph (with the library in your own code) on whichever axis you prefer,
make sure the plot arrays are global and not returned by a method.

I also discovered that the library will plot letters if you let it. Use this information 
however you want. Also, the plots wont make sense if the arrays aren't global, and
will plot in chronological/index order of data appended.

Thanks for your interest in this project, I encorage you to build on it more like I have

[2019]

Greetings. I'm glad you decided to give my calculator a try.
The calculator is written in python and open source, so feel free to hack
into it and develop upon it yourself. I intend for it to always be open source since
it's just a portfolio piece for me, so I won't mind if anyone rips it off.

There is also some documentation on the source code to help you understand
and build upon the calculator yourself.

<Features>

The calculator folder comes with 2 calculators, both of which can switch between each
other. I recommend that you only open "__main__" as it provides an opening GUI that lets
you choose between the two.

--------------------------
The scientific calculator:
--------------------------

The scientific calculator that comes with the calculator folder is capable of many
algebraic and trigonometric functions. It can convert degrees to radians, vice versa,
do simple arithmetic, do trigonometric functions like sine, convert a value to its
reciprocal, etc.

------------------------
The graphing calculator:
------------------------

The graphing calculator is self explanitory; it graphs the function you enter into the
text box below the graph. You can zoom in on a specific part of the graph, save the graph,
switch views, pull up previous functions that were entered in before, etc. Uses the
matplotlib library along with numpy.

<Instructions for the graphing calculator>

-------
Basics:
-------

The graphing calculator graphs a function based off of the x-axis. The y-axis will
represent the functions return on the x-axis value based on what is done to the
variable "x" in your function. The text box in the window will be the place to enter
your mathematical function. The function you put in must be typed out like this:

2 * x, 2 ** x (2 pow x), sin(x), 2 * (x+2), etc...

After you are finished with your function, simply click on the "Graph" button below it
to plot the function.

-------------------------------
Referencing previous functions:
-------------------------------

In the case you want to graph a previous function you entered in before, click on the
"Previous Functions..." button. Another window will pop up with a combolist prompting you
to select from an array of functions you previously entered before. Once you have made your
choice, click "OK" and the graph along with the text box will update to your chosen
function.

-------------------------------------------------------
Regarding the menu bar to the bottom of the calculator:
-------------------------------------------------------

The menu bar belongs to a python library known as matplotlib. Should you ever have the
curiosity for a deeper understanding of the library, refer to the documentation on the
official site as it is most likely the most appropriate source of information for the
subject. Here's a couple links to give you a good start:

https://matplotlib.org/
https://matplotlib.org/users/navigation_toolbar.html

=============
!!IMPORTANT!!
=============

---------------------------------
Regarding the input in the entry:
---------------------------------

Be careful about the operators and words you use in your function. The evaluation method
in python responsible for plotting on the y-axis is very picky about what it will consider
in its calculations. For your convenience I will provide a list of accepted operators and 
keywords to incorporate into your function.

{Accepted inputs}
"+", "-", "*" (times), "/" (divided by), "**" (power to), "%" (modulus), "x", "sin()",
"cos()", "tan()", "arcsin()", "arccos()", "arctan()", "sinh()", "cosh()", "tanh()",
"floor()", "ceil()", "log()", "log2()", "log10()", "sqrt()", "fix()", 
"e" (= 2.718281828...), "PI" (= 3.14159...)

------------------------------------------------------------
Regarding the necessary resources for the calculator to use:
------------------------------------------------------------

Unfortunately, python itself cannot accomplish all the tasks that this calculator demands
without the extra help of a couple libraries. This may require you to do a few
installations through the command prompt (or terminal).

Here is a list of the required libraries to make things easier for you:
-matplotlib
-numpy

If you are new to python, then you should know that if you have python installed in your
PATH directory, you can use an application called "pip" to install external libraries for
python. To do so, type in the following:

"pip install matplotlib"
"pip install numpy"

*Dont run this on Python 3.10  .

<Footer>

Thank you for using this python application I put together. Hope you get the most of it.

If you notice any bugs/issues/errors in the calculator, contact "ca1ksoftware@gmail.com".
 
 