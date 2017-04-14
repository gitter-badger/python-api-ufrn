from setuptools import setup

setup(name='python-api-ufrn',
      version='0.1',
      description='Simple integrate of API eventick.com.br with python',
      url='https://github.com/hudsonbrendon/python-api-ufrn',
      author='Hudson Brendon',
      author_email='contato.hudsonbrendon@gmail.com',
      license='MIT',
      packages=['ufrn'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
