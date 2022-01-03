affirmative_answer = ["yes", "Yes", "yeah", "Yeah"]
ingredients = [
        "apple",
        "apples",
        "apple sauce",
        "pastry",
        "pastries",
        "cases",
    ]


def main():

    ingredient_name = input("Which ingredients do you have? ")

    if ingredient_name not in ingredients:
        have_ingredient = input("Maybe we could use that for something else. Do you want to add this to the list of "
                                "ingredients you have? Yes/No ")
        if have_ingredient in affirmative_answer:
            ingredients.append(ingredient_name)
            print(ingredients)
            main()

        else:
            print("Ok.")
            main()
    else:
        print(f"Great, {ingredient_name}! Let's add that to the list of things we have.")
        with open('To_do.txt', 'r') as todo_file:
            todo = todo_file.read()
        todo = todo + ingredient_name
        with open('To_do.txt', "w+") as todo_file:
            todo_file.write(todo)
        main()


if __name__ == "__main__":
    main()

