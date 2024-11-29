# Import the required module for Instagram
import instaloader

def download_profile_pic():
    # Step 1: Create an Instagram loader
    loader = instaloader.Instaloader()
    
    # Step 2: Ask user for the Instagram username
    username = input("Enter Instagram username: ")
    
    try:
        # Step 3: Get the profile information
        profile = instaloader.Profile.from_username(loader.context, username)
        
        # Step 4: Download the profile picture
        loader.download_profilepic(profile)
        
        # Step 5: Show success message
        print(f"Success! Profile picture downloaded for {username}")
        print("Check the current folder for the downloaded image")
        
    except:
        # If anything goes wrong, show this message
        print("Oops! Something went wrong. Please check:")
        print("1. The username is correct")
        print("2. Your internet connection is working")
        print("3. The profile is public")

# Run the program
if __name__ == "__main__":
    download_profile_pic()