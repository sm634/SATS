from decouple import config
import pandas as pd
import openai

openai.api_key = config('OPENAI_API_KEY')


def generate_summary_prompt(text):
    return """Summarize this in three short sentences:
    
    "{}"
    """.format(text)


def generate_invoice_prompt(data_fields, invoice_text):
    return f"""extract the values for the {data_fields} from the text below. Remove any commas between the numerical
     values in the text. Then Return only the values, without their keys separated by comma:
            "{invoice_text}"
           """


def summarize_text(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=generate_summary_prompt(text),
        max_tokens=1000,
        temperature=0
    )
    summary = response.choices[0].text
    return summary


def extract_invoice_info(data_fields, invoice_text):
    """
    :param data_fields: values for data fields to extract
    :return: a string, comma separated with all of the values we require.
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=generate_invoice_prompt(data_fields=data_fields, invoice_text=invoice_text),
        max_tokens=2500,
        temperature=0
    )
    extracted_values = response.choices[0].text
    return extracted_values


fields = "Document Number, Document Date, Account No., Payment Reference, " \
         "Payment Terms, Quantity, Amount"

invoice = """Registered Office S
sel loo Canard Building (=) Smurfit Kappa
Pier Head

Liverpool, L3 1SF

Web: www.smurfitkappa.com

Site Tel: 01354 662 200

FAERCH UK Delivery : Ex Works Document Number
ELEAN BUSINESS PARK UMAR197864
SUTTON
ELY Document Date
CAMBS 04/11/22
CB6 2QE
Page 1 of 1
Account No. Payment Reference Payment Terms Contact Person
111106 UMAR197864 / 111106 60 days nett end of month J Middleton
Delivery Note Number: 144018 Load Run Number: 87804
Your Reference Print Title Order No. Quantity Price/1000 FSC Amount
6000070 6000070 BOX 7 FSC 273895 9160 930.87 * 8,526.77
Goods Value 8,526.77
VAT @ 20.00% 1,705.35
Total GBP 10,232.12

Weight for Packaging Waste Regulations declaration: 7,378 KG on 33 pallets

Products marked * are FSC Mix 70%, SA-COC-002498

HSBC Bank PLC a/c Name : SMURFIT KAPPA EUROPEAN PACKAGING LTD. A/C Number: 71261886 Sort Code: 40-02-50
IBAN: GBO8MIDL40025071261886 Swift Code: MIDLGB22BHX VAT no. GB 344 0207 96

———~

canran ‘SUBJECT TO OUR TERMS AND CONDITIONS OF SALE'

REDUCING Coz
YEAR ON YEAR

A member of the Smurfit Kappa Group

Smurfit Kappa is a trading unit of Smurfit Kappa UK Ltd, registered in England No. 1017013
Registered Office: Cunard Building, Pier Head, Liverpool, L3 1SF"""

extracted_val = extract_invoice_info(data_fields=fields, invoice_text=invoice)

def txt_to_list(text):
    cleaned_text = text.replace('\n', "").replace(r"\s", "")
    values_list = cleaned_text.split(',')
    return values_list


columns = ['Document Number', 'Document Date', 'Account No.', 'Payment Reference',
           'Payment Terms', 'Quantity', 'Amount']

values = txt_to_list(extracted_val)

df = pd.DataFrame(data=values)
df = df.transpose()
df.columns = columns

df.to_csv('outputs/draft_output.csv')
