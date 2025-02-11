#include <iostream>
#include <vector>
#include <algorithm>

// Función pura para verificar si un número es primo
bool esPrimo(int numero) {
    if (numero < 2) return false;
    for (int i = 2; i * i <= numero; i++) { // Optimización con raíz cuadrada
        if (numero % i == 0) return false;
    }
    return true;
}

// Función para obtener primos sin usar `std::ranges`
std::vector<int> obtenerPrimos(int hasta) {
    std::vector<int> primos;
    for (int i = 2; i <= hasta; i++) {
        if (esPrimo(i)) {
            primos.push_back(i);
        }
    }
    return primos;
}

int main() {
    int n;
    std::cout << "Ingrese un número: ";
    std::cin >> n;

    std::vector<int> primos = obtenerPrimos(n);
    for (int primo : primos) {
        std::cout << primo << " ";
    }
    std::cout << std::endl;

    return 0;
}
