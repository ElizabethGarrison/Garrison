# A random walk Monte Carlo simulation study of proximity-based infection spread

**Objective:** Random walk and Monte Carlo simulation are very useful modeling and simulation tools with many applications in natural and social sciences, as well as in public health. This project is to give students an opportunity of hands-on practice through investigating a simplified version of a proximity based infection spread model and simulation using random walk and Monte Carlo simulations.

**Problem statement:** Since its outbreak in early 2020, the global spread of the novel corona virus disease (COVID-19) has become a worldwide pandemic that impacted our life in a scale that we have never experienced. Scientists and public health experts have been studying infection spread and mortality rates during the pandemic using models and simulations. Here is a brief description about the problem:

- Data from the very initial phase of the COVID-19 outbreak showed good agreement with models that assumed an exponential growth of infections in time (t), with a mean α (alpha)ranging from 2.24 to 3.58.
- After the initial stage, the temporal growth in the cumulative number of infections (N) was instead subexponential with a power-law scaling N<tα^2 (with α = 2.1 ± 0.3) due to certain containment and mitigation strategies that were put in place, where t is ‘time step’ and α is the power-law scale.
- The cumulative number of infections (N) is also impacted by factors such as population density, mobility (how far a person moves in a time step) and transmittable distance called “touching” separation.
- Public health officials need to study and predict the outcomes of cumulative number of infections (N) under different input factors to assess and recommend effective mitigation practices and strategies.

**Model and Simulation:** We use 2D random walks and Monte Carlo simulation to conduct our study. The simulation model description is given below:
- Assume the individuals of an entirely susceptible population are described as identical and independent random walkers, represented by uniformly distributed random points in an isolated twodimensional region on a lattice.
- Assume the simulations begin with an initial condition of one infected walker at the center and all other points are ‘normal’ (uninfected).
- As the simulation progresses, all individual walkers take simultaneous steps in random directions. For cases when walkers step outside the bounded area, a boundary condition was imposed so that the transgressing coordinates were reflected back into the bounded region.
- The ‘spread’ of the disease is said to occur whenever an infected point comes within a ‘touching’ distance from a ‘normal’ susceptible point, thereby passing on the disease. In such a manner, the growth in the number of infected points with respect to the number of discrete time-steps (t) determines the temporal evolution of the infection spread.
- To simplify the model we only consider two virus infection models.
1. The SI (susceptible–infected) model, in which all ‘normal’ points are 100% susceptible.
2. While the SIRS (susceptible–infected-recovered-reinfected) model assumed small recovered
fractions of the population, some of whom are susceptible to reinfection.

To put the above in perspective, for N randomly distributed points over area A, the mean distance of separation ሺrሻ between any two random walkers is about √𝐴/𝑁. Therefore, for a metropolis such as New York City, which has a population density of 10,000/km^2, (r) is about 10 meters. We assume a ‘touching’ separation of 2 meters (about 6 feet), which is the nominal safe distance recommended in most countries. If the distance between any infected data point and a normal (susceptible) point is less than or equal to this value, the normal point is flagged as infected in the simulations. To illustrate the above, we
show an example of such spatial-temporal disease progression in Figure 1. 

Figure1. An example of proximity-based infection spread obtained using the random walk Monte Carlo simulations described in this simulation model. Each of the panels shown above has a population of 2.5k
(N=2500) over a unit area (A=1km^2). The average distance (r) between any two points is r = √A/N meters. In this case every point walker takes randomly directed steps of length l = 0.25(r) meters.

**Project Requirements:**
Students need to conduct two simulation study cases. 
- Simulation case1 is to investigate how the spread of infection is influenced by different mobility confinements, random walk step length l, for a given population density of 10k walker over a unit area (1km^2). 
1. To start, we assume that each walker's spatial mobility is effectively constrained in the area A due to containment (lockdown) measures. It is intuitively reasonable to assume that such a restriction can be achieved by imposing a condition that all members of the population only take random steps of length l = r/4, where (r = 10 meters). This ensures each random walker to be confined (on average) within a local neighborhood. 
2. Board condition: if a walker on the board tries to cross, it will bounce back to the opposite direction. 
3. Then we run the simulation with different step length l = (r)/2, l = (r)/4, and l = (r)/5.
4. For each simulation run, we sey up a condition to end the simulation at the time steps when 95% of the population infected using the SI infection model. The simulation should produce results of the cumulative number of infections (N) over each time step. 
- Simulation case2 is to compare how the SIRS infection model will impact the cumulative number of infections (N) under the same parameter settings as in case1. We study effects of a small recovery and reinfection rate within a fraction of the population and their effects on the cumulative number of infections (N). We independently investigate scenarios with recovery rates of 0.02%, 0.1%, and 0.5%, with two assumptions: (i) all recovered individuals are immune and (ii) a randomly selected 5% of the recovered population is susceptible to reinfection. 