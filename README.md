Kepler's Third Law Verification

Project Description
This project demonstrates the verification of Kepler's Third Law of Planetary Motion (T^2∝r^3) using observational data from the Solar System. By calculating the ratio of the square of the orbital period to the cube of the semi-major axis, we can confirm the constant nature of this ratio for planets orbiting the same central body.

Technologies Used
Python 3.x
Pandas: For astronomical data processing and vectorised calculations.
Matplotlib: For visualization of the physical correlation.

Key Features
Physical Modeling: Implementation of the formula Stosunek=T^2/r^3.

Data Transformation: Creation of custom columns for T^2 and r^3
to linearize the relationship.

Visualization: Log-log scatter plot to verify the linear dependence, providing a clear visual proof of Kepler's law.

How to Run
Ensure you have planets.csv in the same directory (or create the DataFrame directly in the script).
Install dependencies:
pip install pandas matplotlib
Run the script:
python main.py

Results
The script generates a plot where the correlation between the square of the orbital period and the cube of the distance is clearly visible as a linear trend. This confirms the theoretical prediction of Kepler's Third Law.
