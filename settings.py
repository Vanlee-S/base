# RANDOM WALLETS MODE
RANDOM_WALLET = True  # True/False

QUANTITY_RUN_ACCOUNTS = 5

SLEEP_FROM = 500  # Second
SLEEP_TO = 1600  # Second

# GWEI CONTROL MODE
CHECK_GWEI = False  # True/False
MAX_GWEI = 20

GAS_PRIORITY_FEE = {
    "ethereum": 0.05,
    "polygon": 40,
    "arbitrum": 0.1,
    "base": 0.1,
    "zksync": 0.25,
}

GAS_MULTIPLIER = 1.3

# RETRY MODE
RETRY_COUNT = 3

# INCH API KEY
INCH_API_KEY = ""
