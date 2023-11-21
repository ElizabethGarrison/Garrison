# Lab 5 - Monte Carlo Method with Random Walk Model for Advection Diffusion Processes

**Results for Diffusion Process:**
Mean distance after 200 steps: 17.79 units
Longest distance after 200 steps: 60.68 units
Shortest distance after 200 steps: 0.07 units
Confidence interval for mean distance after 200 steps (95%): +/- 0.18 units

**Results for Advection-Diffusion Process:**
Mean distance after 200 steps with velocity: 31.92 units
Longest distance after 200 steps with velocity: 83.51 units
Shortest distance after 200 steps with velocity: 0.40 units
Confidence interval for mean distance after 200 steps with velocity (95%): +/- 0.25 units

**Analysis and Insights:**
The diffusion process demonstrated a relatively contained particle dispersion, as evidenced by a mean distance of 17.79 units after 200 steps. The diffusion-only scenario demonstrated predictability in particle movement, with a narrow spread between the longest (60.68 units) and shortest (0.07 units) distances. The confidence interval for the mean distance was +/- 0.18 units, emphasizing the accuracy of estimating the average displacement.

The advection-diffusion process, on the other hand, produced an expanded mean distance of 31.92 units with a velocity field of (0.1, 0.1). After 200 steps, the inclusion of velocity resulted in a wider distribution, as evidenced by the increased longest distance of 83.51 units and the shortest distance of 0.40 units. The confidence interval for the mean distance, on the other hand, widened slightly to +/- 0.25 units, indicating a marginally higher variability in estimating the average displacement due to the advection effect.

**Conclusion:**
The simulations revealed distinct behavior differences between diffusion-only and advection-diffusion processes. While the diffusion process resulted in a more confined particle spread, the addition of advection via the velocity field significantly increased the particles' range. These findings highlight the importance of external forces like advection in influencing particle dispersion in advection-diffusion scenarios.

![Alt text](<Lab5 - 200 Steps Velocity.png>) ![Alt text](<Lab5 - 200 Steps.png>) ![Alt text](<Lab5 - 50 Steps Velocity.png>) ![Alt text](<Lab5 - 50 Steps.png>) ![Alt text](<Lab5 - 100 Steps Velocity.png>) ![Alt text](<Lab5 - 100 Steps.png>) ![Alt text](<Lab5 - 150 Steps Velocity.png>) ![Alt text](<Lab5 - 150 Steps.png>)