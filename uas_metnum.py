import math

# ==========================================
# 1. DEFINISI FUNGSI MATEMATIKA
# ==========================================

# Fungsi asli: f(x) = 6x^3 + 4x^2 - 5x + 3
def f(x):
    return 6 * (x**3) + 4 * (x**2) - 5 * x + 3

# Turunan pertama: f'(x) = 18x^2 + 8x - 5 (Untuk Newton-Raphson)
def df(x):
    return 18 * (x**2) + 8 * x - 5

# Fungsi untuk Iterasi Sederhana: g(x) = ((-4x^2 + 5x - 3)/6)^(1/3)
# Catatan: Kita buat fungsi custom cbrt agar bisa menangani akar pangkat tiga dari angka negatif
def cbrt(val):
    if val < 0:
        return -math.pow(-val, 1/3)
    else:
        return math.pow(val, 1/3)

def g(x):
    return cbrt((-4 * (x**2) + 5 * x - 3) / 6)


# ==========================================
# 2. IMPLEMENTASI METODE NUMERIK
# ==========================================

def newton_raphson(x0, e, max_iter=50):
    print(f"{'Iterasi':<10} | {'x (old)':<15} | {'f(x)':<15} | {'x (new)':<15} | {'Galat/Error':<15}")
    print("-" * 75)
    
    x_old = x0
    for i in range(1, max_iter + 1):
        fx = f(x_old)
        dfx = df(x_old)
        
        if dfx == 0:
            print("Turunan nol, perhitungan dihentikan.")
            break
            
        x_new = x_old - (fx / dfx)
        galat = abs(x_new - x_old)
        
        print(f"{i:<10} | {x_old:<15.6f} | {fx:<15.6f} | {x_new:<15.6f} | {galat:<15.6f}")
        
        if galat < e:
            print(f"--> [BERHENTI] Konvergen di iterasi ke-{i} dengan akar x = {x_new:.6f}\n")
            break
            
        x_old = x_new

def iterasi_sederhana(x0, e, max_iter=50):
    print(f"{'Iterasi':<10} | {'x':<15} | {'g(x)':<15} | {'f(x)':<15} | {'Keterangan':<15}")
    print("-" * 75)
    
    x_curr = x0
    # Dimulai dari iterasi 0 sesuai format di Excel
    for i in range(0, max_iter):
        gx = g(x_curr)
        # Sesuai Excel: kolom f(x) dihitung dari fungsi x yang baru (g(x))
        fx_new = f(gx) 
        
        # Sesuai Excel: syarat berhenti jika mutlak f(x) < e
        if abs(fx_new) < e:
            keterangan = "berhenti"
        else:
            keterangan = "lanjutkan"
            
        print(f"{i:<10} | {x_curr:<15.6f} | {gx:<15.6f} | {fx_new:<15.6f} | {keterangan:<15}")
        
        if keterangan == "berhenti":
            print(f"--> [BERHENTI] Sesuai Excel, berhenti di iterasi ke-{i} dengan akar x = {gx:.6f}\n")
            break
            
        # Update nilai x untuk iterasi selanjutnya
        x_curr = gx

def secant(x0, x1, e, max_iter=50):
    print(f"{'Iterasi':<10} | {'x0 (xi-1)':<15} | {'x1 (xi)':<15} | {'x (new)':<15} | {'Galat/Error':<15}")
    print("-" * 80)
    
    for i in range(1, max_iter + 1):
        f0 = f(x0)
        f1 = f(x1)
        
        if f1 - f0 == 0:
            print("Pembagian dengan nol, perhitungan dihentikan.")
            break
            
        # Rumus Secant
        x_new = x1 - (f1 * (x1 - x0)) / (f1 - f0)
        galat = abs(x_new - x1)
        
        print(f"{i:<10} | {x0:<15.6f} | {x1:<15.6f} | {x_new:<15.6f} | {galat:<15.6f}")
        
        if galat < e:
            print(f"--> [BERHENTI] Konvergen di iterasi ke-{i} dengan akar x = {x_new:.6f}\n")
            break
            
        # Update nilai untuk iterasi selanjutnya
        x0 = x1
        x1 = x_new


# ==========================================
# 3. MENJALANKAN PROGRAM
# ==========================================
if __name__ == "__main__":
    toleransi = 0.001
    
    print("=== 1. METODE NEWTON-RAPHSON ===")
    newton_raphson(x0=4, e=toleransi)
    
    print("=== 2. METODE ITERASI SEDERHANA ===")
    iterasi_sederhana(x0=4, e=toleransi)
    
    print("=== 3. METODE SECANT ===")
    secant(x0=4, x1=0.5, e=toleransi)