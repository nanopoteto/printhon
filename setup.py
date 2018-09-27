from setuptools import setup


requires = ["requests>=2.14.2"]


setup(
    name='printhon',
    version='0.1',
    description='Awesome library',
    url='https://github.com/nanopoteto/printhon',
    author='nanopoteto',
    author_email='ryota.natsume.26@address.com',
    license='MIT',
    keywords='sample setuptools development',
    packages=[
        "printhon",
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)