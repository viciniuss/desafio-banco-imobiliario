
## Pré-requisitos

- Python 3.8 ou superior
- Dependências: FastAPI, Uvicorn

## Passos para Executar

1. Clone o repositório:
    ```bash
    git clone https://seu-repositorio.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd monopoly-simulator
    ```

3. Crie um ambiente virtual:
    ```bash
    python3 -m venv venv
    ```

4. Ative o ambiente virtual:
    - **Windows**: `venv\Scripts\activate`
    - **Linux/Mac**: `source venv/bin/activate`

5. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

6. Execute o servidor:
    ```bash
    uvicorn api.main:app --reload
    ```

7. Acesse a API na URL:
    ```
    http://localhost:8000/docs
    ```

8. Veja o resultado da simulação na resposta JSON.
