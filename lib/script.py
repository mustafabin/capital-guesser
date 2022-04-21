from capitals import states
import random
random.shuffle(states)
tally = {
    "correct": 0,
    "incorrect": 0
}


def convertSorted(sortedArr):
    result = []
    for i in sortedArr:
        result.append({"name": i[0], "capital": i[1]["capital"]})
    return result


name_dict = {}
for state in states:
    name_dict.setdefault(
        state["name"], {"val": 0, "capital": state["capital"]})
gameOver = None
while not gameOver:
    print("Greetings! How well do you know the geography of the United States?")
    for state in states:
        if input("Enter h for hint : ") == "h":
            print(state["capital"][0:3])
        guess = input("Guess the Capital for "+state["name"] + " : ")
        if guess == state["capital"]:
            tally["correct"] += 1
            print("Correct ")
        else:
            name_dict[state["name"]]["val"] += 1
            tally["incorrect"] += 1
            print("Incorrect  the word was : " + state["capital"])
    print(tally)
    tally["correct"] = 0
    tally["incorrect"] = 0
    gameOver = input(
        "Press enter to continue; Enter any other key to leave : ")
    sorted_arr = sorted(name_dict.items(),
                        key=lambda val: val[1]["val"], reverse=True)

    states = convertSorted(sorted_arr)

print("Thank you for playing my game! Goodbye!")

# Montgomery
