G = (4.1 - 2.1) / (100 - 2.1)
A = 1 - G

G_area = 0.081
G_density = 2.266
A_density = 7.870
correction1 = G_density / (G*G_density + A*A_density)
correction2 = G_density / (G_area*G_density + (1-G_area)*A_density)
correction3 = G_density / (7.5)


print correction2, correction1



# G_wt = G_wt * G_area
# print G_wt