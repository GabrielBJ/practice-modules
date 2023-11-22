# odekepler.kepler module
This module generates a simulation of the two-body problem by solving the ODE system of equations of motions of the Earth:

$$\frac{d\vec{r}}{dt}=\vec{v}$$

$$m\frac{d\vec{v}}{dt}=-\frac{G\,m\,M}{r^3}\vec{r}$$

using the initial conditions:

$$x_0 = 0$$

$$y_0 = a\,(1-e)$$

$$v_{x0} = -\sqrt{\frac{G\,M}{a}\frac{1+e}{1-e}}$$

$$v_{y0} = 0$$

## General structure of the module 

```
midtermpart2.tar

    odekepler
    ├── odekepler
        ├── kepler.py
        ├── __init__.py
    ├── analysis.ipynb
    ├── outputfolder
    ├── helpfolder
    └── README.md
   
```

## Using the module as a script 

Download the `midtermpart2.tar` file. Uncompress it and copy the `odekepler` folder to your working directory.

Open in Terminal an run:
```
cd ~/path_to_module/odekepler/odekepler/
```
this will place you in the directory where the `kepler.py` file is placed.
