class Category:
    
    category_list = []

    def __init__(self, name):
        self.name = name
        self.category_list.append(self)
        self.ledger = []

    # Method to deposit funds to budget object
    def deposit(self, amount, description=""):
        amount = float(amount)
        item = {}
        item.update({"amount" : amount, "description" : description})
        self.ledger.append(item)

    # Method to withdraw funds from budget object
    def withdraw(self, amount, description=""):
        if self.check_funds(amount) == True:
            amount = -abs(amount)
            amount = float(amount)
            item = {}
            item.update({"amount" : amount, "description" : description})
            self.ledger.append(item)
            return True
        else:
            return False

    # Method to get the remaining balance of funds for budget object
    def get_balance(self):
        k = []
        for i in self.ledger:
            j = i.get("amount")
            k.append(j)
        
        balance = k[0]
        for l in k:
            if l == k[0]:
                continue

            if l == abs(l):
                balance += l
            else:
                l = abs(l)
                balance -= l

        return balance

    # Method to check fund availability in budget object
    def check_funds(self, amount):
        amount = float(amount)
        if amount > self.get_balance():
            return False
        else:
            return True
        
    # Method to transfer funds to another budget object
    def transfer(self, amount, budget_category):
        if self.check_funds(amount) == True:
            self.withdraw(amount, f"Transfer to {budget_category.name}")
            budget_category.deposit(amount, f"Transfer from {self.name}")

    # Method to get the percentage of funds spent in budget object
    def get_spending_percent(self):
        k = []
        for i in self.ledger:
            j = i.get("amount")
            k.append(j)
        
        deposits = k[0]
        withdrawals = 0
        for i in k:
            if i == k[0]:
                continue
            
            if i == abs(i):
                deposits += i
            else:
                i = abs(i)
                withdrawals += i
        
        spending_percent = (withdrawals/deposits) * 100
        rounded_spending_percent = round(spending_percent)
        round_to_10 = round(rounded_spending_percent/10) * 10
        return round_to_10
   
    # Method to print out budget object
    def __str__(self):
        f = f"{self.name.center(30, '*')}\n"
        l = []
        for i in self.ledger:
            description = i.get('description')
            amount = i.get('amount')
            amount = f"{amount:.2f}"
            if len(amount) <= 7:
                amended_amount = amount
    
            amended_desc = ""
            if len(description) <= 23:
                for i in description:
                    amended_desc += i
            else:
                for i in description[0:23]:
                    amended_desc += i
            spaces = " " * (30 - ((len(amended_desc)) + (len(amended_amount))))
            result = f"{amended_desc}{spaces}{amended_amount}\n"
            l.append(result)
           
        balance = self.get_balance()
        remainder = f"Total: {balance}"
        m = (("").join(n for n in l))
        return f + m + remainder
    
def create_spend_chart(categories):
    # Mapping list of variables to budget objects
    count = 0
    for i in categories:
        i = Category.category_list[count]
        count += 1
    
    # Calculating spending % for each budget object 
    l = []
    for i in categories:
        spending = i.get_spending_percent()
        l.append(spending)

    # Creating spending bar chart
    title = "Percentage spent by category\n"
    bar_graph = []
    for i in range(100, -10, -10):
        bar_graph.append(f"{str(i).rjust(3)}| {'  '.join(['o' if digit >= i else ' ' for digit in l])}\n")
    dashes = f"{' ' * 4}{'-'*(len(l)+ 7)}\n"
    graph = (''.join(bar_graph))

    q = []
    for i in categories:
        q.append(i.name)

    l = len(q[0])
    for i in q:
        if len(i) > l:
            l = len(i)


    names = []
    for i in range(0, l):
            try:
                names.append(f"{' ' * 5}{'  '.join([digit[i] if len(digit) >= i else ' ' for digit in q])}\n")
            except IndexError:
                names.append(f"{' ' * 5}{'  '.join([' ' if len(digit) <= i else digit[i] for digit in q])}\n")
    category_names = f"{(''.join(names))}"
    
    return title + graph + dashes + category_names