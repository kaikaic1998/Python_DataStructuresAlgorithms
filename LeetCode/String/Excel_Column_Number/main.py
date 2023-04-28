class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        index = 0
        for letter in columnTitle[::-1]:
            num += (ord(letter)-64) * (26 ** index)
            index += 1
        return num
