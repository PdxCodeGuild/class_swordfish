# notes

## 11/29/22

#### The Django Project Setup STATICFILES_DIRS ERROR has been causing issues:
1. Instead of using the `os.path.join`  I can use `'DIRS': [BASE_DIR / 'templates']` 
2.  We also use `STATICFILES_DIRS = [BASE_DIR / 'static']` instead of `os.path.join` etc from the template.


#### lookup what `BASE_DIR = Path(__file__).resolve().parent.parent` is within the django settings

1. ACTION: Will Vincent Custom User tutorial google search for creating users in Django will help with the next section
2. ACTION: Look up django request information and background execution info