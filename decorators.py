import functools

from toolbox.errors import ToolboxError, return_formatted_error


def safe_run(function_for_check):
    """
    Decorator for handling exception which can be raised on decorated functions
    to return only None or value from return_value arg
​
    """

    @functools.wraps(function_for_check)
    def wrapper(*args, **kwargs):
        try:
            return function_for_check(*args, **kwargs)
        except ToolboxError as exception:
            return return_formatted_error(exception)

    return wrapper
