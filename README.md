# Python-Linux Repo

Cheat sheets: https://alta3.com/posters

Helpful tutorial videos: https://www.youtube.com/user/Alta3Research/videos

## Custom Python for Software Developers

Lecture and Labs 10 Day Course

## Course Overview

This course combines three days of Linux Essentials content with two weeks of Python for Developers.

Linux is at the core of nearly all open-source projects. If you want to become a developer, then Linux is the engine that will run nearly all of your code. Your view of Linux will be different from a Linux System admin who must make sure that system availability is as close to 100% as possible. As a developer, you will be required to make Linux bend to your will, which means you will have great power over the system. With great power comes great responsibility. You must be able to use Linux to accomplish your task, while not adversely affecting system reliability, security or operational efficiency. In this course you will learn how to make Linux deliver essential services and in the same motion, maintain the Linux system integrity. Successful students can generally expect their work efficiency to increase dramatically.

Python is an interpreted, object-oriented, high-level language that gets work done in a hurry! Python can improve all professional’s ability to do work and is freely available on all major platforms without a charge.

Application Programming Interfaces (APIs) have become increasingly important as they provide developers with connectivity to everything from rich datasets in an array of formats (such as JSON), to exposing the configurability of software applications and network appliances. The focus of this course is to build strong Python coding skills by teaching the foundations of Python, moving into interacting, designing, and building APIs for the purposes of scripting automated solutions to complex tasks.

Class is mostly live demonstrations and hands-on labs.
What Students Learn

In this course, students will learn how to get started with Python, including an overview of the Standard Library, and popular 3rd party libraries. Lessons include version control with git, storing data in list and dictionaries, working with objects and methods, conditionals, looping, creating functions, and building classes. Highly relevant labs enhance these skills as students learn how to use JSON pulled from APIs, manipulate Excel spreadsheets, create feature rich charts and graphs, and parse log files with the Python regular expression library.

Then we move into API’s and design with Python. Students will learn to develop Python scripts that communicate with RESTful (and non-RESTful) APIs, as well as design RESTful API interfaces themselves. They will use Python to open SSH sessions and pass commands to remote servers, move files via SFTP, parse and manipulate popular data structures (JSON, XML, CSV, and YAML), handle errors, interface with the operating system, create highly efficient regular expressions for parsing, and learn best practice techniques.
Linux Essentials For Developers

    Navigating Linux - As a developer, you must understand the file structure. Your project will work only if you place files in the right place. Expect an epic fail if you do not follow the rules, so let's start with housekeeping. Ignore this chapter at your own peril.
        Using Shell Command cd, tree, and other tools to explore directories
        The POSIX File system
            Why POSIX is critical for a developer to learn and follow
            The POSIX directory structure
            Text files vs. executables
            File naming convention - do and do nots
        The dot files

    Essential Linux tools (Each of these will appear as a chapter in the course documentation)
        vim - Edit files
        tmux essentials - massively reduce keystrokes
        bash shortcuts
        Choosing a Linux cheat sheet - We have several, choose the one that best helps you learn the essentials

    Managing Files in Linux (find, cd, rm, tar, grep, egrep, ln)
        Find, Create, Delete, or Edit Files and directories
        IO redirection (>, >>, 2>, &1)
        Pipes (|)

    Managing User and Group Accounts
        Create User and Group Accounts
        Configure User Profiles
        Administer User and Group Accounts

    Managing Linux Permissions and Ownership (chown and chmod)
        Modify File and Directory Permissions
        Modify Default Permissions
        Modify File and Directory Ownership
        Set Special Permissions and Attributes

    Working with the Bash Shell and Shell Scripts
        Perform Basic Bash Shell Operations
        Write a Bash Shell Script
        Customize the Bash Shell
        Redirect Standard Input and Output
        Use Control Statements in Shell Scripts

