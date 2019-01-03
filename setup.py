import setuptools

setuptools.setup(
    name='python packaging example',
    version='1.0',
    author='Birendra Kumar',
    author_email='birendra7654@gmail.com',
    decsription='Example of python packaging tool',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts':[
            'example = pythonPackaging.python_packaging_example:main',
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
        ]

)
