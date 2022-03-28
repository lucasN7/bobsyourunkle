# Lucas attemp at Unkle's backend use case in Django

## Bonjour! 

And welcome to Lucas' attempt to implement Unkle backend use case. It's called Bob's your uncle in reference to the [idiom](https://www.urbandictionary.com/define.php?term=Bob%27s%20your%20uncle) I've recently learnt and I like , and... Unkle.

I chose English to write the entire project because		
- I think it's good practice to write code and comments in English, you never know when you'll become a successfull international webapp??
- My laptop is Aussie so my keyboard is still a QWERTY => French accents are a pain right now ^_^'

## Stack

1. Django: 3.2.12 => seems to be the best compromise between stability and features (tried 4.0.x but straight up gave me some difficulties)
2. Python: 3.8 => seems to work well with Django 3.2.12 (from my short experience)
3. Database: Sqlite => easy to get going for you to test even if I prefer Postgres
4. Dev Testing: Postman => I quite like it and I'm used to it

## Author's way to run the project
1. Install a Python 3.8 virtual environment and install libraries from the requirements.txt:
* pip install -r requirements.txt
3. Initialize the database: 
*   python manage.py migrate
*   python manage.py loaddata core\fixtures\contract_options_fixture.yaml 
4. Create a super-user: 
* python manage.py create_superuser
5. Recommanded to test: download Postman and use the provided postman collection: 
* Import the postman environment 
* Import the postman collection
* Use the credentials of the superuser you created in the Postman API call "Auth superuser" and then any call is available
* Note that in the Postman "Tests" tab of the "Auth" calls, the generated token is programatically set in the global variables. You don't have to manage that. Just authenticate with the user you want and all subsequent calls with be using the generated token.  

## Notes
1. I wanted to implemented automated unit tests in Python but I've ran out of time (never done automated test in Python so it's a bit of an exploration). I will actually try in the coming week for my own knowledge but I'm already due. 
