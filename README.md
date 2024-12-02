# Package Sorter

## Description

This Python script classifies packages into different stacks based on their volume and mass. The rules for classification are:

- A package is **bulky** if:
  - Its volume (Width × Height × Length) is greater than or equal to 1,000,000 cm³, or
  - Any of its dimensions (Width, Height, Length) is greater than or equal to 150 cm.
- A package is **heavy** if its mass is greater than or equal to 20 kg.

### Stacks:
1. **STANDARD**: Packages that are neither bulky nor heavy.
2. **SPECIAL**: Packages that are either bulky or heavy (but not both).
3. **REJECTED**: Packages that are both bulky and heavy.

---

## How to Run

### Prerequisites:
- Python 3.x installed on your system.

### Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/wahyeung/package-sorter.git

## Hosting on Repl.it

For immediate code review, the script is hosted online. You can test it here: [Run on Replit](https://replit.com/@browahyeung/Python-script-for-sorting-packages#main.py)
