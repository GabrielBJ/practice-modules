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

Now, you are ready to use the `kepler.py` module as a script: 
```
python kepler.py -e  -T  -m  -s  -sg
```
here,
```
-e -> this flag takes as input the eccentricity of the orbit.
-T -> this flag takes as input the period in years.
-m -> this flag takes as input the method to perform the integration (RK2, RK3, RK4)
-s -> this flag takes as input the directory to save the initial map
-sg -> this flag takes as input the directory to save the gif animation of the orbit
```
### Example:
```
python kepler.py -e 0.25 -T 1 -m RK4 -s "./intial_map.png" -sg "./animation.gif"
```
This example will generate the simulation for the Pluto eccentricity using the RK4 method. Then, it will save the initial map in the `"./intial_map.png"` directory,  and the animation in the `"./animation.gif"` directory.

It will also generate a file called `RK4_integrated_orbit.txt`
