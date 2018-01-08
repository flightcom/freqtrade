"""
File that contains the configuration for Hyperopt
"""


def hyperopt_optimize_conf() -> dict:
    """
    This function is used to define which parameters Hyperopt must used.
    The "pair_whitelist" is only used is your are using Hyperopt with MongoDB,
    without MongoDB, Hyperopt will use the pair your have set in your config file.
    :return:
    """
    return {
        'max_open_trades': 30,
        'stake_currency': 'BTC',
        'stake_amount': 1,
        "minimal_roi": {
            # '1440':  -0.05,
            # '720':  0,
            '60':  -1,
            # '120':  0.02,
            # '60':  0.03,
            '0':  0.05,
        },
        'stoploss': -1,
        "bid_strategy": {
            "ask_last_balance": 0.0
        },
        "exchange": {
            "pair_whitelist": [
            ]
        }
    }
