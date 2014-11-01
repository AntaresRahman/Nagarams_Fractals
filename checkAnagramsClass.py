#Antares Rahman
#Nov 22, 2013
#Class for checking for anagrams of a word

class checkAnagrams:

    """This class is a string object lowercased.
    It has three methods: anagrams(), dictWords(), binarySearch() and screenResults()"""
    def __init__(self, s):
        self.s = s.lower() #string s in lowercase

    def anagrams(self, s):
        """checks for all possible combinations of characters in a given string recursively.
        returns a list of all possible anagrams of the string"""
        if s == "": #base case for recursion; empty string
            return [s] #return empty string
        else: #recursive case; non-empty string
            ans = [] #initiate list
            for w in self.anagrams(s[1:]): #loop through each character in s, except the 1st
                for pos in range(len(w)+1): #loop through the list a number of times = length of list w + 1
                    #concatenate various combinations of the characters as strings
                    #append these strings to the list ans
                    ans.append(w[:pos]+s[0]+w[pos:])
            return ans #return the list of all possible combinations of characters in a string

    def dictWords(self):
        """reads a list of words from an English dictionary"""
        dictionary = open("2of12.txt", "r") #opens a file containing words from an english dictionary
        readWords = dictionary.read() #a string of all the words in the dictionary
        words = readWords.split() #a list of strings of all the words in the dictionary
        return words
        
    def binarySearch(self, words, s):
        """uses binary search recursively to check if the words in the list of anagrams are English words.
        Creates a list of anagrams that are English words. returns this new list."""
        if len(words) == 0: #base case for empty list of words
            return self.anagramWords #returns list of anagrams that are English words
        else:
            mid = len(words)//2 #subsequently divide the dictionary list into halves
            if words[mid] == self.w: #the middle dictionary word in the list matches with anagram word
                self.anagramWords.append(self.w)
            elif words[mid]>self.w: #the middle dictionary word in the list comes alphabetically after the anagram word
                return self.binarySearch(words[:mid],self.w)
            else: #the middle dictionary word in the list comes alphabetically before the anagram word
                return self.binarySearch(words[mid+1:],self.w)

    def screenResults(self):
        """screens out any word that is appearing more than once in the list of anagram words by making a new list.
        returns this new list of words with each word only occuring once in the list."""
        words1 = self.dictWords()
        wordList = self.anagrams(self.s) #return the list of all possible combinations of characters in string s
        #make a list of all possible anagrams
        self.anagramWords = [] #initiate list        
        for self.w in wordList:
            self.binarySearch(words1, self.s)
        #screen out outputs that occur several times
        screenWords = [] #initiate another list
        for w in self.anagramWords: #loop through the list of words in anagramWords
            if w not in screenWords: #if the word is not yet in screenWords list
                screenWords.append(w) #append word to the screenWords list
        return screenWords
        
def main():
    word = "OptIoN"
    text = checkAnagrams(word)  
    print(text.anagrams("aBc"))
        #expected output:
            #['aBc', 'Bac', 'Bca', 'acB', 'caB', 'cBa']
    print(text.screenResults())
        ##expected intermediate process:
            #anagramWords = ['option', 'potion', 'option', 'potion']
            #screenWords = ['option', 'potion']
        #expected final output:
            #option
            #potion

if __name__ == "__main__":
    main()
