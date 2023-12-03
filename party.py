Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... 
... party = {}
... 
... print("Enter the number of friends joining (including you):")
... n = int(input())
... 
... if n > 0:
...     print("Enter the name of every friend (including you), each on a new line:")
...     for i in range(n):
...         party[input()] = 0
... 
...     print("Enter the total bill value:")
...     cost = int(input())
... 
...     print("""Do you want to use the "Who is lucky?" feature? Write Yes/No:""")
...     lucky = input()
... 
...     if lucky.lower() == "yes":
...         lucky_one = random.choice(list(party.keys()))
...         print(lucky_one + " is the lucky one!")
...         for j in party:
...             if j != lucky_one:
...                 party[j] = round((cost / (n - 1)), 2)
...     elif lucky.lower() == "no":
...         print("No one is going to be lucky")
...         for j in party:
...             party[j] = round((cost / n), 2)
... 
...     print(party)
... 
... else:
