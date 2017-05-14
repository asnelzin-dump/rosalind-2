masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115,
          128, 129, 131, 137, 147, 156, 163, 186]


def generate_subpeptides(peptide):
    answer = list()
    size = len(peptide)
    for i in range(1, size):
        for j in range(size):
            subpeptide = []
            for k in range(i):
                subpeptide.append(peptide[(j + k) % size])
            answer.append(subpeptide)
    return answer


def cyclospectrum(peptide):
    subpeptides = generate_subpeptides(peptide)
    spectrum = list()

    spectrum.append(0)
    for i in subpeptides:
        spectrum.append(sum(i))
    spectrum.append(sum(peptide))
    return spectrum


def expand(aux):
    result = list()
    for peptide in aux:
        for addition in masses:
            item = peptide.copy()
            item.append(addition)
            result.append(item)
    return result


def cyclopeptide_sequencing(spectrum):
    answer = []
    aux = [[addition] for addition in masses]
    key = 0
    while aux:
        start = len(aux)
        print(key, start)
        key = 0
        for peptide in aux[:]:
            if sum(peptide) not in spectrum:
                aux.remove(peptide)
                key += 1
            elif sorted(cyclospectrum(peptide)) == spectrum:
                result = '-'.join([str(mass) for mass in peptide])
                print(result)
                answer.append(result)
                aux.remove(peptide)
                key += 1
        aux = expand(aux)
    return answer


def main():
    data = input()
    spectrum = [int(mass) for mass in data.split()]
    print(cyclospectrum(cyclopeptide_sequencing(spectrum)))

if __name__ == '__main__':
    main()