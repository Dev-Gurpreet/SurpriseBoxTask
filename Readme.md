Functionalities cover in this app: 
SignUp with email verification, 
Login, 
Logout, 
decorators (restrict user to access some pages), 
Reset password with email verification,
Paypal Integration,
subscribe and unsubcribe
Make user winner on specific number page visit. 

You can user already created user to skip Email host configuration(step 6, 7):
Username :GurpreetSingh2
password :Qwerty@12345

1. install python
2. pip install Django
3. python manage.py migrate
4. python manage.py makemigrations
5. python manage.py create superuser

6. Setup following variables with your host email and password in setting.py file
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''

7. Go to Less secure app access option of gmail account and turn it ON

8. python manage.py runserver

