from Part_2 import ExercisesPart2

class ExerciseMenuPart2(ExercisesPart2):

    @staticmethod
    def show():
        while True:
            print('\n-------- Exercises Menu - Part 2 --------')
            print('1. Max in list.')
            print('2. Longest word.')
            print('3. Filter words by length.')
            print('4. Count uppercase letters.')
            print('5. Binary to integer.')
            print('6. Calculate ages.')
            print('7. Count ages over 20.')
            print('8. Count names starting with a letter.')
            print('9. Count vowels in word.')
            print('10. Is leap year?')
            print('0. Exit.')
            op = input('Select an option: ')
            if op == '1':
                try:
                    values = input('Enter numbers separated by commas: ')
                    numbers = [float(x.strip()) for x in values.split(',')]
                    print('Max number:', ExercisesPart2.max_in_list(numbers))
                except ValueError:
                    print('Invalid input. Please enter valid numbers.')
                input('\nPress Enter to continue...')
            elif op == '2':
                words = input('Enter words separated by commas: ').split(',')
                words = [w.strip() for w in words]
                print('Longest word:', ExercisesPart2.longest_word(words))
                input('\nPress Enter to continue...')
            elif op == '3':
                while True:
                    words = input('Enter words separated by commas: ').split(',')
                    words = [w.strip() for w in words]
                    try:
                        n = int(input('Enter the minimum length: '))
                        result = ExercisesPart2.filter_words(words, n)
                        print('Filtered words:', result)
                        input('\nPress Enter to continue...')
                        break
                    except ValueError:
                        print('Invalid number.')
                    input('\nPress Enter to continue...')
            elif op == '4':
                text = input('Enter a text: ')
                count = ExercisesPart2.count_uppercase(text)
                print(f'Uppercase letters: {count}')
                input('\nPress Enter to continue...')
            elif op == '5':
                while True:
                    binary = input('Enter a binary number (e.g., 1010): ')
                    try:
                        result = ExercisesPart2.binary_to_integer(binary)
                        print('Integer value:', result)
                        input('\nPress Enter to continue...')
                        break
                    except ValueError:
                        print('Invalid binary number.')
                    input('\nPress Enter to continue...')
            elif op == '6':
                while True:
                    try:
                        year = int(input('Enter current year: '))
                        people = []
                        for i in range(3):
                            name = input(f'Enter name of person {i+1}: ')
                            birth_year = int(input(f'Enter birth year of {name}: '))
                            people.append((name, birth_year))
                        result = ExercisesPart2.calculate_ages(year, people)
                        for name, age in result:
                            print(f'{name} will be {age} years old.')
                        input('\nPress Enter to continue...')
                        break
                    except ValueError:
                        print('Invalid year or birth year.')
                    input('\nPress Enter to continue...')
            elif op == '7':
                while True:
                    try:
                        values = input('Enter 10 ages separated by commas: ')
                        ages = [int(x.strip()) for x in values.split(',')]
                        count = ExercisesPart2.count_over_20(ages)
                        print('People over 20:', count)
                        input('\nPress Enter to continue...')
                        break
                    except ValueError:
                        print('Invalid ages.')
                    input('\nPress Enter to continue...')
            elif op == '8':
                names = input('Enter names separated by commas: ').split(',')
                names = [n.strip() for n in names]
                letter = input('Enter the letter to search: ').lower()
                count = ExercisesPart2.count_names_starting_with(names, letter)
                print(f'Names starting with "{letter}": {count}')
                input('\nPress Enter to continue...')
            elif op == '9':
                word = input('Enter a word: ')
                result = ExercisesPart2.count_vowels(word)
                print('Vowel count:', result)
                input('\nPress Enter to continue...')
            elif op == '10':
                while True:
                    try:
                        year = int(input('Enter a year: '))
                        if ExercisesPart2.is_leap_year(year):
                            print(f'{year} is a leap year.')
                        else:
                            print(f'{year} is not a leap year.')
                        input('\nPress Enter to continue...')
                        break
                    except ValueError:
                        print('Invalid year.')
                    input('\nPress Enter to continue...')
            elif op == '0':
                print('Goodbye!')
                break
            else:
                print('Invalid option. Please try again.')
                input('\nPress Enter to continue...')