Python Basics

    Introduction to Python
        Installing Python 3.x
        Preparing to write Python
        Preparing to write a Python file (*.py)
        Using Python in a Linux environment
        Shebang line
        Text Editors and Python IDEs
        Executing a Python file
        Python Interpreter
        Overview of the Standard Library

    Version Controlling Code with Git
        Overview of Git
        Git commands
        Set up a GitHub account
        GitHub essentials
        README course requirements
        How to set up a repo
        Issue a pull request

    Basics of Programming
        Functions and purpose of main()
        Objects
        Methods
        Built in Functions
        Arguments
        Controlling standard out
        White spacing basic rules
        String Literal Escape Sequences
        Python Variables
        Naming Conventions & Rules
        Types as Objects
        Mutable vs Immutable Objects

    Python Basic Variables and Data Types
        Numeric Types
        Operators and Precedence / Arithmetic Expressions
        Integers
        Floating points

    String Types
        Generating Strings in Python
        Common String Methods
        Formatting String Output
        Booleans
        Printing and formatting strings
        Scripting with input()

    Lists & Dictionaries & Tuples
        Lists
        Mixed Lists
        Common List Methods
        An overview on and construction of dictionaries
        Keys and Values
        Dictionary Methods
        Tuples
        Dictionaries vs Lists vs Tuples
        Translating JSON to Pythonic data

    If, elif, else
        Relational and Comparison Operators (>, >=, ==, !=, in, not in)
        Logical operators (and, or, not)
        if, elif, and else conditions
        Nested if conditions
        if name == “main”
        error handling with try/except

    Looping with “while”
        While usage
        Count controlled loop
        Event controlled loop
        Continue
        Break

    Looping with “for”
        The for Loop
        For iteration examples
        Looping across data sets
        Looping across lists of lists
        Looping across lists of dictionaries

    Understanding Iterators
        The range() function
        Iterable Objects
        Looping with dictionaries
        Looping with lists

    Getting Data In and Out of Python
        Opening Files
        Working with Files
        Read data from files
        Controlling output location
        Introduction to working with APIs
        What is a “REST”ful API?
        APIs and JSON

    Creating Python Functions
        Function Basics
        Defining Custom Functions
        Argument Defaults
        What is if name == “main”
        Local vs. Global Variables
        Variable Masking (overwriting/copying variables)
        Preventing Variable Modifications (Global variables)
        Argument Matching Methods
        Basic List Comprehensions

    Modules & Packages
        Pip and pip3
        Module Basics
        Packages
        Defined modules
        Importing modules
        Some useful modules to know
        RESTful APIs and requests
        Query parameters
        API authentication with developer keys
        Dataframes with pandas
        Graphing with matplotlib

    Python Scope
        Naming conventions
        Local scope
        Global scope
        Nested scope

    Object Oriented Python
        About OOP
        The Class Statements
        Defining a class
        Class Inheritance
        Classes as Objects
        Understanding self
        Class fields and constructors
        Data structures
        Static methods

APIs and API Design with Python

    Web and RESTful APIs
        REST
        REST APIS and HTTP CRUD
        URI analysis and formation
        cURL
        Creating a Python client to interact with API endpoints
        API dev keys
        Tokens and APIs

    JSON, YAML, XML, CSV and Excel
        JSON Formatting
        CSV
        json Python module
        Using python to decode data structures like CSV and JSON
        Reading from Excel
        Writing to Excel
        Pandas and data visualization

    Code Review
        Best practice
        Conventions
        Underscore
        Double underscore

    Web API Design with Flask
        Flask Overview
        Decorators
        Building APIs with Python and Flask
        APIs returning Jinja2 templating
        Returning a ‘cookie’
        Building Sessions
        Redirecting from URIs
        Build an API to accept a file upload

    SQLite
        Overview
        Connecting to Python
        Read / Write operations
        Other useful instructions
        Connecting APIs and SQLite
        Reading and Writing to Databases with APIs

Hands on Labs:

    VScode in Alta3 LIVE
    TMUX Basics
    Setting up GitHub
    POSIX File System
    Using VIM
    Choosing a Linux Cheatsheet
    Finding Files
    Installing Python
    Lecture - Python Basics
    Print
    Shebang
    Collecting user input
    Piping Output
    I/O Redirection
    File Management Tasks
    Lecture - Python Strings
    Python Object Methods
    String Methods
    Lecture - Lists
    Working with Lists
    List Objects and Methods
    Lists of Lists
    Configure User Profiles
    Create User and Group Accounts
    Understand User Properties
    Lecture - Dictionaries
    Python Dictionaries
    Lecture - Conditionals
    Testing with if
    IPv4 Testing with if
    Using while, if, elif, else
    try and except
    Basic File Permissions
    Modify File and Directory Permissions
    Copying Files and Folders
    Moving and Renaming Files and Folders
    if name == "main"
    Starting to Learn Loops
    Looping with for
    for loops and range
    Lecture - Reading and Writing to Files
    Parsing Log Files
    Write to Files
    Read from Files
    Scripting Commands with Python
    Creating Functions
    Defining Functions
    Best Practice and pylint
    pip and import
    Creating objects in Python from "Scratch"
    Class Inheritance
    Using Classes
    List and Dict Modeling
    Excel and Intro to Pandas
    Pandas dataframes with Excel, csv, json, HTML and beyond
    CSV data - Standard Library and pandas dataframes
    Producing Graphs and Charts
    Lecture - Converting JSON to Python Data Types
    RESTful APIs and JSON
    LECTURE - Python data types vs JSON
    Python Data to JSON
    Python Data to YAML
    LECTURE - Introduction to HTTP
    Standard vs. Third Party Libraries and Open APIs
    requests library - Open APIs
    requests library - RESTful GET and JSON parsing
    APIs and Dev Keys
    RESTful APIs and Dev Keys
    requests library - GET vs POST to REST APIs
    LECTURE - Intro to Flask
    Building APIs with Python
    Returning and POSTing JSON
    LECTURE - Introduction to Jinja
    Flask APIs and Jinja
    Flask APIs and Cookies
    Flask Sessions
    LECTURE - Controlling your APIs
    Flask Redirection, Errors, and API Limiting
    Flask Uploading and Downloading Files
    LECTURE - Learning sqlite3
    Tracking API Data with sqlite3
    Tracking Inventory with sqlite3
    Bash Scripting Intro
    Bash Read CLI Vars
    Bash Conditional Statements
    Bash Conditionals
    Bash While Loops


