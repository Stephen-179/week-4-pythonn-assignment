def modify_file_content(original_file):
    try:
        with open(original_file, 'r') as file:
            content = file.read()

        modified_content = content.upper()
        new_file = f"modified_{original_file}"

        with open(new_file, 'w') as file:
            file.write(modified_content)

        print(f"✅ Modified content written to '{new_file}' successfully!")

    except FileNotFoundError:
        print("❌ Error: The file was not found.")
    except PermissionError:
        print("❌ Error: Permission denied while accessing the file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Include the file directly here:
filename = "file-handling.txt"
modify_file_content(filename)
