# Virtual Environments Lecture

How to create venv -> check lecture lol

Using virtual environments, you are still grabbing from pip eg. using pip install etc and the python website.

However, Conda has its own packages so, conda add grabs it from different location online.

Can also create environment from conda using:
```conda create -n condatest ```

Then need to activate it eg. ```conda activate condatest``` 

Can also specify the Python version in it. But note that it will behave in a similar to virtual environments but will grab installs from from Conda packages. 

Venv is good for fast operations. Conda is nice for more complex stuff but also safer some times.

No real issues with deactivate.


For Github Actions: if you want to run things in Anaconda environment, can use MiniConda
eg. ```conda-incubator/setup-miniconda ```











