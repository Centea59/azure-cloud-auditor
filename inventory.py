import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient

def list_storage_accounts(subscription_id):
    print(f"Connecting to Subscription: {subscription_id}...")

    credential = DefaultAzureCredential()
    storage_client = StorageManagementClient(credential, subscription_id)

    print("--- Storage Inventory ---")
    storage_list = storage_client.storage_accounts.list()

    count = 0
    for account in storage_list:
        print(f"Name: {account.name} | Location: {account.location} | Tier: {account.sku.name}")
        count += 1

    print(f"Total Storage Accounts Found: {count}")

if __name__ == "__main__":
    # Expecting the ID from Environment Variable this time (Best Practice)
    sub_id = os.environ.get("AZURE_SUBSCRIPTION_ID")
    if sub_id:
        list_storage_accounts(sub_id)
    else:
        print("Error: AZURE_SUBSCRIPTION_ID env var is missing.")