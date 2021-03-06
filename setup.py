from setuptools import setup


setup(
    name = 'sei_py',
    packages = ['sei_py', 'sei_py.base', 'sei_py.rest'],
    version = '0.2.0',
    description = 'A Caveon SEI helper library',
    author = 'Evan Anderson',
    author_email = 'evan.anderson@caveon.com',
    url = 'https://github.com/xh4zr/sei-py',
    keywords = ['caveon', 'sei', 'exam', 'test security'],
    install_requires = ['requests==2.20.0', 'python_jwt==2.0.2']
)
