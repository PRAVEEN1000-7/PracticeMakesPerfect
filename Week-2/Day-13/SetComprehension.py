# Q : Set comprehension: extract unique vowels from a sentence.

sentence = "Apple is a fruit"
unique_vowel = { x for x in sentence if x in "aeiou"}
print(unique_vowel)