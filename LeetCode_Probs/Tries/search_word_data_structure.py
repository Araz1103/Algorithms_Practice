"""
Design a data structure that supports adding new words and searching for existing words.

Implement the WordDictionary class:

void addWord(word) Adds word to the data structure.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. 
word may contain dots '.' where dots can be matched with any letter.
Example 1:

Input:
["WordDictionary", "addWord", "day", "addWord", "bay", "addWord", "may", "search", "say", "search", "day", "search", ".ay", "search", "b.."]

Output:
[null, null, null, null, false, true, true, true]

Explanation:
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("day");
wordDictionary.addWord("bay");
wordDictionary.addWord("may");
wordDictionary.search("say"); // return false
wordDictionary.search("day"); // return true
wordDictionary.search(".ay"); // return true
wordDictionary.search("b.."); // return true
Constraints:

1 <= word.length <= 20
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.

"""

# Time Complexity
# To insert words, each letter can be inserted in O(1)
# So for n letters, it is O(N), n is length of word, #letters

# The time complexity of the search function in the presence of wildcard characters is influenced by 
# both the number of wildcards and the length of the word. 
# Specifically, for m wildchards the function may need to explore up to 26^m different branches, 
# each requiring a traversal of up to n nodes, leading to a worst-case time complexity of O(26^m×n)
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



        
