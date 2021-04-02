def revword(word):
    note=''
    length= len(word)
    j=length-1
    while j >= 0:
        note=note+word[j].lower()
        j=j-1
    return note
  
def countword():
    file= open("text.txt","r")
    countWord=0
    saveWord=file.readline()
    saveWord=saveWord.strip()
    txt=file.readlines()
    for line in txt:
        for note in line.split():
            note= revword(note)
            if note==saveWord:
                countWord= countWord+1
    return countWord+1
    #print(saveWord)

#countword()