# First of all, take a look at your command prompt to try to understand what it can teach us. It should look like:

student@bchd:~$

    student is the name of the user
    bchd is the hostname of the machine
    ~ (to the right of the colon) shows us the present working directory. Specifically, ~ refers to this user's home directory of /home/student.
    $ shows us that this is a typical user (vs. # would indicate that it is the root user)

Now let's run some fundamental commands to get to know our environment a little bit better. Remember, we are starting in our /home/student directory for this.

    pwd - [present working directory] shows you what directory you are in.

    student@bchd:~$ pwd

/home/student

ls - list out the contents of the current directory.

student@bchd:~$ ls

static

cd - [change directory] - allows you to move to a different directory. Here we can move to the static directory.

student@bchd:~$ cd static

mkdir - [make directory] - allows you to make a new directory. Let's make one called training.

student@bchd:~/static$ mkdir training

Also, let's make sure we can see that we made this training directory.

student@bchd:~/static$ ls

training

And let's move into the training directory.

student@bchd:~/static$ cd training

touch - makes a blank file.

student@bchd:~/static/training$ touch example_01.txt

Verify that the file named example_01.txt is there now.

student@bchd:~/static/training$ ls

example_01.txt

echo - returns text to the standard output.

student@bchd:~/static/training$ echo Alta3 Research Training rocks!

Alta3 Research Training rocks!

The > character allows us to redirect standard output to a different place, normally a file.

student@bchd:~/static/training$ echo Alta3 Research has AWESOME labs! > myfile.txt

The >> characters allow us to redirect standard output and append it to the end of a file.

student@bchd:~/static/training$ echo Alta3 Research has AMAZING labs! >> myfile.txt

cat - [concatenate] prints file(s) to standard output.

student@bchd:~/static/training$ cat myfile.txt

Alta3 Research has AWESOME labs!
Alta3 Research has AMAZING labs!

mv - [move] allows us to move a file or directory (often used to rename files).

student@bchd:~/static/training$ mv myfile.txt ego_fuel.txt

Verify that the file has moved.

student@bchd:~/static/training$ ls

ego_fuel.txt example_01.txt

Make sure that the contents of the file have not changed.

student@bchd:~/static/training$ cat ego_fuel.txt

Alta3 Research has AWESOME labs!
Alta3 Research has AMAZING labs!

history - shows all of the commands performed in this shell session.

student@bchd:~/static/training$ history

    1  # copy me
    2  pwd
    3  ls
    4  cd static
    5  mkdir training
    6  ls
    7  cd training
    8  touch example_01.txt
    9  ls
   10  echo Alta3 Research Training rocks!
   11  echo Alta3 Research has AWESOME labs! > myfile.txt
   12  echo Alta3 Research has AMAZING labs! >> myfile.txt
   13  cat myfile.txt
   14  mv myfile.txt ego_fuel.txt
   15  ls
   16  cat ego_fuel.txt
   17  history

man - [manual] show the manual pages (aka documentation) for a given command. This is helpful for understanding any commands you may not feel comfortable with.

student@bchd:~/static/training$ man ls

    To quit out of this view, press the keyboard key q

Excellent work! Now, let's move back to the home directory before you start working on the next lab.

student@bchd:~/static/training$ cd ~

Your prompt should now be back to: student@bchd:~$

If you have any questions throughout the course, please feel free to reach out to:

    Your Instructor
    Live Help via the Alta3 Research Discord Channel
    Email the Alta3 Research's Support Team support@alta3.com
