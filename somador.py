import threading

# Função que cada thread vai executar
def thread_sum(numbers, start_index, end_index, result, index):
    total = sum(numbers[start_index:end_index])
    result[index] = total

def main():
    # Lista de números a serem somados
    numbers = list(range(1, 100))  # Exemplo de uma lista grande de números
    
    # Número de threads a serem usadas
    num_threads = 4
    thread_list = []
    result = [0] * num_threads  # Lista para armazenar o resultado de cada thread
    
    # Calculando o tamanho do pedaço de trabalho para cada thread
    chunk_size = len(numbers) // num_threads

    for i in range(num_threads):
        start_index = i * chunk_size
        end_index = (i + 1) * chunk_size if i != num_threads - 1 else len(numbers)
        
        # Criando e iniciando a thread
        thread = threading.Thread(target=thread_sum, args=(numbers, start_index, end_index, result, i))
        thread_list.append(thread)
        thread.start()

    # Aguardando todas as threads terminarem
    for thread in thread_list:
        thread.join()
    
    # Somando os resultados das threads
    total_sum = sum(result)
    
    print(f"A soma dos números é: {total_sum}")

if __name__ == "__main__":
    main()
