import os

# Directory structure to be created
directory_structure = {
    'BankingApp': [
        'app.py',
        'database.db',
        'models.py',
        'user_interface.py',
        'utils.py',
        'README.md',
        'requirements.txt',
        'assets/'
    ]
}

def create_project_structure(structure):
    for root_folder, files in structure.items():
        # Create the root directory (BankingApp)
        if not os.path.exists(root_folder):
            os.mkdir(root_folder)
        # Create files and subdirectories
        for file in files:
            file_path = os.path.join(root_folder, file)
            if file.endswith('/'):  # If it's a directory
                os.mkdir(file_path)
            else:  # If it's a file
                with open(file_path, 'w') as f:
                    f.write('')  # Create empty file

# Create the directory structure
create_project_structure(directory_structure)

# List the created structure to confirm
os.listdir('BankingApp')
