# TOKINFO

tokinfo is a python program to grab as much useful information from an account via a token without
the need to login, the purpose is for it be used during OSINT, but you can use however.

# Installation

```
git clone https://github.com/n-ptr/TokInfo
```

# How do I use this?

1.    Make sure you have Python 3 installed on your computer.
2.    Download the main.py file from this repository.
3.    Open a terminal or command prompt in the directory where the main.py file is located.
4.    Run the following command to start the script: `python main.py` (you need to set your token and possibly install some pkgs)

# Examples

Options:
```js
arguments = {
    'info': account.get_user_info,
    'dms': account.get_user_dms,
    'friends': account.get_user_friends,
    'connections': account.get_user_connections,
    'payment': account.get_payment_info,
    'notifs': account.get_notifs,
    'servers': account.get_servers,
    'recent_dms': account.get_last_10_dm_messages
}
```
-
```py
python main.py --info
---------------------
```
```json
{
    "account": {
        "id": "000000000000",
        "username": "username",
        "global_name": null,
        "avatar": "xxxxxxxxxxxx",
        "discriminator": "0000",
        "public_flags": 0,
        "flags": 32,
        "banner": null,
        "banner_color": "#000000",
        "accent_color": 0,
        "bio": "",
        "locale": "en-US",
        "nsfw_allowed": true,
        "mfa_enabled": false,
        "premium_type": 0,
        "linked_users": [],
        "avatar_decoration": null,
        "email": "example@example.com",
        "verified": true,
        "phone": "000000000"
    },
    "bio": ""
}
```
-
```py
python main.py --dms
--------------------
```
```js
[
    {
        "id": "0000000000",
        "type": 3,
        "last_message_id": "00000000000",
        "flags": 0,
        "last_pin_timestamp": "000000",
        "recipients": [
            {
                "id": "174653376636649473",
                "username": "Saddie",
                "global_name": "",
                "avatar": "",
                "discriminator": "0000",
                "public_flags": ,
                "avatar_decoration": null
            },
```
