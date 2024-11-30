"""Mongo Demo using pymongo"""
from pymongo import MongoClient

class MongoTransfer:
    """Transfer mongo db"""
    def __init__(self):
        self.source = MongoClient("mongodb+srv://dalei:oarnud9I@analytics.fegzyn1.mongodb.net/?" +
                     "retryWrites=true&w=majority&appName=analytics")
        self.target = MongoClient("mongodb://root:example@localhost:27017")
        self.transfer()

    def transfer(self):
        """Transfer mongo db"""
        for db_item in self.source.list_databases():
            db_name = db_item["name"]
            if db_name.startswith("sample_"):
                self.target.drop_database(db_name)

                db = self.source.get_database(db_name)
                for col_item in db.list_collections():
                    col_name = col_item["name"]
                    col = db.get_collection(col_name)
                    print(f"database: {db_name}, collection: {col_name}")
                    documents = col.find({})
                    for document in documents:
                        self.target[db_name][col_name].insert_one(document)


if __name__ == "__main__":
    mongo_transfer = MongoTransfer()
    print("success")
