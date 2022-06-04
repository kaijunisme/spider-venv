from sqlalchemy.types import Integer, String, Text

class Big:
    START_TERM = "093001"
    TYPE = "1"
    NAME = "big"
    CSV_FILE_ROUTE = "./Lottery/" + NAME + ".csv"

    def __init__(self) -> None:
        pass