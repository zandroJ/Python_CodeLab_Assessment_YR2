import matplotlib.pyplot as plt

# Data to be plotted
data = {
    "Game": [279, 200],
    "Commercials": [81, 156],
    "Won't watch": [132, 160],
}

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Create a bar chart with the data
x = list(data.keys())
y1 = [d[0] for d in data.values()]
y2 = [d[1] for d in data.values()]
ax.bar(x, y1, color="b")
ax.bar(x, y2, color="g", bottom=y1)

# Add labels and a title
ax.set_ylabel("Number of respondents")
ax.set_title("Plans to watch Super Bowl")
ax.legend(["Male", "Female"])

# Show the plot
plt.show()
