# Testes-Estudos
Repositorio para codigos gerados para estudos durante o TCC

___

# 1 Testes com pylint 

Para a primeira metrica temos o pylint adicionei 2 exemplos de codigos diferentes 1 com nota 10 no pylint e outro com uma nota mediana. 

Pylint pode ser instalado usando pip e chamado no env como:
**pylint file.py** 
retornando um score de 0/10 

# 2 Testes con radon 
Pode ser instalado da mesma forma pip install radon. 
E chamado via linha de comando como:
**radon cc good.py -a**
retorna o score da complexidade do script na seguinte avaliacao: 

A (1–5)
B (6–10)
C (11–20)
D (21–30)
E (31–40)
F (>40)

ou seja quanto menor o resultado melhor, podemos normalizar a escala para nosso trabalho da seguinte forma: 

``` Python
    def normalize_radon_complexity(grade):
        scale = {'A': 1.0, 'B': 0.85, 'C': 0.7, 'D': 0.55, 'E': 0.4, 'F': 0.2}
    return scale.get(grade, 0.0)

    print(normalize_radon_complexity("A"))  # 1.0
```

# 3 PoE na pratica

usando o arquivo bad.py como exemplo o score(ou expert) do pylint retorna um score de 6.67/10 (0.667/1)
e o score do radon A (1.0) podemos aplicar o Poe nesse caso apenas multiplicando os resultados, conseguindo um score unificado final de 0.667