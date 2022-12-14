import os
from azure.data.tables import TableServiceClient


class AzureTableRepository:
    def __init__(self, db_name: str):
        self.table_service_client = TableServiceClient.from_connection_string(
            os.getenv('AZURE_TABLE_CONN')
        )
        self.table_client = self.table_service_client.get_table_client(
            table_name=db_name
        )

    def get(self, filter):
        entities = self.table_client.query_entities(filter)
        return entities

    def create(self, model):
        result = self.table_client.create_entity(entity=model)
        return result

    def create_if_not_exists(self, model, rowkey):
        result = self.table_client.query_entities(f"RowKey eq '{rowkey}'")
        if result is None:
            self.create(model)
        else:
            self.update(model)

    def update(self, model):
        self.table_client.update_entity(entity=model)

    def batch_update(self, models):
        for model in models:
            self.table_client.update_entity(entity=model)
