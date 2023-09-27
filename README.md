# Implementation of algorithm LZ78 for the Algorithms 2 course
------------------------------------------------------

## How to use

### Compression
``` console
python3 main.py -c [nome do arquivo de entrada] -o <nome do arquivo de saída>
```
### Decompression
```console
python3 main.py -x [nome do arquivo de entrada] -o <nome do arquivo de saída>
```

In both cases indicating the name of the output file is optional.

------------------------------------------------------

## Overview

In this practical work, we implemented a version of the ***LZ78 algorithm*** using the **Trie** data structure. The work in question was created in *Python3*, using the Linux Ubuntu operating system.

### Compression Implementation

For text file compression, we use a **dictionary** (implemented with a **Trie**) to store the substrings already seen in the text and we associate a unique code with each substring. Reading the file is done as follows: we go through the input file, character by character, and check if this substring is in the dictionary. If so, we add the next character from the file to the end of the substring and repeat the process **until we find a new substring**. When we do, we add it to the dictionary. For each added substring, we add a pair *(code, substring)* to a *vector v*.
At the end of reading, we **convert each pair to its binary representations** and write these representations to the output file.

### Decompression Implementation

Initially, we start a dictionary (implemented with a Trie), having only the node root, which has code 0 and an empty substring. When we receive a compressed file, we read the size of the codes and the size of the characters. After that, we read a code and convert it to an integer and read a character and convert it to a char (the compressed file will be written in the order character code). With this information, we search for the word corresponding to the code in the dictionary and add the read character to the end of it, writing the result in the output file. The new substring will also be added to the dictionary, and your code will be the number of words in the dictionary plus one. We repeat this process until the end of reading the compressed file.
