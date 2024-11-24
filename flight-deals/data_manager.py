"""data manager"""
import os
import requests
import dotenv

class DataManager:
    """data manager"""
    def __init__(self):
        self.endpoint = f"{os.getenv('SHEETY_PRICES_ENDPOINT')}"
        self.headers = { "Authorization": f"{os.getenv('SHEETY_TOKEN')}" }

        response = requests.get(url=self.endpoint, timeout=10, headers=self.headers)
        self.sheet_data = response.json()["prices"]

    def update_iata_code(self, data):
        """update iata code"""
        body = { "price": data }
        requests.put(
            url=f"{self.endpoint}/{data['id']}",
            timeout=10,
            json=body,
            headers=self.headers
        )

    def get_customer_users(self):
        """get customer users"""
        response = requests.get(
            url=f"{os.getenv('SHEETY_USERS_ENDPOINT')}",
            timeout=10, headers=self.headers)
        users = response.json()["users"]
        return [user["whatIsYourEmail?"] for user in users]


if __name__ == "__main__":
    dotenv.load_dotenv()
    data_manager = DataManager()
    emails = data_manager.get_customer_users()
    print(emails)
