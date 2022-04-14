#%%

from upbankapi import Client
from api.config import Config

config = Config()
clients = {k: Client(token=t) for k,t in config.d['SECRET_TOKEN'].items()}

for c in clients.values():
    print(c.ping())

# %%

accounts = []
for c in clients.values():
    c_accounts = list(c.accounts())
    accounts += c_accounts

acc_ids = []
for n,acc in enumerate(accounts):
    if acc.id in acc_ids:
        accounts.pop(n)
    else:
        acc_ids.append(acc.id)
        print(acc)
# %%

transactions = [t for t in acc.transactions() for acc in accounts]
# %%

for t in transactions:
    print(t)
# %%

t_attrs = [d for d in dir(transactions[0]) if not d.startswith('__')]
# %%

t_ids = []
for n,t in enumerate(transactions):
    if t.id in t_ids:
        transactions.pop(n)
    else:
        t_ids.append(t.id)
        print(t)

# %%
print(transactions)
# %%

trans_data = [{k: getattr(t,k) for k in t_attrs} for t in transactions]

import pandas as pd
df = pd.DataFrame(trans_data)
# %%
df.head(5)
# %%
