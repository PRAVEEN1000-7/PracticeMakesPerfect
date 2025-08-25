# libraries
import random as rd

# 1. defining pokemons
pokemons = {
    "pikachu" : {"hp" : 100, "moves" : {"Thunderbolt" : 20, "Quick Attack" : 10}, "type" : "⚡"},
    "charmander" : {"hp": 90, "moves": {"Flamethrower": 25, "Scratch": 15}, "type" : "🔥"},
    "bulbasaur" : {"hp": 110, "moves": {"Vine Whip": 18, "Tackle": 12} ,"type" : "🍀"},
    "squirtle" : {"hp": 100, "moves": {"Water Gun": 20, "Tackle": 12} ,"type" : "💧"}
}

# ===========functions==================

def Banner():
    # banner of the game
    
    print()
    print("".center(80,"="))
    print("POKEMON BATTLE".center(80))
    print("".center(80,"="))

def ChoosePokemon():
    # handles user's & computer's pokemon selection. 
    
    while True:
        
        print("\n")
        user_choice = input("choose your pokemon (pikachu, charmander, bulbasaur, squirtle): ")
        if user_choice in list(pokemons.keys()):
            remainPokemon = [pokemon for pokemon in  pokemons.keys() if pokemon!=user_choice]
            computer_choice = rd.choice(remainPokemon)

            user_pokemon = pokemons[user_choice].copy()
            computer_pokemon = pokemons[computer_choice].copy()
            print(f"You chose {user_choice}!")
            print(f"Computer chose {computer_choice}!")
            
            print("POKEMON BATTLE STARTS 🔥".center(80,"-"))
            print(f"{user_choice.upper()} {user_pokemon['type']} VS {computer_choice.upper()} {computer_pokemon['type']}".center(80))
            print(f"{user_choice} HP: {user_pokemon['hp']} | {computer_choice} HP: {computer_pokemon['hp']}".center(80))
            print("".center(80,"-"))
            return user_choice,computer_choice,user_pokemon,computer_pokemon
        
        else:
            print("❌ Invalid pokemon name try again from (pikachu, charmander, bulbasaur, squirtle) !")


def BattleMechanism(user_choice,computer_choice,user_pokemon,computer_pokemon):
    # runs the battle until one pokeman defeated.
    
    moves_used = set()
    
    while user_pokemon["hp"] > 0 and computer_pokemon["hp"]>0:
        
        user_move = input(f"choose the move {list(user_pokemon['moves'])} : ")
        user_moves = [attack for attack in user_pokemon['moves']]

        if user_move in user_moves:
            # user move
            user_move_point = user_pokemon['moves'][user_move]
            print(f"{user_choice} used {user_move}! {computer_choice} lost {user_move_point} HP.")
            moves_used.add(user_move)
            
            # computer move
            computer_moves = [attack for attack in computer_pokemon['moves'] ]
            computer_move = rd.choice(computer_moves)
            computer_move_point = computer_pokemon["moves"][computer_move]
            moves_used.add(computer_move)
            print(f"{computer_choice} used {computer_move}! {user_choice} lost {computer_move_point} HP.")

            # hp calculations
            user_pokemon["hp"] -= computer_move_point
            computer_pokemon["hp"] -= user_move_point
            print(f"{user_choice} HP: {user_pokemon['hp']} | {computer_choice} HP: {computer_pokemon['hp']}")
                
        else:
            print(" ❌ invalid move try again ")

        print("".center(80,"-"))

    return user_pokemon, computer_pokemon, moves_used


def DeclareWinner(user_choice,computer_choice,user_pokemon,computer_pokemon):
    # declaring the winner and looser of the battle.
    
    print("🕹️ GAME ENDED 🕹️".center(80,"="))
    if user_pokemon['hp']>computer_pokemon['hp']:
        winner = user_choice
        looser = computer_choice
        print(f"{computer_choice} fainted! {user_choice} wins!".center(80))
    else:
        winner = computer_choice
        looser = user_choice
        print(f"{user_choice} fainted! {computer_choice} wins!".center(80))
    print("".center(80,"="))

    return winner, looser
    
    
def SaveGameResult(winner, looser, moves_used):
    # keeping the logs of the battle in battle_log.txt file
    
    with open("battle_log.txt",'a') as file:
        file.write(f"Winner: {winner}\nLoser: {looser}\nMoves Used: {moves_used}\n")
        file.write("\n".rjust(80,"-"))

def PlayAgain():
    # asking users if they want to play again 
            
    while True:
        ip = input("try again (y/n) : ")
        if ip=="y"or ip=="Y":
            break
            
        elif ip=="n"or ip=="N":
            print("".center(80,"="))
            print("  EXITING...❗  ".center(80,"="))
            print("".center(80,"="))
            exit()
        
        else:
            print("❌ Invalid input choose from (y/n) ❗")    
    
    
#============main function================

def main():
    while True:
        
        Banner()
        # 2. choosing pokemons
        user_choice,computer_choice,user_pokemon,computer_pokemon = ChoosePokemon()   
            
        # 3. Battle Mechanics
        user_pokemon, computer_pokemon, moves_used = BattleMechanism(user_choice,computer_choice,user_pokemon,computer_pokemon)
        
        # 4. End of the Game
        winner, looser = DeclareWinner(user_choice,computer_choice,user_pokemon,computer_pokemon)
        
        # 5. Saving the result to a file battle_log.txt
        SaveGameResult(winner, looser,moves_used)
        
        # 6. asking user to restart the game
        PlayAgain()


if __name__ == "__main__":
    main()