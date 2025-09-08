# Day 28 - Mini Project (Capstone)

*Personal Expense Tracker (CLI)*

## Project Completed ✅
- **Personal Expense Tracker** - Full-featured CLI application for expense management

## What I Learned
- Object-oriented design with multiple classes
- CSV file handling for data persistence
- JSON export functionality
- Command-line interface (CLI) development
- Comprehensive error handling and input validation
- Unit testing with setUp and tearDown methods
- Date and time manipulation
- Modular code organization and separation of concerns

## Solution Approaches Implemented
1. **Modular Design:** Separate classes for Expense, ExpenseTracker, and CLI interface
2. **Data Persistence:** CSV file storage with automatic load/save functionality
3. **Comprehensive Testing:** Unit tests covering core functionality and edge cases

## Key Concepts
- **Expense Class:** Single expense representation with validation
- **ExpenseTracker Class:** Manages multiple expenses with CRUD operations
- **CLI Interface:** User-friendly menu system with input validation
- **Data Validation:** Reject invalid amounts and handle date formatting
- **File Operations:** CSV reading/writing and JSON export

## Code Structure
```python
# Modular Design: Separate classes for data model, business logic, and UI
# Data Persistence: CSV storage with automatic backup and recovery
```

## Features Implemented
- Add/view/delete expenses
- Category-based expense grouping
- Date filtering and search functionality
- Total expense calculation
- Summary export to JSON
- Comprehensive error handling
- Unit test coverage

## Files
- `expense.py` (Expense class)
- `tracker.py` (ExpenseTracker class)
- `main.py` (CLI interface)
- `tests/test_tracker.py` (Unit tests)
- `expenses.csv` (Data storage)
- `summary.json` (Export file)

## How to Run
1. **Run the application:**
   ```bash
   python main.py
   ```

2. **Run unit tests:**
   ```bash
   python -m unittest discover tests
   ```

3. **Navigate through the menu:**
   - Use numbers 1-9 to select options
   - Follow prompts for data entry
   - Use 0 to exit and save data

---
**Progress:** 62 problems completed (Week 4 finished!)