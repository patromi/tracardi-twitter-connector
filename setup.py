from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='tracardi-sends-a-tweet',
    version='0.1',
    description='This plugin is tweets to Twitter wall.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Patryk Migaj',
    author_email='patromi123@gmail.com',
    packages=['tracardi_sends_a_tweet'],
    install_requires=[
        'tracardi-plugin-sdk>=0.6.21',
        'tracardi>=0.6.18,<0.7.0',
        'tweepy'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    keywords=['tracardi', 'plugin'],
    include_package_data=True,
    python_requires=">=3.8",
)