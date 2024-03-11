from tkinter import Tk, filedialog
from PIL import Image
import numpy as np

def select_file(message):
    print(message)
    root = Tk()
    root.withdraw() # Hide the main window
    file_path = filedialog.askopenfilename()
    return file_path

def select_folder(message):
    print(message)
    root = Tk()
    root.withdraw() # Hide the main window
    folder_path = filedialog.askdirectory()
    return folder_path

def add_operation(image_array, key):
    # Add key to each pixel value
    return (image_array + key) % 256

def sub_operation(image_array, key):
    # Subtract key from each pixel value
    return (image_array - key) % 256

def div_operation(image_array, key):
    # Divide each pixel value by (key + 1)
    return ((image_array / (key + 1)).astype(int)) % 256

def encrypt_image(image_path, output_folder, key, operation):
    # Open the image
    img = Image.open(image_path)
    
    # Convert the image to numpy array for easier manipulation
    img_array = np.array(img)
    
    # Apply the selected operation
    if operation == 'add':
        encrypted_img_array = add_operation(img_array, key)
    elif operation == 'sub':
        encrypted_img_array = sub_operation(img_array, key)
    elif operation == 'div':
        encrypted_img_array = div_operation(img_array, key)
    elif operation == 'swap':
        encrypted_img_array = np.flipud(img_array)
    
    # Convert the manipulated numpy array back to an image
    encrypted_img = Image.fromarray(encrypted_img_array.astype('uint8'), img.mode)
    
    # Save the encrypted image
    encrypted_img_path = output_folder + "/encrypted_image.png"
    encrypted_img.save(encrypted_img_path)
    print("Image encrypted successfully!")
    
    return encrypted_img_path

def decrypt_image(encrypted_image_path, output_folder, key, operation):
    # Open the encrypted image
    encrypted_img = Image.open(encrypted_image_path)
    
    # Convert the encrypted image to numpy array for easier manipulation
    encrypted_img_array = np.array(encrypted_img)
    
    # Apply the reverse operation
    if operation == 'add':
        decrypted_img_array = sub_operation(encrypted_img_array, key)
    elif operation == 'sub':
        decrypted_img_array = add_operation(encrypted_img_array, key)
    elif operation == 'div':
        decrypted_img_array = (encrypted_img_array * (key + 1)).astype(int) % 256
    elif operation == 'swap':
        decrypted_img_array = np.flipud(encrypted_img_array)
    
    # Convert the manipulated numpy array back to an image
    decrypted_img = Image.fromarray(decrypted_img_array.astype('uint8'), encrypted_img.mode)
    
    # Save the decrypted image
    decrypted_img_path = output_folder + "/decrypted_image.png"
    decrypted_img.save(decrypted_img_path)
    print("Image decrypted successfully!")
    
    return decrypted_img_path

# Allow users to encrypt or decrypt an image with basic mathematical operations
def main():
    print("Welcome to Image Encryption Tool")
    while True:
        print("\nMenu:")
        print("1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            input_file = select_file("Please select the input image file:")
            if not input_file:
                print("No input file selected.")
                continue
            output_folder = select_folder("Please select the folder to save the encrypted image:")
            if not output_folder:
                print("No output folder selected.")
                continue
            try:
                key = int(input("Enter encryption key (an integer): "))
                operation = input("Enter encryption method ('add', 'sub', 'div', 'swap'): ").lower()
                encrypted_image_path = encrypt_image(input_file, output_folder, key, operation)
                print(f"Image encrypted successfully and saved as {encrypted_image_path}")
            except Exception as e:
                print("Error:", str(e))
        elif choice == '2':
            input_file = select_file("Please select the encrypted image file:")
            if not input_file:
                print("No input file selected.")
                continue
            output_folder = select_folder("Please select the folder to save the decrypted image:")
            if not output_folder:
                print("No output folder selected.")
                continue
            try:
                key = int(input("Enter decryption key (an integer): "))
                operation = input("Enter decryption method ('add', 'sub', 'div', 'swap'): ").lower()
                decrypted_image_path = decrypt_image(input_file, output_folder, key, operation)
                print(f"Image decrypted successfully and saved as {decrypted_image_path}")
            except Exception as e:
                print("Error:", str(e))
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2/3).")

if __name__ == "__main__":
    main()
