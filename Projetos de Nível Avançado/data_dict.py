class DataDict:
    def __init__(self) -> None:
        self.database = {
            "0": "Alano",
            "1": "Myllena",
            "2": "Lucas" 
        }

    def get_clients(self):
        return self.database