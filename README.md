Packaging Python Scripts into CLI Commands
------------------------------------------

Few things to note: 

* How to Run python somescript.py to somescript by using CLI

Build setup.py file
------------------------------------------

* python setup.py install


Run CLI command
------------------------------------------

Run CLI command by using:

* In script.py we defined entry_script and assigned `example` is command name
    
    entry_points={
        'console_scripts':[
            'example = pythonPackaging.python_packaging_example:main',
        ]
    },

* example "test message"
* example "whvw phvvdjh" --decrypt
