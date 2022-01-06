from rest_framework import status
from rest_framework.exceptions import APIException, _get_error_details
from django.utils.translation import gettext as _


class RequestBodyValidationException(APIException):
    def __init__(self, detail=None, code=None):
        super().__init__(
            {"error": "ERROR_REQUEST_BODY_VALIDATION", "detail": detail}, code=code
        )
        self.status_code = 400


class UnknownFieldProvided(Exception):
    """
    Raised when an unknown field is provided to an API endpoint.
    """


class QueryParameterValidationException(APIException):
    def __init__(self, detail=None, code=None):
        super().__init__(
            {"error": "ERROR_QUERY_PARAMETER_VALIDATION", "detail": detail}, code=code
        )
        self.status_code = 400


class ValidationError404(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _('Not found')
    default_code = 'ERR_404_NOT_FOUND'

    def __init__(self, detail=None, code=None):
        if detail is None:
            detail = self.default_detail
        if code is None:
            code = self.default_code

        self.detail = _get_error_details(detail, code)


class ValidationError400(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Bad Request')
    default_code = 'ERR_BAD_REQUEST'

    def __init__(self, detail=None, code=None):
        if detail is None:
            detail = self.default_detail
        if code is None:
            code = self.default_code

        self.detail = _get_error_details(detail, code)
