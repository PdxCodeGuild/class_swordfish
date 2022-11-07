from django.conf import settings
from random import choice
from string import ascii_letters, digits

SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 7) #getattribute/variable; make the random code 7 digits
AVAILABLE_CHARS = ascii_letters + digits

def create_random_code(chars=AVAILABLE_CHARS):
    return "".join([choice(chars) for _ in range(SIZE)])

def create_shortened_url(model_instance):
    random_code = create_random_code()
    model_class = model_instance.__class__
    if model_class.objects.filter(short_url=random_code).exists(): #make sure the short code doesn't match previous ones
        return create_shortened_url(model_instance) #get a new random code & recheck it
    return random_code