# Longest common consecutive genome

genome1 = "agctagctagctagctagctagcta"
genome2 = "gctaggcctag"

len1 = len(genome1)
len2 = len(genome2)
longest = ""

for start in range(len2):
    for end in range(start + 1, len2 + 1):
        substring = genome2[start:end]
        if substring in genome1:
            if len(substring) > len(longest):
                longest = substring

print("Longest Common Consecutive Genome:", longest)
