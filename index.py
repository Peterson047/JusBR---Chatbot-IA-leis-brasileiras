import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configuração da API do Gemini
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
if not GOOGLE_API_KEY:
    st.error("Chave da API do Gemini não encontrada. Configure a variável de ambiente GEMINI_API_KEY no arquivo .env.")
    st.stop()

genai.configure(api_key=GOOGLE_API_KEY)

def generate(prompt):
    """
    Gera uma resposta do modelo Gemini Pro, formatada para o contexto jurídico brasileiro.

    Args:
        prompt: A pergunta ou descrição da situação jurídica.

    Returns:
        Um gerador que produz a resposta do modelo em partes.
    """
    try:
        # Inicializa o modelo Gemini Pro
        model = genai.GenerativeModel('gemini-2.0-pro-exp-02-05')
        
        # Configuração dos parâmetros de geração
        generate_content_config = genai.GenerationConfig(
            temperature=1,
            top_p=0.95,
            top_k=64,
            max_output_tokens=8192,
        )
        
        # Instrução de sistema para orientar o modelo
        system_instruction = """Você é uma advogada especialista em Direito Brasileiro, com profundo conhecimento da Constituição Federal e do Código Penal. Seu papel é esclarecer dúvidas jurídicas de forma clara, objetiva e fundamentada nas leis brasileiras. Utilize sempre as seguintes fontes oficiais para embasar suas respostas:

• Constituição Federal: https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm  
• Código Penal: https://www2.senado.leg.br/bdsf/bitstream/handle/id/529748/codigo_penal_1ed.pdf
• Código de transito brasileiro CTB: https://www.planalto.gov.br/ccivil_03/Leis/L9503.htm
• Código de defesa do consumidor: https://www.planalto.gov.br/ccivil_03/Leis/L8078.htm 
• Código Civil: https://www.planalto.gov.br/ccivil_03/Leis/2002/L10406.htm
• Código de Processo Civil: https://www.planalto.gov.br/ccivil_03/_Ato2015-2018/2015/Lei/L13105.htm
• Código de Processo Penal: https://www.planalto.gov.br/ccivil_03/decreto-lei/del3689.htm
• Código Eleitoral: https://www.planalto.gov.br/ccivil_03/Leis/L4737.htm
• Código Florestal: https://www.planalto.gov.br/ccivil_03/Leis/L4771.htm
• Código de Mineração: https://www.planalto.gov.br/ccivil_03/Leis/L4771.htm
• Código de Águas: https://www.planalto.gov.br/ccivil_03/Leis/L4771.htm
• Código de Telecomunicações: https://www.planalto.gov.br/ccivil_03/Leis/L9472.htm
• Código de Ética e Disciplina da OAB: https://www.oab.org.br/codigo-de-etica-e-disciplina-da-oab/
• Código de Ética Médica: https://portal.cfm.org.br/codigo-de-etica-medica/
• Código de Ética dos Contadores: https://cfc.org.br/wp-content/uploads/2019/05/Codigo-de-Etica-Profissional-do-Contador.pdf
• Código de Ética dos Administradores: https://cfa.org.br/legislacao/codigo-de-etica-do-administrador/
• Código de Ética dos Psicólogos: https://site.cfp.org.br/wp-content/uploads/2012/07/codigo_etica.pdf  
• Código de ética e disciplina da OAB: https://www.oab.org.br/content/pdf/legislacaooab/codigodeetica.pdf


Ao responder, considere os seguintes pontos:

Esclarecimento da situação: Indique se a situação descrita configura crime, contravenção ou outra infração, sempre explicando os elementos legais que justificam sua conclusão.  
Raciocínio passo a passo: Demonstre o processo de análise, relacionando os fatos apresentados aos dispositivos legais correspondentes.  
Limitações e recomendações: Se a dúvida for complexa ou envolver aspectos que não possam ser respondidos de forma completa com base nas fontes indicadas, informe que a resposta é meramente informativa e recomende a consulta a um advogado para um parecer definitivo.  
Linguagem acessível: Explique os termos técnicos de maneira que pessoas sem formação jurídica consigam compreender."""
        
        # Concatena a instrução de sistema com o prompt do usuário
        full_prompt = system_instruction + "\n\n" + prompt

        # Gera a resposta utilizando o prompt completo
        response = model.generate_content(
            full_prompt,
            generation_config=generate_content_config,
            safety_settings=[
                {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"}
            ],
            stream=True
        )
        
        # Retorna o gerador de resposta
        return (chunk.text for chunk in response)

    except Exception as e:
        st.error(f"Erro ao gerar resposta: {e}")
        return None

# --- Streamlit App ---
st.set_page_config(page_title="Chat Jurídico Brasileiro", page_icon=":scales:")
st.title("Chat Jurídico Brasileiro :scales:")
st.write("Faça perguntas sobre situações jurídicas e receba respostas baseadas na Constituição Federal e no Código Penal.")

# Inicializa o histórico do chat, se não existir
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe as mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Recebe o input do usuário e gera a resposta
if prompt := st.chat_input("Digite sua pergunta aqui..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Utiliza st.write_stream para exibir a resposta em partes conforme é gerada
        response_stream = generate(prompt)
        if response_stream:
            response_placeholder = st.empty()
            full_response = ""
            for chunk in response_stream:
                full_response += chunk
                response_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
        else:
            st.markdown("Desculpe, não consegui gerar uma resposta.")
            st.session_state.messages.append({"role": "assistant", "content": "Desculpe, não consegui gerar uma resposta."})
