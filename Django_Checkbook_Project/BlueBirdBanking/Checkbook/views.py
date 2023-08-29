from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction


#Function renders home page when called
def home(request):
    form = TransactionForm(data=request.POST or None)  # retrieve transaction form
    #checks if request method is post
    if request.method == 'POST':
        pk = request.POST['account']  # if the form is submitted, retrieve which account the user wants to view
        return balance(request, pk)  # calls balance function to render that account's balance sheet
    content = {'form': form}  # pass content to the template in a dictionary
    # adds the content of the form to the page
    return render(request, 'checkbook/index.html', content)


#Function renders create new account page when called
def create_account(request):
    form = AccountForm(data=request.POST or None)  # retrieves the account form
    #checks if request method is post
    if request.method == 'POST':
        if form.is_valid():  # checks if form is valid, saves it if so
            form.save()  # saves new account
            return redirect('index')  # returns user back to home page
    content = {'form': form}  # saves content to the template as a directory
    #adds content of form to page
    return render(request, 'checkbook/CreateNewAccount.html', content)


#function renders the balance page when called
def balance(request, pk):
    account = get_object_or_404(Account, pk=pk)  # retrieves the requested account using its primary key
    transactions = Transaction.Transactions.filter(account=pk)  # retrieves all of that accounts transactions
    current_total = account.initial_deposit  # creates account total variable, starting with initial deposit value
    table_contents = {}  # creates a dictionary into which transaction information is placed
    for t in transactions:  # loops through transactions and determines which is a deposit and which is a withdrawal
        if t.type == 'Deposit':
            current_total += t.amount  # if it is a deposit it will add amount to the balance
            table_contents.update({t: current_total})  # adds total and transaction to the dictionary
        else:
            current_total -= t.amount  # if it is a withdrawal subtract amount from balance
            table_contents.update({t: current_total})  # adds total and transaction to the dictionary
    # pass account, account total balance, and transaction information to the template
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)


#function renders the transaction page when called
def transaction(request):
    form = TransactionForm(data=request.POST or None)  # retrieves the transaction form
    # checks if request method is POST
    if request.method == 'POST':
        if form.is_valid():  # checks if form is valid, saves it if so
            pk = request.POST['account']  # retrieves which account the transaction was for
            form.save()  # saves the transaction form
            return balance(request, pk)  # renders balance of the accounts balance sheet
            #return redirect('index')  # redirects the user to the home page after form submission
    #passes content to the template in a directory
    content = {'form': form}
    #adds content of form to the page
    return render(request, 'checkbook/AddTransaction.html', content)
