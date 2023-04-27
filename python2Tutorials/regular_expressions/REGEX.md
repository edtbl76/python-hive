# Regular Expressions

The term "regular expression" originated in theoretical computer science as a mechanism to define
a language family w/ certain characteristics, such that the vernacular, syntax, grammar (i.e. the
expressions of the language) become regular (i.e. standardized).

Naming isn't as hard as it has to be ;)

An FSM (Finite State Machine), which accepts language defined by a regular expression,
exists for every regular expression.

RegEx are used in programming languages to filter text to determine if that text matches a particular
regular expression.

NOTE: one of the most important aspects/features of regular expressions is that the syntax of regular
expressions is the SAME for all programming languages, scripting languages, etc.


## Character Classes

[xyz]   This matches the specific characters
        inside the square brackets
        

### Dash '-'
    
    a dash is  regex metacharacter that 
    simplifies statements of 
    contiguous characters. 

[a-e] is the same as [abcde]

[0-5] is the same as [012345]

[A-Z]       = any upper case letter

[A-Za-z]    = any upper/lower case letter

    dash also has a special use case if it
    is immediately next to a bracket.
    
[-az] or [az-]  = in this case the dash is no longer
a metacharacter. This character class only matches '-'
'x' and 'y'

### Caret '^'

    '^' is the negation metacharacter for character
    classes as long as it is the first character 
    specified.
    
    NOTE: the caret only works this way inside a
    character class set. It has a different
    meaning outside this. 
    
[^0-9]  This matches any character but 0-9
[0-9^]  This matches 0-9 AND '^'

### Predefined Character Classes

    \d  = decimal digit (same as [0-9])
    \D  = matches any NON-figit (same as [^0-9])
    \s  = matches any whitespace character
            (same as [ \t\n\r\f\v])
    \S  = matches any NON whitespace character
            (same as [^ \t\n\r\f\v])
    \w  = matches any alphanumeric character
            (same as [A-Za-z0-9_])
          NOTE: with LOCALE, it will match the
          set [A-Za-z0-9_] and any additional 
          characters defined as letters for
          current locale)
    \W  = matches the 'compliment' of \w (i.e.
            everything but what \w matches)
    \b  = Matches an empty string, but only at the
            start or end of the word
    \B  = Matches an empty string, but NOT at the
            start or end of the word.
    \\  = Matches a literal backslash
    

### Special Characters

    ^   Matches from beginning of string
        (NOTE: this must be the first character
        in the string to be matched this way)
        
    $   Matches from the END of a string
        (NOTE: this must be the last character
        in the string to be matched this way) 
        
    ?   This symbol tells us that the preceding
        character may or may not occur. (i.e.
        it is optional) 
        (i.e. it matches either one or none of
        the preceding character, groups, or 
        sets)
        
        NOTE: if multiple characters are grouped
        together in parenthesis then the entire
        string in the parenthesis are optional.
        
        EX: Mar(ch)?  (the 'ch' is optional)
        
    *   This symbol matches 0 or more of the
        the preceding character, set or group
        (the difference between this and the ?
        is that it can match many times)
        
    .*  Matches any seuquence of characters and
        the empty string.
        
    +   This symbol matches 1 or more of the
        preceding character, set or group.
        (This differs from '*', because the
        preceding character must occur at least
        once)
        
    {#} Braces w/ a number inside (not the '#'
        symbol) match the preceding character, 
        set or group EXACTLY the number of 
        times specified in the braces. 
        
        
    (<chars>)  
        Grouping of characters so that we can
        apply operators across the entire 
        group efficiently.
        
        
### Groups and Back Referenes

    Parentheses create 'subexpressions' by
    grouping characters together. 
    
    They also create BACKREFERENCES. 
    
    A backreference is the part of the string 
    matched by the GROUPED part of the regular
    expression.
    
    The value here is that since it is STORED, 
    it can be reused inside the expression 
    itself as well as afterwards. 
        
    NOTE: by default, backreferences are accessed
    by the number in which they are matched
    in the regex pattern. 
    
    In order to use NAMED references, you use the
    following syntax:
    
        (?P<name>group)
            
         name = the name of the back reference
         group = the group you are trying
                    to match.
    
### Compile Flags

    re.I    re.IGNORECASE       makes regex case sensitive
                                
    re.L    re.LOCALE           The behaviour of some special sequences like \w, \W, \b,\s, \S will be made 
                                dependant on the current locale, i.e. the user's language, country aso.  
   
    re.M    re.MULTILINE        ^ and $ will match at the beginning and at the end of each line and not just at the 
                                beginning and the end of the string

    re.S    re.DOTALL           The dot "." will match every character plus the newline

    re.U    re.UNICODE          Makes \w, \W, \b, \B, \d, \D, \s, \S dependent on Unicode character properties

    re.X    re.VERBOSE          Allowing "verbose regular expressions", i.e. whitespace are ignored. This means that 
                                spaces, tabs, and carriage returns are not matched as such. If you want to match a 
                                space in a verbose regular expression, you'll need to escape it by escaping it with a 
                                backslash in front of it or include it in a character class. # are also ignored, except
                                when in a character class or preceded by an non-escaped backslash. Everything 
                                following a "#" will be ignored until the end of the line, so this character can be 
                                used to start a comment.
                                 