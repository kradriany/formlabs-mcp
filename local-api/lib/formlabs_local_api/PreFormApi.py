"""\
Handwritten convenience wrapper around the generated Python library code
"""
from contextlib import contextmanager
import formlabs_local_api as formlabs
import subprocess
import os
import psutil
import socket
import sys
import threading
import queue

from formlabs_local_api_minimal.PreFormApiBase import PreFormApiBase

class PreFormApi(PreFormApiBase):
    server_process = None

    def __init__(self, preform_port=44388):
        self.preform_port = preform_port
        self.client = formlabs.ApiClient(
            formlabs.Configuration(host=f"http://localhost:{preform_port}")
        )
        self.api = formlabs.UnifiedApi(self.client)
