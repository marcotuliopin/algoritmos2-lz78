from sys import argv
import lz78

def main():
    input = argv[2]
    
    if argv[1] == '-c':
        if len(argv) == 5:
            output = argv[4]
        else:
            output = input[:-3] + 'z78'
        lz78.compress(input, output)
    else:
        if len(argv) == 5:
            output = argv[4]
        else:
            output = input[:-3] + 'txt'
        lz78.decompress(input, output)


if __name__ == '__main__':
    main()