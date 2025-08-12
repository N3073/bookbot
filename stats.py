def get_num_words(text:str)->int:
     return len(text.split())

def get_char_freqs(text:str)->dict:
    text_lower = text.lower()
    char_freqs={}
    for char in text_lower: 
        if char not in char_freqs:
            char_freqs[char]=1
        else:
            char_freqs[char]+=1
    return char_freqs

def sort_on(items):
    return items["num"]

def sort_char_freqs(char_freqs:dict)->list[dict]:

    char_dicts = [{"char":key,"num":char_freqs[key]} for key in char_freqs]

    char_dicts.sort(reverse=True,key=sort_on)

    return char_dicts