import datetime

from rest_framework import throttling


class WorkingHoursRateThrottle(throttling.BaseThrottle):
    """True — разрешить запрос, и False — отклонить."""

    def allow_request(self, request, view):
        now = datetime.datetime.now().hour
        if now >= 3 and now < 5:
            return False
        return True
