# Calculator
Python calculator with tkinter GUI that supports the four basic operations +, -, x, /, decimal and negative numbers, parenthesis, and order of operations. Execute main.py to use it.

main.py creates the GUI. You can type mathematical expressions using buttons or by writing directly in the screen entry. To distinguish them from subtraction, negative numbers are denoted by the underscore symbol _. Multiplication is done with the 'x' symbol, others like '*' are not recognized. The '=' button calls compute.py to compute the mathematical expression on screen.

compute.py contains a function that takes a string, and if it is a valid mathematical expression, it returns its result as a string, making use of regular expressions and recursion.
