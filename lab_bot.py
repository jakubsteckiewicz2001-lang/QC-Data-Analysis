import pandas as pd
import matplotlib.pyplot as plt

# --- 1. SYMULACJA DANYCH ---
# Udajemy, że to dane z Twojego ostatniego tygodnia na praktykach
data = {
    'Batch_ID': ['B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07'],
    'pH_Value': [6.55, 6.62, 6.48, 6.75, 6.60, 6.58, 6.82]
}
df = pd.DataFrame(data)

# Definiujemy normy (np. standard dla Twojego produktu)
MIN_NORM = 6.5
MAX_NORM = 6.7

# --- 2. LOGIKA ANALITYCZNA ---
# Program sam znajduje partie (Batches), które są poza normą
alerts = df[(df['pH_Value'] < MIN_NORM) | (df['pH_Value'] > MAX_NORM)]

# --- 3. GENEROWANIE RAPORTU WIZUALNEGO ---
plt.figure(figsize=(10, 6))

# Rysujemy wszystkie punkty
plt.plot(df['Batch_ID'], df['pH_Value'], color='gray', linestyle='--', alpha=0.5)
plt.scatter(df['Batch_ID'], df['pH_Value'], color='blue', label='Partie w normie')

# Zaznaczamy ALERTY na czerwono (to robi wrażenie!)
plt.scatter(alerts['Batch_ID'], alerts['pH_Value'], color='red', s=100, label='ALARM: POZA NORMĄ!')

# Dodajemy linie graniczne
plt.axhline(y=MAX_NORM, color='green', linestyle='-', label='Max Norma')
plt.axhline(y=MIN_NORM, color='green', linestyle='-', label='Min Norma')

# Dodatki graficzne
plt.title('Automatyczny Raport Kontroli Jakości (pH)', fontsize=14)
plt.xlabel('Numer Partii Produkcyjnej')
plt.ylabel('Wartość pH')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)

# --- 4. WYDRUK ---
plt.savefig('raport_koncowy.png')
print("--- ANALIZA ZAKOŃCZONA ---")
print(f"Znaleziono {len(alerts)} odchyleń od normy.")
if not alerts.empty:
    print("Partie do sprawdzenia:", alerts['Batch_ID'].values)
else:
    print("Wszystkie partie w normie. Dobra robota!")

plt.show()