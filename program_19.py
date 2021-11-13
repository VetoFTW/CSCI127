# Name: Martin Czarnecki
# Email: martin.czarnecki99@myhunter.cuny.edu
# Date: September 26, 2021

userFollowers = int(input("Enter amount of social media followers: "))
influenceTier = ""

if userFollowers < 0:
    influenceTier = "Error"
elif userFollowers < 1000:
    influenceTier = "Hyper Influencer"
elif userFollowers < 10000:
    influenceTier = "Nano Influencer"
elif userFollowers < 100000:
    influenceTier = "Micro Influencer"
elif userFollowers < 500000:
    influenceTier = "Mid-Tier Influencer"
elif userFollowers < 1000000:
    influenceTier = "Macro-Influencer"
else:
    influenceTier = "Celebrity Influencer"

print("Your influencer tier is:", influenceTier)