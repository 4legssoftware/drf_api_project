#!/usr/bin/env python
import os
import sys
from time import sleep

from drf_api.settings import NOSE_COVER_MIN_PERCENTAGE, NOSE_COVER_WAIT

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf_api.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    is_testing = 'test' in sys.argv

    if is_testing:
        import coverage

        cov = coverage.coverage(source=['drf_api'], omit=['drf_api/*/tests.py'], )
        cov.erase()
        cov.start()

    execute_from_command_line(sys.argv)

    if is_testing:
        cov.stop()
        cov.save()
        cov.html_report(directory='cover')
        coverage_percent = cov.report()
        sleep(NOSE_COVER_WAIT)
        if coverage_percent < NOSE_COVER_MIN_PERCENTAGE:
            exit(1)
