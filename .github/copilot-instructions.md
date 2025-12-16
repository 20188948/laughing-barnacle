# Copilot Instructions for AI Coding Agents

## Project Overview
This workspace contains a set of small Python scripts and text files, primarily for educational or exercise purposes. There is no complex architecture or multi-file service structure; each file is mostly self-contained and solves a specific problem or task.

## Key Directories and Files
- Root Python scripts: `1B.py`, `1C.py`, `1D.py` (each is a standalone script)
- `Task 1(w1)/`: Contains multiple scripts (`1A`, `1B`, `1C`, `2A`, `3`) and text files (`news.txt`, `sales.txt`, `story.txt`).
- `Task 2(w2)/`: Currently empty.

## Patterns and Conventions
- Each script is designed to be run interactively, often using `input()` for user interaction.
- Scripts in `Task 1(w1)/` often process text files or user input, and print results directly.
- Naming conventions are minimal; file names like `1A`, `1B`, etc., correspond to exercise or task numbers.
- No external dependencies beyond Python standard library modules (`random`, `math`).
- No build system, test framework, or package management is present.

## Developer Workflows
- To run a script, use: `python3 <scriptname>`
- No automated tests or CI/CD; manual execution and inspection is the norm.
- Debugging is done by running scripts and observing printed output.

## Examples of Patterns
- Reading and processing text files:
  ```python
  filename = input()
  with open(filename,'r') as file:
      text = file.read()
  # ...process text...
  ```
- Counting characters or lines in a file:
  ```python
  with open(filename,'r') as file:
      lines = len(file.readlines())
      print("number of lines are :", lines)
  ```
- Simple input/output logic:
  ```python
  teas = int(input("How many teas?: "))
  coffees = int(input("How many coffees?: "))
  print("Total income is £", teas*2 + coffees*3)
  ```

## Integration Points
- No cross-file imports or shared modules; scripts do not interact with each other.
- Text files (`news.txt`, `sales.txt`, `story.txt`) are used as input for some scripts.

## Recommendations for AI Agents
- Treat each script as independent unless explicit instructions indicate otherwise.
- When adding new scripts, follow the pattern of interactive input and direct output.
- Reference existing scripts for examples of file I/O and input handling.
- Avoid introducing external dependencies or complex architecture unless requested.

---

If any section is unclear or missing important details, please provide feedback to improve these instructions.