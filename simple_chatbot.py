Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... # Simple chatbot
... 
... def greet(bot_name, birth_year):
...     print('Hello! My name is ' + bot_name + '.')
...     print('I was created in ' + birth_year + '.')
... 
... 
... def remind_name():
...     print('Please, remind me your name.')
...     name = input()
...     print('What a great name you have, ' + name + '!')
... 
... 
... def guess_age():
...     print('Let me guess your age.')
...     print('Enter remainders of dividing your age by 3, 5 and 7.')
... 
...     rem3 = int(input())
...     rem5 = int(input())
...     rem7 = int(input())
...     age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
... 
...     print("Your age is " + str(age) + "; that's a good time to start programming!")
... 
... 
... def count():
...     print('Now I will prove to you that I can count to any number you want.')
... 
...     num = int(input())
...     curr = 0
...     while curr <= num:
...         print(curr, '!')
...         curr = curr + 1
... 
... 
def test():
    print("Let's test your programming knowledge.")
    print("What year was the Magna Carta issued?")
    print("1. 1100")
    print("2. 1776")
    print("3. 2019")
    print("4. 1215")

    ansr = int(input())
    while ansr != 4:
        print("Please, try again.")
        ansr = int(input())
    end()

def end():
    print('Congratulations, have a nice day!')


greet('Stan Bot', '2023')
remind_name()
guess_age()
count()
test()
