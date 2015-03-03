.. -*- coding: utf-8 -*-

:title: Intro to Programming
:event: Eleven Fifty
:author: Calvin Hendryx-Parker
:pygments: tango
:css: custom.css

.. |space| unicode:: 0xA0 .. non-breaking space
.. |br| raw:: html
    
    <br />

----

Intro to Programming using Python
=================================

----

Your Instructor
===============

Calvin Hendryx-Parker, CTO
++++++++++++++++++++++++++

Six Feet Up, Inc.
-----------------

Eleven Fifty Instructor

.. note::

    Introduce yourself, why are you the person they should be listening to for
    the next 5 days.

    Started programming in 1998 (PHP, Visual Basic and ASP)

    Started using Python in 1999 (with Zope)

----

Quick Survey
============

.. note::

    Why did you sign up for this course?

    Who has written a program before?

    Who knows what the console or terminal is on your computer?

    Would you rate yourself an expert at Excel?

    Who has done an intro programming course before?
   
----

Goals
=====

* Learn basic terminology used by programmers
* Build useful software you can use now

.. note::

    End project will be to build tools to manipulate CSV data you might use in Excel

    Python is the most popular teching language at the university level right now

    Python creator Guido von Rossum believes Python caught on in the labs because “scientists often need to improvise when trying to interpret results, so they are drawn to dynamic languages which allow them to work very quickly and see results almost immediately.”

----

Quick Chat
==========

IRC
+++

http://webchat.freenode.net?channels=#ElevenFifty

irc://chat.freenode.net/ElevenFifty

.. note::

    Internet Relay Chat can be used to overthrow govermnents

    but more importantly, it is a space where many projects developers gather and answer questions

----

Let's get setup for the course
==============================

* Install Python
* Install PyCharm

Optionally:
+++++++++++

* Install VirutalBox
* Import our Virtual Appliance

----

Python Install
==============

* Mac OS X includes Python 2

  * Install Python three from `Home Brew`_
  * OS XCode Command Line tools

* Ubuntu Linux includes Python
* Python Installers @ python.org_

.. _Home Brew: http://brew.sh
.. _python.org: http://www.python.org

.. note::

    xcode-select --install to install the tools on mac

----

Git Install
===========

* Included on OS X
* Install from package repos on Linux
* http://git-scm.com/downloads for other installers

.. note::

    We will be using git during the course

----

PyCharm Install
===============

* Installers for Mac and Windows
* Requires Java

.. code:: sh

    $ $EXTRACTION_PATH/pycharm-edu-1.0.1/bin/pycharm.sh  

.. note::

   ubuntu ppa for java http://www.webupd8.org/2012/09/install-oracle-java-8-in-ubuntu-via-ppa.html

----

What are Computer Programs
==========================

* Collection of instructions

  * Interact with the user
  * Interact with the computer hardware 
  * Process data

.. note::
    We all know what a computer is?  it is a machine that stores pieves of information
    It also moves, arranges and controls that information (or data)

----

Computers are not very smart
============================

.. image:: figures/Spinning_Star.svg

.. note::
    They can only do what you tell them to do

----

They follow sets of Instructions
================================

::

    Strawberry Kiwi Tart

    Ingredients:

    Crust:
    1 box Pillsbury™ refrigerated pie crusts, softened as directed on box
    
    Filling:
    2/3 cup Yoplait® 99% Fat Free creamy vanilla yogurt (from 2-lb container)
    1 container (8 oz) reduced-fat sour cream
    1 box (4-serving size) vanilla instant pudding and pie filling mix
    2 tablespoons orange marmalade
    
    Topping:
    1 cup halved fresh strawberries
    2 kiwifruit, peeled, thinly sliced
    2 tablespoons orange marmalade
    
    Directions:
    
    Step 1: Heat oven to 450°F. Make pie crust as directed on box for One-Crust Baked Shell, using 9-inch tart pan with removable bottom or 9-inch glass pie plate. Bake 9 to 11 minutes or until light golden brown. Cool completely, about 30 minutes.
    
    Step 2: In medium bowl, mix filling ingredients with wire whisk until well blended. Pour into cooled baked shell. Arrange strawberries and kiwifruit on filling.
    
    Step 3: In small microwavable bowl, microwave marmalade uncovered on High 5 to 10 seconds or until melted. Brush over fruit. Refrigerate about 1 hour or until set before serving. Cover and refrigerate any remaining tart.

