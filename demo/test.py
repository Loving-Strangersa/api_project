import itertools


def get_password(digit):
    password = (
        ''.join(x) for x in itertools.product(
            'qwertyuiopasdfghjklmnbvcxzQWERTYUIOPLKJHGFDSAZX'
            'CVBNM0123456789.!@#$_',
            repeat=digit))
    for i in password:
        with open(f"{digit}_password.txt","w",encoding="utf-8") as f:
            f.writelines(i)


if __name__ == '__main__':
    get_password(digit=4)
