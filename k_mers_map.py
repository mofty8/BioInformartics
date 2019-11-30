def FrequencyMap(text, k):
    count = 0
    freq = {}
    for i in range(len(text) - k + 1):
        count = 0
        str = text[i:i + k]

        for j in range(len(text) - k + 1):
            if (text[j: j + k] == str):
                count = count + 1

        freq[str] = count

    return freq
def FreqeuntWords(text,k):


    OCC = FrequencyMap(text, k)
    m = max(OCC.values())
    word = []
    for key in OCC.keys():
       if(OCC[key] == m):
          word.append(key)
    print(word)

text = "CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT"
k = 3
FreqeuntWords(text, k)
a = 1/10
print(int(a))