from rest_framework.response import Response


ERROR_NO_ENVIRONMENT_CONFIGURED = 'CTB-404-001'
TEST_ERROR = 'CTB-TST-000'


ERROR_MESSAGES = {
    ERROR_NO_ENVIRONMENT_CONFIGURED: 'Environment setting is not configured',
    TEST_ERROR: 'Fake error message for unittests'
}


class ToolboxError(Exception):
    """
    Basic class for Toolbox internal errors
    """

    __error_code = None
    __details = None

    def __init__(self, error_code, details=None):
        super(ToolboxError, self).__init__()
        self.__error_code = error_code
        if details:
            self.__details = details

    def __get_message(self):
        return ERROR_MESSAGES[self.__error_code]

    def __get_description(self):
        if self.__details:
            return self.__details
        else:
            return self.__get_message()

    def get_data(self):
        return dict(
            error=self.__error_code,
            message=self.__get_message(),
            description=self.__get_description()
        )

    def get_status(self):
        return int(self.__error_code.split('-')[1])

    def __str__(self):
        return '{code}: {message}'.format(
            code=self.__error_code,
            message=self.__get_message()
        )


def return_formatted_error(error: ToolboxError):
    """
    Wrap error to response with formatted data
    :param error: Error instance
    :return: Response with formatted error
    """
    return Response(
        status=error.get_status(),
        data=error.get_data(),
    )
