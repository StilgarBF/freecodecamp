class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})
    
    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({'amount': amount*-1, 'description': description})
            return True
        return False
    
    def get_balance(self, only_deposit = False):
        if only_deposit:
            return sum(entry['amount'] for entry in self.ledger if entry['amount'] < 0)
        else:
            return sum(entry['amount'] for entry in self.ledger)
    
    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {destination.name}')
            destination.deposit(amount, f'Transfer from {self.name}')
            return True
        return False
    
    def check_funds(self, amount):
        return self.get_balance() >= amount
    
    def __str__(self):
        """
        Returns a string representation of the object, formatted to display the name
        centered within 30 asterisks, followed by a list of categories and their 
        corresponding amounts, and the total balance.
        The ledger entries are grouped by their description and summed up.
        Returns:
            str: A formatted string representation of the object.
        Example output:
        **********Name****************
        Category1               123.45
        Category2                67.89
        Total: 191.34
        """
        ret = f"{self.name.center(30,'*')}"
        categories = {}
        for entry in self.ledger:
            cat = entry['description']
            amount = entry['amount']

            if cat in categories:
                categories[cat] += amount
            else:
                categories[cat] = amount
            
        for cat, amount in categories.items():
            ret += f"\n{cat[:23]:<23}{amount:7.2f}"
        
        total = self.get_balance()
        ret += f"\nTotal: {total:.2f}"
        return ret

def create_spend_chart(categories):
    """
    Creates a bar chart showing the percentage of spending by category.
    Args:
        categories (list): A list of category objects. Each category object must have a 'name' attribute and a 'get_balance' method that returns the total spent in that category.
    Returns:
        str: A string representing the bar chart.
    Example:
        categories = [
            Category("Food", 105.55),
            Category("Entertainment", 33.40),
            Category("Business", 10.90)
        ]
        print(create_spend_chart(categories))
    Sample Output:
        Percentage spent by category
        100|          
         90|          
         80|          
         70|          
         60|          
         50|    o     
         40|    o     
         30|    o     
         20|    o  o  
         10| o  o  o  
          0| o  o  o  
            ----------
             F  E  B  
             o  n  u  
             o  t  s  
             d  e  i  
                r  n  
                t  e  
                a  s  
                i  s  
                n     
                m     
                e     
                n     
                t     
    """
    spent = []
    total = 0

    ret = "Percentage spent by category\n"

    for cat in categories:
        balance = cat.get_balance(True)
        spent.append((cat.name, balance))
        total += balance

    percents = [(name, int((amount / total) * 100 // 10) * 10) for name, amount in spent]

    for i in range(100, -1, -10):
        ret += f'{i:>3}| '+'  '.join('o' if percent >= i else ' ' for _, percent in percents) + "  \n"
    
    ret += '    ' + '-' * (3 * len(percents) + 1)

    cat_names = [name for name, amount in percents]
    max_length = max(len(name) for name in cat_names)
    cat_names = [name.ljust(max_length) for name in cat_names]

    for i in range(max_length):
        ret += "\n     " + '  '.join(name[i] for name in cat_names) + '  '
    return ret
# totally misunderstanding the requirements for create_spend_chart
# made me waste a lot of time here - a LOT of time!!!!
# Maybe I should have read the requirements more carefully
# - especially the "only deposits" part
