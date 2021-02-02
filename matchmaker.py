import csv
import itertools

number_of_matches = 5
people_per_file = 20


def get_match_score(person1, person2, match_list):
    match_score = 0
    for answer1, answer2 in zip(person1[4:], person2[4:]):
        if answer1 == answer2:
            match_score += 1

    if len(match_list) == number_of_matches:
        if match_list[-1][0] >= match_score:
            return
    return [match_score, person2[2], person2[3]]


lst_responses = []
with open('Match-Maker 2021.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    for row in csv_reader:
        lst_responses.append(row)

# all_best_matches = {}
all_best_matches = []
for person1 in lst_responses:
    best_matches = []

    for person2 in lst_responses:
        if person1 == person2:
            continue

        best_matches.sort(reverse=True)
        match_score = get_match_score(person1, person2, best_matches)

        if len(best_matches) < number_of_matches:
            best_matches.append(match_score)
        elif match_score:
            best_matches[-1] = match_score

    best_matches.sort(reverse=True)

    first_name = person1[2].split(' ')[0]
    email_response = f'\nHi {first_name},\n\n'
    email_response += "Your best matches are:\n\n"
    for match in best_matches:
        email_response += f"  --> {round(match[0]/11*100)}%, {match[1]}, {match[2]}\n\n"

    email_response += "\nThank you for participating in Match-Maker 2021,\n\nJMSS Programming Club and Student Council\n"

    all_best_matches.append((person1[2], f"\n{person1[1]}\n", email_response))

for i in itertools.count(start=1):
    try:
        all_best_matches[(i-1)*people_per_file]
        with open(f'matches{i}.csv', 'w') as csv_matches:
            csv_writer = csv.writer(csv_matches)
            for row in all_best_matches[(i-1)*people_per_file:i*people_per_file]:
                csv_writer.writerow(row)

    except IndexError:
        break