Source: http://www.foodista.com/blog/2015/02/27/beautiful-strawberry-kiwi-tart

----

Algorithms
==========

.. note::

    Fancy name for instructions we give to computers

    Like a recipes with specific steps to follow

    Usually with a lot more steps and written in a programming language like Python

    Imagine telling someone to make a PB&J and they have no idea what a knife is or how to open the peanut butter

----

Quick Calculator
================

.. code:: python

    >>> 2 + 2
    >>> 12 -3
    >>> 9 + 5 - 15
    

.. note::

    Open PyCharm and get into the python shell to try it out as a calculator

    In the programming world, we call the + and - operators

----

More Math
=========

.. code:: python

    >>> 6 * 5
    >>> 6 / 2
    >>> 10 * 5 * 3
    >>> 10 / 3

.. note::

    careful with integers and decimals

    Python 3 knows what you "mean", but python 2 would not give you the same answer

    integers vs floats (decimals)

    Ruby for example will tell you 10/3 is 3

    Python 2 is also the same

    If you want decimals, you have to talk in decimals in those languages

----

Comparison Operators
====================

.. list-table::

   * - ``==``
     - Equal to
   * - ``!=``
     - Not equal to
   * - ``<``
     - Less than
   * - ``>``
     - Greater than
   * - ``<=``
     - Less than or equal to
   * - ``>=``
     - Greater than or equal to

.. note::

    we will go over a coule examples and discover another datatype of Python

----

Comparison Practice
===================

.. code:: python

    >>> 5 < 4 + 3
    >>> 12 + 1 >= 12
    >>> 16 * 2 == 32
    >>> 16 != 16
    >>> 5 >= 6

.. note::

    Try these out and see what the interpreter returns to you

----

Editors
=======

Text Editors
++++++++++++

* Vim
* Emacs
* Sublime Text
* Textmate
* Notepad++

IDE
+++

* PyCharm
* Wing IDE
* Komodo
* XCode
* Eclipse

.. note::

    explain IDE

    git init and then add all the course files

----

PyCharm
=======

Hello World
+++++++++++

----

Intro to Shell
==============

At a high level, computers do four things:

- run programs
- store data
- communicate with each other
- interact with us

.. note::

    most of us use windows, icons, mice, and pointers

    These technologies didn't become widespread until the 1980s

    Going back past the 1950s, the only way to interact with early computers was to rewire them.

    But in between, from the 1950s to the 1980s, most people used line printers.

    These devices only allowed input and output of the letters, numbers, and punctuation found on a standard keyboard,

    so programming languages and interfaces had to be designed around that constraint.

----

Command-line interface
======================

CLI vs GUI
++++++++++

.. note::

    The heart of a CLI is a **read-evaluate-print loop**, or REPL:

    when the user types a command and then presses the enter (or return) key,

    the computer reads it, executes it, and prints its output.

----

REPL
====

* **R** ead
* **E** xecute
* **P** rint
* **L** oop

.. note::

    This description makes it sound as though the user sends commands directly to the computer,

    and the computer sends output directly to the user.

    In fact, there is usually a program in between called a **command shell**.

----

Popular Shells
==============

* bash
* zsh
* csh

.. note::

    Windows has a shell as well `cmd.exe`

----

Windows Shell Alternatives
==========================

* Window's PowerShell
* Cygwin

.. note::

    We will not cover these!

----

Let's get started
=================

.. code:: sh

    $ # I'm a prompt


.. note::

   The dollar sign is a prompt, which shows us that the shell is waiting for input; your shell may show something more elaborate.

----

Run some commands
=================

.. code:: sh

    $ whoami
    calvin

