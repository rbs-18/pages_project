from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def bitrate_validator(value):
    """ Validation for bitrate field in Audio model. """

    if value < 0:
        raise ValidationError(
            _('%(value)s is not a positive number'),
            params={'value': value},
        )
