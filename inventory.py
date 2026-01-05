import os
import sys
# Import the specific Azure error handler
from azure.core.exceptions import AzureError, ClientAuthenticationError
from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient

def list_storage_accounts(subscription_id):
    print(f"--- Starting Audit for Subscription: {subscription_id} ---")
    
    try:
        # 1. Attempt Authentication
        credential = DefaultAzureCredential()
        storage_client = StorageManagementClient(credential, subscription_id)

        # 2. Attempt Data Retrieval
        storage_list = storage_client.storage_accounts.list()
        
        count = 0
        print(f"{'NAME':<25} | {'LOCATION':<15} | {'TIER':<15}")
        print("-" * 60)
        
        for account in storage_list:
            print(f"{account.name:<25} | {account.location:<15} | {account.sku.name:<15}")
            count += 1
            
        print("-" * 60)
        print(f"SUCCESS: Found {count} storage accounts.")

    except ClientAuthenticationError:
        # Specific error for bad passwords/IDs
        print("\n[CRITICAL ERROR] Authentication Failed.")
        print("Please check: AZURE_CLIENT_ID, AZURE_CLIENT_SECRET, AZURE_TENANT_ID")
        sys.exit(1) # Exit with error code 1 so Docker/K8s knows it failed

    except AzureError as e:
        # General Azure errors (e.g., Subscription not found, API down)
        print(f"\n[ERROR] Azure API Error: {e}")
        sys.exit(1)

    except Exception as e:
        # Catch-all for unexpected python errors
        print(f"\n[UNEXPECTED ERROR] Something went wrong: {e}")
        sys.exit(1)

if __name__ == "__main__":
    sub_id = os.environ.get("AZURE_SUBSCRIPTION_ID")
    if not sub_id:
        print("[CONFIG ERROR] 'AZURE_SUBSCRIPTION_ID' environment variable is missing.")
        sys.exit(1)
        
    list_storage_accounts(sub_id)