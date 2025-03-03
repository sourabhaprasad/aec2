# mapper
import sys

def mapper():
    for line in sys.stdin:
        line = line.strip()
        doc, *words = line.split()
        for word in words:
            print(f"{word}\t{doc}")

if __name__ == "__main__":
    mapper()


# reducer
import sys

def reducer():
    current_word, doc_list = None, set()

    for line in sys.stdin:
        word, doc = line.strip().split("\t")

        if word == current_word:
            doc_list.add(doc)
        else:
            if current_word:
                print(f"{current_word}: {', '.join(sorted(doc_list))}")
            current_word, doc_list = word, {doc}

    if current_word:
        print(f"{current_word}: {', '.join(sorted(doc_list))}")

if __name__ == "__main__":
    reducer()
    
# ------------------------------------------------------------
# # input.txt
# doc1 apple banana
# doc2 banana orange
# doc3 apple mango
# doc4 banana apple

# # mapper output , reducer input
# apple	doc1
# apple	doc3
# apple	doc4
# banana	doc1
# banana	doc2
# banana	doc4
# mango	doc3
# orange	doc2

# # reducer output
# apple: doc1, doc3, doc4
# banana: doc1, doc2, doc4
# orange: doc2
# mango: doc3
