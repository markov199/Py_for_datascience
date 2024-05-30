import sys
from string import whitespace 
from string import punctuation 
from string import ascii_lowercase 
from string import ascii_uppercase
from string import digits 

def count_text(text: str):
    i = len(text)
    upper = 0
    lower = 0
    punct = 0
    spaces = 0
    num	= 0
    print(f"The text contains {i} characters:")
    for x in text:
	    if x in ascii_uppercase:
		    upper += 1
		elif x in ascii_lowercase:
		    lower += 1
	    elif x in punctuation:
		    punct += 1

		
    
def main():
	try:
		y = len(sys.argv)
		assert y <= 2, "more than one argument is provided"
		if y == 1:
			text = input("What is the text to count?")
		else:
			text = sys.argv[1]
		count_text(text)
	except AssertionError as msg:
		print("AssertionError:", msg)

        
	
        

    
if __name__ == "__main__":
	main()
