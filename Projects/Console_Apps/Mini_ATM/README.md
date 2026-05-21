# Mini ATM (Python)

## Project Goal
To practice Python programming fundamentals and gradually improve project architecture from a simple monolithic script to an object-oriented modular application.

---

## Project Versions

### ATM_v1.py
Basic ATM implementation using a monolithic structure without functions.

Features:
- PIN authentication
- Balance check
- Deposit money
- Withdraw money
- Input validation

---

### ATM_v2.py
Refactored ATM version using functions with improved structure and readability.

Features:
- Function-based architecture
- Cleaner program flow
- Better separation of concerns
- Improved readability
- Reusable logic

---

### ATM_OOP/
Object-oriented ATM system with modular architecture.

Implemented using:
- Classes and objects
- Encapsulation
- Object interaction
- Modular structure

Main entities:
- User
- Account

Features:
- User authentication
- Account balance management
- Deposit and withdraw operations
- Transaction history
- Input validation
- Encapsulated balance and PIN protection

Project structure:

```text
ATM_OOP/
│
├── main.py
├── models/
│   ├── user.py
│   └── account.py
```

---

## Technologies & How to Run

### Technologies
- Python 3

---

### Run Simple Versions

```bash
git clone https://github.com/OliinykBohdan/Learning-Python.git

cd Learning-Python/Projects/Console_Apps/Mini_ATM/ATM_simple_versions

python ATM_v1.py
```

or

```bash
python ATM_v2.py
```

---

### Run OOP Version

```bash
cd Learning-Python/Projects/Console_Apps/Mini_ATM/ATM_OOP

python main.py
```

---

## What I Learned

### General Python
- Loops and conditions
- User input handling
- Error handling
- Program flow control

### Functions
- Function decomposition
- Cleaner architecture
- Separation of responsibilities

### OOP
- Classes and objects
- Encapsulation
- Object interaction
- Modular project structure
- Authentication flow
- Working with collections of objects

---

## Key Improvements Across Versions

### v1 → v2
- Introduced functions
- Improved readability
- Cleaner logic separation

### v2 → OOP
- Added modular architecture
- Introduced classes and object interaction
- Encapsulated sensitive data
- Improved scalability and maintainability
- More realistic project structure
