import stringlist as st

from services.blob_services import upload_blob
from services.credit_card_service import analyze_credit_card

def configure_interface():
    st.title("Upload de arquivos DIO - Desafio - Azure - Fake Docs")
    uploaded_file = st.file_uploaded("Escolha um arquivo", type=["png","jpg", "jpeg"])

    if uploaded_file is not None:
        fileName = uploaded_file.name
        # Enviar para o Blob storage
        blob_url = upload_blob(uploaded_file, fileName)
        if blob_url:
            st.write(f"Arquivo {fileName} enviado com sucesso para o Azure Blob Storage")
            credit_card_info = analyze_credit_card(blob_url)
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write(f"Erro ao enviar o arquivo {fileName} para o Azure Blob Storage")    

def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Imagem enviada", use_column_width=True)
    st.write("Resultado da validação:")
    if credit_card_infoand and credit_card_info['card_name']:
        st.markdown(f"<h1 style='color: green;'>Cartão Validado </h1>") 
        st.write(f"Nome do titular: {credit_card_info['card_name']}")
        st.write(f"Banco emissor: {credit_card_info['bank_name']}")   
        st.write(f"Data de validade: {credit_card_info['expirity_date']}")
    else:
        st.write(f"<h1 style='color:red;' > Cartão inválido </h1>")
        st.write(f"Este não é um cartão de crédito válido")
    

if __name__ == "__main__":
    configure_interface()    