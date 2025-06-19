import matplotlib.pyplot as plt
import math


#funcao que define a sequencia numerica de termo geral e(n) 2(e)
def e(n):
    return ((n**2) / (n + 1)) - ((n**2) / (n + 2))

#funcao que gera a sequencia numerica de termo geral a(n) 2(a)
def a(n):
    return (n - 1) / (n + 1)

#funcao que gera a sequencia numerica de termo geral g(n) 2(g)
def g(n):
    numerador = math.sqrt(math.factorial(n)) + math.exp(2 * n)
    demoninador =  5 * math.sqrt(math.factorial(n)) - math.exp(n)
    return numerador/demoninador

#funcao que gera a sequncia numerica de termo geral c(n) 2(c)
def c(n):
    return math.log(n) / math.exp(n)

#funcao que gera a sequencia numerica de termo geral i(n) 2(i)
def i(n):
    return (n**2) / (n + 1)



#difinição de nmin e nmax
nmin = int(input("Digite o nmin: "))
nmax = int(input("Digite nmax: "))
print(f"nmin: {nmin}, nmax: {nmax}")


#separa nos casos em que o limite é e não é conhecido
existeLimite = (input("eh conhecido se a sequencia converge para um limite L? (a se sim, b se nao): "))
print(f"opcao escolhida: {existeLimite}")


valoresN = []
valoresAn = []
print(f"\n{'n':>5} {'a(n)':>10}")
print("-" * 15)

for n in range( nmin, nmax +1):
    an = a(n)
    print(f"{n:>5} {an:>10.6f}")
    valoresN.append(n)
    valoresAn.append(an)

# Plota o gráfico da sequência a(n)
plt.figure(figsize=(8, 5))
plt.plot(valoresN, valoresAn, 'bo-', label='a(n)')
plt.xlabel('n')
plt.ylabel('a(n)')
plt.title('Gráfico da sequência')
plt.grid(True)

#funcao que verifica se o modulo da diferença entre o termo geral e o limite é menor ou igual a epsilon 
def N_epsilon_is_true(x, L, epsilon):
    if abs(x - L) <= epsilon:
        return True
    else:
        return False
    

if existeLimite == "b":
    L = float(input("Digite o valor do limite L: "))
    epsilon = float(input("Digite a tolerância epsilon: "))
    N_epsilon = float(input("Digite o valor de N(epsilon): "))
    
    Ne = N_epsilon_is_true(a(n), L, epsilon)

    while Ne == False:
        L = float(input("Digite o valor do limite L: "))
        epsilon = float(input("Digite a tolerância epsilon: "))
        N_epsilon = int(input("Digite o valor de N(epsilon): "))
        Ne = N_epsilon_is_true(a(n), L, epsilon)

    plt.axhline(y=L, color='green', linestyle='--', label='y = L')
    plt.axhline(y=L+epsilon, color='red', linestyle=':', label='y = L + ε')
    plt.axhline(y=L-epsilon, color='red', linestyle=':', label='y = L - ε')

    plt.legend()
    plt.show()