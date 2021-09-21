print("name: sandeep chouhan")
print("scholar no: 30203")
import re
quote=input('Enter the quote: ')
word=input('Enter the word: ')
num_occurence=len(re.findall(word,quote))
print("Number of occurences of "+word+" in '"+quote+"' are:")
print(num_occurence)
