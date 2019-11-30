import string as st
text = "CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT"
k  = 3
count = 0
freq = {}
for i in range (len(text) - k + 1):
    count = 0
    str = text[i:i+k]

    for j in range(len(text) - k + 1):
        if (text [j : j+k] == str):
            count = count + 1

    freq[str]=count

print (freq)
print (max(freq))
