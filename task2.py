def average_gdp(population, gdp):
    total_population = sum(population)
    total_gdp = sum(gdp)
    return total_gdp / total_population


population = [1000, 2000, 1500, 1200, 1800]
gdp = [50000, 60000, 70000, 80000, 90000]

print(average_gdp(population, gdp))
