import traceback


class DataSSBaseException(Exception):
    """
    param pandas.DataFrame df: dataframe base exception

    :param str message: exception message
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