.. code:: sh

    $ pwd
    /home/calvin

.. note::

    finds a program called whoami,

    runs that program,

    displays that program's output, then

    displays a new prompt to tell us that it's ready for more commands.

    whoami and why not whereami?

    in the early 1970s, when Unix was first being developed, every keystroke counted: the devices of the day were slow, and backspacing on a teletype was so painful that cutting the number of keystrokes in order to cut the number of typing mistakes was actually a win for usability

----

The Filesystem
==============

.. image:: figures/filesystem.svg

.. note::

    To understand what a "home directory" is, let's have a look at how the file system as a whole is organized. At the top is the root directory that holds everything else. We refer to it using a slash character / on its own; this is the leading slash in /users/nelle.

----

Home Directories
================

.. image:: figures/home-directories.svg

.. note::

    Underneath /users, we find one directory for each user with an account on this machine

    two meanings for the / character. in front of name it is the directory root, inside a name, it is a seperator.

----

Listing Files
=============

.. code:: sh

    $ ls
    creatures  molecules           pizza.cfg
    data       north-pacific-gyre  solar.pdf
    Desktop    notes.txt           writing

----

Listing Files
=============

.. code:: sh

    $ ls -F
    creatures/  molecules/           pizza.cfg
    data/       north-pacific-gyre/  solar.pdf
    Desktop/    notes.txt            writing/

.. code:: sh

    $ ls -F data
    amino-acids.txt   elements/     morse.txt
    pdb/              planets.txt   sunspot.txt

.. note::

    we use an flag `-F` to change the output

    we use an argument to get different information

    data doesn't have a slash, it is relative to where you are

----

Listing Files
=============

.. code:: sh

    $ ls -F /data
    access.log    backup/    hardware.cfg
    network.cfg

.. note::

    Now we are using an absolute path

----

Changing Directories
====================

.. code:: sh

    $ cd data
    $ pwd
    /home/calvin/data

.. note::

    nothing fancy here, we change into the directory

    try running `pwd`

.. code:: sh

    $ cd ..
    $ pwd
    /home/calvin

.. note::

    ".." is a special directory meaning the one containing this one or its parent
    this special directory doesn't show up unless we use the `-a` flag
    the current directory is "."

    . and .. don't belong to the command ls, every program can use them.

    stop and explain about what using `cd` with no args will do and what the special `~` shortcut are

----

Creating Files and Directories
==============================

.. code:: sh

    $ mkdir thesis

.. code:: sh

    $ cd thesis
    $ touch draft.txt

.. note::

    use ls to verify that your directory has been created

----

Removing Files and Directories
==============================

.. code:: sh

    $ rm draft.txt

.. code:: sh

    $ cd ..
    $ rmdir thesis
    rmdir: failed to remove `thesis`: Directory not empty

.. code:: sh

    $ rm thesis/draft.txt
    $ rmdir thesis

.. code:: sh

    $ rm -r thesis

.. note::

    there is no "trash" here, deleting is forever

----

Moving Files and Directories
============================

.. code:: sh

    $ mv thesis/draft.txt .

.. note::

    Can do the same as a copy as well using `cp`

----

Wildcards
=========

\* is a **wildcard**
++++++++++++++++++++

\? is also a **wildcard**
+++++++++++++++++++++++++

.. note::

    \* matches zero or more charaters

    \? matches one charater

    we can talk more shell later, but lets get to some programming

    pipes and redirecting output are extremely useful as a developer

----

Version Control
===============

* git
* Mercurial (hg)
* Subversion (svn)
* CVS

.. note::

    we will only cover git

    mention github and bitbucket as social coding platforms

----

Why Version Control
===================

.. image:: figures/phd101212s.gif

----

Quick Git Primer
================

.. image:: figures/git-staging-area.svg

----

Quick Git Primer
================

.. image:: figures/git-committing.svg

----

Setup git Environment
=====================

* Name
* Email Address

----

Quick git Excercises
====================

* Initialize your PyCharm Introduction
* Stage all of the project files
* Commit the changes
* Do the "Comments" tutorial
* Diff your changes
* Stage and Commit these changes

