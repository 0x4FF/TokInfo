import requests
import argparse
import os
import json

class Tokinfo:
    def __init__(self, token):
        self.token = token
        self.headers = {"Authorization": self.token}

    def get_user_info(self):
        user_response = requests.get("https://discord.com/api/v9/users/@me", headers=self.headers)
        user_body = user_response.json()
        if user_response.status_code != 200:
            print("Error retrieving user information")
            return

        bio_response = requests.get(
            f"https://discord.com/api/v9/users/{user_body['id']}/profile?with_mutual_guilds=false&with_mutual_friends_count=false",
            headers=self.headers
        )
        bio_body = bio_response.json()['user_profile']['bio']
        if bio_response.status_code != 200:
            print("Error retrieving user bio")
            return

        user_dict = {
            "account": user_body,
            "bio": bio_body
        }
        return json.dumps(user_dict, indent=4)

    def get_user_dms(self):
        dms_response = requests.get("https://discord.com/api/v9/users/@me/channels", headers=self.headers)
        dms_body = dms_response.json()
        if dms_response.status_code != 200:
            print("Error retrieving user DMs")
            return

        return json.dumps(dms_body, indent=4)

    def get_user_friends(self):
        friend_response = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=self.headers)
        friend_body = friend_response.json()
        if friend_response.status_code != 200:
            print("Error retrieving user friends")
            return

        return json.dumps(friend_body, indent=4)

    def get_user_connections(self):
        connections_response = requests.get("https://discord.com/api/v9/users/@me/connections", headers=self.headers)
        connections_body = connections_response.json()
        if connections_response.status_code != 200:
            print("Error retrieving user connections")
            return

        return json.dumps(connections_body, indent=4)

    def get_payment_info(self):
        payments_response = requests.get("https://discord.com/api/v9/users/@me/billing/subscriptions", headers=self.headers)
        payments_body = payments_response.json()
        if payments_response.status_code != 200:
            print("Error retrieving user payments")
            return

        billing_response = requests.get("https://discord.com/api/v9/users/@me/billing/payment-sources", headers=self.headers)
        billing_body = billing_response.json()
        if billing_response.status_code != 200:
            print("Error retrieving user billing info")
            return

        gifts_response = requests.get("https://discord.com/api/v9/users/@me/entitlements/gifts", headers=self.headers)
        gifts_body = gifts_response.json()
        if gifts_response.status_code != 200:
            print("Error retrieving user gifts")
            return

        likelihood_response = requests.get("https://discord.com/api/v9/users/@me/billing/premium-likelihood", headers=self.headers)
        likelihood = likelihood_response.json()
        if likelihood_response.status_code != 200:
            print("Error retrieving user premium likelihood")
            return

        payment_dict = {
            "subscriptions": payments_body,
            "payment_sources": billing_body,
            "gifts": gifts_body,
            "likelihood": likelihood
        }
        return json.dumps(payment_dict, indent=4)

    def get_notifs(self):
        notifs_response = requests.get("https://discord.com/api/v9/users/@me/notification-center/items?limit=100", headers

