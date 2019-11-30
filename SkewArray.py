import matplotlib.pyplot as plt

def Skewarray(genome):
    score = {"A":0, "T":0, "G": 1,"C":-1}
    skew = [0]
    for i in range (0, len(genome) ):
        skew.append(score[genome[i]] + skew[i])
    return (skew)
def MinimimumSkew(genome):
    countSkew = Skewarray(genome)
    positions = []
    min = 0
    for i in range (len(genome)):
        if(min > countSkew[i]):
            min = countSkew[i]

    for i in range(len(countSkew)):
        if (countSkew[i] == min):
            positions.append(i)

    return positions

text= "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
skew = Skewarray(text)
print(skew)
min = MinimimumSkew(text)
print(min)
