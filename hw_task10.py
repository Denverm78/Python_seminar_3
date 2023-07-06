# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку.

with open ('granatovy_braslet.txt') as f:
    book_split = f.read().lower().replace("?", "").replace(",", "").replace("-", "").replace(".", "").\
        replace("—", "").replace(":", "").replace("!", "").split()
        
book_dict = {}
book_set = set(book_split)
for i in book_set:
    if (i not in book_dict.keys() and i.isalpha()):
        book_dict[i] = book_split.count(i)
    
sorted_dict = {}
sorted_keys = sorted(book_dict, key=book_dict.get, reverse=True)  
for i in sorted_keys:
    sorted_dict[i] = book_dict[i]

print("Десять самых частых слов в тексте:")
NUMBER_FOR_PRINT = 10
NUMBER_CHAR_IN_WORD = 5 # Будем считать, что слово - от 5 букв, а остальные предлоги, местоимения и т.д.
count = 0
for key in sorted_dict:
    if count < NUMBER_FOR_PRINT:
        if(len(key) >= NUMBER_CHAR_IN_WORD): 
            print (f'{count+1}. Слово "{key}" повторяется в тексте {sorted_dict[key]} раз')
            count += 1
print()
    




 