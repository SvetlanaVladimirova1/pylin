import subprocess
import string


def virt(k: str, s: str):
    result = subprocess.run(k, shell=True, stdout=subprocess.PIPE, encoding='UTF-8')
    out = result.stdout
    if s in out and result.returncode == 0:
        res = string.punctuation
        for i in s:
            if i in res:
                n = s.replace(i, ' ')
        return n
    else:
        return False


if __name__ == '__main__':
    print(virt('cat /etc/os-release', '22.04.3'))