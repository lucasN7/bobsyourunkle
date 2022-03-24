from django.core.exceptions import ValidationError
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


def django_error_handler(exc, context):
	"""Handle django core's errors."""

	# Call REST framework's default exception handler first,
	# to get the standard error response.
	response = exception_handler(exc, context)
	# print ValidationError nicely
	if response is None and isinstance(exc, ValidationError):
		return Response(status=400, data=exc.message_dict)
	# try to catch and print exceptions to debug
	if response is None:
		status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
		return Response({"details " : repr(exc)}, status=status_code)
	return response