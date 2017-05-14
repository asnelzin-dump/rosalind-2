import itertools
from mass_table import mass_table


def mass_peptide(peptide):
    mass = 0
    for acid in peptide:
        mass += mass_table[acid]
    return mass


def generate_subpeptides(peptide):
    answer = list()
    size = len(peptide)
    for i in range(1, size):
        for j in range(size):
            subpeptide = ''
            for k in range(i):
                subpeptide += peptide[(j + k) % size]
            answer.append(subpeptide)
    return answer


def main():
    peptide = input()

    subpeptides = generate_subpeptides(peptide)

    spectrum = list()

    spectrum.append(0)
    for i in subpeptides:
        spectrum.append(mass_peptide(i))
    spectrum.append(mass_peptide(peptide))

    print(' '.join([str(mass) for mass in spectrum]))


if __name__ == '__main__':
    main()