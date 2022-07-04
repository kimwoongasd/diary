import string
from django.core.exceptions import ValidationError

def contains_special_character(value):
    for ch in str(value):
        if ch in string.punctuation:
            return True
    return False
    
def validate_no_numbers(value):
    for ch in value:
        if ch.isdigit():
            raise ValidationError('숫자는 들어갈 수 없습니다.')
        
def validate_score(value):
    if 0 > value or 10 < value:
        raise ValidationError('0부터 10사이의 숫자만 입력 가능합니다.')

def contains_uppercase(value):
    for char in value:
        if char.isupper():
            return True
    return False

def contains_lowercase(value):
    for char in value:
        if char.islower():
            return True
    return False
    
def contains_number(value):
    for char in value:
        if char.isdigit():
            return True
    return False

class CustomPasswordValidator:
    def validate(self, password, user=None):
        if (
                len(password) < 8 or
                not contains_uppercase(password) or
                not contains_lowercase(password) or
                not contains_number(password) or
                not contains_special_character(password)
        ):
            raise ValidationError("8자 이상의 영문 대/소문자, 숫자, 특수문자 조합이어야 합니다.")

    def get_help_text(self):
        return "8자 이상의 영문 대/소문자, 숫자, 특수문자 조합을 입력해 주세요."
    
def validate_no_special_characters(value):
    if contains_special_character(value):
        raise ValidationError("특수문자를 포함할 수 없습니다.")