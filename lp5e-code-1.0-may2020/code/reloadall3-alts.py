"""
===========================================================================
reloadall3.py: transitively reload nested modules (explicit stack).

A May 2020 update to an example from Learning Python, 5th Edition.
This version demos three recodings that fix a problem in the original.
Comments are errata-page replies to the reader who found the issue.
Run this file directly to see the output of its four alternatives.
===========================================================================
"""

import types
from imp import reload                              # from required in 3.X
from reloadall import status, tryreload, tester


"""
===========================================================================
You're right (and great catch! - I wish this had been reported earlier).  
As coded in the book originally, reloadall3 can indeed reload a module 
more than once, because it checks only modules already visited, not those 
currently scheduled to be visited on the stack.  Because a module is never
again checked for prior visits once it's scheduled for reloading, modules
that are rescheduled before they are reloaded will be reloaded redundantly.
Though uncaught in testing and somewhat dependent on ordering, this can 
happen anytime a module is imported by multiple others:
===========================================================================
"""

def transitive_reload0(modules, visited):           # 0: Original version
    while modules:
        next = modules.pop()                        # Delete next item at end
        status(next)                                # Reload this, push attrs
        tryreload(next)
        visited.add(next)
        modules.extend(x for x in next.__dict__.values()
            if type(x) == types.ModuleType and x not in visited)

def reload_all0(*modules):
    transitive_reload0(list(modules), set())


"""
===========================================================================
Your proposed solution works, because it checks the already-scheduled 
stack too, before extending it.  This prevents the reschedules, and 
hence the duplicate reloads:
===========================================================================
"""

def transitive_reload1(modules, visited):           # 1: Reader's working fix
    while modules:
        next = modules.pop()                        # Delete next item at end
        status(next)                                # Reload this, push attrs
        tryreload(next)
        visited.add(next)
        modules.extend(x for x in next.__dict__.values()
            if type(x) == types.ModuleType and x not in visited and x not in modules)

def reload_all1(*modules):
    transitive_reload1(list(modules), set())


"""
===========================================================================
If pressed, though, I'd say that it seems a bit gray to check for 
membership in a list while it is in the process of being extended.  
The generator passed to extend() yields one item to tack onto the 
list at a time - while also checking the contents of the list.  That
works, but seems very implicit (if not implementation dependent). 
I'd rather avoid the ambiguity and drama, and move the visited test 
up as follows, to trap repeats before their reload is attempted. 
This also _might_ be marginally faster because it trades list scans 
for set hashing, but benchmarking results are extra credit here:
===========================================================================
"""

def transitive_reload2(modules, visited):           # 2: Avoid 'in' during 'extend'
    while modules:
        next = modules.pop()                        # Delete next item at end
        if next in visited: continue                # Already reloaded anywhere?
        status(next)                                # Reload this, push attrs
        tryreload(next)
        visited.add(next)
        modules.extend(x for x in next.__dict__.values() 
            if type(x) == types.ModuleType)

def reload_all2(*modules):
    transitive_reload2(list(modules), set())


"""
===========================================================================
Better still: the following coding is much closer in structure to the 
recursive reloadall2 version that precedes it in the book, and hence 
better illustrates the real recursive-versus-stack point of this section.
It also traps non-module arguments at the top level; neither the original 
nor the two other alternatives above do.  Hence, this is how this example
will be patched in future reprints of the book (see the errata page):
===========================================================================
"""

def transitive_reload3(modules, visited):           # 3: Symmetry, catch non-mods
    while modules:
        next = modules.pop()                        # Delete next item at end
        if (type(next) == types.ModuleType          # Valid module object?
            and next not in visited):               # Not already reloaded?
            status(next)                            # Reload this, push attrs
            tryreload(next)
            visited.add(next)
            modules.extend(next.__dict__.values())

def reload_all3(*modules):
    transitive_reload3(list(modules), set())


"""
===========================================================================
When tested, all three recodings fully avoid the duplicate reloads 
and produce the same results, though visitation order varies slightly 
as expected (you can run all this code live by grabbing a copy from 
https://learning-python.com/reloadall3.py):
===========================================================================
"""

# prior API compatibility
reload_all = reload_all3

if __name__ == '__main__':
    # self-test
    import os, tkinter, reloadall3

    for test in (os, tkinter, reloadall3):
        print('\n%s\n[%s]' % ('-' * 40, test.__name__))

        for ra in (reload_all0, reload_all1, reload_all2, reload_all3):
            print('\n<%s>' % ra.__name__)
            ra(test)


"""
===========================================================================
RELATED NOTE: when this example is run today, Python 3.8 (and perhaps 
earlier) generate a deprecation warning that:
 
   "the imp module is deprecated in favour of importlib"  

Alas, Python's module API has been a moving target for some time now 
(per the book, reload() used to be a built-in function in 2.X), and 
3.X has a now-long history of arbitrary and opinion-based changes like 
this that rudely break existing code.  

In this case, reload() has been pointlessly relocated  _twice_ in 3.X, 
and this example will probably also require changing "imp" to "importlib" 
in the near future to avoid failing altogether with an exception.  This 
is too much change to patch in reprints, so this note will have to suffice.

On the other hand, recursion coding concepts illustrated by this example
are still as relevant to the art of programming as ever.  Small details 
like module names do morph, but the larger fundamentals presented by 
this book don't.
===========================================================================
"""