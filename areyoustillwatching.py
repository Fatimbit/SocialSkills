import instaloader


username = input("Hey! First we need to log into an Instagram account. You can use your existing one or make a new account really quick, I'll wait. :) Just a heads-up, but if the account you're looking into is a private account you have to be following them from the account you signed in with. Once you're ready, what's your username? ")
password = input("So I'm gonna need the password for this too brotha: ")
mysteryprofile = input("Whose profile are we checking? Tell us the @!! ")
print("Okay! Here's the info for @"+mysteryprofile)

insta = instaloader.Instaloader()
insta.login(username, password) 
profile = instaloader.Profile.from_username(insta.context, mysteryprofile)
followers = profile.get_followers()
following = profile.get_followees()
nofollowback = list(set(following) - set(followers))

 
print("Here's all the people "+mysteryprofile+" is following that don't follow " +mysteryprofile+" back...")
for account in nofollowback:
    print(account)

print("That's a total of "+str(len(nofollowback))+" accounts.")

