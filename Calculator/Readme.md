# Simple Calculator with History

A simple command-line calculator written in Python. It performs basic arithmetic operations and saves every calculation to a history file.

## Features

- Addition, subtraction, multiplication and division
- Division by zero check
- Saves every calculation in `history.txt`
- View history (latest calculation first)
- Clear history
- Runs in a loop until you type `exit`

## Requirements

- Python 3

## How to Run

```bash
python3 calculator_with_history.py
```

## Usage

Type a calculation at the prompt:

```
8+8
10 - 3
4 * 5
20 / 4
2.5 * 2
```

Commands:

| Command   | Description                       |
|-----------|-----------------------------------|
| `history` | Show all previous calculations    |
| `clear`   | Delete all saved history          |
| `exit`    | Close the program                 |

## Example

```
--SIMPLE CALCULATOR (type history,clear or exit)
ENter Calculation (+ - * /) or command (history,clear ,exit): 8+8
Result:  16
ENter Calculation (+ - * /) or command (history,clear ,exit): 20 / 4
Result:  5
ENter Calculation (+ - * /) or command (history,clear ,exit): history
20 / 4=5
8+8=16
ENter Calculation (+ - * /) or command (history,clear ,exit): exit
GoodBye
```

## Project Files

| File                          | Description                      |
|-------------------------------|----------------------------------|
| `calculator_with_history.py`  | Main program                     |
| `history.txt`                 | Auto-created, stores history     |

## Notes

- `history.txt` is created after the first calculation, so do at least one calculation before using `history`.
- Negative numbers as the first value (e.g. `-5+3`) are not supported.
- Do not run `python3 ...` again while the program is already running; type `exit` first.

## Author

Fatema