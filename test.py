def count_words(text):
    
    text = text.strip()
    
    words = text.split()
    
    return len(words)

if __name__ == '__main__':
    
    text = input("Enter your text: ")
    
 
    word_count = count_words(text)
    
    
    print(f"The number of words in the given text is: {word_count}")