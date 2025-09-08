import csv
import os
import json
from expense import Expense

class ExpenseTracker:
    
    def __init__(self, filename="expenses.csv"):
        self.filename = filename
        self.expenses = []
        self.load_expenses()
    
    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename, mode="r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.expenses.append(Expense.from_dict(row))
    
    def save_expenses(self):
        with open(self.filename, mode="w", newline="") as file:
            fieldnames = ['date','category','amount']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for exp in self.expenses:
                writer.writerow(exp.to_dict())
    
    def add_expense(self, category, amount, date_str=None):
        exp = Expense(category, amount, date_str)
        self.expenses.append(exp)
    
    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        for i, exp in enumerate(self.expenses, start=1):
            print(f"{i}. {exp.date} | {exp.category} | {exp.amount:.2f}")
    
    def total_expenses(self):
        total = sum(exp.amount for exp in self.expenses)
        print(f"Total Expenses: {total:.2f}")
        
    def category_summary(self):
        summary={}
        for exp in self.expenses:
            summary[exp.category] = summary.get(exp.category, 0) + exp.amount
        for cat, amt in summary.items():
            print(f"{cat}: {amt:.2f}")
        
    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            removed = self.expenses.pop(index)
            print(f"Deleted: {removed.category} {removed.amount:.2f} on {removed.date}")
        else:
            print("Invalid index.")
            
    def filter_by_month_year(self, month, year):
        results = [ exp for exp in self.expenses if exp.date.month==month and exp.date.year==year]
        self._print_filtered(results)
        
    def search_by_category(self, category):
        results = [exp for exp in self.expenses if exp.category.lower() == category.lower()]
        self._print_filtered(results)
        
    def search_by_date_range(self, start_date, end_date):
        results = [exp for exp in self.expenses if start_date <= exp.date <= end_date]
        self._print_filtered(results)
    
    def export_summary(self, filename="summary.json"):
        summary={}
        for exp in self.expenses:
            summary[exp.category] = summary.get(exp.category, 0) + exp.amount
        total = sum(exp.amount for exp in self.expenses)
        data = {'total': total, 'by_category':summary}
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Summary exported to {filename}")

    def _print_filtered(self, expenses):
        if not expenses:
            print("No matching expenses found.")
            return
        for i, exp in enumerate(expenses, start=1):
            print(f"{i}. {exp.date} | {exp.category} | {exp.amount:.2f}")


