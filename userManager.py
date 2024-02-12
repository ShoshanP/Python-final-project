import os
import re
from typing import List

class UsersManager:
    def __init__(self):
        self.users_file_path = "UsersName.txt"
        self.emails_file_path = "UsersEmail.txt"
        self.users = []
        self.first_10_percent_users = []
        self.valid_emails = []
        self.gmail_addresses = []

    def create_missing_file(self):
        """
        Check if the users file exists, if not, create it.
        """
        if not os.path.exists(self.users_file_path):
            with open(self.users_file_path, "w") as f:
                f.write("")

    def read_users_from_file(self):
        """
        Read usernames from the users file into a generator.
        """
        with open(self.users_file_path, "r") as f:
            for line in f:
                yield line.strip()

    def read_users_into_array(self):
        """
        Read usernames from the users file into an array.
        """
        with open(self.users_file_path, "r") as f:
            self.users = [line.strip() for line in f]

    def get_first_10_percent_users(self):
        """
        Get the first 10% of users and store them in a separate list.
        """
        num_users = len(self.users)
        ten_percent = int(0.1 * num_users)
        self.first_10_percent_users = self.users[:ten_percent]

    def process_even_rows(self):
        """
        Process usernames from even rows in the users file.
        """
        with open(self.users_file_path, "r") as f:
            for idx, line in enumerate(f):
                if idx % 2 == 0:
                    print(line.strip())

    def read_emails(self):
        """
        Read and validate email addresses of users.
        """
        valid_emails = []
        with open(self.emails_file_path, "r") as f:
            for line in f:
                email = line.strip()
                if re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    valid_emails.append(email)
        self.valid_emails = valid_emails

    def get_gmail_addresses(self):
        """
        Get Gmail addresses from the list of emails.
        """
        self.gmail_addresses = [email for email in self.valid_emails if email.endswith("@gmail.com")]

    def check_username_in_list(self, username: str):
        """
        Check if a username exists in the list of users.
        """
        if username in self.users:
            print(f"{username} exists in the list of users.")
        else:
            print(f"{username} does not exist in the list of users.")

    def check_email_username(self):
        for email, username in zip(self.valid_emails, self.users):
            if username in email:
                print(f"Username {username} is present in email {email}")
            else:
                print(f"Username {username} is not present in email {email}")





    def count_letter_a_occurrences(self, username: str):
        """
        Count occurrences of the letter 'a' in a username.
        """
        a_count = username.lower().count("a")
        print(f"The letter 'a' appears {a_count} times in the username.")

    def capitalize_all_users(self):
        """
        Capitalize all usernames in the list.
        """
        for username in self.users:
            if username[0].isupper():
                print(f"{username} begin with upper")
            else:
                print(f"{username} dont begin with upper")



    def calculate_payment(self, customer_numbers: List[int]):
        """
        Calculate total payment for a group of customers based on the specified payment rules.
        """
        total_payment = 0
        for num in customer_numbers:
           save = num % 8
           x = num//8
           total_payment += save*50+x*200
        return total_payment

# Example usage:
if __name__ == '__main__':
    manager = UsersManager()
    manager.create_missing_file()
    manager.read_users_into_array()
    manager.get_first_10_percent_users()
    manager.process_even_rows()
    manager.read_emails()
    manager.get_gmail_addresses()
    manager.check_email_username()
    manager.check_username_in_list("John")
    manager.count_letter_a_occurrences("John")
    manager.capitalize_all_users()
    total_payment = manager.calculate_payment([9, 5])
    print("Total payment:", total_payment)