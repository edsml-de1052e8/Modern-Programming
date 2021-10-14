# Lecture 4: Automated Testing
***Thursday 14th October 2021***

Story time: bad stories due to lack of testing 
Ex: NASA Mars Mission 1998 wrong units used and resulting in crashing and missed landing

- Ad hoc testing: the one you do on the reg where you print your variables throughout 
- Testing to fail: operations you expect to raise an exception error actually do so. You can almost always go from Test to Fail to Test to Pass.
- ```Assert``` function: aims to have an error and can print a string with it such as why one segment of code is misbehaving.

NB: ```try:
    assert(False, "oops" ``` actually creates a tuple so not exactly what we are looking for (?)
    
Exercise One

***Assessment Info***
- See MPM General channel for updates
- life2colour is non-periodic
- lifepent cells stay alive with 2 or 3 neighbours
- removed spurious reference to rule thirty
- bottom left corner, if you feed an array to the pent func then it will print the output to visualise it
- Even with smaller array there will be a cross pattern 


----

***Test Driven Development (TDD)***

- TDD: 
1. Write a failing test
2. Write ...?


- Tests are often much harder to write than code
- Deal with them first: spend energy on the hard part


- Good tests for numerical methods: they are fast, complete, reliable and maintainable (doscstrings, comments etc

**Packages for tests**

- Doctests: ```doctest``` library is part of standard library. It allows you to write simple tests which are also self documenting examples 
```doctest.testfile``` (

Can run test by running module as script ``` python -m docstring_test``` in command line 

Perks of doctest:
- simple
- clear
- tests example
- easy to maintain (can just rerun the example) 

Bad points:
- fragile
- still adds maintenance cost 
- only does string comparisons
- can't test what you can't write 
- Even if you change one character then test goes crazy 

```Unitesttest``` module:
- another inbuilt module, framework for generic testing allowing you to do 3 stages : Set Up, Run and Tear Down (clean up)
example: ```unittest_example.py```
- Good and easy to set up but syntax is quite complicated 

```Pytest``` package:
- similar to unittest but basic mode is easier to set up 
- install the package (not built in): ```pip install pytest``` in terminal
- Can write in everyday format using things like asserts or '=='
- tests should be ready to error on failure
- tool automatically searches for files & directories with test in the name

Code coverage
- 100% code coverage is useful but only means every line in isolation not that every possible code logic branch has been tested 
- Often becomes a tool of managers (like lines of code)

Taxonomy of tests:
1. unit tests: small, fast single unit
2. integreation tests which combine units together
3. Feature/functionality testing
4. Regression testing
5. Other stuff: GUIs, business logic

When doing unit tests, good to use fake inputs: Mocking up inputs
Tests need input

**Automatic documentation**
Documentation is written for 3 board groups of people
1. users: don't really care how it works, care what it does
2. user-developers: build what they need
3. Developers: Make the software but don't use it

For all of these groups, the best documentation is in docstring

**Sphinx**
- Sphinx convert docstring into manuals or web pages using reStructured Text mark up
- to install it: need to import sys and os --> lecture 4 info 

- Format:

#########

Title

#########


---- heading ----


Can do that in VSCode Terminal and build an entire html documentation just with ```sphinx-build -b html docs docs/html```
then you will get an html folder at the same +1 level -> click on folder and open html doc to visualise in Chrome. 