----

Quick Overview of Computer Languages
====================================

* Low Level
* High Level
* Compiled
* Interpreted
* Strongly Typed
* Dynamically Typed
* Weakly Typed

.. note::

     languages require total and complete detail about everything. C and C++ are such languages

     Other languages will make all sorts of assumptions, and this lets the programmer specify less detail. Python and Basic are such languages, and are called high-level languages

    Java and C are strongly typed

    Python is Strongly typed, but typically it is referred to as dynamically typed

    Javascript, Perl and PHP are weakly typed

----

Zen of Python
=============

Let's get this started with the right mindset

.. code:: python

    >>> import this

.. note::

    These are specific to Python, but let's go over them quickly and we will refer back to them from time to time during the class
    
----

Variables
=========

In many other languages, assigning to a variable puts a value into a box.

.. list-table::
   :class: incremental borderless

   * - ::

        int a = 1;

     - .. image:: figures/a1box.png
          :class: incremental

Assigning another value to the same variable replaces the contents of the box:

.. list-table::
   :class: incremental borderless

   * - ::

           a = 2;

     - .. image:: figures/a2box.png
          :class: incremental


Assigning one variable to another makes a copy of the value and puts it in the new box:

.. list-table::
   :class: incremental borderless

   * - ::

           int b = a;

     - .. image:: figures/b2box.png
          :class: incremental

     - .. image:: figures/a2box.png
          :class: incremental


.. note::

    Box "a" now contains an integer 1.

    Now box "a" contains an integer 2.

    "b" is a second box, with a copy of integer 2.  Box "a" has a separate copy.

----

Python has "names"
==================

In Python, a "name" or "identifier" is like a parcel tag (or nametag) attached to an object.

.. list-table::
   :class: incremental borderless

   * - ::

           a = 1

     - .. image:: figures/a1tag.png
          :class: incremental


If we reassign to "a", we just move the tag to another object:

.. list-table::
   :class: incremental borderless

   * - ::

           a = 2

     - .. image:: figures/a2tag.png
          :class: incremental

     - .. image:: figures/1.png
          :class: incremental

If we assign one name to another, we're just attaching another
nametag to an existing object:

.. list-table::
   :class: incremental borderless

   * - ::

           b = a

     - .. image:: figures/ab2tag.png
          :class: incremental

