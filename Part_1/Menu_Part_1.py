from Part_1 import Exercises_Part_1

class ExerciseMenu(Exercises_Part_1):

    @staticmethod
    def show():
        while True:
            print('\n--------Exercises Menu--------')
            print('1. Max of two numbers.')
            print('2. Max of three numbers.')
            print('3. Calculete lenght.')
            print('5. Operations.')
            print('6. Inverse.')
            print('7. Is a Palindrome.')
            print('8. Super position.')
            print('9. Generate Character.')
            print('10. Procedure.')
            print('0. Exit.')
            op = input('Select an option: ')
            if op == '1':
                while True:
                    try:
                        a = float(input('\nEnter the first number: '))
                        b = float(input('Enter the second number: '))
                        print('Max number: ', Exercises_Part_1.max(a, b))
                        input('\nPress Enter to continue...')
                        break
                    except ValueError:
                        print('Invalid entry. Please try again.')
            elif op == '2':
                while True:
                    try:
                        a = float(input('Enter the first number: '))
                        b = float(input('Enter the second number: '))
                        c = float(input('Enter the third number: '))
                        print('Max number: ', Exercises_Part_1.max_of_tree(a, b, c))
                        input('\nPress Enter to continue...')
                        break
                    except ValueError:
                        print('Invalid entry. Please try again.')
            elif op == '3':
                obj = input('\nEnter a string or list (as comma "," to separated values): ')
                if "," in obj:
                    count = obj.split(',')
                    print('Lenght of list to "' , obj, '" : ', Exercises_Part_1.lenght(count))
                else:
                    print('Lenght of string "', obj, '" : ', Exercises_Part_1.lenght(obj))
                input('\nPress Enter to continue...')
            elif op == '4':
                char = input('\nEnter a single character: ')
                print('Is "', char, '" a vowel? ', Exercises_Part_1.is_vowel(char))
                input('\nPress Enter to continue...')
            elif op == '5':
                while True:
                    print('\n--------Choose an operation--------')
                    print('1. Sum.')
                    print('2. Mult.')
                    print('0. Exit.')
                    op1 = input('Select an operation: ')
                    if op1 == '1':
                        selection = input('Enter the numbers (separated by comma ","): ')
                        numbers = [float(x.strip()) for x in selection.split(',')]
                        print('Sum: ', Exercises_Part_1.sum(numbers))
                        input('\nPress Enter to continue...')
                    elif op1 == '2':
                        selection = input('Enter the numbers (separated by comma ","): ')
                        numbers = [float(x.strip()) for x in selection.split(',')]
                        print('Mult: ', Exercises_Part_1.multip(numbers))
                        input('\nPress Enter to continue...')
                    elif op1 == '0':
                        print('Back to main menu.')
                        input('\nPress Enter to continue...')
                        break
                    else:
                        print('Wrong input. Please try again.')
            elif op == '6':
                text = input('Enter a text to invert: ')
                print('Inverted: ', Exercises_Part_1.invers(text))
                input('\nPress Enter to continue...')
            elif op == '7':
                text = input('Enter a word or phrase: ')
                print('Is palindrome? ', Exercises_Part_1.is_palindrome(text))
                input('\nPress Enter to continue...')
            elif op == '8':
                list1 = input('Enter a list (separated by comma ","): ')
                list2 = input('Enter a list (separated by comma ","): ')
                list1 = [x.strip() for x in list1.split(',')]
                list2 = [x.strip() for x in list2.split(',')]
                print('Super position: ', Exercises_Part_1.superposition(list1, list2))
                input('\nPress Enter to continue...')
            elif op == '9':
                while True:
                    try:
                        n = int(input('Enter how many times to repeat: '))
                        char = input('Enter a single character: ')
                        if len(char) != 1:
                            print('Wrong input, you must enter exactly one character. Try again.')
                        else:
                            print('Result: ', Exercises_Part_1.generate_n_characters(n, char))
                        input('\nPress Enter to continue...')
                        break
                    except ValueError:
                        print('Invalid number. Try again.')
            elif op == '10':
                while True:
                    try:
                        selection = input('Enter the numbers (separated by comma ","): ')
                        numbers = [int(x.strip()) for x in selection.split(',')]
                        Exercises_Part_1.prodecure(numbers)
                        input('\nPress Enter to continue...')
                        break
                    except ValueError:
                        print('Invalid input. Please enter integers only.')
            elif op == '0':
                print('Goodbye!')
                break
            else:
                print('\n--------Invalid option. Please try again.--------')
                input('\nPress Enter to continue...')