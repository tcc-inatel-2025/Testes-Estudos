# Testes-Estudos

Repositório com códigos gerados para estudos durante o TCC.

---

## 🟢 Testes com **Pylint**

Pylint é usado para análise de qualidade do código Python.

- Instalação:

```bash
pip install pylint
```

- Uso:

```bash
pylint file.py
```

- Retorna uma pontuação de 0 a 10.

| Arquivo    | Pylint Score | Badge |
|------------|-------------|-------|
| `good.py`  | 10/10       | ![10/10](https://img.shields.io/badge/Pylint-10/10-brightgreen) |
| `bad.py`   | 6.67/10     | ![6.67/10](https://img.shields.io/badge/Pylint-6.67/10-yellow) |

---

## 🔵 Testes com **Radon**

Radon avalia a **complexidade ciclomática** do código.

- Instalação:

```bash
pip install radon
```

- Uso:

```bash
radon cc good.py -a
```

- Classificação de complexidade:

| Nota | Complexidade | Normalizado |
|------|-------------|-------------|
| A    | 1–5         | 1.0         |
| B    | 6–10        | 0.85        |
| C    | 11–20       | 0.7         |
| D    | 21–30       | 0.55        |
| E    | 31–40       | 0.4         |
| F    | >40         | 0.2         |

Exemplo de normalização:

```python
def normalize_radon_complexity(grade):
    scale = {'A': 1.0, 'B': 0.85, 'C': 0.7, 'D': 0.55, 'E': 0.4, 'F': 0.2}
    return scale.get(grade, 0.0)

print(normalize_radon_complexity("A"))  # 1.0
```

| Arquivo    | Radon Score | Normalizado | Badge |
|------------|------------|-------------|-------|
| `good.py`  | A          | 1.0         | ![A](https://img.shields.io/badge/Radon-A-brightgreen) |
| `bad.py`   | A          | 1.0         | ![A](https://img.shields.io/badge/Radon-A-brightgreen) |

---

## ⚡ Aplicando **PoE** (Point of Evaluation)

Para unir as métricas Pylint e Radon, multiplicamos os scores normalizados:

```python
pylint_score = 0.667  # normalizado 6.67/10
radon_score = 1.0     # normalizado
final_score = pylint_score * radon_score
print(final_score)  # 0.667
```

| Arquivo    | Pylint | Radon | PoE Score | Badge |
|------------|--------|-------|-----------|-------|
| `good.py`  | 10/10  | A     | 1.0       | ![1.0](https://img.shields.io/badge/PoE-1.0-brightgreen) |
| `bad.py`   | 6.67/10| A     | 0.667     | ![0.667](https://img.shields.io/badge/PoE-0.667-yellow) |

> O **PoE Score** representa uma avaliação unificada da qualidade e complexidade do código.
