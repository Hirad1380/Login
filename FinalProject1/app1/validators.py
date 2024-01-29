from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import MinimumLengthValidator, CommonPasswordValidator

class UniquePasswordValidator:
    def __init__(self, history_length=3):
        self.history_length = history_length

    def validate(self, password, user=None):
        if user and user.password_history.filter(password=password).exists():
            raise ValidationError("This password was used recently. Please choose a new one.")
        
    def get_help_text(self):
        return "Your new password must not be one of the last {} passwords you've used.".format(self.history_length)