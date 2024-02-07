Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #12-07-18
>>> #data types in python
>>> 							#python numbers
>>> " hello" +"ravi"
' helloravi'
>>> "hello"/123
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    "hello"/123
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> "hi" +" "+"ravi"
'hi ravi'
>>> x=5.3+0.9j
>>> print(x.real  x.imag)
SyntaxError: invalid syntax
>>> print(x.real)
5.3
>>> print(x.img)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(x.img)
AttributeError: 'complex' object has no attribute 'img'
>>> 				#operations on numbers
>>> 						#operations on numbers
>>> #"type()" returns type of expression
>>> x=65
>>> print(chr(x))
A
>>> y='a'
>>> print(ord(y))
97
>>> 			#input operation
>>> #input()
>>> #raw_input()
>>> name=input("enter your name")
enter your name veera
>>> name
' veera'
>>> age=input("enter your age")
enter your age12re
>>> age
'12re'
>>> age=input("enter your age")
enter your age12
>>> type(age)
<class 'str'>
>>> dob=input("enter date")
enter date12-09-98
>>> dob
'12-09-98'
>>> type(dob)
<class 'str'>
>>> age=int(input(enter age))
SyntaxError: invalid syntax
>>> age=int(input("enter age"))
enter age4
>>> age
4
>>> age=int(input("enter age"))
enter agert
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    age=int(input("enter age"))
ValueError: invalid literal for int() with base 10: 'rt'
>>> 
>>> 			#output formating
>>> 			#tuple{}
>>> x=5,y=6
SyntaxError: can't assign to literal
>>> x,y=5,6
>>> print("x is {} and y is {}".format((x,y)))
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print("x is {} and y is {}".format((x,y)))
IndexError: tuple index out of range
>>> print("x is {} and y is {}"format((x,y)))
SyntaxError: invalid syntax
>>> print("x is {} and y is {}".format((x,y)))
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print("x is {} and y is {}".format((x,y)))
IndexError: tuple index out of range
>>> print("x is {} and y is {}".format(x,y))
x is 5 and y is 6
>>> print("x is {0} and y is {1}".format(x,y))
x is 5 and y is 6
>>> print("x is {1} and y is {0}".format(x,y))
x is 6 and y is 5
>>> help("modules")

Please wait a moment while I gather a list of all available modules...

1                   audioop             idle                search
8-7-18              autocomplete        idle_test           searchbase
__future__          autocomplete_w      idlelib             searchengine
__main__            autoexpand          imaplib             secrets
_ast                base64              imghdr              select
_asyncio            bdb                 imp                 selectors
_bisect             binascii            importlib           setuptools
_blake2             binhex              inspect             shelve
_bootlocale         bisect              io                  shlex
_bz2                browser             iomenu              shutil
_codecs             builtins            ipaddress           signal
_codecs_cn          bz2                 itertools           site
_codecs_hk          cProfile            json                smtpd
_codecs_iso2022     calendar            keyword             smtplib
_codecs_jp          calltip_w           lib2to3             sndhdr
_codecs_kr          calltips            linecache           socket
_codecs_tw          cgi                 locale              socketserver
_collections        cgitb               logging             sqlite3
_collections_abc    chunk               lzma                sre_compile
_compat_pickle      cmath               macosx              sre_constants
_compression        cmd                 macpath             sre_parse
_csv                code                macurl2path         ssl
_ctypes             codecontext         mailbox             stackviewer
_ctypes_test        codecs              mailcap             stat
_datetime           codeop              mainmenu            statistics
_decimal            collections         marshal             statusbar
_dummy_thread       colorizer           math                string
_elementtree        colorsys            mimetypes           stringprep
_findvs             compileall          mmap                struct
_functools          concurrent          modulefinder        subprocess
_hashlib            config              msilib              sunau
_heapq              config_key          msvcrt              symbol
_imp                configdialog        multicall           symtable
_io                 configparser        multiprocessing     sys
_json               contextlib          netrc               sysconfig
_locale             copy                nntplib             tabbedpages
_lsprof             copyreg             nt                  tabnanny
_lzma               crypt               ntpath              tarfile
_markupbase         csv                 nturl2path          telnetlib
_md5                ctypes              numbers             tempfile
_msi                curses              opcode              test
_multibytecodec     datetime            operator            textview
_multiprocessing    dbm                 optparse            textwrap
_opcode             debugger            os                  this
_operator           debugger_r          outwin              threading
_osx_support        debugobj            paragraph           time
_overlapped         debugobj_r          parenmatch          timeit
_pickle             decimal             parser              tkinter
_pydecimal          delegator           pathbrowser         token
_pyio               dfghj               pathlib             tokenize
_random             difflib             pdb                 tooltip
_sha1               dis                 percolator          trace
_sha256             distutils           pickle              traceback
_sha3               doctest             pickletools         tracemalloc
_sha512             dummy_threading     pip                 tree
_signal             dynoption           pipes               tty
_sitebuiltins       easy_install        pkg_resources       turtle
_socket             editor              pkgutil             turtledemo
_sqlite3            email               platform            types
_sre                encodings           plistlib            typing
_ssl                ensurepip           poplib              undo
_stat               enum                posixpath           unicodedata
_string             errno               pprint              unittest
_strptime           faulthandler        profile             urllib
_struct             filecmp             pstats              uu
_symtable           fileinput           pty                 uuid
_testbuffer         filelist            py_compile          venv
_testcapi           fnmatch             pyclbr              warnings
_testconsole        formatter           pydoc               wave
_testimportmultiple fractions           pydoc_data          weakref
_testmultiphase     ftplib              pyexpat             webbrowser
_thread             functools           pyparse             welcome
_threading_local    gc                  pyshell             windows
_tkinter            genericpath         query               winreg
_tracemalloc        getopt              queue               winsound
_warnings           getpass             quopri              wsgiref
_weakref            gettext             random              xdrlib
_weakrefset         glob                re                  xml
_winapi             grep                redirector          xmlrpc
abc                 gzip                replace             xxsubtype
aifc                hashlib             reprlib             zipapp
antigravity         heapq               rlcompleter         zipfile
argparse            help                rpc                 zipimport
array               help_about          rstrip              zlib
ast                 history             run                 zoomheight
asynchat            hmac                runpy               zzdummy
asyncio             html                runscript           
asyncore            http                sched               
atexit              hyperparser         scrolledlist        

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

