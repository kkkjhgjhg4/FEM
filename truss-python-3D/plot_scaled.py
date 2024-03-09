#! usr/bin/env python3
import FEData as model
import numpy as np
import matplotlib.pyplot as plt

def plottruss_displacement(scale_factor):
    '''
    plot the scaled truss with displacement
    '''
    plt.clf()
    # add displacement to coordinates
    x = model.x
    y = model.y
    scaled_d = model.d * scale_factor


    for i in range(2, 12):
        x[i] = model.x[i] + scaled_d[2*i]
        y[i] = model.y[i] + scaled_d[2*i + 1]

    if model.ndof == 1:
        for i in range(model.nel):
            XX = np.array([x[model.IEN[i, 0]-1], 
                           x[model.IEN[i, 1]-1]])
            YY = np.array([0.0, 0.0])
            plt.plot(XX, YY, "blue")

            if model.plot_node == "yes":
                plt.text(XX[0], YY[0], str(model.IEN[i, 0]))
                plt.text(XX[1], YY[1], str(model.IEN[i, 1]))
    elif model.ndof == 2:
        for i in range(model.nel):
            XX = np.array([x[model.IEN[i, 0]-1], 
                           x[model.IEN[i, 1]-1]])
            YY = np.array([y[model.IEN[i, 0]-1], 
                           y[model.IEN[i, 1]-1]])
            plt.plot(XX, YY, "blue")

            if model.plot_node == "yes":
                plt.text(XX[0], YY[0], str(model.IEN[i, 0]))
                plt.text(XX[1], YY[1], str(model.IEN[i, 1]))
    elif model.ndof == 3:
        for i in range(model.nel):
            XX = np.array([model.x[model.IEN[i, 0]-1], 
                           model.x[model.IEN[i, 1]-1]])
            YY = np.array([model.y[model.IEN[i, 0]-1], 
                           model.y[model.IEN[i, 1]-1]])
            ZZ = np.array([model.z[model.IEN[i, 0]-1], 
                           model.z[model.IEN[i, 1]-1]])
            plt.plot(XX, YY, ZZ, "blue")

            if model.plot_node == "yes":
                plt.text(XX[0], YY[0], ZZ[0], str(model.IEN[i, 0]))
                plt.text(XX[1], YY[1], ZZ[0], str(model.IEN[i, 1]))
    else:
        raise ValueError("The dimension (ndof = {0}) given for the \
                         plottruss is invalid".format(model.ndof))
        
    plt.title("Truss Plot")
    plt.xlabel(r"$x$")
    plt.ylabel(r"$y$")
    plt.axis("equal")
    plt.savefig("truss_displacement_scaled.pdf")

    # Convert matplotlib figures into PGFPlots figures stored in a Tikz file, 
    # which can be added into your LaTex source code by "\input{fe_plot.tex}"
    if model.plot_tex == "yes":
        import tikzplotlib
        tikzplotlib.clean_figure()
        tikzplotlib.save("truss_displacement_scaled.tex")
    