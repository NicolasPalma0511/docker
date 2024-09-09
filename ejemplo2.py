from scipy.stats import variation

data = [10, 20, 30, 40, 50]

cv = variation(data)

print(f"El coeficiente de variación es: {cv:.2f}")
