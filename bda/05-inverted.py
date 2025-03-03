# Mapper.py 
import sys 
def mapper(): 
    for line in sys.stdin: 
        line = line.strip() 
        document, words = line.split(" ", 1) 
        word_list = words.split() 
        for word in word_list: 
            print(f"{word}\t{document}") 
 
if __name__ == "__main__": 
    mapper() 

# Reducer.py 
import sys 
 
def reducer(): 
    current_word = None 
    doc_list = [] 
 
    for line in sys.stdin: 
        line = line.strip() 
        word, document = line.split("\t", 1) 
 
        if current_word == word: 
            doc_list.append(document) 
        else: 
            if current_word: 
                print(f"{current_word}\t{', '.join(set(doc_list))}") 
            doc_list = [document] 
            current_word = word 
 
    if current_word: 
        print(f"{current_word}\t{', '.join(set(doc_list))}") 
 
if __name__ == "__main__": 
    reducer() 
    
    
"""    
Input.txt 
 
doc1 apple banana 
doc2 banana orange 
doc3 apple mango 
doc4 banana apple
"""