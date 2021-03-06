def rev_comp(s):
    s2 = s[::-1]
    seq = ""
    for chr in s2:
        if chr == "A":
            seq += "T"
        if chr == "T":
            seq += "A"
        if chr == "G":
            seq += "C"
        if chr == "C":
            seq += "G"
    return seq


f = open("rosalind_revp.txt", "r")
DNAstrand = f.readlines()
seq = ""
for line in DNAstrand:
    line = line.strip()
    if line[0] != ">":
        seq += line

for i in range(len(seq)):
     for n in range(4,13):
         if seq[i:i+n] == rev_comp(seq[i:i+n]):
             if i + n <= len(seq):
                 print (i+1, n)
