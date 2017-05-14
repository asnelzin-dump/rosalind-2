def reverse_pattern(pattern):
    ans = ''
    for nucl in reversed(pattern):
        if nucl == 'A':
            ans += 'T'
        if nucl == 'T':
            ans += 'A'
        if nucl == 'G':
            ans += 'C'
        if nucl == 'C':
            ans += 'G'
    return ans

def main():
    print(reverse_pattern(input()))

if __name__ == '__main__':
    main()