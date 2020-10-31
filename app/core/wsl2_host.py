from pathlib import Path


def get_host():
    wsl_conf = Path("/etc/resolv.conf")

    if not wsl_conf.is_file():
        raise Exception("wsl2 configuration file not found.")

    with wsl_conf.open() as f:
        for line in f:
            if (line.startswith("nameserver")):
                return line.replace("nameserver ", "").replace("\n", "")

    raise Exception("wsl2 nameserver not found.")
