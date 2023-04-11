from words import *


def text_gen():
    # Get the number of texts to combine
    num_texts = int(input("How many texts would you like to combine: "))

    # Display the available library of texts
    print("Library: \n"
          "=> ann_of_the_island.txt\n"
          "=> peter_pan.txt\n"
          "=> time-machine.txt\n"
          "=> alice.txt\n")

    # Get the names of the texts to combine
    file_name = input("Enter the file names separated with commas: ").split(",")

    # Check if the number of texts entered matches the required number
    if len(file_name) != num_texts:
        print("Sorry, the total number of texts and given texts are not the same.")
        return

    # Combine the data from the specified texts
    data = "".join([readdata(text) for text in file_name])

    # Get the window size, temperature and number of words for the generated text
    temperature_value = float(input("Enter temperature target: "))
    window_value, word_length = map(int, input(
        "Enter the window size, and number of words to generate (separated by commas): ").split(","))

    # Generate the rule, count the rules and create the generated text
    rule = makerule(data, window_value)
    stats = countrules(rule)
    generated_text = makestring(stats, word_length, temperature_value)

    return generated_text


def main():
    while True:
        new_texts = text_gen()
        print(f"\n{new_texts}\n")
        choice = input("Do you want to repeat the process? 'reply with Y or N'").lower()
        if choice != "y":
            break


if __name__ == '__main__':
    main()
