from setuptools import setup, find_packages

setup(
    name='vidaas_agent',
    version='0.1',
    author='André Cerutti Franciscatto',
    author_email='andre@franciscatto.com',
    description='Uma biblioteca Python para interagir com a API VIDaaS',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/afmaster/vidaas_agent',
    packages=find_packages(),
    install_requires=[
        'certifi==2023.7.22',
        'charset-normalizer==3.3.1',
        'idna==3.4',
        'requests==2.31.0',
        'urllib3==2.0.7'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
