from django.db import models


#Creates the account model
class Account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    initial_deposit = models.DecimalField(max_digits=15, decimal_places=2)

    #defines model manager for accounts
    Accounts = models.Manager()

    #Allows references to be account owners name instead of primary key
    def __str__(self):
        return self.first_name + ' ' + self.last_name


#transaction choices
TransactionTypes = [('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')]


#creates transaction model
class Transaction(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=10, choices=TransactionTypes)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    #defines model manager for transactions
    Transactions = models.Manager()
