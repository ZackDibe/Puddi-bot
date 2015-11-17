from setuptools import setup

setup(name='Puddi-bot',
      version='0.1',
      description='Slack bot that plays the Puddi Puddi song on PR closed',
      url='https://github.com/Zack--/Puddi-bot',
      author='Zack--',
      license='MIT',
      packages=['slackclient'],
      install_requires=[
          'websocket-client'
      ],
      zip_safe=False)
