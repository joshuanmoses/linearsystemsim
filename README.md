<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">

</head>
<body>

<h1>Linear System Simulation using 4th-Order Runge-Kutta</h1>

<p><strong>Description:</strong></p>
<p>This project simulates the time evolution of a linear system of differential equations of the form:</p>

<pre><code>dx/dt = A * x</code></pre>

<p>where <code>A</code> is a constant coefficient matrix and <code>x</code> is the state vector. The system is solved using the 4th-order Runge-Kutta (RK4) numerical integration method. The results are displayed both numerically and graphically using Matplotlib.</p>

<hr>

<h2>Features</h2>
<ul>
    <li>Simulates systems of any size (adjustable number of variables).</li>
    <li>Uses efficient NumPy-based calculations.</li>
    <li>Plots the trajectories of all variables over time on a single graph or on separate subplots.</li>
    <li>Supports customizable system matrices and initial conditions.</li>
    <li>Flexible output options (print numerical values, choose different plotting styles).</li>
</ul>

<hr>

<h2>Installation</h2>
<p>Make sure you have Python 3 installed along with the following packages:</p>
<pre><code>pip install numpy matplotlib</code></pre>

<hr>

<h2>How to Use</h2>
<ol>
    <li>Clone or download this repository.</li>
    <li>Edit the system matrix <code>A</code> and initial conditions <code>x</code> if you want to simulate a different system.</li>
    <li>Run the script using:</li>
    <pre><code>python simulate_system.py</code></pre>
    <li>View printed results and plots generated after the simulation.</li>
</ol>

<hr>

<h2>Configuration Options</h2>
<p>At the top of the script, you can configure the following:</p>
<ul>
    <li><strong>DISPLAY_NUMERICAL:</strong> Set to <code>True</code> to print numerical results after simulation.</li>
    <li><strong>PLOT_TRAJECTORIES:</strong> Set to <code>True</code> to generate plots of the state variables.</li>
    <li><strong>ONE_PLOT:</strong> If <code>True</code>, plots all trajectories on a single figure. If <code>False</code>, plots each variable in separate subplots.</li>
    <li><strong>FRAME:</strong> If <code>PLOT_TRAJECTORIES = False</code>, defines which two variables to plot against each other (phase plane plot).</li>
</ul>

<hr>

<h2>File Structure</h2>
<ul>
    <li><code>simulate_system.py</code> - Main simulation script.</li>
</ul>

<hr>

<h2>Example Output</h2>
<p>The script generates:</p>
<ul>
    <li>Console output showing the time series for each state variable.</li>
    <li>A Matplotlib figure showing the trajectories of all state variables over time.</li>
</ul>
<p>Example plot:</p>
<img src="https://via.placeholder.com/700x400.png?text=Example+Trajectory+Plot" alt="Example Trajectory Plot">


</body>
</html>
