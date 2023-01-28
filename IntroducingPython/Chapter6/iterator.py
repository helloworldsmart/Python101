word = 'thud'
offset = 0
while offset < len(word):
    print(word[offset])
    offset += 1
print('---')

for letter in word:
    print(letter)
print('---')

for letter in word:
    if letter == 'u':
        break
    print(letter)
print('---')

for letter in word:
    if letter == 'x':
        print("Eek! An 'x'!")
        break
    print(letter)
else:
    print("No 'x' in there.")
