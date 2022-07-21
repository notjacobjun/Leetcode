"""
You were able to do this all by yourself! 8/10!
Obser:
- Using a trie would be best for this use case, since there is the . that we have to wildcard match for
- The only downside is the large space complexity
- Need to mark when it is the end of a word for each node

- Search with a trie takes O(m * n) time, where m is the length of the key
- addWord takes O(m) time
The main con is the large amount of storage that it takes

Hash map with keys as the length of the string and values as a list of strings entered with that length
- Adding word is simple
- searching for word would be finding the list of that size then removing all chars in the ith positions, where i is wherever there is a . in the
query word. So for each string entered into the dictionary so far go through each string to check for equality
- addWord takes O(1) time, where m is the length of the word 
- search takes O(n * m^2), where n is the size of words stored in the list (len(wordsEntered)) and m is the len of the largest string entered
Space O(n)

Trie:
- Entered the words as you would enter them into a normal trie (making sure that we mark which nodes represent the end of an entered word)
- search is same as normal trie but if we have a wildcard then we have to try all the child letters from the current node (which can be very time intensive
if our trie contains a lot of nodes)
addWord takes O(m)
search takes O(26^n) time in the worst case
Space: O(n * m)

Hash set with brute force search algorithm:
- Interal storage is a hash set
- For searching if there are any wildcards then iterate through all permutations with each wildcard trying to replace by all 26 chars, and check if there
is a hash-match in the hash set
Search still takes O(26^n) because we can have nearly all wildcards for a search query
add takes O(1)
Space: O(n)
"""


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node, n = self.root, len(word) - 1
        for i, ch in enumerate(word):
            # if the letter isn't already in the current TrieNode then add it
            if ch not in node.children:
                node.children[ch] = TrieNode()

            # update the current node reference
            node = node.children[ch]

            # check if we have reached the end of the word and if necessary update the current node's is_word attribute
            if i == n:
                node.is_word = True

    def search(self, word: str) -> bool:

        # define a quick dfs helper method
        def dfs(idx, node):
            n = len(word) - 1
            for i in range(idx, len(word)):
                ch = word[i]
                # wildcard case: try searching all the children nodes with the remaining letters
                if ch == '.':
                    for child in node.children.values():
                        # TODO need to define a helper method because this needs to update the node reference in each case
                        if dfs(i + 1, child):
                            return True
                    # if we iterate through all the children and still can't find a path then return false
                    return False

                # base case (failure case)
                if ch not in node.children:
                    return False

                # update the trie node reference
                node = node.children[ch]

            # once we have iterated through all that chars in the query word then return whether we have reached a TrieNode that was previously marked as the end of a word or not
            return node.is_word

        # call our dfs helper function
        return dfs(0, self.root)

# working implementation using dictionary but too slow for search
# class WordDictionary:

#     def __init__(self):
#         # key=> len(word): int    value=> set of words of size len(word): set()
#         self.words = {}

#     def addWord(self, word: str) -> None:
#         # insert the word into the respective bucket
#         if len(word) in self.words:
#             self.words[len(word)].add(word)
#         else:
#             self.words[len(word)] = set()
#             self.words[len(word)].add(word)

#     def search(self, word: str) -> bool:
#         # find all the indices of the wildcards in the query string
#         wildcards = [i for i, ch in enumerate(word) if ch == '.']

#         # go through the list of stored words to find out if pattern matches
#         words_bucket = self.words.get(len(word), {})
#         mod_words_bucket = set()
#         for temp in words_bucket:
#             # replace all the chars in the respective indices where the wildcards were for all the words in the list
#             for idx in wildcards:
#                 temp = temp[:idx] + '.' + temp[idx + 1:]
#             mod_words_bucket.add(temp)

#         # check for contains
#         return word in mod_words_bucket
