# Formats the written documents like HTML does

# Step 3: Define a function with a temporary function as paramter; give
# whatever name you like.


def add_html_formatting(tempFunction):
    # Step 4: Define another function with the same paramter to wrap the
    # defined function at step 1.
    def wrap_html_formatting(article):
        # Step 6: Add anything before that function to decorate
        print("<article>")
        # Step 7: Call the function defined at step 1 with same parameter
        tempFunction(article)
        # Step 7: Add anything after that function to decorate
        print("</article>")

    # Step 8: Return the wrapper function without parameter
    return wrap_html_formatting


@add_html_formatting
# Step 1: Define a function normally.
def html_formatting(article):
    print(article)


# Step 2: Call that function to test
html_formatting("My name is Arjun Adhikari")
