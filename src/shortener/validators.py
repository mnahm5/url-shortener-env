from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_url(url):
    url_validator = URLValidator()

    flag_1 = False
    flag_2 = False

    try:
        url_validator(url)
    except:
        flag_1 = True
    try:
        url_validator("http://" + url)
    except:
        flag_2 = True

    if flag_2 == False and flag_1 == False:
        raise ValidationError("Invalid Url for this field")
    return url