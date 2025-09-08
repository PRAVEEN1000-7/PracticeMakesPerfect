from datetime import date, datetime

class Expense:
    
    def __init__(self, category, amount, date_str=None):
        self.category = category
        self.amount = float(amount)
        if self.amount <=0:
            raise ValueError("Amount must be positive.")
        
        if date_str:
            try :
                self.date = datetime.strptime(date_str,"%Y-%m-%d").date()
            except ValueError:
                raise ValueError("Invalid date format. Use YYYY-MM-DD.")
        else:
            self.date = date.today()

    def to_dict(self):
        return {
            'date': self.date.isoformat(),
            'category': self.category,
            'amount': self.amount
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            category=data['category'],
            amount=float(data['amount']),
            date_str=data['date']
        )
            
        