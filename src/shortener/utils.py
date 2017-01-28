import random
import string

from django.conf import settings

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6)

def code_generated(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):
    code = ''
    for _ in range(size):
        code += random.choice(chars)
    return code

def create_shortcode(instance, size=SHORTCODE_MIN):
    new_code = code_generated(size=size)
    ShortenedUrlClass = instance.__class__
    qs_exists = ShortenedUrlClass.objects.filter(shortCode=new_code).exists()

    if qs_exists:
        return create_shortcode(instance, size=size)
    return new_code