import subprocess


def virt(k: str, s: str, s1: str):
    result = subprocess.run(k, shell=True, stdout=subprocess.PIPE, encoding='UTF-8')
    out = result.stdout
    if s in out and s1 in out and result.returncode == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(virt('cat /etc/os-release', '22.04.3', 'jammy'))