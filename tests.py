import unittest
import mismatch_freq_words


class ChangeLettersCheck(unittest.TestCase):
    #'def change_letters(original, positions, exchanges):'
    samples = (
        (('Hiilo', (1, 2), 'el'), 'Hello'),
        (('AAAA', (0, 1, 3), 'TGC'), 'TGAC'),
        (('GCATGCGAT', (5,), ' '), 'GCATG GAT'),
        (('TEST', (), ''), 'TEST')
    )

    def test_change_letters_with_samples(self):
        """Testing change_letters with samples:"""
        for args, result in self.samples:
            answer = mismatch_freq_words.change_letters(args[0], args[1], args[2])
            print('Arguments: {0}\n'
                  'Expected: {1}\n'
                  'Answer: {2}\n'.format(args, result, answer))
            self.assertEqual(answer, result)


if __name__ == '__main__':
    unittest.main()