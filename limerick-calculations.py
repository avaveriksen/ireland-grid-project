import numpy as np

# Population
ireland_pop = 5e6
limerick_pop = 102e3
galway_pop = 86e3

# Real power demand
P_ireland = 6000e6
P_limerick = limerick_pop / ireland_pop * P_ireland
P_galway= galway_pop / ireland_pop * P_ireland

print("Limerick demand: ", P_limerick / 1e6, " [MW]")
print("Galway demand: ", P_galway / 1e6, " [MW]\n")

# Residential and industrial load
P_limerick_res = 0.7 * P_limerick
P_limerick_ind = 0.3 * P_limerick
print("Limerick loads:\nResidential: ", P_limerick_res / 1e6, "[MW]\nIndustrial: ", P_limerick_ind / 1e6, "[MW]\n")

P_galway_res = 0.7 * P_galway
P_galway_ind = 0.3 * P_galway_res
print("Galway loads:\nResidential: ", P_galway_res / 1e6, "[MW]\nIndustrial: ", P_galway_ind / 1e6, "[MW]\n\n")

# Ardnacrusha generator
P_ard = 86e6 # rated 86 MW
generator_pf = 0.9
S_ard = P_ard / generator_pf
print("Rated power Ardnacrusha: ", round(S_ard / 1e6, 3), "[MVA]", P_ard / 1e6, "[MW]")

# Moneypoint generator: Three in parallel of 305 MW rated power each
P_money = 305e6
S_money = P_money / generator_pf
print("Rated power Moneypoint: ", round(S_money / 1e6, 3), "[MVA]", P_money / 1e6, "[MW]")

