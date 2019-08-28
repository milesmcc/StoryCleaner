import clean

articles = []

def give_prompt():
    print("----------")
    print("Currently stored: %s\nPlease enter each article below, followed by 'end'. Enter 'stop' when finished.\n" % len(articles))

recent_inputs = []

give_prompt()
while True:
    text_input = input("> ") + "\n"
    if text_input.lower() == "save\n":
        with open("output.txt", "w") as outfile:
            for i in range(len(articles)):
                outfile.write("ARTICLE %s of %s -- Ordering: ___ / %s\n\n" % (i, len(articles), len(articles)))
                outfile.write(articles[i])
                outfile.write("\n----------\n\n")
        break
    if text_input.lower() == "end\n":
        article = "".join(recent_inputs)
        cleaned = clean.clean_text(article)
        print(cleaned)
        articles.append(cleaned)
        recent_inputs = []
        give_prompt()
    else:
        recent_inputs.append(text_input)
