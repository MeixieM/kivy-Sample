from kivy.lang import Builder
from kivymd.app import MDApp
import sqlite3


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        # Create DB
        conn = sqlite3.connect('first_db.db')

        # Create cursor
        c = conn.cursor()

        # Create table
        c.execute("""CREATE TABLE IF NOT EXISTS customers(
                first_name text
            )
        """)

        # Commit changes
        conn.commit()

        # Close connection
        conn.close()

        return Builder.load_file('main.kv')

    def submit(self):
        # Create DB
        conn = sqlite3.connect('first_db.db')

        # Create cursor
        c = conn.cursor()

        # Add record
        c.execute("INSERT INTO customers VALUES (:first_name)",
                  {
                      'first_name': self.root.ids.word_input.text,
                  })

        # Add message
        self.root.ids.word_label.text = f'{self.root.ids.word_input.text} added to the database'

        # Clear input box
        self.root.ids.word_input.text = ''

        # Commit changes
        conn.commit()

        # Close connection
        conn.close()

    def show_records(self):
        # Create DB
        conn = sqlite3.connect('first_db.db')

        # Create cursor
        c = conn.cursor()

        # Fetch records
        c.execute("SELECT * FROM customers")
        records = c.fetchall()

        word = ''
        for record in records:
            word += f'\n{record[0]}'  # Concatenate records

        self.root.ids.word_label.text = word  # Update label outside the loop

        # Commit changes
        conn.commit()

        # Close connection
        conn.close()


MainApp().run()
