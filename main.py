def get_columns(headers):
    header_list = headers.split()
    # Creates dict where each header is associated with alphabet key like in G-Sheets
    return {chr(65 + i): header for i, header in enumerate(header_list)}

headers = "slug name payment-methods facilities accreditations open_saturday open_sunday after_hours wheelchair_access accepts_dva_card accepts_healthcare_card billing telehealth languages_spoken main_category suburb state postcode city"
columns = get_columns(headers)
print(columns)
print(columns['A'])