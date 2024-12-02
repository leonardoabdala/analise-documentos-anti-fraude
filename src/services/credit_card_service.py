from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRquest
from utils.Config import Config

def analyze_credit_card(card_url):

    credential = AzureKeyCredential(Config.key)

    documet_intelligence_client = DocumentIntelligenceClient(Config.ENDPOINT, credential)

    card_info = documet_intelligence_client.begin_analyze_document("prebuilt-creditCard", AnalyzeDocumentRquest(url_source=card_url))
    result = card_info.result()

    for document in result.documents:
        fields = document.get("fields", {})

        return {
            "card_name": fields.get('CardHolderName', {}).get('content'),
            "card_number": fields.get('CardNumber', {}).get('content'),
            "expirity_date": fields.get('ExpirationDate', {}).get('content'),
            "bank_name": fields.get('InssuingBank',{}).get('content'),

        }
    
    



    