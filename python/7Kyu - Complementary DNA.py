# My Solution

from string import maketrans
def DNA_strand(dna):
    trantab = maketrans("ACTG", "TGAC")
    return dna.translate(trantab)
