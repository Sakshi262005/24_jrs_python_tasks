def count_even():
    answer= []
    for x in range(1, 6):
        if x % 2 == 0:
            answer.append(x)
    return answer


print(count_even())


def count_vowels():
s = input("Please Enter a String : ")
vowels = 0
consonants = 0

for i in s:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
       or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
    else:
        consonants = consonants + 1
 
print("Total Number of Vowels  = ", vowels)
print("Total Number of Consonants  = ", consonants)


ls = ["apple", "banana", "mango", "kiwi", "dragonfruit"]
longest_word = ""
for word in ls:
    if len(word) > len(longest_word):
        longest_word = word
print(longest_word)


class Solution(object):
    def majorityElement(self, nums):
        candidate, count = 0, 0
        for num in nums:
            if count == 0:
                candidate = num
                count += 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
    

    class Solution:
    def canConstruct(self, ransomNote: str, magazine: str)
        cnt = Counter(magazine)
        for c in ransomNote:
            cnt[c] -= 1
            if cnt[c] < 0:
                return False
        return True
    

    class Solution:
    def firstUniqueChar(self, s: str)
        cnt = Counter(s)
        for i, c in enumerate(s):
            if cnt[c] == 1:
                return i
        return -1