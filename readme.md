Aqui está um modelo de README para o seu código:

---

## Chat Jurídico Brasileiro com Gemini Pro

Este aplicativo utiliza **Streamlit** para fornecer uma interface web interativa que permite aos usuários fazer perguntas jurídicas e obter respostas fundamentadas na **Constituição Federal** e no **Código Penal Brasileiro**. A geração das respostas é feita utilizando a **Google Gemini API**.

- Autor: [Peterson Alves](https://github.com/Peterson047)

### Tecnologias Utilizadas

- **Streamlit**: Para a construção da interface web interativa.
- **Google Gemini API**: Para gerar as respostas jurídicas.
- **dotenv**: Para carregar variáveis de ambiente de um arquivo `.env`.
- **Python 3.x**: Para o desenvolvimento do backend.

### Funcionalidades

- Usuários podem fazer perguntas sobre questões jurídicas.
- Respostas geradas pelo modelo Gemini com base na legislação brasileira.
- As respostas são fornecidas de forma segmentada à medida que são geradas.
- Controle de segurança para garantir a remoção de conteúdo prejudicial.

### Como Usar

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/seu-usuario/chat-juridico-brasileiro.git
   cd chat-juridico-brasileiro
   ```

2. **Instale as Dependências**:
   Com o arquivo `requirements.txt`, instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure as Variáveis de Ambiente**:
   Crie um arquivo `.env` na raiz do projeto e adicione sua chave de API do Gemini:
   ```plaintext
   GEMINI_API_KEY=sua_chave_da_api_aqui
   ```

4. **Execute o Aplicativo**:
   Inicie o aplicativo Streamlit com o comando:
   ```bash
   streamlit run app.py
   ```

5. **Acesse o Aplicativo**:
   Abra o navegador e acesse o aplicativo em `http://localhost:8501`.

### Estrutura do Código

- **app.py**: Código principal do aplicativo, que integra o Streamlit com a API Gemini.
- **.env**: Arquivo para configurar as variáveis de ambiente, como a chave de API do Gemini.
- **requirements.txt**: Lista de dependências do Python para o projeto.

### Requisitos

- **Python 3.x**
- **Chave de API do Google Gemini**: A chave deve ser configurada no arquivo `.env`.

### Dependências

No `requirements.txt`:

```plaintext
streamlit
google-generativeai
python-dotenv
```

### Contribuições

Contribuições são bem-vindas! Se você encontrar problemas ou quiser melhorar o projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.

### Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

### Como Funciona

1. O usuário insere uma pergunta jurídica no chat.
2. O modelo Gemini gera uma resposta com base na Constituição e no Código Penal.
3. As respostas são exibidas à medida que são geradas, criando uma interação em tempo real.

### Personalizações

- **Sistema de Instrução**: O modelo Gemini é configurado para fornecer respostas com base em fontes jurídicas oficiais, como a Constituição e o Código Penal.
- **Parâmetros de Geração**: O modelo usa configurações como temperatura, top-p, e top-k para controlar a geração das respostas.

### Problemas Conhecidos

- É necessário configurar corretamente a chave da API do Gemini no arquivo `.env` para o funcionamento adequado.
- Essa versão ainda não oferece suporte a histórico de chat
  

