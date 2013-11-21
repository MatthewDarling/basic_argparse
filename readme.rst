Provides some common setup actions for argparse. Import and be happy.

Specifically: init_parser() sets up help, version, and docstring options for
a program. Help and version are easy to get with argparse normally; printing
your docstring is the interesting part. It returns a parser with these basic
options configured. After that, you'll want to your application-specific
customizations.

print_and_exit() is an argparse action for printing an arbitrary string -
specifically, in this case, a program's docstring.

Usage
-----

    >>> import basic_argparse
    >>> parser = basic_argparse.init_parser("my awesome program", __version__,
    >>>                                     __date__, __doc__)
    >>> #note that __date__ is meant to be the date of the last update