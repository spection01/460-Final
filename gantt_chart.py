import matplotlib.pyplot as plt

def plot_gantt(schedule, title, D):
    fig, ax = plt.subplots(figsize=(10, 2))
    for i, (email_id, start_day) in enumerate(schedule):
        ax.broken_barh([(start_day, 1)], (i - 0.4, 0.8), facecolors='tab:blue')
        ax.text(start_day + 0.5, i, f"E{email_id}", va='center', ha='left')
    ax.set_ylim(-1, len(schedule))
    ax.set_xlim(0, D)
    ax.set_xlabel("Day")
    ax.set_yticks([])
    ax.set_title(title)
    plt.tight_layout()
    plt.show()
