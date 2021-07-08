#!/usr/bin/env python

from hummingbot.strategy.trend_trade import TrendTradeStrategy
from hummingbot.strategy.trend_trade.trend_trade_config_map import trend_trade_config_map
from hummingbot.core.event.events import PriceType


def start(self):
    try:
        exchange = trend_trade_config_map.get("exchange").value.lower()
        trading_pair = trend_trade_config_map.get("trading_pair").value
        is_buy = trend_trade_config_map.get("is_buy").value
        spread = trend_trade_config_map.get("spread").value
        order_amount = trend_trade_config_map.get("order_amount").value
        price_type = trend_trade_config_map.get("price_type").value.lower()

        if price_type == "mid_price":
            price_type = PriceType.MidPrice
        elif price_type == "last_price":
            price_type = PriceType.LastTrade
        elif price_type == "last_own_trade_price":
            price_type = PriceType.LastOwnTrade
        else:
            raise ValueError(f"Invalid Price Type: {price_type}")

        self._initialize_markets([(exchange, [trading_pair])])

        exchange = self.markets[exchange]
        self.strategy = TrendTradeStrategy(
            exchange=exchange,
            trading_pair=trading_pair,
            is_buy=is_buy,
            spread=spread,
            order_amount=order_amount,
            price_type=price_type,
            hb_app_notification=True,
        )
    except Exception as e:
        self._notify(str(e))
        self.logger().error("Unknown error during initialization.", exc_info=True)
