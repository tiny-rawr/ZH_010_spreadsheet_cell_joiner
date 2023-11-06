headers = "slug name payment-methods facilities accreditations open_saturday open_sunday after_hours wheelchair_access accepts_dva_card accepts_healthcare_card billing telehealth languages_spoken main_category suburb state postcode city"

header_list = headers.split()

columns = {chr(65 + i): header for i, header in enumerate(header_list)}

print(columns)
