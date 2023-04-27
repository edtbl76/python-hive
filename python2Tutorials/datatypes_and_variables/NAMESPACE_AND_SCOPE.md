Namespaces (a.k.a Contexts)
-

-    naming system for making names unique in order to avoid 
ambiguity. 
- used in programming languages as identifiers. 
    -   An identifier defined in a namespace is 
    associated with that namespace. 
    -   allows the same identifier to be independently
    defined in multiple namespaces. 
    

Python namespaces are implemented as dicts. \
EX:
  - GLOBAL NAMES of a module
  - LOCAL NAMES in a function or method invocation
  - BUILT-IN NAMES, which contains built-in functions and 
  built-in exception names
 
 
 Lifetime of a Namespace
-

- built-in names is created when Python interpreter 
starts up and is never deleted. 

- global namespace of a module is generated when module
is read in to memory. 
    - (normally they last until the script ends, i.e the 
    interpreter quits)

- when a function is called, a local namespace is
created for the function. 
    - This namespace is deleted if the function ends (i.e. 
    it returns) or if the function raises an exception
    that isn't handled in the function
    
 Scopes
-

- A scope is a region of a program where a namespace can be 
directly accessed
    - (i.e. w/o the namespace prefix)
    - the scope of a name is the area of a program
    where the name can be unambiguously used
    
- A name's namespace is identical to its scope
- scopes are defined statically but used dynamically

- available nested scopes during program execution:
    - innermost scope is searched first
        - (it contains local names)
    - scopes of any enclosing functions, which 
    are searched starting w/ the nearest enclosing 
    scope
    - next-to-last scope contains the current module's
    global names
    - the outermost scope, which is searched last, is
    the namespace containing the built-in names.