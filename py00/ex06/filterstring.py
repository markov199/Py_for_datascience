from ft_filter import ft_filter
import sys

def main():
    try:
        args_count = len(sys.argv)
        assert args_count == 3, "The arguments are bad"
        assert type(sys.argv[1]) is str, "The first argument needs to be a string"
        try:
            number = int(sys.argv[2])
        except ValueError:
            raise AssertionError("Second argument has to be an integer")
        words = sys.argv[1].split()
        f = lambda x:len(x) >= number
        filtered_words = [x for x in words if f(x)]
        print(filtered_words) 
    except AssertionError as msg:
         print("AssertionError:", msg)
    except Exception as e:
          print(type(e).__name__ + ":", e)
          
if __name__ == "__main__":
	    main()
    
""" 
https://www.quora.com/How-do-you-approach-list-comprehension-with-lambda-Python-lambda-list-comprehension-development
https://stackoverflow.com/questions/6076270/lambda-function-in-list-comprehensions
""" 




