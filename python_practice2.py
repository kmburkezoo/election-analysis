# counties = ["Arapahoe", "Denver", "Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])


# temperature = int(input("What is the temperature outside? "))

# if temperature > 80:
#     print("Turn on the AC.")
# else:
#     print("Open the windows.")

# What is the score?
# score = int(input("What is your test score?"))

# # Determine the grade
# if score >= 90:
#     print('Your grade is an A')
# elif score >= 80:
#     print('Your grade is a B')
# elif score >= 70:
#     print('Your grade is a C')
# elif score >= 60:
#     print('Your grade is a D')
# else:
#     print('Your grade is an F')

# counties = ["Arapahoe", "Denver", "Jefferson"]
# if "Arapahoe" in counties or "El Paso" in counties:
#     print("Arapahoe or El Paso is in the list of counties")
# else:
#     print("Arapahoe or El Paso is not in the list of counties")

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county, voters in counties_dict:
#     print(f'{county} county has {voters}voters')

# for county in counties_dict:
#     print(county)

# for voters in counties_dict.values():
#     print(voters)

# for county, voters in counties_dict.items():
#     print(f'{county} county has {voters} voters')

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict)

# for i in range(len(voting_data)):
#       print(voting_data[i]['county'])

# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)

# for county_dict in voting_data:
#     print(county_dict['county'])

# for county_dict in voting_data:
#     for key, value in county_dict.items():
#         print(value)

# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes:,}. "
#     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

# print(message_to_candidate)

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county, voters in counties_dict.items():
#     print(
#         f'{county} county has {voters:,} voters'
    # )

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
        print(
            f'{county_dict["county"]} county has {county_dict["registered_voters"]:,} voters'
        )

# for county_dict in voting_data:
#     print(county_dict)