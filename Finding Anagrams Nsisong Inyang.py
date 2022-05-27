def find_anagrams(word, anagram):
    if len(word) != len(anagram):
      return False

    word = sorted(word)
    anagram = sorted(anagram)
   
    return word==anagram

word = input("Enter word: ")
anagram = input("Enter anagram: ")
print(find_anagrams(word, anagram))

 