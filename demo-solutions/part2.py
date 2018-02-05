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


class ArticleText(luigi.ExternalTask):
    def output(self):
        return luigi.LocalTarget("/p1/example.txt")


class SubstitutionTask(luigi.Task):

    subs = luigi.DictParameter(default=substitutions)

    def requires(self):
        return ArticleText()

    def run(self):
        with self.input().open('r') as infile, self.output().open('w') as outfile:
            text = infile.read()
            for key, val in self.subs.items():
                text.replace(key, val)
            outfile.write(text)

    def output(self):
        return luigi.LocalTarget("/p1/subbed.txt")

if __name__ == '__main__':
    luigi.run()
