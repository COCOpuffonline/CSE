def shutdown(self):
    import subprocess
    subprocess.call(["shutdown", "-f", "-r", "-t", "60"])
