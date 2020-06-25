import pandas as pd
import numpy as np

from datetime import datetime
from datetime import time
from datetime import timezone

from typing import List
from typing import Dict
from typing import Union

import pandas.core.groupby as DataFrameGroupBy
import pandas.core.window as RollingGroupBy


class StockFrame():

    def __init__(self, data: List[dict]) -> None:

        self._data = data
        self._frame: pd.DataFrame = self.create_frame()
        self._symbol_groups: DataFrameGroupBy = None
        self._symbol_rolling_groups: RollingGroupBy = None

    @property
    def frame(self) -> pd.DataFrame:
        return self._frame

    @property
    def symbol_groups(self) -> DataFrameGroupBy:
        self._symbol_groups = self._frame.groupby(
            by='symbol',
            as_index=False,
            sort=True
        )

        return self._symbol_groups

    @property
    def symbol_rolling_groups(self, size: int) -> RollingGroupBy:

        if not self._symbol_groups:
            self.symbol_groups

        self._symbol_rolling_groups = self._symbol_rolling_groups(size)

        return self._symbol_rolling_groups

    def create_frame(self) -> pd.DataFrame:

        price_df = pd.DataFrame(data=self._data)
        price_df = self._parse_datetime_column(price_df=price_df)
        price_df = self._det_multiple_index(price=price_df)

        return price_df

    def _parse_datetime_column(self, price_df: pd.DataFrame) -> pd.DataFrame:

        price_df['datetime'] = pd.to_datetime(
            price_df['datetime'], unit='ms', origin='unix')

        return price_df

    def _set_multiple_index(self, price_df: pd.DataFrame) -> pd.DataFrame:

        price_df = price_df.set_index(keys=['symbol', 'datetime'])

        return price_df

    def add_rows(self, data: dict) -> None:
        pass
