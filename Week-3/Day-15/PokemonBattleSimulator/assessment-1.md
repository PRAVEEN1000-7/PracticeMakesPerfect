# Problem 1 – Pokémon Battle Simulator Problem 1

Ash and his friends want you to build a text-based Pokémon battle game. Your job is to simulate a simple battle between the player’s Pokémon and the computer’s Pokémon.

## Requirements

#### 1. Pokémon Setup 
Define at least 3 Pokémon as Python dictionaries.
Each Pokémon must have:

```hp``` → hit points (integer, e.g., 100)
```moves``` → another dictionary (move name → damage value)
```
pikachu = {"hp": 100, "moves": {"Thunderbolt": 20, "Quick Attack": 10}}
charmander = {"hp": 90, "moves": {"Flamethrower": 25, "Scratch": 15}}
bulbasaur = {"hp": 110, "moves": {"Vine Whip": 18, "Tackle": 12}}
```
####  2. Choosing Pokémon 
Ask the user to pick a Pokémon by name.
The computer randomly chooses one from the remaining Pokémon.
Display the match-up:
```
You chose Pikachu!
Computer chose Charmander!
```
####  3. Battle Mechanics 
While both Pokémon have hp > 0:
Display user’s Pokémon HP and moves.
Ask the user to select a move ```(input())```.
Subtract that move’s damage from the opponent’s HP.
Computer randomly selects a move and attacks back.
Display round summary:
```
Pikachu used Thunderbolt! Charmander lost 20 HP.
Charmander used Scratch! Pikachu lost 15 HP.
Pikachu HP: 85 | Charmander HP: 70
```
####  4. Game Over 
When any Pokémon’s HP ≤ 0 → game ends.
Announce winner:
```
Charmander fainted! Pikachu wins!
```
####  5. Battle Logs 
Save the result to a file ```battle_log.txt```:
```
Winner: Pikachu
Loser: Charmander
Moves Used: Thunderbolt, Scratch, Quick Attack
```
If file doesn’t exist → create it. If it exists → append.
####  6. Extra Fun (Optional Enhancements)
- Handle ```invalid user inputs``` (e.g., wrong Pokémon or move name).
- Use a ```set comprehension``` to show all unique moves used in the match.
- Add a mini ```Play Again?``` option that lets the user restart with new Pokémon.


