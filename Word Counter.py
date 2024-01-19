def word_count(sentence):
    """
    Function to count the number of words in a given sentence.

    Parameters:
    - sentence (str): The input sentence.

    Returns:
    - int: The count of words.
    """
    # Initialize a counter
    count = 0

    # Split the sentence into words using whitespace as the delimiter
    words = sentence.split()

    # Iterate through each word and increment the counter
    for word in words:
        count += 1

    # Return the count of words
    return count

def main():
    """
    Main function to execute the Word Counter program.
    """
    try:
        # Prompt user for input
        user_input = input("Enter a sentence or paragraph: ")

        # Check for empty input
        if not user_input.strip():
            raise ValueError("Error: Input is empty. Please enter a valid sentence or paragraph.")

        # Count words
        count = word_count(user_input)

        # Display the entered sentence or paragraph
        print(f"\nYou entered: {user_input}")

        # Display the word count
        print(f"Word Count: {count}")

    except ValueError as ve:
        # Handle empty input error
        print(ve)

if __name__ == "__main__":
    # Execute the main function
    main()
