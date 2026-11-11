"""Tiny static file server (Python standard library only, no pip packages).
Start command for hosts that require one:  python3 server.py
It serves this folder on the port given by the PORT environment variable (default 8000)."""
import mimetypes
import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from functools import partial

mimetypes.add_type('text/javascript', '.mjs')  # browsers refuse module scripts without this type
mimetypes.add_type('text/javascript', '.js')

HERE = os.path.dirname(os.path.abspath(__file__))
PORT = int(os.environ.get('PORT', 8000))

if __name__ == '__main__':
    handler = partial(SimpleHTTPRequestHandler, directory=HERE)
    print(f'Serving {HERE} on 0.0.0.0:{PORT}', flush=True)
    ThreadingHTTPServer(('0.0.0.0', PORT), handler).serve_forever()
