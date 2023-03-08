import requests
import hashlib
import os
import subprocess

def main():

    # Get the expected SHA-256 hash value of the VLC installer
    expected_sha256 = get_expected_sha256()
    # Send GET message to download the file
    file_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe.sha256'
    resp_msg = requests.get(file_url)
    # Check whether the download was successful
    if resp_msg.status_code == requests.codes.ok:
    # Extract binary file content from response message body
        file_content = resp_msg.content
        # Calculate SHA-256 hash value
        image_hash = hashlib.sha256(file_content).hexdigest()
        # Print the hash value
        print(image_hash)

    
    
    # Download (but don't save) the VLC installer from the VLC website
    installer_data = download_installer()
    # Send GET message to download the file
    file_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe'
    resp_msg = requests.get(file_url)
    # Check whether the download was successful
    if resp_msg.status_code == requests.codes.ok:
        # Extract binary file content from response message
        file_content = resp_msg.content


    # Verify the integrity of the downloaded VLC installer by comparing the
    # expected and computed SHA-256 hash values
    if installer_ok(installer_data, expected_sha256):
        image_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe.sha256'
        # Send GET request for image
        resp = requests.get(image_url)
        # Check if GET request was successful
        if resp.ok:
            # Extract response message content as bytes object
            image_data = resp.content
            # Calculate SHA-1 hash value
            image_hash = hashlib.sha1(image_data).hexdigest()
            print(image_hash)
                
            # Save the downloaded VLC installer to disk
            installer_path = save_installer(installer_data)
            #Save the binary file to disk
            with open(r'C:\Users\markt\OneDrive\Desktop', 'wb') as file:
                file.write(file_url)

        # Silently run the VLC installer and then delete from disk
        run_installer(installer_path)
        installer_path = r'C:\temp\vlc-3.0.17.4-win64.exe'
        subprocess.run([installer_path, '/L=1033', '/S'])
        os.remove(installer_path)

      
        
def get_expected_sha256():
    return 

def download_installer():
    return

def installer_ok(installer_data, expected_sha256):
    return

def save_installer(installer_data):
    return

def run_installer(installer_path):
    return
    
def delete_installer(installer_path):
    return

if __name__ == '__main__':
    main()