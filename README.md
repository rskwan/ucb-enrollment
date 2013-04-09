ucb-enrollment
==============

Tool for scraping enrollment information from the UCB Online Schedule of Classes.

## Requirements

* Python 2.7.x
* pip
* virtualenv

The contents of `requirements.txt`:

    argparse==1.2.1
    beautifulsoup4==4.1.3
    requests==1.2.0
    wsgiref==0.1.2

## Usage

Running `python getInfo.py` will get the information for the fall 2013 courses
in the math department, and will print the results like so:

    MATHEMATICS 1A P 001 LEC (CCN 53403): Limit 408, Enrolled 0, Waitlist 0 (04/07/13)
    MATHEMATICS 1A S 101 DIS (CCN 53406): Limit 27, Enrolled 0, Waitlist 0 (04/07/13)
    MATHEMATICS 1A S 102 DIS (CCN 53409): Limit 27, Enrolled 0, Waitlist 0 (04/07/13)
    MATHEMATICS 1A S 103 DIS (CCN 53412): Limit 27, Enrolled 0, Waitlist 0 (04/07/13)
    MATHEMATICS 1A S 104 DIS (CCN 53415): Limit 27, Enrolled 0, Waitlist 0 (04/07/13)
    MATHEMATICS 1A S 105 DIS (CCN 53418): Limit 25, Enrolled 0, Waitlist 0 (04/07/13)