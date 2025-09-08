from tracker import ExpenseTracker
from datetime import datetime

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Category Summary")
        print("5. Delete Expense by Index")
        print("6. Filter by Month/Year")
        print("7. Search by Category")
        print("8. Search by Date Range")
        print("9. Export Summary to JSON")
        print("0. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            category = input("Enter category: ")
            try:
                amount = input("Enter amount: ")
            except ValueError:
                print("Invalid amount!")
                continue
            
            date_str = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
            if not date_str.strip():
                date_str = None
                
            try:
                tracker.add_expense(category, amount, date_str)
                tracker.save_expenses()
                print("Expense added and saved!")
            except ValueError as e:
                print(e)
        
        elif choice == '2':
            tracker.view_expenses()
        
        elif choice == '3':
            tracker.total_expenses()
            
        elif choice == '4':
            tracker.category_summary()
            
        elif choice == '5':
            tracker.view_expenses()
            
            try:
                index = int(input("Enter expense index to delete: ")) -1
                tracker.delete_expense(index)
                tracker.save_expenses()
            except ValueError:
                print("Invalid innput.")
            
        elif choice == '6':
            try:
                month = int(input("Enter month (1-12): "))
                year = int(input("Enter year: "))
                tracker.filter_by_month_year(month, year)
            except ValueError:
                print("Invalid input.")
                
        elif choice == '7':
            category = input("Enter category to search: ")
            tracker.search_by_category(category)
            
        elif choice == '8':
            start_str = input("Enter start date (YYYY-MM-DD): ")
            end_str = input("Enter end date (YYYY-MM-DD): ")
            try:
                start = datetime.strptime(start_str,"%Y-%m-%d").date()
                end = datetime.strptime(end_str, "%Y-%m-%d").date()
                tracker.search_by_date_range(start, end)
            except ValueError:
                print("Invalid date format.")
                
        elif choice == '9':
            tracker.export_summary()
            
        elif choice == '0':
            tracker.save_expenses()
            print("Expenses saved. Goodbye!")
            break
        
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":           
    main()
    
    