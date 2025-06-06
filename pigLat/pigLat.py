# English to Pig Latin

message = input("Enter a message to convert to Pig Latin: ")
pigLatin = []

VOWELS = "aeiouy"
for word in message.split():
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
        
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue
        
    suffixNonLetters = ''
    while len(word) > 0 and not word[-1].isalpha():
        suffixNonLetters = word[-1] + suffixNonLetters
        word = word[:-1]
        
    isWordUpper = word.isupper()
    isWordTitle = word.istitle()
    
    word = word.lower()
    prefixConsonants = ''
    while len(word) > 0 and word[0] not in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]
        
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'
        
    if isWordUpper:
        word = word.upper()
    
    if isWordTitle:
        word = word.title()
        
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)
    
print(' '.join(pigLatin))
        
    
