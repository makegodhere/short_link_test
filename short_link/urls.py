from .resources import LongToShortResource, RedirectToLongLinkResource, StatisticsResource

urls = [
    [LongToShortResource, '/long_to_short'],
    [RedirectToLongLinkResource, '/<string:short_postfix>'],
    [StatisticsResource, '/statistics/<string:short_postfix>'],
]
