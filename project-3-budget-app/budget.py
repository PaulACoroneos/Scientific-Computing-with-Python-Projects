import math

class Category:

  def __init__(self,name):
    self.name = name
    self.ledger = []

  def __str__(self):
    print_str = ''
    print_str += '{:*^30}\n'.format(self.name)
    #now iterate through everything in ledger
    for item in self.ledger:
      print_str += '{:<23} {:>.2f}\n'.format(item['description'][:23],item['amount'])
    print_str += f'Total: {self.get_balance()}'
    return print_str
    
  def deposit(self, amount, description = ''):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self,amount, description=''):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False

  def get_balance(self):
    balance = 0.0
    for entry in self.ledger:
      balance += entry['amount']
    return balance

  def transfer(self,amount,budget_category):
    if self.check_funds(amount):
      self.withdraw(amount,f'Transfer to {budget_category.name.title()}')
      budget_category.deposit(amount,f'Transfer from {self.name.title()}')
      return True
    else:
      return False


  def check_funds(self, amount):
    return True if self.get_balance() - amount >= 0 else False


  


def create_spend_chart(categories):
  # lets calculate relative percentages of passed category budgets
  category_spending = {};
  for category in categories:
    #now sum up spending for each category
    for transaction in category.ledger:
      if transaction['description'] != 'deposit':
        if category.name in category_spending:
          category_spending[category.name] += float(transaction['amount'])
        else:
          category_spending[category.name] = float(transaction['amount'])
  # calculate spending sum
  spending_sum = 0.0
  for spending in category_spending.values():
    spending_sum += spending

  spend_chart = ''
  spend_chart += 'Percentage spent by category\n'
  # generate y-axis lines for bar chart
  for horizontal in range(100,-10,-10):
    # y-axis label
    spend_chart += '{:>3}|'.format(horizontal)
    # conditional bar chart value per category
    for spent in category_spending.values():
      # if spending threshold is met for this horizontal category
      if math.floor((spent/spending_sum)*100) >= horizontal:
        spend_chart += ' o '
      else:
        spend_chart += '   '
    # terminate
    spend_chart += ' \n'
  # add dash lines
  spend_chart += '    ' + '-' * (len(category_spending)+2) * 2 + '\n'

  # now handle vertical category names
  max_name_len = 0

  # find longest length name
  for name in category_spending.keys():
    max_name_len = max(max_name_len,len(name))

  #now generate strings
  for idx in range(0,max_name_len):
    spend_chart += '    '
    for name in category_spending.keys():
      # are we in bounds of len of name
      if idx < len(name):
        spend_chart += f' {name[idx]} '
      else:
        spend_chart += '   '
    # a little bit of a hack to pass whitespace requirements (2 spaces at end of line, refactor to use fixed length line later)
    if idx < max_name_len-1:
      spend_chart += ' \n'
    else:
      spend_chart += ' '
  return spend_chart