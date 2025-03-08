class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
class WordDictionary:

    def __init__(self):
        self.trie_root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr_node = self.trie_root
        for letter in word:
            if letter not in curr_node.children:
                curr_node.children[letter] = TrieNode()
            curr_node = curr_node.children[letter]
        curr_node.is_word = True

    def search(self, word: str) -> bool:
        # If letter is '.', we need to check in every letter's children
        # Recursive function which can backtrack and check

        def check_letter(word_index, curr_node):
            # Base Case
            if word_index >= len(word):
                return curr_node.is_word #Reached End of Word, so just return if there is a word here

            # If curr node has no children here, return False
            if not len(curr_node.children):
                return False

            letter = word[word_index]
            if letter!=".":
                if letter not in curr_node.children:
                    return False #Cannot proceed further, we know won't be present
                else:
                    # Check ahead
                    return check_letter(word_index + 1, curr_node.children[letter])

            else: 
                # With dot, we have to check @every child ahead
                # If any of them true, we return that, else False
                for child in curr_node.children:
                    if check_letter(word_index + 1, curr_node.children[child]):
                        return True
                return False #None of them have the word ahead

        return check_letter(0, self.trie_root)



        
