from setuptools import setup, find_packages

setup(
    name='coinbase_commerce',
    version='0.1.0',
    author='MaxieDev',
    author_email='support@trinixbot.xyz',
    description='A simple Python wrapper for the Coinbase Commerce API.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/MaxieDev/Coinbase-Commerce',
    packages=find_packages(),
    install_requires=[
        'httpx',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)
