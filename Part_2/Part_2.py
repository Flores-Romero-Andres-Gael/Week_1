class ExercisesPart2:

    @staticmethod
    def max_in_list(numbers):
        if not numbers:
            return None
        max_value = numbers[0]
        for num in numbers[1:]:
            if num > max_value:
                max_value = num
        return max_value

    @staticmethod
    def longest_word(words):
        if not words:
            return None
        longest = words[0]
        for word in words[1:]:
            if len(word) > len(longest):
                longest = word
        return longest

    @staticmethod
    def filter_words(words, n):
        return [word for word in words if len(word) > n]

    @staticmethod
    def count_uppercase(text):
        count = 0
        for char in text:
            if char.isupper():
                count += 1
        return count

    @staticmethod
    def binary_to_integer(binary_str):
        return int(binary_str, 2)

    @staticmethod
    def calculate_ages(current_year, people):
        result = []
        for name, birth_year in people:
            age = current_year - birth_year
            result.append((name, age))
        return result

    @staticmethod
    def count_over_20(ages):
        count = 0
        for age in ages:
            if age > 20:
                count += 1
        return count

    @staticmethod
    def count_names_starting_with(names, letter=''):
        count = 0
        for name in names:
            if name.lower().startswith(letter.lower()):
                count += 1
        return count

    @staticmethod
    def count_vowels(word):
        vowels = "aeiou"
        counts = {v: 0 for v in vowels}
        for char in word.lower():
            if char in counts:
                counts[char] += 1
        return counts

    @staticmethod
    def is_leap_year(year):
         return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)