from setuptools import setup

setup(
    name='pipedream',
    version='0.1',
    py_modules=['pipedream'],
    install_requires=[
        'Click',
		'awscli'
    ],
    entry_points='''
        [console_scripts]
        pipedream=pipedream:cli
    ''',
)