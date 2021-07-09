#!/usr/bin/env python

from .indicator_perps import IndicatorPerpsStrategy
from hummingbot.strategy.perpetual_market_making.asset_price_delegate import AssetPriceDelegate
from hummingbot.strategy.perpetual_market_making.order_book_asset_price_delegate import OrderBookAssetPriceDelegate
from hummingbot.strategy.perpetual_market_making.api_asset_price_delegate import APIAssetPriceDelegate

__all__ = [
    IndicatorPerpsStrategy,
    AssetPriceDelegate,
    OrderBookAssetPriceDelegate,
    APIAssetPriceDelegate
]
