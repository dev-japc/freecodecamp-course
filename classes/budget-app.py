class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def __str__(self):
        # getting name length to center name between * characters
        name_length = '*'*(int((30 - len(self.name))/2))
        category_name = name_length + self.name + name_length # the output should be a 30 length characters str
        entries = []
        for transaction in self.ledger:
            description = transaction['description'][:23]
            amount = '{:.2f}'.format(transaction['amount'])
            entries.append(f"{description.ljust(23)}{amount.rjust(7)}")
        entries.append(f"Total: {self.get_balance()}")
        return category_name+'\n'+'\n'.join(entries)


    def deposit(self, amount, description=''):
        self.amount = amount
        self.description = description        

        # deposits the specified amount to the called category's ledger
        self.ledger.append({'amount': self.amount, 'description': self.description})

    def withdraw(self, amount, description=''):
        # checking funds first
        if self.check_funds(amount):
            # withdrawing when funds are available otherwise fails
            self.ledger.append({'amount': -amount, 'description': description})
            # print(True)
            return True
        else:
            # print(f'operation-> [[{amount}, {description}]] \nNot approved, insufficient funds\ncurrent balance: {self.get_balance()}')
            return False
    
    def get_balance(self):
        # setting current balance to zero
        current_balance = 0

        # sumarizing all the amounts from self.ledger to obtain the current balance
        for operation in self.ledger:
            current_balance += operation['amount']
        return current_balance
    
    def transfer(self, amount, destination_category):
        self.destination_category = destination_category

        # checking if the current funds allows the transfer
        if self.check_funds(amount):
            # print('current_balance:'.upper(), self.get_balance())
            self.withdraw(amount, f'Transfer to {self.destination_category.name}')
            destination_category.deposit(amount, f'Transfer from {self.name}')
            # print('transfer_approved \n-->'.upper(), self.get_balance(), f'\nto: {destination_category.name}'.upper())
            return True
        else:
            # print(False)
            return False

    def check_funds(self, amount):
        return amount <= self.get_balance()



def create_spend_chart(categories):
    category_names = []
    spent = []
    
    # Obtener gastos por categoría
    for category in categories:
        total = 0
        for item in category.ledger:
            if item['amount'] < 0:
                total -= item['amount']
        spent.append(total)
        category_names.append(category.name)

    # Calcular porcentajes (redondeados hacia abajo a la decena más cercana)
    total_spent = sum(spent)
    # Importante: Usamos una lista para mantener el orden
    percentages = [int((s / total_spent * 100) // 10) * 10 for s in spent]

    # 1. Título
    res = "Percentage spent by category\n"

    # 2. El cuerpo de las barras (Eje Y)
    for i in range(100, -1, -10):
        res += f"{str(i).rjust(3)}| "
        for p in percentages:
            res += "o  " if p >= i else "   "
        res += "\n"

    # Debe ser "    " + "---" por cada categoría + "-"
    res += "    " + "-" * (3 * len(categories) + 1) + "\n"

    # 4. Nombres verticales 
    max_len = max(len(name) for name in category_names)
    
    for i in range(max_len):
        res += "     "
        for name in category_names:
            if i < len(name):
                res += name[i] + "  "
            else:
                res += "   "
        # Añadimos el salto de línea solo si NO es la última línea
        if i < max_len - 1:
            res += "\n"

    return res


food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(500.00, "groceries")

clothing = Category("Clothing")
clothing.deposit(1000, "deposit")
clothing.withdraw(100.00, "buying new clothes")

auto = Category("Auto")
auto.deposit(1000, "deposit")
auto.withdraw(200.00, "fuel")

food.transfer(200, clothing)


categories = [food, clothing, auto]
chart_str = create_spend_chart(categories)

print(clothing)
print(chart_str)