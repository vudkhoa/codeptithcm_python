import sys

def chuanhoa(sentence):
    words = sentence.split()
    normalized_sentence = ' '.join(words)  
    normalized_sentence = normalized_sentence.capitalize()  
    return normalized_sentence

def main():
    text = sys.stdin.read()

    sentences = []
    temp_sentence = ""

    for char in text:
        if char in ".?!":  
            if temp_sentence.strip(): 
                sentences.append(chuanhoa(temp_sentence.strip()))
            temp_sentence = ""
        else:
            temp_sentence += char
    
    if temp_sentence.strip():
        sentences.append(chuanhoa(temp_sentence.strip()))

    for sentence in sentences:
        print(sentence)

if __name__ == "__main__":
    main()
