import string
def removePunctuation(sentence : str):
        return str.translate(sentence, str.maketrans('','', string.punctuation))

def removeWord(removeWordList: list, sentence : list):
    for removeWord in removeWordList:
        sentence = list(filter(removeWord.__ne__,sentence))
    return sentence