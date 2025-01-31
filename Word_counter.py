def count_words(text):
    """
    Count the number of words in the given text.
    
    Parameters:
    text (str): The text from where you want to count words.
    
    Returns:
    int: The number of words in the text.
    """
    # Use whitespace to split the text into words
    words = text.split()
    return len(words)

def main():
    print("Welcome to the Word Count Program!")
    # Word Count Program for Beginners
    while True:
        try:
            # Get user input
            user_input = input("Please enter the text you want to count words for (or type 'exit' to quit): ")
            
            # Exit Condition for User
            if user_input.lower() == 'exit':
                print("Thank you for using the Word Count Program. Goodbye!")
                break
            
            # Count the words in the input text
            word_count = count_words(user_input)
            
            # Display the result
            print(f"The number of words in the given text is: {word_count}")
        
        except Exception as e:
            # Handle any unexpected errors
            print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    main()
