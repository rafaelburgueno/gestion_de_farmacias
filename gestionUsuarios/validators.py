from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class ConsecutivelyRepeatingCharacterValidator:
    def __init__(self, length=4):
        self.length = length

    def validate(self, password, user=None):
        for character in password:
            if password.count(character) >= self.length:
                check_character = character * self.length

                if check_character in password:
                    raise ValidationError(
                            _("La contraseña contiene caracteres que se repiten consecutivamente. por ejemplo, 1111 o aaaa")
                            )

    def get_help_text(self):
        return _("Los caracteres de la contraseña no se pueden repetir consecutivamente. P.ej. 1111 o aaaa")

class ConsecutivelyIncreasingIntegerValidator:
    def __init__(self, length=4):
        self.length = length

    def validate(self, password, user=None):
        for character in password:
            if character.isdigit():
                count = 0
                number = int(character)
                index = password.index(character)

                try:
                    for i in range(1, self.length):
                        if password[index+i].isdigit():
                            if int(password[index+i]) == number + 1:
                                count += 1
                                number += 1

                                while count >= self.length - 1:
                                    raise ValidationError(
                                        _("La contraseña contiene números enteros que aumentan consecutivamente. P.ej. 1234")
                                    )
                except IndexError:
                    pass

    def get_help_text(self):
        return _("Los caracteres de la contraseña no pueden contener números enteros crecientes consecutivamente. P.ej. 1234")


class ConsecutivelyDecreasingIntegerValidator:
    def __init__(self, length=4):
        self.length = length

    def validate(self, password, user=None):
        for character in password:
            if character.isdigit():
                count = 0
                number = int(character)
                index = password.index(character)

                try:
                    for i in range(1, self.length):
                        if password[index+i].isdigit():
                            if int(password[index+i]) == number - 1:
                                count += 1
                                number -= 1

                                while count >= self.length - 1:
                                    raise ValidationError(
                                        _("La contraseña contiene números enteros decrecientes consecutivamente. P.ej. 4321")
                                    )
                except IndexError:
                    pass

    def get_help_text(self):
        return _("Los caracteres de la contraseña no pueden contener números enteros decrecientes consecutivamente. P.ej. 4321")

class ConsecutivelyIncreasingAlphabetValidator:
    def __init__(self, length=4):
        self.length = length

    def validate(self, password, user=None):
        for character in password:
            if character.isalpha():
                count = 0
                index = password.index(character)

                try:
                    for i in range(1, self.length):
                        if password[index+i].isalpha():
                            if ord(password[index+i]) == ord(character) + 1:
                                count += 1
                                character = chr(ord(character) + 1)

                                while count >= self.length - 1:
                                    raise ValidationError(
                                        _("La contraseña contiene alfabetos que aumentan consecutivamente. P.ej. abcd")
                                    )
                except IndexError:
                    pass

    def get_help_text(self):
        return _("Los caracteres de la contraseña no pueden contener alfabetos que aumenten consecutivamente. P.ej. abcd")

class ConsecutivelyDecreasingAlphabetValidator:
    def __init__(self, length=4):
        self.length = length

    def validate(self, password, user=None):
        for character in password:
            if character.isalpha():
                count = 0
                index = password.index(character)

                try:
                    for i in range(1, self.length):
                        if password[index+i].isalpha():
                            if ord(password[index+i]) == ord(character) - 1:
                                count += 1
                                character = chr(ord(character) - 1)

                                while count >= self.length - 1:
                                    raise ValidationError(
                                        _("La contraseña contiene alfabetos decrecientes consecutivos. P.ej. dcba")
                                    )
                except IndexError:
                    pass

    def get_help_text(self):
        return _("Los caracteres de la contraseña no pueden contener alfabetos decrecientes consecutivos. P.ej. dcba")



