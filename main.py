from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Make sure these URLs have NO SLASH at the end
origins = [
    "https://trust-bank-ashy.vercel.app",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# ... your accounts list and @app.get("/accounts") route below ...

accounts = [
    {
      "id": "acc_1",
      "label": "Savings Account",
      "type": "Savings",
      "balance": 24500.00,
      "trend": "+2.5%",
      'currency': "$",
      'accountNumber': "**** 8829",
      'color': "bg-indigo-600",
    },
    {
      "id": "acc_2",
      "label": "Checking Account",
      "type": "Checking",
      "balance": 1240.50,
      "trend": "-1.2%",
      'currency': "$",
      'accountNumber': "**** 1102",
    },
    {
      "id": "acc_3",
      "label": "Investment Portfolio",
      "type": "Investment",
      "balance": 8900.00,
      "trend": "+5.8%",
      'currency': "$",
      'accountNumber': "**** 4432",
      'color': "bg-amber-600",
    }
]

@app.get("/accounts")
def get_accounts():
    return accounts