>>> help("math"0
     
SyntaxError: invalid syntax
>>> help("math")
Help on built-in module math:

NAME
    math

DESCRIPTION
    This module is always available.  It provides access to the
    mathematical functions defined by the C standard.

FUNCTIONS
    acos(...)
        acos(x)
        
        Return the arc cosine (measured in radians) of x.
    
    acosh(...)
        acosh(x)
        
        Return the inverse hyperbolic cosine of x.
    
    asin(...)
        asin(x)
        
        Return the arc sine (measured in radians) of x.
    
    asinh(...)
        asinh(x)
        
        Return the inverse hyperbolic sine of x.
    
    atan(...)
        atan(x)
        
        Return the arc tangent (measured in radians) of x.
    
    atan2(...)
        atan2(y, x)
        
        Return the arc tangent (measured in radians) of y/x.
        Unlike atan(y/x), the signs of both x and y are considered.
    
    atanh(...)
        atanh(x)
        
        Return the inverse hyperbolic tangent of x.
    
    ceil(...)
        ceil(x)
        
        Return the ceiling of x as an Integral.
        This is the smallest integer >= x.
    
    copysign(...)
        copysign(x, y)
        
        Return a float with the magnitude (absolute value) of x but the sign 
        of y. On platforms that support signed zeros, copysign(1.0, -0.0) 
        returns -1.0.
    
    cos(...)
        cos(x)
        
        Return the cosine of x (measured in radians).
    
    cosh(...)
        cosh(x)
        
        Return the hyperbolic cosine of x.
    
    degrees(...)
        degrees(x)
        
        Convert angle x from radians to degrees.
    
    erf(...)
        erf(x)
        
        Error function at x.
    
    erfc(...)
        erfc(x)
        
        Complementary error function at x.
    
    exp(...)
        exp(x)
        
        Return e raised to the power of x.
    
    expm1(...)
        expm1(x)
        
        Return exp(x)-1.
        This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
    
    fabs(...)
        fabs(x)
        
        Return the absolute value of the float x.
    
    factorial(...)
        factorial(x) -> Integral
        
        Find x!. Raise a ValueError if x is negative or non-integral.
    
    floor(...)
        floor(x)
        
        Return the floor of x as an Integral.
        This is the largest integer <= x.
    
    fmod(...)
        fmod(x, y)
        
        Return fmod(x, y), according to platform C.  x % y may differ.
    
    frexp(...)
        frexp(x)
        
        Return the mantissa and exponent of x, as pair (m, e).
        m is a float and e is an int, such that x = m * 2.**e.
        If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
    
    fsum(...)
        fsum(iterable)
        
        Return an accurate floating point sum of values in the iterable.
        Assumes IEEE-754 floating point arithmetic.
    
    gamma(...)
        gamma(x)
        
        Gamma function at x.
    
    gcd(...)
        gcd(x, y) -> int
        greatest common divisor of x and y
    
    hypot(...)
        hypot(x, y)
        
        Return the Euclidean distance, sqrt(x*x + y*y).
    
    isclose(...)
        isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0) -> bool
        
        Determine whether two floating point numbers are close in value.
        
           rel_tol
               maximum difference for being considered "close", relative to the
               magnitude of the input values
            abs_tol
               maximum difference for being considered "close", regardless of the
               magnitude of the input values
        
        Return True if a is close in value to b, and False otherwise.
        
        For the values to be considered close, the difference between them
        must be smaller than at least one of the tolerances.
        
        -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
        is, NaN is not close to anything, even itself.  inf and -inf are
        only close to themselves.
    
    isfinite(...)
        isfinite(x) -> bool
        
        Return True if x is neither an infinity nor a NaN, and False otherwise.
    
    isinf(...)
        isinf(x) -> bool
        
        Return True if x is a positive or negative infinity, and False otherwise.
    
    isnan(...)
        isnan(x) -> bool
        
        Return True if x is a NaN (not a number), and False otherwise.
    
    ldexp(...)
        ldexp(x, i)
        
        Return x * (2**i).
    
    lgamma(...)
        lgamma(x)
        
        Natural logarithm of absolute value of Gamma function at x.
    
    log(...)
        log(x[, base])
        
        Return the logarithm of x to the given base.
        If the base not specified, returns the natural logarithm (base e) of x.
    
    log10(...)
        log10(x)
        
        Return the base 10 logarithm of x.
    
    log1p(...)
        log1p(x)
        
        Return the natural logarithm of 1+x (base e).
        The result is computed in a way which is accurate for x near zero.
    
    log2(...)
        log2(x)
        
        Return the base 2 logarithm of x.
    
    modf(...)
        modf(x)
        
        Return the fractional and integer parts of x.  Both results carry the sign
        of x and are floats.
    
    pow(...)
        pow(x, y)
        
        Return x**y (x to the power of y).
    
    radians(...)
        radians(x)
        
        Convert angle x from degrees to radians.
    
    sin(...)
        sin(x)
        
        Return the sine of x (measured in radians).
    
    sinh(...)
        sinh(x)
        
        Return the hyperbolic sine of x.
    
    sqrt(...)
        sqrt(x)
        
        Return the square root of x.
    
    tan(...)
        tan(x)
        
        Return the tangent of x (measured in radians).
    
    tanh(...)
        tanh(x)
        
        Return the hyperbolic tangent of x.
    
    trunc(...)
        trunc(x:Real) -> Integral
        
        Truncates x to the nearest Integral toward 0. Uses the __trunc__ magic method.

DATA
    e = 2.718281828459045
    inf = inf
    nan = nan
    pi = 3.141592653589793
    tau = 6.283185307179586

FILE
    (built-in)


>>> import keyword
>>> print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> import time
>>> print(time.ctime())
Thu Jul 12 09:55:13 2018
>>> import 05
SyntaxError: invalid token
>>> import os
>>> print(os.mkdir("ravi"))
None
>>> import sys
>>> print(sys.version)
3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)]
>>> import math
>>> math(sqrt(4))
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    math(sqrt(4))
NameError: name 'sqrt' is not defined
>>> print(math(sqrt(4)))
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    print(math(sqrt(4)))
NameError: name 'sqrt' is not defined
>>> print(math.sqrt(4))
2.0
>>> sizeof(x)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    sizeof(x)
NameError: name 'sizeof' is not defined
>>> import sys
>>> #size
>>> x=1
>>> sys.getsizeof(x)
28
>>> id(x)
1990222048
>>> x="r"sys.getsizeof(x)
SyntaxError: invalid syntax
>>> x="r"
>>> sys.getsizeof(x)
50
>>> #int 28 float 24 string 49
>>> """ thise are comments"""
' thise are comments'
>>> ''' '''
' '
>>> 
>>> 
