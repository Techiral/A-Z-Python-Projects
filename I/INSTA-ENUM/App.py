from ensta import Guest
from ensta import Host
import sys
import json
import argparse

def fetch_profile_by_username(username):
    guest = Guest()
    profile = guest.profile(username)
    profile_data=profile.raw
    print("UserName :" , profile_data['username'])
    print("Full Name :" , profile_data['full_name'])
    print("BIO :" , profile_data['biography'],end='\n')
    print("ID (User ID) :" , profile_data['id'])
    print("PIC URL :" , profile_data['profile_pic_url'])
    print("PIC URL HD :" , profile_data['profile_pic_url_hd'])
    print("UserName :" , profile_data['username'])
    print("FB ID :" , profile_data['fbid'])
    print("Count of Followers :" , profile_data['edge_followed_by']['count'])
    print("Count of Following :" , profile_data['edge_follow']['count'])
    print("Post Count :" , profile_data['edge_owner_to_timeline_media']['count'])
    profile_data_json = json.dumps(profile_data)
    profile_output=open(f'{username}.txt','+w')
    profile_output.write(profile_data_json)
    profile_output.close()



def fetch_profile_by_userid(userid):
    guest = Guest()
    real_username=guest.get_username(userid)
    fetch_profile_by_username(real_username)

def main():
    parser = argparse.ArgumentParser(description="Fetch Instagram user profiles")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-r", action="store_true", help="Fetch profile by username")
    group.add_argument("-d", action="store_true", help="Fetch profile by user ID")
    
    parser.add_argument("-u", "--username", help="Instagram username")
    parser.add_argument("-i", "--userid", help="Instagram user ID")
    
    args = parser.parse_args()

    if args.r:
        if args.username:
            fetch_profile_by_username(args.username)
            
        else:
            print("Username is required when using -r option.")
            return
    else:
        if args.userid:
            fetch_profile_by_userid(args.userid)
        else:
            print("User ID is required when using -d option.")
            return

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
