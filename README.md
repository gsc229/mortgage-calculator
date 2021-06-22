## Pipenv Environment Manager

>You can use pip to install Pipenv
>```
>$ pip install --user pipenv
>```
>[Pipenv Documentation](https://pipenv.pypa.io/en/latest/install/)
>After install run:
>```
>$ pipenv shell
>```
>When shell is running, run command:
>```
>$ pipenv install
>```
> This will install all the dependencies in the Pipfile.
> You can now use all the normal Django manage.py commands from inside the pipenv shell.
## Starting The Server
>While still in the pipenv shell run:
>```
>$ python manage.py runserver
>```
>The server should now be running on localhost:8000.
>Open browser and navigate to localhost:8000.

## Using the APP
> localhost:8000
>|endpoints| request | description  |
>|--|--|--|
>| / | POST  | takes you to a basic calculator |
>| /bulk-calculate | POST  | file uploader for bulk calculations |
>### Bulk Calculations
>You can upload .txt files with data in the form:
>```
>amount: 100000 
>interest: 5.5% 
>downpayment: 20000 
>term: 30
>
>amount: 150000 
>interest: 5.2% 
>downpayment: 23000 
>term: 30
>```
>Data should be separated by a space.
>There is a loanData.txt file in the root directory for you to try.
>Also, there is a 'Send JSON' option in the bulk-calculate endpoint for you to get back raw JSON Data.
## Testing
> In the pipenv shell run:
>```
>python mange.py test pages
>```
>You can find the test file in the pages. It's called test_calc.py.
>It tests the root calculation which generates the results.
