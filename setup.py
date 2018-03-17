import re
import io
from setuptools import setup
from setuptools.extension import Extension

__version__ = re.search(
    r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',  # It excludes inline comment too
    io.open('qrcrypto/__init__.py', encoding='utf_8').read()
    ).group(1)

setup(
    author="Somdip Dey",
    author_email="somdip007-at-gmail.com",
    name='qrcrypto',
    version=__version__,
    url='https://github.com/somdipdey/Encrypted_QR_Code',
    description='Use this Python3 package to encrypt messages and embed in QR code, and decrypt the message back.',
    license='MIT',
    install_requires=['simple-crypt','qrcode','pypng','pillow'],
    packages=['qrcrypto'],
    classifiers=textwrap.dedent("""
        Development Status :: 5 - Production/Stable
        Intended Audience :: Developers
        License :: OSI Approved :: MIT License
        Operating System :: OS Independent
        Programming Language :: Python :: 3
        Programming Language :: Python :: 3.3
        Programming Language :: Python :: 3.4
        Programming Language :: Python :: 3.5
        Programming Language :: Python :: 3.6
        Topic :: Software Development :: Libraries :: Python Modules
        Topic :: System :: Archiving :: Packaging
        Topic :: System :: Systems Administration
        Topic :: Utilities
        """).strip().splitlines(),
    python_requires='>=3.0'
)
