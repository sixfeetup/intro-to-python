.. -*- coding: utf-8 -*-

Intro to Programming using Python
=================================

----

Your instructor
===============

Calvin Hendryx-Parker, CTO
++++++++++++++++++++++++++

Six Feet Up, Inc.
+++++++++++++++++

Eleven Fifty Instructor
+++++++++++++++++++++++

.. note::
    Introduce yourself, why are you the person they should be listening to for
    the next 5 days.
    Started using Python in 1999 (with Zope)

----

Goals
=====

* Learn basic terminology used by programmers
* Build useful software you can use now

.. note::
    End project will be to build tools to manipulate CSV data you might use in Excel

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

.. note::
    The heart of a CLI is a **read-evaluate-print loop**, or REPL:
    when the user types a command and then presses the enter (or return) key,
    the computer reads it, executes it, and prints its output.

----

REPL
====

* Read
* Execute
* Print
* Loop

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
Quick Overview of computer languages
====================================

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


Python Install
==============

* Mac
  * Home Brew
  * OS X Dev Tools
* Ubuntu Linux

----

Editor setup
============

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

     - .. image:: a1box.png
          :class: incremental

.. container:: handout

   Box "a" now contains an integer 1.

   Assigning another value to the same variable replaces the contents
   of the box:

.. list-table::
   :class: incremental borderless

   * - ::

           a = 2;

     - .. image:: a2box.png
          :class: incremental

   Now box "a" contains an integer 2.

   Assigning one variable to another makes a copy of the value and
   puts it in the new box:

.. list-table::
   :class: incremental borderless

   * - ::

           int b = a;

     - .. image:: b2box.png
          :class: incremental

     - .. image:: a2box.png
          :class: incremental

   "b" is a second box, with a copy of integer 2.  Box "a" has a
   separate copy.

----

Python has "names"
==================

   In Python, a "name" or "identifier" is like a parcel tag (or
   nametag) attached to an object.

.. list-table::
   :class: incremental borderless

   * - ::

           a = 1

     - .. image:: a1tag.png
          :class: incremental

   Here, an integer 1 object has a tag labelled "a".

   If we reassign to "a", we just move the tag to another object:

.. list-table::
   :class: incremental borderless

   * - ::

           a = 2

     - .. image:: a2tag.png
          :class: incremental

     - .. image:: 1.png
          :class: incremental

   Now the name "a" is attached to an integer 2 object.

   The original integer 1 object no longer has a tag "a".  It may live
   on, but we can't get to it through the name "a".  (When an object
   has no more references or tags, it is removed from memory.)

   If we assign one name to another, we're just attaching another
   nametag to an existing object:

.. list-table::
   :class: incremental borderless

   * - ::

           b = a

     - .. image:: ab2tag.png
          :class: incremental

   The name "b" is just a second tag bound to the same object as "a".

   Although we commonly refer to "variables" even in Python (because
   it's common terminology), we really mean "names" or "identifiers".
   In Python, "variables" are nametags for values, not labelled boxes.

   If you get nothing else out of this tutorial, I hope you understand
   how Python names work.  A good understanding is certain to pay
   dividends, helping you to avoid cases like this:

.. note::
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

----

Strings
=======

----


* Data Structures
* Conditional Expressions
* Conditional Loops
* Logical Operators
* Loops
* Functions
* Style and Idioms
* Algorithms and code
* Classes and Objects
* Modules and packages
* Building Command Line Programs
* Working with Files
  * read in a CSV file
* Working with the web
  * show urllib2
  * install requests and show the good life
* Testing your code
* Error handling
* Logging
* Defensive Programming and Common Gotchas
* Tools
  * Basic Shell Commands
  * Reading a Diff


----

Credits
=======

Shell -- http://swcarpentry.github.io/shell-novice/
Variables -- http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html
Datatypes -- http://www.diveintopython3.net/
