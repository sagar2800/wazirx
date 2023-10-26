import time
import requests
from wazirx_sapi_client.rest import Client

class Bot:
    def __init__(self):
        # initialize a new instance of the WazirX API client
        self.client = Client()
        # list of assets to monitor
        self.assets = ["usdt","busd"]

    def get_wazirx_highest_price_today(self, asset):
        # if the response is successful, break out of the loop
        while True:
            response = self.client.send("ticker",{'symbol':f"{asset}inr"})
            if response[0] == 200:
               break
            time.sleep(2)

        # extract the highest price for the day from the API response
        highest_price = float(response[1]['highPrice'])
        return highest_price

    def send_telegram_notification(self, asset, highest_price):
        message = f"Today's highest price for {asset.upper()} on WazirX is {highest_price:.2f} INR"

    def run(self):
        while True:
            # loop over each asset in the list
            for asset in self.assets:
                highest_price = self.get_wazirx_highest_price_today(asset)
                # if the highest price is greater than required price, send a notification
                if highest_price > 87.01:
                    self.send_telegram_notification(asset, highest_price)
                    # wait for 10 minutes before checking the price again
                    time.sleep(600)

if __name__ == "__main__":
    bot = Bot()
    bot.run()

