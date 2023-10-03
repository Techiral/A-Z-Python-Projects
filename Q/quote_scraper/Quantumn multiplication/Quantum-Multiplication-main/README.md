# Quantum-Multiplication
This repository is created as a task for QOSF event. I have implemented multiplication using Quantum Fourier Transformation.

<h1> Lets see how classical computers multiply</h1>
<p> In a classical computer thre are two numbers, multiplier and multplicand. We take the multiplier and multiply the multiplicand with each of the digits of the multiplier individually and then add these partial multiplications to arrive at the final product.

<h1> Make it faster using Fourier Transformation</h1>
<p> We can use Quantum Fourier Transformation to compute the sum using less number of qubits and more efficiently. This process consistes of three stages. These are converting the number to fourier trasform, applying operations on it, ad then converting it back to its original form.</p>
<h1> Multiplication as repeated addition</h1>
<p> We can perform multiplication in such a way that the multiplier is reduced each time and the multiplicand is added to itself every cycle. Thus we will perform the cycle number of times equal to multiplier. We can add an accumulator which holds the value of the new muplicand after the end of every cyce.</p>
<h1>Creating the Quantum Multiplier</h1>
<p> The three processes for QFT based addition are as follows:createInputState, evolveQFTState, inverseQFT.</p><p>
Thus the final steps for creating the quantum multiplier are:
<ul>
<li>Obtain the multiplicand and multiplier from the user.</li>
<li>The accumulator will be a quantum register you create.
Quantum Fourier transform-based addition is used to add the multiplicand to the accumulator.
</li>
<li>
Using quantum Fourier transform-based subtraction, decrease the multiplier.
</li><li>
Till the multiplier reaches zero, keep doing this.
</li><li>
Print the value of the accumulator, which now contains the sum of the two supplied values.
</li>
