import faster_than_requests as requests
import bs4 as parser

error = "Une erreur a été rencontrée, contactez un Admin ou un Modérateur"
a = ['Score :', 'Excercices résolus :', 'Problèmes résolus :', 'Combinatoire :', 'Géométrie :', 'Théorie des nombres :',
     'Algèbre :', 'Équations Fonctionnelles :', 'Inégalités :']


class User:
    def __init__(self, user: int, url="https://www.mathraining.be"):
        self.url = url
        self.user = user
        self.content = self.__fetch_info()
        self.admin = self.is_admin()

    def page(self):
        return self.content.prettify()

    def score(self):
        a = self.content.find_all('p', attrs={"style": u"font-size:24px; margin-top:20px;"})
        if a:
            a = str(a[0])
            return int(a[51:-4])
        else:
            if self.admin:
                return float("infinity")
            else:
                return 0

    def is_admin(self):
        return self.content.find_all('span', attrs={"style": u"margin-left:30px; color:black;"}) != []

    def progressions(self):
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

    def info(self):
        score = self.score()
        progressions = self.progressions()
        if score == 0:
            return {"error": error}
        if score == float('infinity'):
            return {"error": error}
        response = {}
        l1 = progressions[0]
        l2 = progressions[1]
        response[a[0]] = score
        i = 1
        for s in l1:
            response[a[i]] = s
            i += 1
        for d in l2:
            response[a[i]] = d
            i += 1
        return response

    def __fetch_info(self):
        urls = self.url + "/users/" + str(self.user)
        data = requests.get2str(urls)
        return parser.BeautifulSoup(data, "lxml")

    @staticmethod
    def __progression_to_number(s: str):
        s = str(s)
        a = s.splitlines()[1][30:-7]
        return a if a != '' else '0%'
