# Calculator
Simple python calculator with tkinter gui, supporting the four elementary operations +, -, x, /, decimal and negative numbers, parenthesis and order of operations. Execute main.py to use it.
main.py creates the gui. You can type mathematical expression using buttons, or by writing directly in the screen entry. Negative numbers are marked by the underscore symbol '_', to distinguish it from subtraction, marked by '-'. Multiplication is done with the 'x' symbol, others like '*' are not recognized. The '=' button calls compute.py to compute the mathematical expression on screen.
compute.py contains a function that takes a string, and if it is a valid mathematical expression, returns its result as a string, making use of regular expressions and recursion.
