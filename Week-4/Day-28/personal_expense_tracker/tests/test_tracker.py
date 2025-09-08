import unittest
import os
import json
from datetime import timedelta, date
from tracker import ExpenseTracker

class TestExpenseTracker(unittest.TestCase):
    
    def setUp(self):
        self.test_file = "test_expenses.csv"
        self.tracker = ExpenseTracker(filename=self.test_file)
        self.tracker.expenses = []
        self.tracker.save_expenses()
        
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists("summary.json"):
            os.remove("summary.json")
            
    def test_add_expense(self):
        self.tracker.add_expense("food", 50, '2025-09-08')
        self.tracker.save_expenses()
        self.assertEqual(len(self.tracker.expenses), 1)
        self.assertEqual(self.tracker.expenses[0].category, 'food')
        self.assertEqual(self.tracker.expenses[0].amount, 50)
    
    def test_reject_invalid_amount(self):
        with self.assertRaises(ValueError):
            self.tracker.add_expense('travel',-100,'2025-08-08')
    
    def test_delete_expense(self):
        self.tracker.add_expense('food',100,'2025-08-09')
        self.tracker.save_expenses()
        self.tracker.delete_expense(0)
        self.tracker.save_expenses()
        self.assertEqual(len(self.tracker.expenses), 0)
        
    def test_total_expenses(self):
        self.tracker.add_expense('travel',30)
        self.tracker.add_expense('food',100)
        total = sum(e.amount for e in self.tracker.expenses)
        self.assertEqual(total, 130)
        
    def test_category_summary(self):
        self.tracker.add_expense('food', 100)
        self.tracker.add_expense('food',150)
        self.tracker.add_expense('travel', 100)
        foodTotal = sum( e.amount for e in self.tracker.expenses if e.category == 'food')
        self.assertEqual(foodTotal, 250)
        
        
    def test_filter_by_month_year(self):
        today = date.today()
        last_month = today - timedelta(days=30)
        self.tracker.add_expense('food',100, today.isoformat())
        self.tracker.add_expense('travel',150, last_month.isoformat())
        results = [ e for e in self.tracker.expenses if e.date.month == today.month and e.date.year == today.year]
        self.assertEqual(len(results), 1)
        
    def test_search_by_category(self):
        self.tracker.add_expense('food', 10)
        self.tracker.add_expense('travel',20)
        results = [ e for e in self.tracker.expenses if e.category.lower() == 'food']
        self.assertEqual(len(results), 1)
    
    def test_export_summary(self):
        self.tracker.add_expense('food', 50)
        self.tracker.export_summary()
        self.assertTrue(os.path.exists('summary.json'))
        with open('summary.json', 'r') as f:
            data = json.load(f)
        self.assertIn('food', data['by_category'])
        

if __name__ == "__main__":
    unittest.main()