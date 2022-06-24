import matplotlib.pyplot as plt

def plot_variable(x, y, z='', **kwargs):
    l = []
    for d in [x, y]:
        l.append(d.data)
    plt.plot(l[0], l[1], z, **kwargs)