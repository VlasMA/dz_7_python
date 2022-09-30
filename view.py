def new_contacts() :

    contacts = ['Number', 'Name', 'Surname', 'Text']
    dict_contact = {contact: input(f'укажите{contact}') for contact in contacts}
    return dict_contact
