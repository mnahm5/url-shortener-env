import random
import string

def code_generated(size=6, chars=string.ascii_lowercase + string.digits):
    code = ''
    for _ in range(size):
        code += random.choice(chars)
    return code

def create_shortcode(instance, size=6):
    new_code = code_generated(size=size)
    ShortenedUrlClass = instance.__class__
    qs_exists = ShortenedUrlClass.objects.filter(shortCode=new_code).exists()

    if qs_exists:
        return create_shortcode(instance, size=size)
    return new_code