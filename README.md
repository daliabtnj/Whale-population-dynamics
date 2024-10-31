# Whale Population Dynamics Simulation

Using Euler's method, this project simulates the population dynamics of blue and fin whales on Python and Mathematica software, exploring the impact of interspecies competition, growth rates, and environmental carrying capacities. The aim is to determine if both species of whales can recover from current population levels or if one or both will become extinct.

## Background

The blue whale and fin whale are two similar species that inhabit the same areas and are thought to compete. Key parameters include:

- **Intrinsic Growth Rates**: 5% per year for blue whales, 8% per year for fin whales.
- **Environmental Carrying Capacities**: 150,000 blue whales and 400,000 fin whales.
- **Current Populations**: Reduced to approximately 3,000 blue whales and 15,000 fin whales due to intense harvesting over the last 100 years.

## Model

The whale populations are modeled as a dynamical system using the following differential equations:

dBdt[B_, F_] := 0.05*B*((B - 3000)/(B + 3000))*(1 - B/150000) - 10^-8*B*F

dFdt[B_, F_] := 0.08*F*((F - 15000)/(F + 15000))*(1 - F/400000) - 10^-8*B*F

where:
- \(B\) = number of blue whales
- \(F\) = number of fin whales

## Methodology

### Euler's Method

Euler's method is used for the numerical solution of the differential equations. The behavior of the model is simulated starting with initial conditions \(B(0) = 5,000\) and \(F(0) = 70,000\).

### Sensitivity Analysis

A sensitivity analysis on the total simulation time (\(T\)) and the number of steps (\(N\)) ensures the validity of the results. The analysis indicates that both species grow back, leveling off at \(T > 200\). It is estimated to take around 200 years for the species to reach a coexistence state.

### Initial Condition Variations

The model is tested with different initial conditions to observe long-term outcomes:
- \( (B(0), F(0)) = (4000, 16000) \)
- \( (B(0), F(0)) = (3000, 16000) \)
- \( (B(0), F(0)) = (4000, 15000) \)
- \( (B(0), F(0)) = (3000, 15000) \)

Results:
- **(4000, 16000)**: Both species grow back.
- **(3000, 16000)**: Blue whales go extinct, fin whales approach carrying capacity.
- **(4000, 15000)**: Fin whales go extinct, blue whales approach carrying capacity.
- **(3000, 15000)**: Both species go extinct.

## Visualization

Graphs illustrating the population dynamics under various initial conditions are included in the repository. These visualizations provide insights into the long-term trends and interactions between the two whale species.

## Conclusion

This project highlights the complex interactions and potential outcomes for blue and fin whale populations. The model offers valuable insights into the sustainability of these species and can be further refined or extended to include additional factors or species.

## Usage

To run the simulations, use the provided Python code and adjust the parameters as needed, or use the Mathematica code pdf. The results can be visualized using the included plotting functions.

