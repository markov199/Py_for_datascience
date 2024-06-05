import sys
from string import punctuation 

def count_text(text: str):
    chars = len(text)
    upper = 0
    lower = 0
    punct = 0
    spaces = 0
    num	= 0
    print(f"The text contains {chars} characters:")
    for x in text:
        if x.isupper():
            upper += 1
        elif x.islower():
            lower += 1
        elif x in punctuation:
            punct += 1
        elif x.isspace:
            spaces += 1
        elif x.isdigit:
              num += 1
    print(f"{upper} upper letters\n{lower} lower letters\n{punct} punctuation marks\n{spaces} spaces\n{num} digits")		
    
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
