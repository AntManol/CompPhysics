import numpy as np
import matplotlib.pyplot as plt

# Παράμετροι της κατανομής Rayleigh 
σ = 2
N = 10000

# Δημιουργία N ομοιόμορφα κατανεμημένων τυχαίων αριθμών U 
U = np.random.rand(N)

# Εφαρμογή του αντίστροφου μετασχηματισμού για την παραγωγή τυχαίων αριθμών Rayleigh
X = σ * np.sqrt(-2 * np.log(U))

# Έλενχος αριθμού κυμάτων τα οποία έχουν ύψος 3<x<5 [m] και τυχαίων αριθμών που χρειάστηκαν
acc = 0 # Aρχικοποίηση του μετρητή

for i in range(N):
    if 3 < X[i] <5: # Ελέγχος αν το ύψος του κάθε κύματος βρίσκεται μεταξύ του 3 και 5
        acc += 1

per = acc / N*100
print('\nThere were used %d uniform random numbers for the production of %d Rayleigh numbers with the Inverse Tranformation method' % (N, N) )
print('The %f percent of those waves are between 3 and 5 meters\n' % per)

# Σχεδίαση του γραφήματος θεωρητικής και παραγόμενης κατανομής.
plt.hist(X, bins=30, color='green',ec='black',density=True, label ='Παραγόμενα Δεδομένα')

# Υπολογισμός της θεωρητικής κατανομής Rayleigh απο τον γνωστό τύπο για σύγκριση
x = np.linspace(0, 10, 1000)
rayleigh_pdf = (x / σ**2) * np.exp(-x**2 / (2 * σ**2))
plt.plot(x, rayleigh_pdf, 'r-', linewidth=2, label='Θεωρητική κατανομή Rayleigh')

# ΣΗμειώσεις πάνω στο διάγραμμα
plt.title('Παραγωγή τυχαίων αριθμών με κατανομή Rayleigh')
plt.xlabel('Ύψος κύματος (m)')
plt.ylabel('Πυκνότητα πιθανότητας')
plt.legend()
plt.show()
