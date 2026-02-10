'''phrase="She sells,sea shells on the sea shore.sea shells on the sea shore are really beautiful"
words=phrase.lower().replace('.','').replace(',','').split( )
unique_words={x  for x in words }
print(words)'''
phrase = "the cat is in the hut.The bug is under the table.You must buy a pair of nwe shoes before the annual day"
words = phrase.lower().replace(',', '').replace('.', ' ').split()
unique_word = {i for i in words if len(i) < 3}
print(unique_word)


