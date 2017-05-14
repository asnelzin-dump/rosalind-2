import re
from codon_table import codon_table


def translate(pattern):
    return ''.join([codon_table[codon] for codon in re.findall('.{3}', pattern)])


def reverse(pattern):
    answer = ''
    for n in reversed(pattern):
        if n == 'A':
            answer += 'T'
        if n == 'T':
            answer += 'A'
        if n == 'G':
            answer += 'C'
        if n == 'C':
            answer += 'G'
    return answer


def main():
    dna = input()
    peptide = input()
    len_pattern = len(peptide) * 3

    for i in range(len(dna) - len_pattern + 1):
        pattern = dna[i:i + len_pattern]
        rev_pattern = reverse(pattern)
        if translate(pattern.replace('T', 'U')) == peptide or \
           translate(rev_pattern.replace('T', 'U')) == peptide:
            print(pattern)


if __name__ == '__main__':
    main()