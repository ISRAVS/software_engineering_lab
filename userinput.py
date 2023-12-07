import matplotlib.pyplot as plt
import numpy as np

def quadratic_model(time):
    a = 0.1
    b = -1
    c = 30

    temperature = a * (time**2) + b * time + c
    return temperature, a, b, c

def main():
    time_values = np.linspace(0, 10, 100)

    temperature_hardcoded, a, b, c = quadratic_model(time_values)

    plt.plot(time_values, temperature_hardcoded, label='hard-coded coefficient')
    plt.xlabel('time')
    plt.ylabel('temperature')

    coefficients_text = f'a = {a}\nb = {b}\nc = {c}'
    plt.text(7, quadratic_model(7)[0], coefficients_text, bbox=dict(facecolor='white', alpha=0.5))

    plt.legend()
    plt.title('Weather Modeling with Quadratic Equation (Hard-coded Coefficients)')

    plt.show()

if __name__ == "__main__":
    main()
