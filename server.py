#!/usr/bin/env python3
"""
Simple HTTP Server for serving the static website
Serves files from the 'website' subdirectory on port 3000
"""

import http.server
import socketserver
import os
import sys

# Configuration
PORT = 3000
DIRECTORY = "website"

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        # Add CORS headers if needed
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

def main():
    # Check if website directory exists
    if not os.path.exists(DIRECTORY):
        print(f"Error: Directory '{DIRECTORY}' does not exist!")
        sys.exit(1)
    
    # Check if index.html exists
    index_file = os.path.join(DIRECTORY, "index.html")
    if not os.path.exists(index_file):
        print(f"Warning: {index_file} not found!")
    
    # Create server
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"🚀 Server starting...")
        print(f"📁 Serving files from: {os.path.abspath(DIRECTORY)}")
        print(f"🌐 Server running at: http://localhost:{PORT}")
        print(f"🌐 Also available at: http://127.0.0.1:{PORT}")
        print(f"\n✨ Website for Luda Borovikova - AI Product Manager")
        print(f"   Domain: lada-pm.com\n")
        print("Press Ctrl+C to stop the server\n")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n🛑 Server stopped by user")
            sys.exit(0)

if __name__ == "__main__":
    main()
