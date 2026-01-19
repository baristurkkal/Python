import seaborn as sns
import matplotlib.pyplot as plt

# Apply the default theme
sns.set_theme()

# Load dataset
tips = sns.load_dataset("tips")

# Create the visualization
g = sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size",
)

# Save the figure
g.savefig("relplot_tips.png")  # <-- saves the plot as PNG
