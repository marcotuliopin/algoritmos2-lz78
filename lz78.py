from trie import Trie


def compress(input, output):
    """Create a file with a compressed version of an input text using LZ78."""
    with open(input, 'r') as inf, open(output, 'wb') as outf:
        dictionary = Trie()
        array = []
        char_size = 0

        while True:
            substring = find_new_substring(inf, dictionary)
            if not substring:
                break
            # add substring to the dictionary
            code = dictionary.insert(substring)
            #convert the code into its binary representation
            code = str(bin(code)[2:])
            # convert the char into its binary representation
            char = format(ord(substring[-1]), '08b')
            char_size = max(char_size, len(char))
            # add tuple to array
            array.append((code, char))

        code_size = dictionary.word_count.bit_length()
        # define number of bytes necessary to represent all code numbers
        code_size = code_size + 7
        code_size -= (code_size % 8)
        # define number of bytes necessary to represent all characters
        char_size = char_size + 7
        char_size -= (char_size % 8)
        # write the code and character size to output file
        coded_code_size = str(bin(code_size)[2:]).rjust(8, '0')
        coded_char_size = str(bin(char_size)[2:]).rjust(8, '0')
        write_bin(outf, coded_code_size + coded_char_size)
        # write encoded text to output file
        for tuple in array:
            coded_code = tuple[0].rjust(code_size, '0')
            coded_char = tuple[1].rjust(char_size, '0')
            write_bin(outf, coded_code + coded_char)


def decompress(input, output):
    """Create a file by decompressing an input file using LZ78."""
    dictionary = Trie()

    with open(input, 'rb') as inf, open(output, 'w') as outf:
        # read code and character size
        code_size = ord((inf.read(1)).decode('latin-1'))
        char_size = ord((inf.read(1)).decode('latin-1'))
        while True:
            # read code (node key on the dictionary)
            byte = inf.read(1)
            # check eof
            if not byte:
                break
            byte = ord(byte.decode('latin-1'))
            code = byte 
            for i in range(code_size // 8 - 1):
                byte = inf.read(1)
                byte = ord(byte.decode('latin-1'))
                # convert code from binary to integer
                code = (code << 8) + byte
            # read character to append
            byte = inf.read(1)
            # decode character
            byte = ord(byte.decode('latin-1'))
            char = byte
            for i in range(char_size // 8 - 1):
                byte = inf.read(1)
                byte = ord(byte.decode('latin-1'))
                # convert character from binary to integer
                char = (char << 8) + byte
            # convert integer into a unicode character
            char = chr(char) 

            # insert decoded word in the dictionary
            str = dictionary.search_by_code(int(code)) + char
            dictionary.insert(str)
            # print decoded word in the output file
            outf.write(str)


def find_new_substring(inf, dictionary):
    """Find substring in the file that is not in the dictionary."""
    substring = inf.read(1)
    if not substring:
        return ''
    while dictionary.search_by_word(substring):
        letter = inf.read(1)
        if not letter:
            break
        substring += letter
    return substring


def write_bin(outf, str):
    """Take a binary array and print it in an output file."""
    arr = bytearray()

    for i in range(0, len(str), 8):
        num = int(str[i: i+ 8], 2)
        arr.append(num)
    outf.write(arr)