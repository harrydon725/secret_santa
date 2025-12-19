import smtplib
from email.message import EmailMessage
from details import password, emails
import random

round = input("Year?\n\n>>> ")

details=emails
names_list=['Harry','Mum','Dad','Jack','Georgina']
shuffled = names_list[:]
while any(shuffled[i] == names_list[i] for i in range(len(names_list))):
        random.shuffle(shuffled)
pairs = list(zip(names_list, shuffled))
print(pairs)
'''
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:

    server.login("jjuly7446@gmail.com", password)
    for pair in pairs:
        msg = EmailMessage()
        msg["From"] = "jjuly7446@gmail.com"
        msg["To"] = details[pair[0]]
        msg["Subject"] = "Secret Santa Test"
        msg.set_content(f"Hello {pair[0]}! This is a test email for secret santa\n\n\nYou have {pair[1]}.")
        server.send_message(msg)
        print("Email sent successfully!")
'''
with open("results.txt", "a") as f:
  f.write(f"{round}\n---------------------------------\n{pairs}\n---------------------------------\n")