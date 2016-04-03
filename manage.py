#!/usr/bin/env python
try:
    from gevent import monkey
    # monkey.patch_all()
except ImportError:
    pass

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gdc.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
