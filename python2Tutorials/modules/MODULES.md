#Modules

Kinds of Modules

    - .py (Written in Python)
    - .dll, .pyd, .so, .sl (Dynamically Linked C
    Modules)
    - C-Modules linked w/ the Interpreter. 
    (see py2_complete_list_of_builtin_modules for
    a list of these) 
    
    
Module Search Path

    The python interpreter searches for a module
    specified with the 'import <module_name>' 
    statement in the following order:
    
    - directory of the top-level file
        - (the file being executed)
    - the directories specified in PYTHONPATH
        - if this Global EV is set in the OS
    - standard installation path of python
        - e.g. /usr/lib/python

Location a Module in the file system. 

    - after importing a module, you can determine
    where it is stored on the file system by:
        
        print(<module_name>.__file__)
        
        (Not every module supports this)
    
Get Contents of a Module

    - dir(