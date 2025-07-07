class DataRedundancyRemovalSystem:
    def __init__(self):
        self.database = set()

    def validate_data(self, new_entry):
        if new_entry in self.database:
            return 'redundant'
        else:
            return 'unique'

    def add_data(self, new_entry):
        status = self.validate_data(new_entry)
        if status == 'unique':
            self.database.add(new_entry)
            print(f"✅ '{new_entry}' added successfully.")
        else:
            print(f"⚠️ '{new_entry}' is redundant and was not added.")
        return status

    def display_database(self):
        print("\n📦 Current Unique Entries in Database:")
        for item in sorted(self.database):
            print(f"- {item}")
        print(f"Total Unique Entries: {len(self.database)}")


if __name__ == "__main__":
    system = DataRedundancyRemovalSystem()
    
    print("👋 Welcome to the Interactive Data Redundancy Removal System!")
    print("👉 Type your data entries one by one.")
    print("👉 Type 'show' to display current database.")
    print("👉 Type 'exit' to quit.\n")
    
    while True:
        user_input = input("Enter data (or 'show' / 'exit'): ").strip().lower()
        
        if user_input == 'exit':
            print("\n👋 Exiting the system. Goodbye!")
            break
        elif user_input == 'show':
            system.display_database()
        elif user_input == '':
            print("⚠️ Please enter some data!")
        else:
            system.add_data(user_input)
