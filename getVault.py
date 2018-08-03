import json
import sys
from azure.keyvault import KeyVaultClient, KeyVaultAuthentication
from azure.common.credentials import ServicePrincipalCredentials


##python getVault.py vault_url appid appsecretkey apptenantid 

credentials = None
resource_uri = "https://vault.azure.net"

vault_url = None
client_id = None
secretKey = None
tenant_id = None

def main(argv):
    if len(sys.argv) < 3:
        raise ValueError('Expecting vault_url, client_id, clientSecretKey,tenant_id')
    
    vault_url = sys.argv[1]
    client_id = sys.argv[2]
    secretKey = sys.argv[3]
    tenant_id = sys.argv[4]

    credentials = ServicePrincipalCredentials(
        client_id = client_id, 
        secret = secretKey,
        tenant = tenant_id,
        resource = resource_uri
    )

    client = KeyVaultClient(KeyVaultAuthentication(None, credentials))
    token = credentials.token
    token_type = token['token_type']
    access_token = token['access_token']

    secrets = client.get_secrets(vault_url)

    secretsData = {}
    
    for secret in secrets:
        secretName = secret.id.rsplit('/',1)[-1]
        secretItem = client.get_secret(vault_url,secretName,'')
        secretVersion = secretItem.id.rsplit('/',1)[-1]
        secretsData[secretName] = secretVersion

    json_data = json.dumps(secretsData)
    print(json_data)

if __name__ == "__main__":
    main(sys.argv)




