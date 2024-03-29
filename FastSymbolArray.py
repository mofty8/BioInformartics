def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n // 2]

    array[0] = PatternCount(symbol, Genome[0:n // 2])

    for i in range(1, n):

        array[i] = array[i - 1]

        if ExtendedGenome[i - 1] == symbol:
            array[i] = array[i] - 1
        if ExtendedGenome[i + (n // 2) - 1] == symbol:
            array[i] = array[i] + 1
    return array


# Input:  Strings Text and Pattern
# Output: The number of times Pattern appears in Text
# HINT:   This code should be identical to when you last implemented PatternCount
def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i:i + len(Pattern)] == Pattern:
            count = count + 1
    return count
text = ""
symbol = 'A'
countarray = FasterSymbolArray(text, symbol)
