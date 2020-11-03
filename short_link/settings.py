import os

DOMAIN = os.environ.get('DOMAIN', 'localhost')

DOMAIN_HTTP = os.environ.get('DOMAIN_HTTP', 'http')

DOMAIN_PORT = os.environ.get('DOMAIN', 80)

BASE_URL = f'{DOMAIN_HTTP}://{DOMAIN}:{DOMAIN_PORT}/' if DOMAIN_PORT not in [80, 443] else f'{DOMAIN_HTTP}://{DOMAIN}/'
