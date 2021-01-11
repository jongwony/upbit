import requests

from upbit import server_api


class Market:
    @staticmethod
    def all(is_details: bool = None):
        """
        :param is_details: 유의종목 필드과 같은 상세 정보 노출 여부(선택 파라미터)
        :return:
        """
        response = requests.get(server_api("/v1/market/all"), params={"isDetails": str(is_details).lower()})
        return response.json()


class Candle:
    @staticmethod
    def minutes(unit: int, market: str, to: str = None, count: int = None):
        """
        :param unit: 분 단위. 가능한 값 : 1, 3, 5, 15, 10, 30, 60, 240
        :param market: 마켓 코드 (ex. KRW-BTC)
        :param to: 마지막 캔들 시각 (exclusive). 포맷 : yyyy-MM-dd'T'HH:mm:ssXXX or yyyy-MM-dd HH:mm:ss. 비워서 요청시 가장 최근 캔들
        :param count: 캔들 개수(최대 200개까지 요청 가능)
        :return:
        """
        response = requests.get(server_api(f'/v1/candles/minutes/{unit}'),
                                params={'market': market, 'to': to, 'count': count})
        return response.json()

    @staticmethod
    def days(market: str, to: str = None, count: int = None, converting_price_unit: str = None):
        """
        :param market: 마켓 코드 (ex. KRW-BTC, BTC-BCC)
        :param to: 마지막 캔들 시각 (exclusive). 포맷 : yyyy-MM-dd'T'HH:mm:ssXXX or yyyy-MM-dd HH:mm:ss. 비워서 요청시 가장 최근 캔들
        :param count: 캔들 개수
        :param converting_price_unit: 종가 환산 화폐 단위 (생략 가능, KRW로 명시할 시 원화 환산 가격을 반환.)
        :return:
        """
        response = requests.get(
            server_api(f'/v1/candles/days'),
            params={'market': market, 'to': to, 'count': count, 'convertingPriceUnit': converting_price_unit})
        return response.json()

    @staticmethod
    def weeks(market: str, to: str = None, count: int = None):
        response = requests.get(server_api(f'/v1/candles/weeks'), params={'market': market, 'to': to, 'count': count})
        return response.json()

    @staticmethod
    def months(market: str, to: str = None, count: int = None):
        response = requests.get(server_api(f'/v1/candles/months'), params={'market': market, 'to': to, 'count': count})
        return response.json()


class Trades:
    @staticmethod
    def ticks(market: str, to: str = None, count: int = None, cursor: str = None, days_ago: int = None):
        """

        :param market:
        :param to:
        :param count:
        :param cursor:
        :param days_ago:
        :return:
        """
        response = requests.get(
            server_api(f'/v1/trades/ticks'),
            params={'market': market, 'to': to, 'count': count, 'cursor': cursor, 'daysAgo': days_ago})
        return response.json()


class Ticker:
    def __call__(self, markets: str):
        """
        요청 당시 종목의 스냅샷을 반환한다.
        :param markets: 반점으로 구분되는 마켓 코드 (ex. KRW-BTC, BTC-BCC)
        :return:
        """
        response = requests.get(server_api('/v1/ticker'), params={'markets': markets})
        return response.json()


class Orderbook:
    def __call__(self, markets: str):
        """
        :param markets: 반점으로 구분되는 마켓 코드 (ex. KRW-BTC, BTC-BCC)
        :return:
        """
        response = requests.get(server_api('/v1/ticker'), params={'markets': markets})
        return response.json()
