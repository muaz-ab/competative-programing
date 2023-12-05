class Solution:
    def romanToInt(self, s: str) -> int:
        alphabet = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        dec_number = 0
        last_add = 0

        for ch in s[::-1]:
            if last_add > alphabet[ch]:
                dec_number -= alphabet[ch]
            else:
                dec_number += alphabet[ch]
            last_add = alphabet[ch]

        return dec_number