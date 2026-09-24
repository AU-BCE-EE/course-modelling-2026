# Mini-project I - Ammonia volatilization from slurry storage

## Introduction

On dairy cattle farms animal slurry (mixture of feces, urine, bedding, washing water, and wasted feed) is collected pits below the floor in the barn.
Then after a few days the slurry is pumped to an external outdoor storage tank. 
The slurry contains a high amount of ammonia, which, as you know, includes two chemical species: $\ce{NH3}$ (free ammonia) and $\ce{NH4+}$ (ammonium ion). 
You know from your chemistry classes that these two species exist in an equilibrium that depends on the pH. 
In fact you should have developed a free ammonia calculator for the Chapter 6 work.

A livestock experts explains to you that actually the $\ce{NH3}$ and $\ce{NH4+}$ comes from urea hydrolysis and urea is excreted in animal urine, this process of urea hydrolysis to ammonia is very quick; within a day virtually 100% is converted. 
Slurry is pumped into the tank from the barn, and then later removed from the tank for application in the field to fertilize crops.

The slurry tank is open in the top and ammonia (NH3) is therefore volatilized as a gas (or vapor) from the tank. 
To be sure of the quantity of ammonia applied in the field, it is necessary to know how much is lost through volatilization.
In this project you will develop a model for slurry ammonia that can predict this loss of ammonia and the effect on available ammonia for field application. 

## Task

### 1. Model formulation

The first task is to develop a simplified model for predicting the ammonia concentration in the slurry tank. 
You should follow the model formulation steps from class. 
When necessary, make assumptions, but try to be realistic. 
When you do make assumption be explicit in your report about them. 
Selecting an appropriate level of complexity in a model is often difficult and somewhat arbitrary. 
Our advice is to start relatively simply, and if you find at the end or along the way that the model is not realistic enough, add components as needed.
For this model you should think about how it will be used (see task 2 below) and also the level of complexity we have used in class.

### 2. Model implementation

Once you have formulated the model implement it in Python using the module approach we have covered in class.
Be sure to document your module and all functions using the docstring approach we have used.

Avoid using Copilot or any other AI tools.

### 3. Model application

Use your model to make an estimate of the fraction of total ammonia (commonly described as "total ammoniacal nitrogen" or TAN) from slurry that is lost from the storage tank.
Then, evaluate at least two design or management options for limiting the loss of ammonia to the atmosphere, which in practice is done both for pollution control and to save valuable fertilizer nitrogen.
You can come up with ideas, but you are welcome to use some from the list below. 
Evaluate at least two options by comparing them to a reference scenario.

1.  Floating covers that go on top of the tank.
2.  Dimensioning of the slurry tank
4.  Slowing down hydrolysis of urea to ammonia by adding inhibitors

You are free to ask us for help in finding realistic values for parameters and other inputs.
But you need to be able to describe what it is you need!

## Report

The report should follow a structure with these headings: 

* Problem definition (brief)
* Conceptual model (include sketch of system)
* Mathematical model and description of implementation in Python
* Application (including presentation of results)
* Python code (in appendix)

While we recommend following the model formulation steps described in the book, you do not need to include a description these steps in your report.

Report length: The report should be no more than 5 pages (fewer is fine as long) excluding the Python code in the appendix.

Groups: Work on the project and report in groups of 3-5 people

Deadline: Submit the report through Brightspace before 23:59 on the 8th of September. 

