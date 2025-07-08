from operator import length_hint


class Exercises_Part_1:

    def max(a, b):
        if a > b:
            return a
        else:
            return b

    def max_of_tree(a, b, c):
        if a >= b and a >= c:
            return a
        elif b >= a and b >= c:
            return b
        else:
            return c

    def lenght(list):
        leng = 0
        for _ in list:
            leng += 1
        return leng

    def is_vowel(char):
        if char in 'aeiou':
            return True
        else:
            return False

    def sum(numbers):
        total = 0
        for num in numbers:
            total += num
        return total

    def multip(numbers):
        total = 1
        for num in numbers:
            total *= num
        return total

    def invers(text):
        return text[::-1]

    def is_palindrome(text):
        cleaned = text.replace(" ","").lower()
        return cleaned == cleaned[::-1]

    def superposition(list1, list2):
        for items1 in list1:
            for items2 in list2:
                if items1 == items2:
                    return True
        return False

    def generate_n_characters(n, char):
        return char * n

    def prodecure(numbers):
        for num in numbers:
            print('*' * num)