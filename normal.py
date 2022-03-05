#%%
import pandas as pd
import json

json_example = """
    {
    "data": [
        {
        "type": "accounts",
        "id": "ACTUAL_FIRST",
        "attributes": {
            "displayName": "Spending",
            "accountType": "TRANSACTIONAL",
            "ownershipType": "INDIVIDUAL",
            "balance": {
            "currencyCode": "AUD",
            "value": "1.00",
            "valueInBaseUnits": 100
            },
            "createdAt": "2022-03-03T09:45:23+11:00"
        },
        "relationships": {
            "transactions": {
            "links": {
                "related": "https://api.up.com.au/api/v1/accounts/3109473c-8752-43e3-ad2e-ddfc57c1e077/transactions"
            }
            }
        },
        "links": {
            "self": "https://api.up.com.au/api/v1/accounts/3109473c-8752-43e3-ad2e-ddfc57c1e077"
        }
        },
        {
        "type": "accounts",
        "id": "FIRST",
        "attributes": {
            "displayName": "Spending",
            "accountType": "TRANSACTIONAL",
            "ownershipType": "INDIVIDUAL",
            "balance": {
            "currencyCode": "AUD",
            "value": "1.00",
            "valueInBaseUnits": 100
            },
            "createdAt": "2022-03-03T09:45:23+11:00"
        },
        "relationships": {
            "transactions": {
            "links": {
                "related": "https://api.up.com.au/api/v1/accounts/3109473c-8752-43e3-ad2e-ddfc57c1e077/transactions"
            }
            }
        },
        "links": {
            "self": "https://api.up.com.au/api/v1/accounts/3109473c-8752-43e3-ad2e-ddfc57c1e077"
        }
        }
    ],
    "links": {
        "prev": null,
        "next": "https://api.up.com.au/api/v1/accounts?page%5Bafter%5D=WyIyMDIyLTAzLTAyVDIyOjQ1OjIzLjY0NzM0NDAwMFoiLCIzMTA5NDczYy04NzUyLTQzZTMtYWQyZS1kZGZjNTdjMWUwNzciXQ%3D%3D&page%5Bsize%5D=1"
    }
    }
"""

data = json.loads(json_example)
df = pd.json_normalize(
    data,
    record_path = ["data"]
    )

df.to_csv('example.csv')