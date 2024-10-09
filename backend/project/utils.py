import traceback

from django.db import transaction
from rest_framework.exceptions import APIException
from django.utils.translation import gettext_lazy as _


class ExceptionWithMessage(APIException):
    status_code = 400
    default_detail = _('Ошибка')

    def __init__(self, detail='Ошибка', code=400):
        self.detail = detail
        self.status_code = code
        super().__init__(detail, code)


def atomic_transaction(message='Произошла ошибка, обратитесь к администратору'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                with transaction.atomic():
                    return func(*args, **kwargs)
            except ExceptionWithMessage as e:
                raise e
            except Exception as e:
                print(traceback.format_exc())
                raise ExceptionWithMessage(message)
        return wrapper
    return decorator
