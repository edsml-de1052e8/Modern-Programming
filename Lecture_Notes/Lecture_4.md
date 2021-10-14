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

--

***Test Driven Development (TDD)***

- TDD: 
1. Write a failing test
2. Write ...?


- Tests are often much harder to write than code
- Deal with them first: spend energy on the hard part


