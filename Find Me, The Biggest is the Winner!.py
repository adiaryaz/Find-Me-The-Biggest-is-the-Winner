def factorial(n):
    """
    Fungsi untuk menghitung faktorial dari sebuah angka non-negatif.
    """
    if n < 0:
        return "NoProceed"
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def find_largest_and_factorial():
    """
    Meminta 5 input angka, mencari yang terbesar, lalu menghitung faktorialnya.
    """
    try:
        numbers = [int(input()) for _ in range(5)]
        
        largest = max(numbers)
        
        print(largest)
        
        print(factorial(largest))

    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

find_largest_and_factorial()