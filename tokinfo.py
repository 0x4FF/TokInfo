from requests import get

from os import getenv

from json import (
      dumps,
      load,
)

# Configurating the token
try:
    with open("config.json", "r") as config_file:
        config = load(config_file)
        token = config.get("Token")
        if not token:
            token = getenv("Token")
except FileNotFoundError:
    print("Error: config.json not found, loading from env")
    token = getenv("Token")

headers = {"Authorization": f"{token}"}
                

class Tokinfo:
  
  def __init__(self, token):
    self.token = token

  def get_user_info(self):
          user_body = get("https://discord.com/api/v9/users/@me", 
                          headers=headers).json()
          bio_body = get(f"https://discord.com/api/v9/users/{user_body['id']}/profile?with_mutual_guilds=false&with_mutual_friends_count=false", 
                         headers=headers).json()['user_profile']['bio']
          user_dict = {
                  "account": user_body,
                  "bio": bio_body
          }
 
          return dumps(user_dict, indent=4)
    
  def get_user_dms(self):
          dms_body = get("https://discord.com/api/v9/users/@me/channels", 
                         headers=headers).json()
    
          return dumps(dms_body, indent=4)
    
  def get_user_friends(self):
          friend_body = get("https://discord.com/api/v9/users/@me/relationships", 
                            headers=headers).json()
    
          return dumps(friend_body, indent=4)
    
  def get_user_connections(self):
          connections_body = get("https://discord.com/api/v9/users/@me/connections", 
                                 headers=headers).json()
    
          return dumps(connections_body, indent=4)
    
  def get_payment_info(self):
          payments_body = get("https://discord.com/api/v9/users/@me/billing/subscriptions", 
                              headers=headers).json()
          billing_body = get("https://discord.com/api/v9/users/@me/billing/payment-sources", 
                             headers=headers).json()
          gifts_body = get("https://discord.com/api/v9/users/@me/entitlements/gifts", 
                           headers=headers).json()
          likelihood = get("https://discord.com/api/v9/users/@me/billing/premium-likelihood", 
                           headers=headers).json()
          payment_dict = {
               "subscriptions": payments_body,
               "payment_sources": billing_body,
               "gifts": gifts_body,
               "likelihood": likelihood
          }
    
          return dumps(payment_dict, indent=4)
    
  def get_notifs(self):
          get_notifs = get("https://discord.com/api/v9/users/@me/notification-center/items?limit=100", 
                           headers=headers).json()
          return dumps(get_notifs, indent=4)
    
  def get_servers(self):
          get_account_servers = get("https://discord.com/api/users/@me/guilds", 
                                    headers=headers).json()
          return dumps(get_account_servers, indent=4)
 
    
  
# Create an instant to use
account = Tokinfo(token)

# Example

print(
      account.get_user_info(), 
      account.get_user_dms(),
      account.get_user_friends(),
      account.get_user_connections(),
      account.get_payment_info(),
      account.get_notifs(),
      account.get_servers()
)
