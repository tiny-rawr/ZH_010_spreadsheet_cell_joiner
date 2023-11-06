def get_columns(headers):
    header_list = headers.split()
    # Creates dict where each header is associated with alphabet key like in G-Sheets
    return {chr(65 + i): header for i, header in enumerate(header_list)}

def join(columns, excluding=''):
    exclude = excluding.split() if excluding else []
    join_statements = []
    for key, value in columns.items():
        if key not in exclude:
            join_statements.append(f'IF({key}2<>"", "{value}: " & {key}2, "")')
    join_statements = ', '.join(join_statements)
    return f"""
    =TEXTJOIN(CHAR(10),
      TRUE,
      {join_statements}
    )
    """

# Headers are copy pasted from header row of Google Sheets
headers = "slug name payment-methods facilities accreditations open_saturday open_sunday after_hours wheelchair_access accepts_dva_card accepts_healthcare_card billing telehealth languages_spoken main_category suburb state postcode city"
columns = get_columns(headers)
print(columns)

print(join(columns, "A R"))
print(join(columns))