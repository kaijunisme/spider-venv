from sqlalchemy.types import Integer, String, Text

class Power:
    START_TERM = "097001"
    TYPE = "2"
    NAME = "power"
    CSV_FILE_ROUTE = "./Lottery/" + NAME + ".csv"

    def __init__(self) -> None:
        pass