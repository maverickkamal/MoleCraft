# MoleCraft

A terminal-based chemistry puzzle game. You build molecules on a grid by placing atoms and creating bonds before the timer runs out.

Built with Python and [Textual](https://github.com/Textualize/textual).

## Requirements

- Python 3.10+
- Textual 0.47+

## Install

Clone the repo and install dependencies:

```
git clone https://github.com/maverickkamal/MoleCraft.git
cd MoleCraft
pip install textual
```

Or install the package directly:

```
pip install .
```

## Run

```
python run.py
```

Or as a module:

```
python -m src
```

Or if installed via `pip install .`:

```
molecraft
```

## How to play

1. Pick a difficulty (Easy, Medium, Hard) from the main menu.
2. You get a molecule to build. Carbon atoms are pre-placed on the grid (locked).
3. Place other atoms (H, O, N, Cl) at the correct positions.
4. Create bonds between atoms by selecting two atoms with Space.
5. Submit your solution with Enter before time runs out.

Ghost hints (dim lowercase letters) show where atoms should go.

## Controls

| Key | Action |
|-----|--------|
| Arrow keys | Move cursor |
| H | Place hydrogen |
| O | Place oxygen |
| N | Place nitrogen |
| L | Place chlorine |
| Space | Select atom / create bond between two selected atoms |
| Delete/Backspace | Remove atom at cursor |
| U | Undo last action |
| Enter | Submit solution |
| R | Reset puzzle |
| P | Pause game |
| Escape | Go back |

## Scoring

- Base: 100 points per correct solve
- Time bonus: remaining seconds x 10
- Streak bonus: +25 per consecutive solve (x2 = +25, x3 = +50, etc.)

## Lives

You start with 3 lives. Running out of time costs one life. Lose all 3 and it's game over.

## Progression

- Puzzles you haven't solved yet are served first.
- Clearing all puzzles in a difficulty automatically promotes you to the next tier.

## Save data

Progress is saved automatically to `~/.molecraft/save.json`. This includes high score, completed puzzles, fastest solve time, and best streak.

## Puzzles

30 molecules across 3 difficulty levels:

- **Easy** (10): H2, Cl2, HCl, Water, Ammonia, Methane, Ethane, Propane, Methanol, Hydrogen Peroxide
- **Medium** (10): Ethene, Ethyne, CO2, Formaldehyde, Ethanol, Acetic Acid, Propene, Acetone, Formic Acid, Dimethyl Ether
- **Hard** (10): Butane, Butadiene, Glycine, Urea, Methyl Formate, Chloroform, Acetaldehyde, Nitromethane, Propanol, Lactic Acid
