class TrieNode:
    """A node in the trie object.

    Attributes:
        number : int
            the number of the node.
        data : str 
            the string stored in the node (default None).
        end : int
            the number of strings that end in the node.
        next : dict 
            the child nodes of the node.
        parent : TrieNode
            pointer to the parent node.
    """

    def __init__(self, _parent, _code = 0, _data = None):
        self.code = _code 
        self.data = _data
        self.end = 0
        self.next = {} 
        self.parent = _parent


class Trie:
    """The trie structure.

    Attributes:
        top : TrieNode
            the root of the trie.
        norm : char
            the index norm (default 'a').
        node_count : int
            number of nodes in the trie.
        adresses : dict
            adresses to the nodes based on their codes.
    """
    def __init__(self, norm = 'a'):
        self.top = TrieNode(_parent = None, _code = 0)
        self.norm = norm 
        self.node_count = 0
        self.word_count = 0
        self.adresses = {0 : self.top}


    def insert(self, word, start = None):
        """Insert string into the radix trie."""
        # define initial lookup node (default self.top)
        crawler = start
        if start == None:
            crawler = self.top

        for i in range(len(word)):
            # define lookup key in the dictionary
            index = ord(word[i]) - ord(self.norm)

            if not index in crawler.next:
                # if the key is not in the dictionary, create new node
                return self.__add_node(word[i:], index, crawler)
            else: 
                parent = crawler
                crawler = crawler.next[index]
        return parent.code
        

    def remove(self, target):
        """Remove string from the radix trie."""
        node_parent, index = self.__search(target)
        node = node_parent.next[index]

        if node.next == []:
            node_parent.remove(node)
        else:
            node.end -= 1
    

    def search_by_word(self, word):
        """Search string in the radix trie"""
        crawler = self.top

        for i in range(len(word)):
            # define lookup key in the dictionary
            index = ord(word[i]) - ord(self.norm)
            if not index in crawler.next:
                # if string is not it the trie
                return 0
            crawler = crawler.next[index]
        return crawler.code


    def search_by_code(self, code):
        """Search a node by its code."""
        if not code in self.adresses:
            return ''

        word = ''
        node = self.adresses[code]

        while node != self.top:
            word = node.data + word
            node = node.parent

        return word


    def __add_node(self, word, index, current_node):
        """Add node to the trie."""
        self.word_count += 1
        parent_node = current_node
        for i in range(len(word)):
            # create new node
            self.node_count += 1
            new_node = TrieNode(_parent = current_node, _data = word[i])
            # add new node to the trie
            current_node.next[index] = new_node 
            # go to next node
            parent_node = current_node
            current_node = current_node.next[index]
        current_node.code = self.word_count
        current_node.end += 1
        # add node adress to dictionary of adresses
        self.adresses[current_node.code] = current_node
        return parent_node.code