# you will need Shopping_List.txt and Ingredients_in_stock.txt text files to run this programme properly

affirmative_answer = ["yes", "yeah"]
ingredients = [
        "apple",
        "apples",
        "apple sauce",
        "pastry",
        "pastries",
        "cases",
    ]


def main():

    ingredient_name = input("Which ingredients do you have? ").casefold()

    def ask_to_shop():
        need_ingredient = input("Do you want to add this item to your shopping list for next time anyway? ").casefold()
        if need_ingredient in affirmative_answer:
            with open('Shopping_List.txt', 'r') as todo_file:
                todo = todo_file.read()
            todo = todo + ingredient_name.capitalize() + "\n"
            with open('Shopping_List.txt', "w+") as todo_file:
                todo_file.write(todo)
                print("Ok, added to Shopping List")
        else:
            print("Ok.", end=" ")

    def add_to_stock_list():
        with open('Ingredients_in_stock.txt', 'r') as todo_file:
            todo = todo_file.read()
        todo = todo + ingredient_name.capitalize() + "\n"
        with open('Ingredients_in_stock.txt', "w+") as todo_file:
            todo_file.write(todo)

    if ingredient_name not in ingredients:
        have_ingredient = input("Maybe we could use that. Do you want to add this to the recipe? Yes/No ")
        if have_ingredient in affirmative_answer:
            ingredients.append(ingredient_name)
            add_to_stock_list()
            see_ingredient_list = input("Do you want to see your list? ")
            if see_ingredient_list in affirmative_answer:
                print(ingredients)
            ask_to_shop()
            main()

        else:
            print("Ok.", end=" ")
            ask_to_shop()
            main()
    else:
        print(f"Great, {ingredient_name}! Let's add that to the list of recipe ingredients we have in stock.")
        add_to_stock_list()
        ask_to_shop()
        main()


if __name__ == "__main__":
    main()
