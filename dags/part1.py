import luigi

substitutions = {
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

def get_input_file():
    return "/usr/local/luigi/datafiles/example1.txt"

# write your task classees here
# when you are done, you can run them using docker exec pytn2018luigi_scheduler_1 python3 dags/part1.py <TaskClassName>
# the visualizer is located at localhost:8082 where you can check on your dag's progress
#
# tip: the output file you write to should be located in /usr/local/luigi
# you can read it using docker exec pytn2018luigi_scheduler_1 cat <your_output_file>


if __name__ == "__main__":
    luigi.run()