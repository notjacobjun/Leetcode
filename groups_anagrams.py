"""
You did this all by yourself! 8/10 :)
Observ:
- Words are defined as words that are in the strs list

Brute force:
- For each word in strs, go through all the permutation of the letters and check if it is a word if so then insert it into the adjacency list 
node corresponding to that word (bidirectional relationship)

Keeping track of letter count
- K.I. Anagrams can be easily found by matching the letter counts for each word
- Go through the strs to produce the letter count for each word in the list
- Each word can be represented as a tuple (of size 26 where each num in the tuple corresponds to the letter count for that respective letter)
This way we can hash the tuples and check for duplicates in O(1)
Time: O(n * m), where n is the size of strs and m is the size of the largest str in the strs list
Space: O(n) b/c we are storing a tuple of size 26 for each word in the hashset
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initialize a dictionary for the different letter counts and corresponding words
        count_dict = {}
        for word in strs:
            # initialize an empty letter count for each word (start as list then change to tuple once done)
            temp_count = [0 for _ in range(26)]

            # produce the letter count for the current string
            for ch in word:
                idx = ord(ch) - 97
                temp_count[idx] += 1
            
            # convert the letter count to tuple
            letter_count = tuple(temp_count)
            if not letter_count in count_dict:
                count_dict[letter_count] = []
            count_dict.get(letter_count).append(word)
        
        # get the result from all the letter_counts
        return count_dict.values()
        