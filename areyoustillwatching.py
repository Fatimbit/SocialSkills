import instaloader


username = input("Whose profile are we checking? Tell us the @!! ")
password = input("So I'm gonna need the password for this too brotha: ")

print("Okay! Here's the info for @"+username)

insta = instaloader.Instaloader()
insta.login(username, password) 
profile = instaloader.Profile.from_username(insta.context, username)
followers = profile.get_followers()
following = profile.get_followees()
nofollowback = list(set(following) - set(followers))

 
print("Here's all the people "+username+" is following that don't follow " +username+" back...")
for account in nofollowback:
    print(account)

