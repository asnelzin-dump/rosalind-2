import re
from codon_table import codon_table

dna = input()

print(''.join([codon_table[codon] for codon in re.findall('.{3}', dna)]))
