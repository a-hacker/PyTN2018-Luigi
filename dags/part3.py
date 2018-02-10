import luigi

substitutions1 = {
    "witnesses": "these dudes I know",
    "allegedly": "kinda probably",
    "new study": "tumblr post",
    "rebuild": "avenge",
    "space": "spaaace",
    "google glass": "virtual boy",
    "smartphone": "pokedex",
    "electric": "atomic",
    "senator": "elf-lord",
    "car": "cat",
    "election": "eating contest",
    "congressional leaders": "river spirits",
    "homeland security": "homestar runner",
    "could not be reached for comment": "is guilty and everyone knows it"
}

substitutions2 = {
    "witnesses": "these dudes I know",
    "allegedly": "kinda probably",
    "new study": "tumblr post",
    "rebuild": "avenge",
    "space": "spaaace",
    "google glass": "virtual boy",
    "smartphone": "pokedex",
    "electric": "atomic",
    "senator": "elf-lord",
    "car": "cat",
    "election": "eating contest",
    "congressional leaders": "river spirits",
    "homeland security": "homestar runner",
    "could not be reached for comment": "is guilty and everyone knows it"
}


def get_input_files():
    return ["/usr/local/luigi/datafiles/example{i}.txt".format(i) for i in range(1, 3)]


if __name__ == "__main__":
    luigi.run()