from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='AISCpy',
      version='0.1',
      description='American Institute of Steel Construction in Python',
      long_description=readme(),
      license='GPL 3.0',
      author='mlw',
      url='https://github.com/mwhit74/AISCpy',
      packages=[],
      install_requires=[])
