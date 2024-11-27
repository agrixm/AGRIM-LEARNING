import instaloader
import os

def download_profile_pic():
    # Create directory if it doesn't exist
    if not os.path.exists('profile_pics'):
        os.makedirs('profile_pics')
        
    # Create an Instaloader instance with target directory
    loader = instaloader.Instaloader(dirname_pattern='profile_pics')
    try:
        # Get the Instagram username or profile URL from user
        profile_input = input("Enter Instagram username or profile URL: ")
        
        # Extract username from URL if URL is provided
        username = profile_input.split('/')[-1].split('?')[0] if 'instagram.com' in profile_input else profile_input
        
        # Get profile data
        profile = instaloader.Profile.from_username(loader.context, username)
        
        # Download the profile picture (fixed method)
        loader.download_profilepic(profile)
        print(f"Profile picture downloaded successfully for {username}!")
        print(f"Check the 'profile_pics' folder")
        
    except instaloader.exceptions.ProfileNotExistsException:
        print("The profile does not exist.")
    except instaloader.exceptions.ConnectionException:
        print("Failed to connect to Instagram. Please check your internet connection.")
    except instaloader.exceptions.BadCredentialsException:
        print("Invalid credentials. Please check your login details.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    download_profile_pic()