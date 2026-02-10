# CDC - Complex Desktop Calculator

A Python implementation of a stack-based Reverse Polish Notation (RPN) calculator supporting both real and complex numbers, inspired by the classic Unix `dc` utility.

## 📋 Overview

This project is a modern take on the historical Unix `dc` ("desk calculator") command, extended to handle complex arithmetic. Built using **strict Test-Driven Development (TDD)** principles as defined by Kent Beck.

### Key Features
- **Stack-based RPN evaluation** (operands pushed, operators pop and compute)
- **Real and complex number support** (e.g., `3`, `-2.5`, `3+j4`, `j5`)
- **Canonical output format**: `RVAL ± jIMAG` with normalization
- **Comprehensive error handling**: stack underflow, division by zero, invalid tokens
- **Pure Python implementation** with `pytest` test suite

## 🏗️ Architecture

```
ECSE-428-A/
├── src/
│   ├── cli.py          # Command-line interface
│   ├── engine.py       # Core RPN engine and command execution
│   ├── stack.py        # Stack data structure with (real, imag) tuples
│   └── errors.py       # Error message constants
├── tests/
│   ├── test_push_pop.py
│   ├── test_add.py
│   ├── test_sub.py
│   ├── test_mul.py
│   ├── test_div.py
│   ├── test_delete.py
│   └── test_invalid_token.py
└── README.md
```

### Components

- **`Engine`**: Parses and executes RPN commands, maintains computation state
- **`Stack`**: Stores values as `(real, imaginary)` tuples with underflow protection
- **`CLI`**: Command-line interface for interactive or scripted use
- **`errors.py`**: Centralized error message definitions

## 🚀 Installation

### Prerequisites
- Python 3.8+
- `pytest` library

### Setup
```bash
# Clone the repository
git clone <repository-url>
cd ECSE-428-A

# Install dependencies
pip install pytest

# Run tests
pytest -v

# run cli
python -m src.cli
# exit cli with control+c
```


## 📖 Usage

### Command Reference

| Command | Description | Example |
|---------|-------------|---------|
| `push <number>` | Push a number onto the stack | `push 3`, `push 2+j4` |
| `pop` | Pop and print the top value | `pop` |
| `add` | Add top two values | `push 2 push 3 add` |
| `sub` | Subtract (second - top) | `push 5 push 2 sub` |
| `mul` | Multiply top two values | `push 3 push 4 mul` |
| `div` | Divide (second / top) | `push 8 push 2 div` |
| `delete` | Remove top value (no output) | `delete` |

### Number Formats

#### Real Numbers
```bash
push 3          # Integer
push -2.5       # Decimal
```

#### Complex Numbers
```bash
push 3+j4       # Compact form
push 3 + j 4    # Spaced form (parsed the same)
push j5         # Pure imaginary (0 + j5)
push -1.5-j2    # Negative components
```

### Output Format

All outputs follow canonical form: `RVAL ± jIMAG`

**Normalization rules:**
- `-0` converted to `0`
- Trailing `.0` dropped when appropriate
- Always includes `± j` separator

**Examples:**
```
6 + j0          # Real result
3 - j1          # Complex with negative imaginary
0 + j5          # Pure imaginary
```

### Example Sessions

#### Basic Arithmetic
```bash
# Real number multiplication
push 3
push -2
mul
pop
# Output: -6 + j0
```

#### Complex Arithmetic
```bash
# Complex division: (4+j2) / (1+j1) = 3-j1
push 4+j2
push 1+j1
div
pop
# Output: 3 - j1
```

#### Stack Manipulation
```bash
push 1
push 2
push 3
delete      # Removes 3
pop         # Output: 2 + j0
pop         # Output: 1 + j0
```

## 🧪 Testing

### Run All Tests
```bash
pytest -v
```

### Run Specific Test File
```bash
pytest tests/test_mul.py -v
```

### Run Specific Test
```bash
pytest tests/test_mul.py::test_mul_cplx1 -v
```

### Test Coverage

| Operation | Test Count | Test IDs |
|-----------|------------|----------|
| PUSH/POP | 3 | T-PUSH-REAL1, T-PUSH-CPLX1, T-POP-ERR1 |
| ADD | 3 | T-ADD-REAL1, T-ADD-CPLX1, T-ADD-ERR1 |
| SUB | 3 | T-SUB-REAL1, T-SUB-CPLX1, T-SUB-ERR1 |
| MUL | 3 | T-MUL-REAL1, T-MUL-CPLX1, T-MUL-ERR1 |
| DIV | 4 | T-DIV-REAL1, T-DIV-CPLX1, T-DIV-ERR1, T-DIV-ERR2 |
| DELETE | 3 | T-DEL-REAL1, T-DEL-CPLX1, T-DEL-ERR1 |
| Invalid Token | 2+ | Token validation tests |

## ⚠️ Error Handling

### Stack Underflow
```bash
pop
# Error: stack underflow

add
# Error: stack underflow (needs 2 values)
```

### Division by Zero
```bash
push 1
push 0
div
# Error: division by zero
```

### Invalid Token
```bash
push blah
# Error: invalid token

banana
# Error: invalid token
```

## 🔬 Development Methodology

This project strictly follows **Test-Driven Development (TDD)**:

1. ✅ Write the smallest possible failing test
2. ✅ Write minimal code to make that test pass
3. ✅ Run full test suite to ensure no regressions
4. ✅ Refactor only when all tests are green

### TDD Workflow Example
```bash
# 1. Write failing test
# Edit tests/test_mul.py

# 2. Verify failure
pytest tests/test_mul.py -v
# Screenshot RED

# 3. Implement minimal code
# Edit src/engine.py

# 4. Verify pass
pytest -v
# Screenshot GREEN

# 5. Commit
git add .
git commit -m "T-MUL-REAL1 pass"
```

## 🧮 Mathematical Operations

### Complex Multiplication
```
(a + jb) × (c + jd) = (ac - bd) + j(ad + bc)
```

### Complex Division
```
(a + jb) / (c + jd) = [(ac + bd) + j(bc - ad)] / (c² + d²)
```

Division by zero occurs when `c² + d² = 0`.

## 👥 Contributors

- **Jeremias**: MUL, DIV, DELETE operations + tests
- **Deon**: PUSH, POP, ADD, SUB operations + tests

## 🔗 References

1. Unix `dc` manual page
2. Kent Beck - Test-Driven Development
3. ECSE 428 Assignment A Specification