# ask for user input
print('Do you want to convert Unicode or ASCII?')


def get_input():
    global mode
    global ascii
    global unicode
    global inputrecieved
    # receive input
    mode = input()
    # check which way the conversion should run
    if mode == 'ASCII' or mode == 'ascii':
        # request string
        print('please input an ASCII string')
        ascii = input()
        # allow code to progress
        inputrecieved = True
    elif mode == 'unicode' or mode == 'Unicode':
        # request string
        print('please input a unicode string with spaces between characters')
        unicode = input()
        # allow code to progress
        inputrecieved = True
    else:
        return


def use_input():
    global mode
    global ascii
    global unicode
    global complete
    # check which way the conversion should run
    if mode == 'ASCII' or mode == 'ascii':
        for character in ascii:
            # check if input is valid ascii character
            if not character.isascii():
                print('Invalid input')
                return
            else:
                # separate out characters in order
                seprate.append(character)
        for part in seprate:
            # convert characters to unicode
            value = ord(part)
            # convert integers to strings
            word = str(value)
            newseprate.append(word)
        # combine and display new string
        ascresult = ''.join(newseprate)
        print('Your converted string is:')
        print(ascresult)
    elif mode == 'unicode' or mode == 'Unicode':
        characters = unicode.split()
        for number in characters:
            value = int(number)
            # check if input corresponds to an ASCII character
            if value > 127 or value < 1:
                print('Invalid input')
                return
            else:
                # separate out characters in order
                seprate.append(value)
        for digit in seprate:
            # convert characters to ascii
            newseprate.append(chr(digit))
        # combine and display new string
        unresult = ''.join(newseprate)
        print('Your converted string is:')
        print(unresult)



seprate = []
newseprate = []
mode = ''
ascii = ''
unicode = ''
inputrecieved = False


# prevent code from progressing until a conversion direction is selected
while not inputrecieved:
    get_input()
# convert input
use_input()

