    is_ok = messagebox.askokcancel(title=website_entry_data, message=f"These are the details entered: \nEmail: {email_entry_data} "
                            f"\nPassword: {password_entry_data} \nIs it ok to save?")
        
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website_entry_data} | {email_entry_data} | {password_entry_data}\n")
            detele_data()