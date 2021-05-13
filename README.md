This is my lexer program for the final assignment submission. As you can see, given an input (currently given as a string), the lexer splits the text into proper tokens based on our specified language.

Ex. Given Strings

String 1:
"""
func area_of_triangle(a, b, c) {
    # Initialize a,b,c
    int a = 1;
    int b = 2;
    int c = 3;
    double area = (a+b+c)/2;
    double area_final = sqrt(area*(area-a)*(area-b)*(area-c));
    return(area)
}"""

OUTPUT:
['\nfunc', 'area_of_triangle', '(', 'a', ',', 'b', ',', 'c', ')', '{', '\n', '#', 'Initialize', 'a', ',', 'b', ',', 'c\n', 'int', 'a', '=', '1', ';', '\n', 'int', 'b', '=', '2', ';', '\n', 'int', 'c', '=', '3', ';', '\n', 'double', 'area', '=', '(', 'a', '+', 'b', '+', 'c', ')', '/', '2', ';', '\n', 'double', 'area_final', '=', 'sqrt', '(', 'area', '*', '(', 'area', '-', 'a', ')', '*', '(', 'area', '-', 'b', ')', '*', '(', 'area', '-', 'c', ')', ')', ';', '\n', 'return', '(', 'area', ')', '\n', '}']

String 2:
"""
func addNums(a, b) {
		# Two numbers a and b are defined.
		int a = 2;
		int b = 6;
		int sum = a + b;
		return sum;
}
 """
 
 OUTPUT:
 ['\nfunc', 'addNums', '(', 'a', ',', 'b', ')', '{', '\n\t\t', '#', 'Two', 'numbers', 'a', 'and', 'b', 'are', 'defined', '.', '\n\t\tint', 'a', '=', '2', ';', '\n\t\tint', 'b', '=', '6', ';', '\n\t\tint', 'sum', '=', 'a', '+', 'b', ';', '\n\t\treturn', 'sum', ';', '\n', '}', '\n']
 
String 3:
"""
 	func quadrantofCoords(x, y) {
		# x and y are a pair of coordinates (x,y)
int quadrant;
		if (x > 0 and y > 0) { # E.g., (1, 2){
			quadrant = 1;
        }
		elif (x < 0 and y > 0) { # E.g., (-1, 2){
			quadrant = 2;
        }
		elif (x > 0 and y < 0) { # E.g., (1, -2){
			quadrant = 4;
        }
        else { # Coordinate is origin
        	quadrant = 0;
        }
        return quadrant;
        }

"""

OUTPUT:
['\n', '\tfunc', 'quadrantofCoords', '(', 'x', ',', 'y', ')', '{', '\n\t\t', '#', 'x', 'and', 'y', 'are', 'a', 'pair', 'of', 'coordinates', '(', 'x', ',', 'y', ')', '\nint', 'quadrant', ';', '\n\t\tif', '(', 'x', '>', '0', 'and', 'y', '>', '0', ')', '{', '#', 'E', '.', 'g', '.', ',', '(', '1', ',', '2', ')', '{', '\n\t\t\tquadrant', '=', '1', ';', '\n', '}', '\n\t\telif', '(', 'x', '<', '0', 'and', 'y', '>', '0', ')', '{', '#', 'E', '.', 'g', '.', ',', '(', '-', '1', ',', '2', ')', '{', '\n\t\t\tquadrant', '=', '2', ';', '\n', '}', '\n\t\telif', '(', 'x', '>', '0', 'and', 'y', '<', '0', ')', '{', '#', 'E', '.', 'g', '.', ',', '(', '1', ',', '-', '2', ')', '{', '\n\t\t\tquadrant', '=', '4', ';', '\n', '}', '\n', 'else', '{', '#', 'Coordinate', 'is', 'or', 'igin\n', '\tquadrant', '=', '0', ';', '\n', '}', '\n', 'return', 'quadrant', ';', '\n', '}']
