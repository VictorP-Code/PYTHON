import math
from flask import request, render_template

def calcular():
    num1_str = request.form.get("num1", "").strip()
    operacao = request.form.get("operacao", "")
    
    if not num1_str:
        return "Informe o primeiro número.", ""
    
    try:
        num1 = float(num1_str)
    except ValueError:
        return "Erro: Primeiro número inválido.", ""
    
    # Raiz quadrada
    if operacao == "sqrt":
        if num1 < 0:
            return f"Erro: Não existe raiz real de {num1}.", ""
        resultado = math.sqrt(num1)
        return f"√{num1} = {resultado}", resultado
    
    # "FODEU TEM LOG" 5 avai desmaiar, 10 vão correr...
    elif operacao == "log":
        if num1 <= 0:
            return f"Erro: Logaritmo não definido para {num1}.", ""
        resultado = math.log(num1)
        return f"log({num1}) = {resultado}", resultado
    
    # num1 e num2
    num2_str = request.form.get("num2", "").strip()
    if not num2_str:
        return "Informe o segundo número para esta operação.", ""
    
    try:
        num2 = float(num2_str)
    except ValueError:
        return "Erro: Segundo número inválido.", ""
    
    # Operações básicas
    if operacao == "+":
        resultado = num1 + num2
        return f"{num1} + {num2} = {resultado}", resultado
    
    elif operacao == "-":
        resultado = num1 - num2
        return f"{num1} - {num2} = {resultado}", resultado
    
    elif operacao == "*":
        resultado = num1 * num2
        return f"{num1} × {num2} = {resultado}", resultado
    
    elif operacao == "/":
        if num2 == 0:
            return "Erro: Divisão por zero não é permitida.", ""
        resultado = num1 / num2
        return f"{num1} ÷ {num2} = {resultado}", resultado
    
    elif operacao == "**":
        resultado = num1 ** num2
        return f"{num1}^{num2} = {resultado}", resultado
    
    # Bhaskara
    elif operacao == "bhaskara":
        num3_str = request.form.get("num3", "").strip()
        if not num3_str:
            return "Para Bhaskara, informe os três coeficientes (a, b, c).", ""
        
        try:
            num3 = float(num3_str)
        except ValueError:
            return "Erro: Terceiro coeficiente inválido.", ""
        
        a, b, c = num1, num2, num3
        
        if a == 0:
            return "Erro: Para Bhaskara, 'a' não pode ser zero (não é equação do 2º grau).", ""
        
        delta = b**2 - 4*a*c
        
        if delta < 0:
            return f"Δ = {delta} → Não existem raízes reais.", ""
        elif delta == 0:
            x = -b / (2*a)
            return f"Δ = {delta} → Uma raiz real: x = {x}", x
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            return f"Δ = {delta} → Duas raízes: x₁ = {x1}, x₂ = {x2}", f"x₁={x1}, x₂={x2}"
    
    # Quando a conta tá tiranu no bglh
    return "Operação inválida.", ""