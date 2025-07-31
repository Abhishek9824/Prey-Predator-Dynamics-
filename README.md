# Prey-predator-dynamics-simulation
My attempt to understand the prey-predator ecosystem of three-species interaction. This project is based on system of Ordinary differential equation (ODEs). The mathematical prediction is done by Lotka-Volterra's equations. The prey-predator model describes the relationship between two groups of animals in nature
one prey and another predator. Once predators become plentiful, they eat more prey, causing
the prey population to drop. With less food available, some predators can’t survive or have
fewer babies, so their numbers shrink. This allows the prey to increase again, and the
cycle continues in a repeating pattern. This model shows how the populations of prey and
predators are closely linked and constantly affect each other, highlighting the balance and
connectedness of nature.

## preypredatormodel.py
The mathematical prediction of the  model is a system of 2 coupled ordinary differential equation each representing one species in the ecosystem, one prey and other predator. These equations are based on Lotka-Volterra dynamics.
The simulated dynamics of wolves and deer is an classic oscillating cycle where deer increase first as a function of vegetation availability then experience a time lagged increase in wolves as a consequence of ample amount of prey. Predation brings number of deer down which also cause a deline in wolves population.

### Notes
* The Lotka-Volterra model is a mathematical framework used to describe how the populations of two interacting species changes over time. These are a set of first-order, nonlinear differential equations that model
the cyclical dynamics often observed in natural predator-prey systems.

$$
\frac{dx}{dt}=\alpha x-\beta xy
$$

* The above equation is an system model for prey where $\alpha x$ prey reproduces naturally at rate and $-\beta xy$ represent prey are eaten by predators at rate proportional to both populations.

* The predator equation consist of two constant which represent predator gains from consuming prey ($\delta$) and  predator dies naturally in absence of food ($\gamma$) respectively.

$$
\frac{dy}{dt}=\delta xy-\gamma y 
$$

## threesytempopulation.py
Predator-Prey model interaction is simulated between two species but do not represent the real ecosystem, ecosystem is complex and consists of multiple factors, trophic food levels or chains. So, the overall simulation is same but I have introduced an 3rd species: Grass Population (G). The graphical analysis of simulation shows plant population increases rapidly due to low herbivore pressure which is followed by multiple oscillations in the herbivore (deer) and predator (wolf) populations which predator peaks lagging slightly behind prey peaks at consistent with the classical predator-prey dyamics. However, the oscillations are damped over time and the system reaches a stable equilibrium. 

### Notes
* Refer to report.pdf/

## Conclusion
The population dynamics of three species interaction reflects a realistic ecological scenario
in which a dominant predator indirectly facilitates plant persistence by controlling
herbivore abundance. The phase plot of prey versus predators displays a closed-loop trajectory, indicating stable,cyclic population dynamics. As the prey population rises, predator numbers follow with a time delay, eventually causing a decline in prey due to predation.

P.S.-I might update or expand this project in the future. If you're interested in ecology, mathematical modeling, or theoretical ecology, feel free to drop your email.
