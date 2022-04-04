from PyDictionary import PyDictionary

#dictionary object
dic = PyDictionary()

#take word input
search = input('Enter the word you want the meaning : ')

#display meaning

result = dic.meaning(search)
for i in result:
    print(f'{i} : {result[i]}')
    print('\n')