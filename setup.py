import re
import io
from setuptools import setup
from setuptools.extension import Extension

__version__ = re.search(
    r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',  # It excludes inline comment too
    io.open('src/__init__.py', encoding='utf_8').read()
    ).group(1)

setup(
    author="Somdip Dey",
    author_email="somdip007-at-gmail.com",
    name='src',
    version=__version__,
    url='https://github.com/somdipdey/Encrypted_QR_Code',
    description='Use this package to encrypt messages and embed in QR code, and decode the message back.',
    license='MIT',
    install_requires=['pycryptodome','qrcode','pypng','zbar','pillow'],
    packages=['src']
)
