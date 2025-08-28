Personal Financial Management Application (PFM ) 
The Personal Financial Management App is a personal financial tracking solution built using Django REST Framework for the backend. The application will assist individuals, petty traders, SMEs, entrepreneurs, and organizations to take control of their finances by enabling daily expense tracking, income recording, and monthly budget planning.

✨ Core Features

Daily Expense Recording – Log daily spending with amount, category, date, and description.


Daily Income Recording – Track income sources and amounts.


Monthly Budget Setup – Set and edit monthly budgets to guide spending.


User Authentication – Secure login/logout using token authentication.


View Transaction History – View and filter past expenses and income.


Dashboard Summary – Aggregate view of total income, expenses, and balance.


🔌 Backend Technology & API
Framework: Django + Django REST Framework (DRF)


Authentication: Token Authentication (DRF’s Token Auth)


Hosting Platform: Heroku (or PythonAnywhere)

Models
1. User (Django default)
username
Email
First Name
Last Name
Location
Phone Number


2. Expense
user (FK)	
Name
amount
category
description
date


3. Income
user (FK)
Name
amount
source
description
date


4. Budget
user (FK)
Name
Amount Allocated
month (DateField - first day of the month)
Start Date
End Date



📡 Endpoint                      Method                          Description

/api/expenses/              GET/POST                .......List or create expenses

/api/expenses/id/        PUT/DELETE               .......Update/delete an expense

/api/income/                GET/POST                ......List or create income

/api/income/id/          PUT/DELETE               .......Update/delete income

/api/budgets/              GET/POST                 ........List or create budget

/api/budgets/id/         PUT/DELETE               .......Update/delete budget

/api/login/                  POST                   .......Login to get auth token




Feature updates
Create an expense category table
Creaate income source table
Budget can be setup for all created expense categories for variance analysis
Run variance for a paticular month

