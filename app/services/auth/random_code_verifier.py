from app.providers.database import redis_client
from pkg.util.helper import numeric_random
from app.settings.config import settings


def make(phone, expired=60, length=4) -> str:
    code = numeric_random(length)
    redis_client.setex(_get_redis_key(phone), expired, code)
    return code


def check(phone, verification_code) -> bool:
    super_code = '9999'
    if (settings.ENV == 'dev' or settings.ENV == 'test') and verification_code == super_code:
        return True

    key = _get_redis_key(phone)
    code = redis_client.get(key)
    passed = code and code == verification_code
    if passed:
        redis_client.delete(key)
    return passed


def _get_redis_key(phone):
    return 'send:code:' + phone
