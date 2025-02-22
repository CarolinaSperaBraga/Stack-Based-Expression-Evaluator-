
# Cria a classe Pilha
class Pilha:
# Função para encontrar a precedência dos operadores
    def ordem_operadores(self, op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        return 0
    
    # Função que realiza as operações aritméticas
    def operacoes(self, a, b, op):
         
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/': return a / b
        raise Exception("Expressao invalida")
        
    # Função que retorna o valor da expressão aritmética
    def resultado(self, equacao):
        # Pilha que armazenas os valores numéricos
        valores = []
        # Pilha que armazena os operadores
        ops = []
        i = 0
        # Lista para armazenar flags e determinar se a expressão é válida e pode ser 
        # calculada ou não
        bandeiras = []
        # Lista para armazenar flags dos sinais agrupadores
        # [chaves, colchetes, parênteses]
        agrupadores = [0, 0, 0]
        
        while i < len(equacao):
            # Caso apareça um espaço na equação, seguimos para o próximo índice
            if equacao[i] == ' ':
                i += 1
                continue
                
            # Armazena chaves, colchetes e parêntesis na pilha dos operadores    
            elif equacao[i] == "{":
                if agrupadores[0]  or agrupadores[1] or agrupadores[2]:
                    return ("Expressao invalida")
                agrupadores[0] = 1
                ops.append(equacao[i])
            elif equacao[i] == "[":
                if agrupadores[1] or agrupadores[2]:
                    return ("Expressao invalida")
                agrupadores[1] = 1
                ops.append(equacao[i])
            elif equacao[i] == '(':
                if agrupadores[2]:
                    return ("Expressao invalida")
                agrupadores[2] = 1
                ops.append(equacao[i])
                
            # Armazena números na pilha dos valores numéricos    
            elif equacao[i].isdigit():
                val = 0
                # Caso um número tenha mais de um dígito
                while (i < len(equacao) and equacao[i].isdigit()):
                    val = (val * 10) + int(equacao[i]) 
                    i += 1
                # Caso tenha ponto, adicionar a parte decimal
                if i < len(equacao) and equacao[i] == ".":
                    e = 0
                    i += 1
                    while (i < len(equacao) and equacao[i].isdigit()):
                        e -= 1
                        val = val + float(equacao[i])*10**(e)
                        i += 1
                valores.append(val)
                # Aqui i está ao lado do dígito, e como o loop aumenta i nós pularíamos uma 
                # posição, então diminuímos o valor de i por 1 para corrigir isso
                i-=1
                
            # Resolvemos o que estiver dentro dos parêntesis, encontrando seu começo e fim "()"
            elif equacao[i] == ')':
                flag = True
                try:
                    while len(ops) != 0 and ops[-1] != '(':
                        val2 = valores.pop()
                        val1 = valores.pop()
                        op = ops.pop()
                        valores.append(self.operacoes(val1, val2, op))
                    # Tira o parêntesis aberto da pilha
                    ops.pop()
                except:
                    flag = False
                    bandeiras.append(flag)
                    break
            # Resolvemos o que estiver dentro dos colchetes, encontrando seu começo e fim "[]"
            elif equacao[i] == "]":
                flag = True
                try:
                    while len(ops) != 0 and ops[-1] != "[":
                        val2 = valores.pop()
                        val1 = valores.pop()
                        op = ops.pop()
                        valores.append(self.operacoes(val1, val2, op))
                    # Tira o colchete aberto da pilha
                    ops.pop()
                except:
                    flag = False
                    bandeiras.append(flag)
                    break
            # Resolvemos o que estiver dentro das chaves, encontrando seu começo e fim "{}"    
            elif equacao[i] == "}":
                flag = True
                try:
                    while len(ops) != 0 and ops[-1] != "{":
                        val2 = valores.pop()
                        val1 = valores.pop()
                        op = ops.pop()
                        valores.append(self.operacoes(val1, val2, op))
                    # Tira a chave aberta da pilha
                    ops.pop()  
                except:
                    flag = False
                    bandeiras.append(flag)
                    break
            # Caso o índice atual seja um operador
            else:
                # Executa o operador no topo de da pilha de operadores aos dois
                # primeiros elementos do topo da pilha de valores
                while (len(ops) != 0 and 
                        self.ordem_operadores(ops[-1]) >= self.ordem_operadores(equacao[i])):
                    try:    
                        val2 = valores.pop()
                        val1 = valores.pop()
                        op = ops.pop()
                        valores.append(self.operacoes(val1, val2, op))
                    except:
                        return ("Expressao invalida")
                # Insere o índice atual na pilha de operadores
                ops.append(equacao[i])
            i += 1
        # Executa as operações restantes
        while len(ops) != 0:
            flag = True
            try:
                val2 = valores.pop()
                val1 = valores.pop()
                op = ops.pop()
                valores.append(self.operacoes(val1, val2, op))
            except:
                flag = False
                bandeiras.append(flag)
                break
        # Retornamos o número do topo da pilha dos valores que contém o resultado
        if False in bandeiras:
            return ("Expressao invalida")
        else:
            if isinstance(valores[-1], float):
                if valores[-1].is_integer():
                    return (int(valores[-1]))
                #else:
            return (valores[-1])

# Entrada que armazena a equação        
e = input()  
# Impressão do resultado    
pilha = Pilha()
print(pilha.resultado(e))    