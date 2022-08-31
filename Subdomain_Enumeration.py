from requests import get
from os import strerror
def subdomain_enum(wordlist: str, domain: str):
    try:
        archive = open(wordlist, 'r')
        for subdomain in archive:
            try:
                r = get(f"http://{subdomain.strip()}.{domain}")
                r
                if r.status_code != 404:
                    print(f"\033[1;32;40mSubdomain found!: {subdomain.strip()}\033[0m")
            except:
                continue
    except IOError as e:
        print(f"\033[1;31;40mI/O Error occurred: {strerror(e.errno)}\033[0m")
        exit()

if __name__ == '__main__':
    path_to_file = 'C:\\Users\\rafae\\OneDrive\\Escritorio\\CIBERSEGURIDAD\\PYTHON_C_BASH_PHP_REGEX_JAVA\\PYTHON\\Herramientas_pentesting\\dominios1.txt'
    domain_name = 'google.com'
    subdomain_enum(path_to_file, domain_name)