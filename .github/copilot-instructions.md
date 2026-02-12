# Copilot Instructions for Python Games Project

## Project Overview
Educational Python game collection containing five simple command-line games/programs. Each file is standalone and focused on fundamental programming concepts without external dependencies (only `random` module used).

## Architecture & Key Patterns

### Project Structure
- **Single-file games**: Each `.py` file is an independent, self-contained program with no inter-file imports
- **No shared utilities**: No `utils.py`, `helpers.py`, or common module patterns - duplicated logic across files is intentional
- **Educational focus**: Emphasizes basic control flow, user input validation, and game loops over code reuse

### Common Patterns Observed

#### Input Validation Pattern
Most files use `.lower()` for case-insensitive comparison and `.isdigit()` for numeric validation:
```python
# From numguess.py - preferred approach
if user_guess.isdigit():
    user_guess = int(user_guess)
else:
    print("Please type a number next time.")
    continue
```
Use this same defensive pattern when accepting user input.

#### Game Loop Pattern
Multiple files use `while True` with manual `break` statements for game loops:
```python
# From rockpaperscissors.py
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
```
Prefer `while True` with explicit exit conditions over conditional while loops.

#### Conditional Branching
Use simple `if/elif/else` chains rather than helper functions. Decision trees are kept inline for clarity (see `choose_your_own_adventure.py` with nested conditionals).

**Narrative/Branching Pattern Example** (`choose_your_own_adventure.py`):
```python
# Each decision point uses nested if/elif/else for story branches
answer = input("You are on a dirt road... left or right? ").lower()
if answer == "left":
    answer = input("You come to a river... walk or swim? ")
    if answer == "swim":
        print("You were eaten by an alligator.")
    elif answer == "walk":
        print("You ran out of water and lost.")
```
When expanding narratives: add new decision points with nested conditionals, maintain consistent win/loss terminal states at all paths.

#### Score/State Tracking
Track game state with simple variables (see `rockpaperscissors.py`: `user_wins`, `computer_wins`; `quizgame.py`: `score` counter).

## File-Specific Conventions

| File | Purpose | Key Pattern |
|------|---------|------------|
| `choose_your_own_adventure.py` | Branching narrative | Nested if/elif chains for story paths |
| `diceroll.py` | Loop & random generation | Simple while loop, random.randint(1,6) for dice |
| `numguess.py` | Number guessing game | Input validation with `.isdigit()`, guesses counter |
| `quizgame.py` | Multiple choice quiz | Hardcoded Q&A, score calculation at end |
| `rockpaperscissors.py` | Game vs computer | Options list, random.randint(0,2) for choice mapping |

## Development Guidelines

### Before Modifying Files
- Treat each file independently - changes don't cascade
- Maintain educational simplicity - avoid refactoring into classes or helper functions
- Keep input/output via `input()` and `print()` only - no file I/O or external dependencies
- Validate all user input case-insensitively with `.lower()`

### Testing Approach
- Run individual files directly: `python filename.py`
- Test all branches: valid input, invalid input, edge cases (empty strings, wrong types)
- Verify game loop behavior (exit conditions, state accumulation)

### When Adding New Games
- Create new `.py` file with standalone, self-contained code
- Follow the observed input validation and game loop patterns above
- Keep game logic within single file; don't import from other game files

### Common Enhancements (If Requested)
These should be added as separate versions or files, maintaining existing files unchanged:

**Difficulty Levels** (`numguess.py` example):
```python
difficulty = input("Easy/Hard? ").lower()
if difficulty == "easy":
    top_of_range = 10
elif difficulty == "hard":
    top_of_range = 100
```

**Best Score Tracking** (`rockpaperscissors.py` example):
```python
best_score = 0
while True:
    # ... existing game loop ...
    if user_wins > best_score:
        best_score = user_wins
```

**Multiple Rounds** (`quizgame.py` example):
- Wrap entire game in outer `while True` loop asking "Play again?"
- Reset `score = 0` at loop start
- Use `input("Play again? ")` at end before `break` or `continue`

## Common Pitfalls
- **Don't refactor common code**: Duplication (e.g., `.lower()` patterns) appears intentional for learning
- **Don't add external dependencies**: Avoid importing packages beyond `random`
- **Don't use classes**: All existing code is procedural - maintain this style
- **Input handling**: Always chain `.lower()` after `input()` for text comparison
