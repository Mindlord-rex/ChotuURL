from django.conf import settings
from random import choices
from string import ascii_letters, digits

SIZE = getattr(settings, 'SIZE', 6)

AVAILABLE_CHARS = ascii_letters + digits

def arbitary_code(chars=AVAILABLE_CHARS):
    return ''.join(choices(chars, k=SIZE))

def generate_short_code(model_instance):
    code = arbitary_code()
    
    model_class = model_instance.__class__
    
    if model_class.objects.filter(short_url=code).exists():
        return generate_short_code(model_instance)
    return code