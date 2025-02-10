import os

def get_size(path):
    """Recursively calculate the total size of files in a directory."""
    total_size = 0
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                total_size += os.path.getsize(file_path)
    else:
        total_size = os.path.getsize(path)
    return total_size

def scan_directory(directory):
    """Scan the directory and print the size of each file and folder in descending order."""
    file_sizes = []
    folder_sizes = {}
    
    # Traverse the directory and collect file sizes
    print(f"Scanning directory: {directory}")
    for root, dirs, files in os.walk(directory):
        # Skip hidden directories (optional)
        if '.git' in root:
            continue
        
        # Add file size data to the list
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            file_sizes.append((file_path, file_size))

        # Calculate the total size of each directory
        folder_size = get_size(root)
        folder_sizes[root] = folder_size

    # Sort the files and directories by size in descending order
    file_sizes.sort(key=lambda x: x[1], reverse=True)
    sorted_folders = sorted(folder_sizes.items(), key=lambda x: x[1], reverse=True)

    # Print the sorted file sizes
    print("\nFiles sorted by size (Descending order):")
    for file_path, size in file_sizes:
        print(f"File: {file_path} | Size: {size / (1024 * 1024):.2f} MB")

    # Print the sorted folder sizes
    print("\nFolders sorted by size (Descending order):")
    for folder, size in sorted_folders:
        print(f"Directory: {folder} | Total size: {size / (1024 * 1024):.2f} MB")

if __name__ == "__main__":
    # Provide the path to your folder (where PaddleOCR is located)
    folder_path = "C:\\Users\\HP\\Desktop\\hm\\PaddleOCR"
    
    if os.path.exists(folder_path):
        scan_directory(folder_path)
    else:
        print("The specified folder does not exist.")
