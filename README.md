# AzureKeyVault-FetchSecretsVersion
Applicable only for Azure KeyVault. Use this script if you want to print all the secret names and the corresponding version. Useful when you want to have a log with list of secrets used and what version of the same is the latest at the time the script was run. This script can be tweaked to fetch more attributes of the secrets.

Pre-requisites:
Python installed
Install packages mentioned in "instal-package.txt"
Setup in Azure:
  1. Get Access to Azure portal and the keyVault
  2. Create App in Azure AD and make sure you have apps secretkey created for API access (explained in appsecretkey description below)
  3. In KeyVault, under IAM provide access to the registered App for minimum reader permissions
  4. Under Secrets Access policies, provide the registered App with permissions such as GET

Following values need to be fetched for the script to work:

vault_url - The URI pointing to your KeyVault. In the Azure management portal, "DNS Name" value is your vault_url

appid - In order for this script to work and get access to the keyvault API, you need to register a App in Azure AD (mentioned in #2). Once you register you will get an Application Id. This Application id to be used as appid

appsecretkey - Aftet the app is registered (#2), go to "keys" under API access and create a new password. Copy the secret value generated and use it as appsecretkey

apptenantid - Tenantid of the Azure subscription. Go to Azure AD and check for directory value within the properties section

Use the below format to run the py file:
##python getVault.py vault_url appid appsecretkey apptenantid
