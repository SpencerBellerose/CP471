#lexer
#reference https://medium.com/@pythonmembers.club/building-a-lexer-in-python-a-tutorial-3b6de161fe84


#inputs: test_string - a string of code to tokenize
def lex(test_string):
    symbols = [ #formatted for readability
    '#', '<', '>',
    '+', '-', '*',
    '%','/', '{',
    '}', '[', ']',
    '"', "'", '=',
    '(', ')', ':',
    ';', '.', ','
    ] #greater than or equal to error

    keywords = [
    'not', 'if', 'else',
    'elif', 'and', 'func',
    'for', 'TRUE', 'FALSE',
    'while', 'or', 'NONE',
    'int', 'string', 'double',
    'char', 'equals'
    ]

    lexemes = []

    all = symbols + keywords

    whitespace = ' '
    lexeme = ''

    for i, char in enumerate(test_string):

        if char != whitespace:
            lexeme += char #adds 1 char at a time

        if (i+1 < len(test_string)): #error handling
            if test_string[i+1] == whitespace or test_string[i+1] in all or lexeme in all: #if next character is whitespace
                if lexeme != '':
                    lexeme.replace('\n', '@new line@') #make new line character more visible
                    lexemes.append(lexeme)
                    lexeme = ''

    return lexemes

#test
test1 = """
func area_of_triangle(a, b, c) {
    # Initialize a,b,c
    int a = 1;
    int b = 2;
    int c = 3;
    double area = (a+b+c)/2;
    double area_final = sqrt(area*(area-a)*(area-b)*(area-c));
    return(area)
}
"""
print('Test 1: ', test1)
print()
print('now testing test 1:')
print()
test1 = lex(test1)
print(test1)
print("===============================================================================")

test2 = """
func addNums(a, b) {
		# Two numbers a and b are defined.
		int a = 2;
		int b = 6;
		int sum = a + b;
		return sum;
}
 """
print()
print()
print('Test 2: ', test2)
print()
print('now testing test 2:')
print()
test2 = lex(test2)
print(test2)
print("===============================================================================")
test3 = """
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
print()
print()
print('Test 3: ', test3)
print()
print()

print()
print('now testing test 3:')
print()
test3 = lex(test3)
print(test3)
print()
print("===============================================================================")
