#!/usr/bin/env python3
import socket
import time
import ftplib
import os
from http.server import HTTPServer, BaseHTTPRequestHandler

FTP_HOST    = os.getenv("FTP_HOST", "ftpd")
FTP_PORT    = int(os.getenv("FTP_PORT", "21"))
FTP_USER    = os.getenv("FTP_USER", "ftpuser")
FTP_PASS    = os.getenv("FTP_PASS", "ftp123")
LISTEN_PORT = int(os.getenv("LISTEN_PORT", "9144"))


def collect_metrics():
    m = {
        "ftpd_up": 0,
        "ftpd_port_open": 0,
        "ftpd_login_success": 0,
        "ftpd_connect_duration_seconds": 0,
        "ftpd_files_total": 0,
        "ftpd_sessions_active": 0,
    }

    # TCP port check
    try:
        s = socket.create_connection((FTP_HOST, FTP_PORT), timeout=3)
        s.close()
        m["ftpd_port_open"] = 1
    except Exception:
        return m

    # FTP login + stats
    try:
        t0 = time.time()
        ftp = ftplib.FTP()
        ftp.connect(FTP_HOST, FTP_PORT, timeout=5)
        ftp.login(FTP_USER, FTP_PASS)
        m["ftpd_connect_duration_seconds"] = round(time.time() - t0, 4)
        m["ftpd_up"] = 1
        m["ftpd_login_success"] = 1

        try:
            files = ftp.nlst()
            m["ftpd_files_total"] = len(files)
        except Exception:
            pass

        try:
            stat = ftp.sendcmd("STAT")
            lines = [l for l in stat.splitlines()
                     if "connected" in l.lower() or "logged in" in l.lower()]
            m["ftpd_sessions_active"] = len(lines) if lines else 1
        except Exception:
            m["ftpd_sessions_active"] = 1

        ftp.quit()
    except Exception:
        pass

    return m


def render(m):
    def gauge(name, help_text, val):
        return (
            f"# HELP {name} {help_text}\n"
            f"# TYPE {name} gauge\n"
            f"{name} {val}\n"
        )
    return (
        gauge("ftpd_up",                       "FTP server is reachable and responding",          m["ftpd_up"])
      + gauge("ftpd_port_open",                "FTP TCP port 21 is open",                         m["ftpd_port_open"])
      + gauge("ftpd_login_success",            "FTP login with configured credentials succeeded", m["ftpd_login_success"])
      + gauge("ftpd_connect_duration_seconds", "Time in seconds to connect and authenticate",     m["ftpd_connect_duration_seconds"])
      + gauge("ftpd_files_total",              "Number of files in FTP home directory",           m["ftpd_files_total"])
      + gauge("ftpd_sessions_active",          "Estimated number of active FTP sessions",         m["ftpd_sessions_active"])
    )


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/metrics":
            body = render(collect_metrics()).encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; version=0.0.4")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    print(f"[ftpd_exporter] Listening on 0.0.0.0:{LISTEN_PORT}/metrics", flush=True)
    HTTPServer(("0.0.0.0", LISTEN_PORT), Handler).serve_forever()
