import os
from falconpy import OAuth2

client_id = os.getenv("FALCON_CLIENT_ID")
client_secret = os.getenv("FALCON_CLIENT_SECRET")

print(client_id)
print(client_secret)


'''
auth = OAuth2(
    client_id = client_id,
    cliend_secret = client_secret
)


print("Authenticated", auth.token_status)
'''

print("falconpy executed")
