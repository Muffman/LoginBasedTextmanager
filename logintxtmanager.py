import os


while True:
    with open('accounts.txt', 'a') as account_book:
        pass

    encryption_deviate = 1

    def encrypt(to_encrypt):
        encrypted = ""
        for i in to_encrypt:
            enc = chr(ord(i) + encryption_deviate)
            encrypted += enc

        return encrypted

    def decrypt(to_decrypt):
        decrypted = ""
        for i in to_decrypt:
            enc = chr(ord(i) - encryption_deviate)
            decrypted += enc

        return decrypted


    def signup(account_log):
        with open('accounts.txt', 'a') as account_book:
            signup_ID = input('Enter enter ID:').lower()
            signup_password = input("Enter password:")
            account_log[signup_ID] = signup_password
            encrypted_password = encrypt(signup_password)
            account_book.write(signup_ID + "|" + encrypted_password + '\n')

    def login():
        login_ID = input('Enter enter ID:')
        if login_ID in account_log:
            login_password = input("Enter password:")
            account_password = account_log[login_ID]
            if login_password == account_password:
                print("You are in")
                return True, login_ID
            else:
                print("Wrong password")
                return False, login_ID
            
    def text_file_opener(username):
        user_file = username+'.txt'
        with open(user_file, 'a') as text_file:
                pass
            
        text_list = []
        with open(user_file, 'r') as text_file:
            for lines in text_file.readlines():
                decrypted_text = decrypt(lines)
                text_list.append(decrypted_text.rstrip())

        return text_list

        

    def edit_text(text_list):
        edit_index = int(input("which text do you want to edit(input in number): "))
        text_list.pop(edit_index-1)
        edited_text = input("Enter edited text: ")
        text_list.insert(edit_index-1, edited_text)
        
        return text_list

    def delete_text(text_list):
        edit_index = int(input("which text do you want to edit(input in number): "))
        text_list.pop(edit_index-1)
        
        return text_list

    def delete_account(account_log,username):
        del account_log[username]
        os.remove(username+".txt")
        
        return account_log


    account_log = {}
    with open('accounts.txt', 'r') as account_book:
        for account in account_book.readlines():
            account.rstrip()
            username, password = account.split('|')
            decrypted_password = decrypt(password)
            account_log[username] = decrypted_password.rstrip()


    login_type = input("LOGIN or SIGNUP\n").lower()
    if login_type == 'login':
        logged, username = login()
        run = True
        while run and logged:
            text_list = text_file_opener(username)
            mode = input("(read/add/edit/delete/deleteAccount/quit): ")

            if mode == 'read':
                with open(username+'.txt', 'r') as text_file:
                    for i, lines in enumerate(text_file.readlines(), 1):
                        decrypted_lines = decrypt(lines)
                        print(f"{i}:{decrypted_lines}".rstrip())
                          
            elif mode == 'add':
                with open(username+'.txt', 'a') as text_file:
                    text = input("Input text to add: ")
                    encrypted_text = encrypt(text)
                    text_file.write(encrypted_text + '\n')

            elif mode == 'edit':
                text_list = edit_text(text_list)
                with open(username+'.txt', 'w') as text_file:
                    for text in text_list:
                        encrypted_text = encrypt(text)
                        text_file.write(encrypted_text + '\n')

            elif mode == 'delete':
                text_list = delete_text(text_list)
                with open(username+'.txt', 'w') as text_file:
                    for text in text_list:
                        encrypted_text = encrypt(text)
                        text_file.write(encrypted_text + '\n')

            elif mode == 'deleteAccount':
                account_log = delete_account(account_log, username)
                with open('accounts.txt', 'w') as text_file:
                    for name in account_log:
                        encrypted_password = encrypt(account_log[name])
                        text_file.write(name + '|' + encrypted_password + '\n')
                        
                run = False
                
            elif mode == 'quit':
                run = False

    elif login_type == 'signup':
        signup(account_log)
            


 
