import random
import string
import streamlit as st
from supabase import create_client, Client

class Bank:
    # Initialize Supabase Client
    # Expects st.secrets["SUPABASE_URL"] and st.secrets["SUPABASE_KEY"]
    
    @staticmethod
    def _get_client() -> Client:
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_KEY"]
        return create_client(url, key)

    @classmethod
    def generate_account_number(cls):
        chars = random.choices(string.ascii_letters, k=3) + \
                random.choices(string.digits, k=3) + \
                random.choices("!@#$%^&*", k=1)
        random.shuffle(chars)
        return ''.join(chars)

    @classmethod
    def create_account(cls, name, age, email, pin):
        if age < 18 or len(str(pin)) != 4:
            return None, "Age must be 18+ and PIN should be 4 digits"
        
        acc_no = cls.generate_account_number()
        user_data = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "account_number": acc_no,
            "balance": 0
        }

        try:
            supabase = cls._get_client()
            response = supabase.table("users").insert(user_data).execute()
            # Check if insertion was successful (response.data should not be empty)
            if response.data:
                 return {"accountNo.": acc_no}, "Account created successfully" # Returning dict with key expected by app.py
            else:
                 return None, "Failed to create account (No data returned)"

        except Exception as e:
            return None, f"Error creating account: {str(e)}"

    # Placeholder/Legacy methods - needing update for full DB support
    @classmethod
    def find_user(cls, acc_no, pin):
        # TODO: Update to fetch from Supabase
        pass

    @classmethod
    def deposit(cls, acc_no, pin, amount):
         # TODO: Update to update Supabase
        pass

    @classmethod
    def withdraw(cls, acc_no, pin, amount):
         # TODO: Update to update Supabase
        pass

    @classmethod
    def update_user(cls, acc_no, pin, name=None, email=None, new_pin=None):
         # TODO: Update to update Supabase
        pass

    @classmethod
    def delete_user(cls, acc_no, pin):
         # TODO: Update to delete from Supabase
        pass

