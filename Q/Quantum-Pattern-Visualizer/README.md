### **Quantum Number Pattern Visualizer**

#### **Project Overview:**

The **Quantum Number Pattern Visualizer** is a Python-based tool designed to visualize the probability distributions of atomic orbitals, based on quantum numbers in quantum mechanics. Using mathematical models like spherical harmonics and radial wavefunctions, the visualizer generates 3D plots of wavefunction probability densities, representing where an electron is most likely to be found around an atom.

This tool provides insights into the abstract concepts of quantum mechanics, making it easier to understand the shapes and distributions of atomic orbitals for different quantum numbers.

---

### **Features:**

- Visualizes 3D probability distributions of atomic orbitals based on the quantum numbers \( n \), \( l \), and \( m \).
- Uses color mapping to represent the probability distribution, with higher probabilities indicated by darker colors.
- The user can input quantum numbers to generate and observe different orbitals, including \( s \), \( p \), \( d \), and higher orbitals.
- Interactive 3D scatter plot, which allows users to rotate and explore the distribution.
- A color bar that indicates the intensity of the wavefunction.

---

### **How it Works:**

#### **Quantum Numbers:**

1. **Principal Quantum Number (n)**: Governs the size of the orbital. Larger values of \( n \) correspond to orbitals that are farther from the nucleus.

   - Example values: 1, 2, 3, ...

2. **Angular Momentum Quantum Number (l)**: Defines the shape of the orbital. For a given \( n \), \( l \) can take values from 0 to \( n-1 \).

   - Example values: 0 (s), 1 (p), 2 (d), ...

3. **Magnetic Quantum Number (m)**: Determines the orientation of the orbital. For a given \( l \), \( m \) can take values from \( -l \) to \( +l \).
   - Example values: \( -l \), \( 0 \), \( +l \)

#### **Mathematical Foundation:**

- The **radial wavefunction** describes the probability distribution as a function of the distance from the nucleus.
- The **angular wavefunction** is based on spherical harmonics and describes the distribution as a function of angles \( \theta \) and \( \phi \).
- The product of the radial and angular wavefunctions gives the total wavefunction \( \psi \), and the absolute square \( |\psi|^2 \) represents the probability density for finding an electron in a given region.

---

### **Installation Instructions:**

#### **1. Prerequisites:**

- Python 3.x installed on your system.
- The following Python packages are required:
  - **NumPy**: For numerical calculations.
  - **SciPy**: For special functions like spherical harmonics and Laguerre polynomials.
  - **Matplotlib**: For 3D plotting and visualization.

#### **2. Install Required Packages:**

Run the following command in your terminal to install the required packages:

```bash
pip install numpy scipy matplotlib
```

#### **3. Clone the Repository:**

### **How to Run:**

1. **Run the Python script:**

   ```bash
   python visualizer.py
   ```

2. **Input Quantum Numbers:**

   When prompted, input values for the principal quantum number \( n \), angular momentum quantum number \( l \), and magnetic quantum number \( m \).

   - Example:
     - Enter principal quantum number \( n \): `2`
     - Enter angular momentum quantum number \( l \): `1`
     - Enter magnetic quantum number \( m \): `0`

3. **Observe the Visualization:**

   - A 3D plot will be generated showing the probability distribution of the orbital corresponding to the input quantum numbers. You can rotate and zoom in on the plot to explore the shape of the orbital.

---

### **Project Structure:**

```
Quantum-Number-Pattern-Visualizer/
│
├── visualizer.py           # Main script for running the visualizer
├── README.md               # Project documentation
├── requirements.txt        # Required Python packages

```

---

### **Key Functions in `visualizer.py`:**

- **`radial_wavefunction(n, l, r)`**:

  - Computes the radial part of the wavefunction using associated Laguerre polynomials.

- **`angular_wavefunction(l, m, theta, phi)`**:

  - Computes the angular part of the wavefunction using spherical harmonics.

- **`wavefunction(n, l, m, r, theta, phi)`**:

  - Combines the radial and angular components to compute the total wavefunction.

- **`generate_grid(size_r, size_theta, size_phi)`**:

  - Generates a 3D grid in spherical coordinates for plotting.

- **`spherical_to_cartesian(r, theta, phi)`**:

  - Converts spherical coordinates to Cartesian coordinates for 3D visualization.

- **`plot_wavefunction(n, l, m)`**:
  - Plots the 3D scatter plot showing the probability distribution of the wavefunction based on the quantum numbers.

---

### **Sample Usage:**

Here’s how the output will vary for different quantum numbers:

#### **For \( n = 2, l = 1, m = 0 \):**

- You will see a probability distribution corresponding to a \( p \)-orbital, which has a characteristic dumbbell shape.

#### **For \( n = 3, l = 2, m = 1 \):**

- The visualization will represent a more complex \( d \)-orbital with distinct regions of probability density.

---

### **Customization:**

- **Grid Size**: You can change the grid resolution by adjusting the `size_r`, `size_theta`, and `size_phi` parameters in the `generate_grid()` function for finer or coarser visualizations.
- **Transparency and Color Mapping**: The transparency (`alpha`) and color scheme (`cmap`) used in the scatter plot can be customized for different visual effects.

---

### **Known Issues:**

- **Performance**: The 3D scatter plot can become computationally expensive for larger grids. Reducing the grid size (using `generate_grid(size_r=30, size_theta=30, size_phi=30)`) can improve performance without significantly affecting the visualization quality.

### **Contact:**

For any questions or feedback, feel free to reach at:

- **Email**: aswinpkumar03@gmail.com
- **GitHub**: [AswinPKumar01](https://github.com/AswinPKumar01)
