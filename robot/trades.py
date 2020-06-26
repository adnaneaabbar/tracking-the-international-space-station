from datetime import datetime

from typing import List
from typing import Dict
from typing import Union
from typing import Optional


class Trade():

    def __init__(self):

        self.order = {}
        self.trade_id = ""

        self.side = ""
        self.side_opposite = ""
        self.enter_or_exit = ""
        self.enter_or_exit_opposite = ""

        self._order_response = {}
        self._triggered_added = False
        self._multi_leg = False

    def new_trade(self, trade_id: str, order_type: str, side: str, enter_or_exit: str, price: float = 0.0, stop_limit_price: float = 0.0) -> Dict:
        '''
            order_type {str} -- The type of order you would like to create. Can be
        one of the following: ['mkt', 'lmt', 'stop', 'stop_lmt', 'trailing_stop']

            side {str} -- The side the trade will take, can be one of the
        following: ['long', 'short']

            enter_or_exit {str} -- Specifices whether this trade will enter a new
        position or exit an existing position. If used to enter then specify, 'enter'. If used to exit a trade specify, 'exit'.
        '''

        self.trade_id = trade_id

        self.order_types = {
            'mkt': 'MARKET',
            'lmt': 'LIMIT',
            'stop': 'STOP',
            'stop_lmt': 'STOP_LIMIT',
            'trailing_stop': 'TRAILING_STOP'
        }

        self.order_instructions = {
            'enter': {
                'long': 'BUY',
                'short': 'SELL_SHORT'
            },
            'exit': {
                'long': 'SELL',
                'short': 'BUY_TO_COVER'
            }
        }

        self.order = {
            "orderStrategyType": "SINGLE",
            "orderType": self.order_types[order_type],
            "session": "NORMAL",
            "duration": "DAY",
            "orderLegCollection": [
                {
                    "instruction": self.order_instructions[enter_or_exit][side],
                    "quantity": 0,
                    "instrument": {
                        "symbol": None,
                        "assetType": None
                    }
                }
            ]
        }

        if self.order['orderType'] == 'STOP':
            self.order['stopPrice'] = price

        elif self.order['orderType'] == 'LIMIT':
            self.order['price'] = price

        elif self.order['orderType'] == 'STOP_LIMIT':
            self.order['price'] = stop_limit_price
            self.order['stopPrice'] = price

        elif self.order['orderType'] == 'TRAILING_STOP':
            self.order['stopPriceLinkBasis'] == ""
            self.order['stopPriceLinkType'] == ""
            self.order['stopPriceOffset'] == 0.00
            self.order['stopType'] == 'STANDARD'

        # Make a refrence to the side we take, useful when adding other components.
        self.enter_or_exit = enter_or_exit
        self.side = side
        self.order_type = order_type
        self.price = price

        if order_type == 'stop' or order_type == 'stop-lmt':
            self.stop_price = price
        else:
            self.stop_price = 0.0

        if self.enter_or_exit == 'enter':
            self.enter_or_exit_opposite = 'exit'
        if self.enter_or_exit == 'exit':
            self.enter_or_exit_opposite = 'enter'

        if self.side == 'long':
            self.side_opposite == 'short'
        if self.side == 'short':
            self.side_opposite == 'long'
