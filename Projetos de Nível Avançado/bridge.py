from abc import ABC, abstractmethod

class DataIngestion(ABC):
    @abstractmethod
    def extract_data(self):
        pass

    @abstractmethod
    def transform_data(self):
        pass

    @abstractmethod
    def load_data(self):
        pass

class ETLRemote:
    def __init__(self, data_ingestion: DataIngestion) -> None:
        self.data_ingestion = data_ingestion

    def ingest_data(self):
        data = self.data_ingestion.extract_data()
        print(data)
        data_transformed = self.data_ingestion.transform_data()
        print(data_transformed)
        data_loaded = self.data_ingestion.load_data()
        print(data_loaded)

class ExportFiles(ETLRemote):
    def export_csv(self):
        data = self.data_ingestion.extract_data()
        print(data)
        print("Exportando dados para CSV")


class WebScrapingPage1(DataIngestion):
    
    def extract_data(self):
        return "Extraindo dados na página web"

    def transform_data(self):
        return "Transformando dados da página web"

    def load_data(self):
        return "Carregando dados da página web"

class GoogleDriveFolder(DataIngestion):
    
    def extract_data(self):
        return "Extraindo dados da pasta do google drive"

    def transform_data(self):
        return "Transformando dados da pasta do google drive"

    def load_data(self):
        return "Carregando dados da pasta do google drive"

class ClientCode:
    def main(self):
        google_drive = GoogleDriveFolder()
        etl = ETLRemote(google_drive)
        etl.ingest_data()
        export_file = ExportFiles(google_drive)
        export_file.export_csv()

client_code = ClientCode()
client_code.main()