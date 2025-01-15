from contextlib import contextmanager

import subprocess
import os
import shlex
import sys
import threading
import queue

class PreFormApiBase:
    server_process = None

    def __init__(self, preform_port=44388):
        self.preform_port = preform_port
    def __init__(self, preform_port=44388):
        self.preform_port = preform_port

    @classmethod
    def start_preform_sync(cls, pathToPreformServer=None, preform_port=44388, command_prefix=None):
        preformserver_path = _find_preform_server(pathToPreformServer)

        command_str = f"{preformserver_path} --port {preform_port}"
        if command_prefix:
            command_str = f"{command_prefix} {command_str}"
        process_args = shlex.split(command_str)
        if sys.platform == "win32":
            process_args = command_str
        server_process = subprocess.Popen(
            process_args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True)
        
        def output_reader(proc, outq):
            for line in iter(proc.stdout.readline, ""):
                outq.put(line)
        
        outq = queue.Queue()
        t = threading.Thread(target=output_reader, args=(server_process, outq))
        t.start()

        while True:
            try:
                line = outq.get(block=True) # Add timeout?
                if "READY FOR INPUT" in line:
                    # Use cls() to instantiate either the minimal or full PreFormApi class, depending on the caller
                    preformApi = cls(preform_port)
                    preformApi.server_process = server_process
                    return preformApi
                if "address is already in use" in line:
                    raise RuntimeError("Port already in use, probably another PreForm server is already running.")
            except queue.Empty:
                print('could not get line from queue')

    @contextmanager
    @classmethod
    def start_preform_server(cls, pathToPreformServer=None, preform_port=44388, command_prefix=None):
        preformApi = None
        try:
            preformApi = cls.start_preform_sync(pathToPreformServer, preform_port, command_prefix)
            print("PreForm server ready")
            yield preformApi
            return
        finally:
            if (preformApi):
                preformApi.stop_preform_server()
                print("PreForm server stopped.")

    def stop_preform_server(self):
        if self.server_process is not None:
            self.server_process.terminate()
            self.server_process.wait()
            self.server_process = None

def _find_preform_server(pathToPreformServer=None):
    if pathToPreformServer is None:
        formlabs_path = os.path.dirname(os.path.realpath(__file__))
        library_path = os.path.dirname(os.path.dirname(formlabs_path))

        filename = "PreFormServer"
        if sys.platform == "win32":
            filename += ".exe"

        pathToPreformServer = os.path.join(library_path, filename)
    if not os.path.isfile(pathToPreformServer):
        raise FileNotFoundError("PreFormServer executable not found at " + str(pathToPreformServer))

    return pathToPreformServer
