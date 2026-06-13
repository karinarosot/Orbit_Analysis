import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('planets.csv')

data["T_square"] = data["Orbital_Period_Years"]**2
data["r_cube"] = data["Distance_AU"]**3
data["Ratio"] = data["T_square"] / data["r_cube"]

#DataFrame
df = pd.DataFrame(data)

print(df.sort_values(by='Ratio', ascending=True))
print(data[['Planet', 'Ratio']])

#Visualisation
fig, ax = plt.subplots(figsize=(8,6))
ax.set_facecolor('#FFCAD4')
ax.scatter(data['r_cube'], data['T_square'], color='#DA344D')
fig.patch.set_facecolor('#FFCAD4')


for i, txt in enumerate(data['Planet']):
    plt.annotate(txt, (data['r_cube'][i], data['T_square'][i]))

#3.Description
plt.title("III Keplers Law: T^2 as a function of r^3")
plt.xlabel("Distance to cube (r^3) [AU^3]")
plt.ylabel("Orbital period to square (T^2) [lat^2")
plt.grid(True)

plt.yscale('log')
plt.xscale('log')
plt.show()
