import bs4 as parser
import faster_than_requests as requests
import random as r


class Mathraining:
    def __init__(self, url="https://mathraining.be"):
        self.url = url
        self.content = self._fetch_infos()

    def fetch_correctors(self, i=10000000000) -> list:
        correctors = self.content.find_all("tr")
        list = {}
        a = len(correctors)
        a = min(a - 1, i)
        for i in range(1, a + 1):
            corrector = self.__extract_corrector(correctors[i])
            list[corrector[0]] = corrector[1]
        return list

    def __extract_corrector(self, corrector: str) -> list:
        s = str(corrector).splitlines()
        line = str(s[1])
        splited_line = line.split(" ")
        name = self.__extract_name(splited_line)
        total_correction = int(s[2][31:-5])
        last_corrections = int(s[3][31:-5])
        return [name, (total_correction, last_corrections)]

    @staticmethod
    def __extract_name(splited_line: list) -> str:
        color = splited_line[2][14:-9]
        if color == "00000":
            name = " ".join(splited_line[4:])
            name = name.replace("font-weight:bold;\">", "").replace("</span></a></td>", "")
        else:
            name = " ".join(splited_line[4:])
            a = name.split(" ")[0].replace("font-weight:bold;\">", "").replace("</span><span", "")
            to_replace = "font-weight:bold;\">" + a + "</span><span style=\"color:#" + color + ";" + " font-weight:bold;\">"
            b = name[len(to_replace) + 1:-16]
            name = a + b
        return name

    def top_correctors(self, number=10, by_last_correction=False) -> dict:
        correctors = self.fetch_correctors(number)
        if by_last_correction:
            correctors = dict(sorted(correctors.items(), key=lambda x: -1 * x[1][1]))
        return correctors

    @staticmethod
    def random_citation() -> list:
        a = requests.get2str("http://math.furman.edu/~mwoodard/www/data.html")
        list = parser.BeautifulSoup(a, "lxml").find_all("p")
        citation = list[r.randint(0, len(list)) - 1]
        a = parser.BeautifulSoup(str(citation), "lxml")
        name = str(a.find_all('b')[0])[3:-10]
        content = str(citation).replace("<p> ", "") \
            .replace("<b>" + str(name) + "<br/> </b>", "") \
            .replace("</p>", "") \
            .replace("<i>", "") \
            .replace("</i>", "") \
            .replace("<b>", "") \
            .replace("<br/>", "") \
            .replace("</b>", "") \
            .replace("<br/>", "")
        return [str(name), str(content)]

    def _fetch_infos(self) -> parser.BeautifulSoup:
        data = requests.get2str(self.url + "/correctors")
        return parser.BeautifulSoup(data, "lxml")
