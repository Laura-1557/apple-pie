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

    def add_to_shop():
        need_ingredient = input("Do you want to add this item to your shopping list for next time anyway? ")
        if need_ingredient in affirmative_answer:
            with open('Shopping_List.txt', 'r') as todo_file:
                todo = todo_file.read()
            todo = todo + ingredient_name + "\n"
            with open('Shopping_List.txt', "w+") as todo_file:
                todo_file.write(todo)
                print("Ok, added to Shopping List")

    ingredient_name = input("Which ingredients do you have? ")

    if ingredient_name not in ingredients:
        have_ingredient = input("Maybe we could use that. Do you want to add this to the recipe? Yes/No ")
        if have_ingredient in affirmative_answer:
            ingredients.append(ingredient_name)
            with open('Ingredients_in_stock.txt', 'r') as todo_file:
                todo = todo_file.read()
            todo = todo + ingredient_name + "\n"
            with open('Ingredients_in_stock.txt', "w+") as todo_file:
                todo_file.write(todo)
            see_ingredient_list = input("Do you want to see your list? ")
            if see_ingredient_list in affirmative_answer:
                    print(ingredients)
            main()

        else:
            add_to_shop()
            main()
    else:
        print(f"Great, {ingredient_name}! Let's add that to the list of things we have.")
        with open('Ingredients_in_stock.txt', 'r') as todo_file:
            todo = todo_file.read()
        todo = todo + ingredient_name + "\n"
        with open('Ingredients_in_stock.txt', "w+") as todo_file:
            todo_file.write(todo)
        add_to_shop()
        main()


if __name__ == "__main__":
    main()
