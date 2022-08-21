import numpy
import matplotlib.pyplot as plt

def bayes_formula(E: float, S: float, x: numpy.ndarray, type: str):
    if type == 'VPP':
        y = numpy.array([(D * S) / ((D * S) + ((1 - D) * (1 - E))) for D in x])
    else:
        y = numpy.array([((1 - D) * E) / (((1 - D) * E) + (D * (1 - S))) for D in x])
    return y


if __name__ == '__main__':
    x = numpy.arange(0,1.001,0.01)
    especificidade = [0.8, 0.9, 0.99]
    sensibilidade = [0.8, 0.9, 0.99]
    figure, graphs = plt.subplots(4,3)
    i = -1
    for E in especificidade:
        i+=1
        for S in sensibilidade:
            y_VPP = bayes_formula(E, S, x, type='VPP')
            y_VPN = bayes_formula(E, S, x, type='VPN')
            graphs[0, i].plot(x,y_VPP, label=f"S={S}")
            graphs[1, i].plot(x,y_VPN, label=f"S={S}")
        graphs[0, i].set_title(f"T+ | E = {E} e S = {sensibilidade}")
        graphs[0, i].legend(loc='best')
        graphs[1, i].set_title(f"T- | E = {E} e S = {sensibilidade}")
        graphs[1, i].legend(loc='best')
    i = -1
    for S in sensibilidade:
        i+=1
        for E in especificidade:
            y_VPP = bayes_formula(E, S, x, type='VPP')
            y_VPN = bayes_formula(E, S, x, type='VPN')
            graphs[2, i].plot(x,y_VPP, label=f"E={E}")
            graphs[3, i].plot(x,y_VPN, label=f"E={E}")
        graphs[2, i].set_title(f"T+ | S = {S} e E = {especificidade}")
        graphs[2, i].legend(loc='best')
        graphs[3, i].set_title(f"T- | S = {S} e E = {especificidade}")
        graphs[3, i].legend(loc='best')
    plt.show()

