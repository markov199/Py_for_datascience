import sys
def to_morse(string)-> str:  

    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                        'C':'-.-.', 'D':'-..', 'E':'.',
                        'F':'..-.', 'G':'--.', 'H':'....',
                        'I':'..', 'J':'.---', 'K':'-.-',
                        'L':'.-..', 'M':'--', 'N':'-.',
                        'O':'---', 'P':'.--.', 'Q':'--.-',
                        'R':'.-.', 'S':'...', 'T':'-',
                        'U':'..-', 'V':'...-', 'W':'.--',
                        'X':'-..-', 'Y':'-.--', 'Z':'--..',
                        '1':'.----', '2':'..---', '3':'...--',
                        '4':'....-', '5':'.....', '6':'-....',
                        '7':'--...', '8':'---..', '9':'----.',
                        '0':'-----', ' ':'\\'}
    
    text = string.upper()
    morse_string = ""
    for i in range(len(text)):
        morse_string = morse_string + MORSE_CODE_DICT[text[i]]  + " "
    new_str = morse_string.rstrip()
    return (new_str)

def main():
    args_count = len(sys.argv)
    text = sys.argv[1]
    try:
        assert args_count == 2, "The arguments are bad"
        for x in text:
            if not (x.isalpha() or x.isspace()):
                raise AssertionError("The arguments are bad")
        print(to_morse(text))
    except AssertionError as msg:
        print(msg)
    except Exception as e:
        print(type(e).__name__ + ":" , e)



if __name__ == "__main__":
    main()
