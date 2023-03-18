import gspread
import openai
import os


from oauth2client.service_account import ServiceAccountCredentials



def read_google_spreadsheet(sheet_id, worksheet_name):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('./custom-name-381012-da941d5e5107.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(sheet_id).worksheet(worksheet_name)
    data = sheet.get_all_values()
    headers = data.pop(0)
    rows = []
    for row in data:
        row_dict = {}
        for i in range(len(headers)):
            row_dict[headers[i]] = row[i]
        rows.append(row_dict)
    return rows

def openai_request(prompt):
    openai.api_key = openAI_API_key 
    model_engine = "text-davinci-003"  
    max_tokens = 100 # Max tokens
    prompt_length = len(prompt) 
    temperature = 0.7  
    stop = "#"  
 
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        stop=stop
    )
    #print(response)
    text = response.choices[0].text
    return text

sheet_id = '1bhCpAd0v0cN9DQe_OOaG8sGm8VlH5pNhgpGowR9vVkU'
openAI_API_key = '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'
worksheet_name = 'test'
rows = read_google_spreadsheet(sheet_id, worksheet_name)
print(rows)
prompt = rows
#print(str(prompt))
print(openai_request(str(prompt).strip('\n')+ " \n     ->give me all the values of column 4 #" ))







 

  


