import faster_than_requests as requests
import bs4 as parser

error = "Une erreur a été rencontrée, contactez un Admin ou un Modérateur"
field_names = ['name', 'Score :', 'Excercices résolus :', 'Problèmes résolus :', 'Combinatoire :', 'Géométrie :',
               'Théorie des nombres :', 'Algèbre :', 'Équations Fonctionnelles :', 'Inégalités :']


class User:
    def __init__(self, user: int, url="https://www.mathraining.be"):
        self.url = url
        self.user = user
        self.content = self.__fetch_info()
        self.admin = self.is_admin()

    def score(self) -> int:
        a = self.content.find_all('p', attrs={"style": u"font-size:24px; margin-top:20px;"})
        if a:
            a = str(a[0])
            return int(a[51:-4])
        else:
            if self.admin:
                return float("infinity")
            else:
                return 0

    def is_admin(self) -> bool:
        return self.content.find_all('span', attrs={"style": u"margin-left:30px; color:black;"}) != []

    def progressions(self) -> list[int]:
        progressions = self.content.find_all('div', attrs={"class": "progress-bar", "role": "progressbar"})
        progressions_by_type = []
        progressions_by_section = []
        if self.admin:
            return ["Administrator"]
        if progressions:
            for i in range(2):
                progressions_by_type.append(self.__progression_to_number(progressions[i]))
            for i in range(2, len(progressions)):
                progressions_by_section.append(self.__progression_to_number(progressions[i]))
        else:
            return [0]
        return [progressions_by_type, progressions_by_section]

    def name(self) -> str:
        a = self.content.find('h1')
        return " ".join(a.text.splitlines())

    def info(self) -> dict:
        score = self.score()
        progressions = self.progressions()
        if score == 0:
            return {"error": "Utilisateur à 0 points"}
        if score == float('infinity'):
            return {"error": "Cet utilisateur est un Administrateur"}
        name = self.name()
        response = {field_names[0]: name, field_names[1]: score}
        i = 2
        for s in progressions[0]:
            response[field_names[i]] = s
            i += 1
        for d in progressions[1]:
            response[field_names[i]] = d
            i += 1
        return response

    def solved(self, problem: int) -> bool:
        try:
            return self.content.text.__contains__("Problème #" + str(problem))
        except:
            return False

    def __fetch_info(self) -> parser.BeautifulSoup:
        urls = self.url + "/users/" + str(self.user)
        data = requests.get2str(urls)
        return parser.BeautifulSoup(data, "lxml")

    @staticmethod
    def __progression_to_number(s: str) -> int:
        s = str(s)
        a = s.splitlines()[1][30:-7]
        return a if a != '' else '0%'