.. note::

    Here, an integer 1 object has a tag labelled "a".

    Now the name "a" is attached to an integer 2 object.
    
    The original integer 1 object no longer has a tag "a".  It may live
    on, but we can't get to it through the name "a".  (When an object
    has no more references or tags, it is removed from memory.)

    The name "b" is just a second tag bound to the same object as "a".
    
    Although we commonly refer to "variables" even in Python (because
    it's common terminology), we really mean "names" or "identifiers".
    In Python, "variables" are nametags for values, not labelled boxes.
    
    If you get nothing else out of this tutorial, I hope you understand
    how Python names work.  A good understanding is certain to pay
    dividends, helping you to avoid cases like this:

    We will go over why this is more important later when we get into examples of functions.
    Not understanding how a language handles variables (and scope) can lead to confusing results.
    You "assign" a name to a value and that process is called "assignment"
    Next we talk about data types which are determined when you perform assignment

----

Data Types
==========

Python has many native datatypes. Here are the important ones:

* **Booleans** are either True or False.
* **Numbers** can be integers (1 and 2), floats (1.1 and 1.2), fractions (1/2 and 2/3), or even complex numbers.
* **Strings** are sequences of Unicode characters, e.g. an HTML document.
* **Bytes** and **byte arrays**, e.g. a JPEG image file.
* **Lists** are ordered sequences of values.
* **Tuples** are ordered, immutable sequences of values.
* **Sets** are unordered bags of values.
* **Dictionaries** are *unordered* bags of key-value pairs. 

.. note::
    Some languages make you declare the type of a value when you assign it, but Python determines it for you and tracks it internally so you don't have to
    "Duck Typing"
    
    Do PyCharm Variables Excercises


----

Strings
=======

Warning: Gory Details Ahead
+++++++++++++++++++++++++++

.. note::

   gory details ahead

   Briefly mentions character encoding and unicode usage in Python 3

   all strings in python are unicode

----

Strings
=======

Examples:
+++++++++

.. code:: python

    >>> "Hello!"
    >>> "Eleven Fifty"
    >>> "3 + 5"

Try this:
+++++++++

.. code:: python

    >>> apple

.. note::

    Python has a built-in string class named "str" with many handy features

    Strings must be in quotes

    String literals can be enclosed by either double or single quotes, although single quotes are more commonly used.

    A double quoted string literal can contain single quotes without any fuss

    Python strings are "immutable" which means they cannot be changed after they are created


----

Strings
=======

.. code:: python

    s = 'hi'
    print(s[1])          ## i
    print(len(s))        ## 2
    print(s + ' there')  ## hi there

.. note::

    Characters in a string can be accessed using the standard [ ] syntax

    Strings support operators like + and *

    What is the standard [ ] syntax

----

Slicing Strings
===============

The "slice" syntax is a handy way to refer to sub-parts of sequences
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

string[start:end]

.. image:: figures/hello.png

.. note::

    The slice s[start:end] is the elements beginning at start and extending up to but not including end. the Suppose we have s = "Hello"

    The standard zero-based index numbers give easy access to chars near the start of the string. As an alternative, Python uses negative numbers to give easy access to the chars at the end of the string

    It is a neat truism of slices that for any index n, s[:n] + s[n:] == s

    Or put another way s[:n] and s[n:] always partition the string into two string parts, conserving all the characters

    Demo string immutability, try to set one character in a string

----

Strings
=======

.. code:: python

  pi = 3.14
  text = 'The value of pi is ' + pi      ## NO, does not work

But...

.. code:: python

  text = 'The value of pi is '  + str(pi)  ## yes

.. note::

    Unlike Java, the '+' does not automatically convert numbers or other types to string form. The str() function converts values to a string form so they can be combined with other strings.

----

String Methods
==============

Strings are very powerful in Python
+++++++++++++++++++++++++++++++++++


* s.lower(), s.upper()
* s.strip()
* s.isalpha()/s.isdigit()/s.isspace()...
* s.startswith('other'), s.endswith('other')
* s.find('other')
* s.replace('old', 'new')
* s.split('delim')
* s.join(list)

.. note::

    http://rgruet.free.fr/PQR27/PQR2.7.html

    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

    We could use regular expressions, but they get complicated and hard to maintain fast

----

String Formatting
=================

.. code:: python

    >>> "The sum of 1 + 2 is {0}".format(1+2)
    >>> thing = "bucket"
    >>> "Bring me a {}".format(thing)
    >>> "My quest is {name}".format(name="simple")

Advanced Examples
+++++++++++++++++

.. code:: python

    >>> '{:<30}'.format('left aligned')
    >>> '{:>30}'.format('right aligned')
    >>> '{:^30}'.format('centered')
    >>> '{:*^30}'.format('centered')
    >>> '{:,}'.format(1234567890)
    >>> points = 19
    >>> total = 22
    >>> 'Correct answers: {:.2%}'.format(points/total)


.. note::

     The string on which this method is called can contain literal text or replacement fields delimited by braces {}

    https://docs.python.org/3/library/string.html#formatstrings

----

List
====

A list is an ordered container of objects

.. code:: python

   groceries = ['vegetables', 'chips', 'milk']
   mixed_bag = [1, 'two', 3.0, 'four']
   inception = [1, [1, [1, 1]]]

.. note::

    It can contain strings

    Mix between types

    Even contain lists that contain more lists

----

List length
===========

We can use ``len()`` to check the length of a list

.. code:: python

   >>> len(groceries)
   3
   >>> len(mixed_bag)
   4
   >>> len(inception)
   2

.. note::

    Notice that the return value of len is an integer

    The inception list has more items, but at the top level, just an int and
    another list.

----

Adding elements
===============

You can add lists together.

.. code:: python

   >>> two_lists = [1, 3, 5] + [2, 4, 6]
   >>> two_lists
   [1, 3, 5, 2, 4, 6]

Or add a value.

.. code:: python

   >>> two_lists.append(7)
   >>> two_lists
   [1, 3, 5, 2, 4, 6, 7]

----

Removing elements
==================

.. code:: python

   >>> two_lists
   [1, 3, 5, 2, 4, 6, 7]
   >>> two_lists.pop()
   7
   >>> two_lists.pop(2)
   5

----

Accessing List Elements
=======================

.. code:: python

    >>> groceries[0]
    'vegetables'
    >>> groceries[2]
    'milk'
    >>> groceries[-1]
    'milk'
    >>> groceries[-3]
    'vegetables'

.. note::

    Notice that indexing starts at 0

    Going in reverse starting with -1, to retrieve values near the end of the
    list

----

List slicing
============

----

Conditional Expressions
=======================

It's about making decisions
+++++++++++++++++++++++++++

::

    If you're hungry, let's each lunch
    
    If the trash is full, go empty it.

.. note::

    Check out IFTTT.com

----

``if`` Statements
=================

.. code:: python

    >>> name = "Calvin"
    >>> if name == "Calvin":
    >>>     print("Hi Calvin!")

.. note::

    check out the usage of whitespace here and the lack of curly braces and parens

    Python does not use { } to enclose blocks of code for if/loops/function

    indentation/whitespace to group statements

----

``if`` Statements
=================

::

    If you're hungry, let's eat lunch.
        Or else we can eat in an hour.

    If there's mint ice cream. I'll have a scoop.
        Or else I'll take vanilla.

.. code:: python

    >>> if name == "Calvin":
    >>>     print("Hi Calvin!")
    >>> else:
    >>>     print("Impostor!")

.. note::

    Now we add an extra choice

----

``if`` Statements
=================

::

    If there's mint ice cream. I'll have a scoop.
        Or else if we have vanilla, I'll have 2!
        Or else if there's chocolate, give me 3!
        Or I'll just have a donut.

.. code:: python

    >>> if name == "Calvin":
    >>>     print("Hi Calvin!")
    >>> elif name == "John":
    >>>     print("Hi John!")
    >>> else:
    >>>     print("Who are you?")

.. note::

    Now we added even more choice!

    and it can have *elif* and *else* clauses (mnemonic: the word "elif" is the same length as the word "else").

----

Boolean Operators
=================

.. code:: python

    if speed >= 80:
      print 'License and registration please'
      if mood == 'terrible' or speed >= 100:
        print 'You have the right to remain silent.'
      elif mood == 'bad' or speed >= 90:
        print "I'm going to have to write you a ticket."
        write_ticket()
      else:
        print "Let's try to keep it under 80 ok?"


.. note::

    The boolean operators are the spelled out words *and*, *or*, *not* (Python does not use the C-style && || !).

    Let's do the conditional exercises on PyCharm to practice

----

Tuple
=====

----

Dictionary
==========

----

Set
===

----

Conditional Loops
==========================================

----

Logical Operators
==========================================

----

Loops
==========================================

----

Functions
==========================================

----

Style and Idioms
==========================================

----

Algorithms and code
==========================================

----

Classes and Objects
==========================================

----

Modules and packages
==========================================

----

Building Command Line Programs
==========================================

----

Working with Files
==========================================

  - read in a CSV file

----

Working with the web
==========================================

  - show urllib2
  - install requests and show the good life

----

Testing your code
==========================================

----

Error handling
==========================================

----

Logging
==========================================

----

Defensive Programming and Common Gotchas
==========================================

----

Tools
==========================================

  - Basic Shell Commands
  - Reading a Diff

----

Credits
=======

* Shell -- http://swcarpentry.github.io/shell-novice
* Variables -- http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html
* Datatypes -- http://www.diveintopython3.net
* Strings -- http://www.diveintopython3.net/strings.html
