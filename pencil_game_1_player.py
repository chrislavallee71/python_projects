Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... 
... players = ["John", "Jack"]
... 
... while True:
...     try:
...         pencils = int(input("How many pencils would you like to use:"))
...         if pencils == 0:
...             print("The number of pencils should be positive")
...             continue
...         
...         if pencils < 0:
...             print("The number of pencils should be numeric (the minus sign is not a numeric)")
...             continue
...         
...         while True:
...             name = input("Who will be the first (John, Jack):")
...             if name in players:
...                 break
...             else:
...                 print(f"Choose between {players[0]} and {players[1]}")
...                 
...         print("|" * pencils)
...         break
...     
...     except ValueError:
...         print("The number of pencils should be numeric")
...         continue
... 
... def game(name):
...     global players, pencils
...     while pencils > 0:
...         try:
...             if name == "Jack":
...                 print("Jack's turn:")
...                 if pencils % 4 == 0:
                    take = 3
                elif pencils % 4 == 3:
                    take = 2
                elif pencils % 4 == 2:
                    take = 1
                else:
                    take = random.randint(1, 3)
                print(take)
            else:
                take = int(input(f"{name}'s turn:"))
                
                if take not in [1, 2, 3]:
                    print("Possible values: '1', '2' or '3'")
                    continue
                
                if take > pencils:
                    print("Too many pencils were taken")
                    continue
            
            pencils = max(0, pencils - take)
            print("|" * pencils)
            
            # Switch to the other player's turn
            name = players[1] if name == players[0] else players[0]

        except ValueError:
            print("Possible values: '1', '2' or '3'")
            continue

    # The current player lost, switch back to the original player
    winner = name
    print(f"{winner} won!")


starting_player = players[0] if name == players[0] else players[1]

game(starting_player)
