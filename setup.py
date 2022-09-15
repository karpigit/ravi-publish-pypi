from setuptools import setup, find_packages


setup(
    name='ravi',
    version='0.1',
    license='MIT',
    author="Karpi",
    author_email='karpiworld@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/karpigit/ravi-publish-pypi',
    keywords='ravi',
    install_requires=[
      ],
)