
class Player:

    def __init__(self, eachplayer):
        # recibe un diccionario
        self.name = eachplayer['name']
        self.age = eachplayer['age']
        self.position = eachplayer['position']
        self.team = eachplayer['team']

    # recibe una lista de diccionarios
    @classmethod
    def get_team(cls, team_list):
        new_team = []
        for i in team_list:
            player = Player(i)
            new_team.append(player)
        return new_team

    def printplayer(self):
        print(self.name)
        print(self.age)
        print(self.position)
        print(self.team)

    def print_new_team(new_team_list):
        for player in new_team_list:
            player.printplayer()

# 2 crear el objeto


kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets"
}
player_kevin = Player(kevin)
player_kevin.printplayer()

jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "small forward",
    "team": "Boston Celtics"
}
player_jason = Player(jason)
player_jason.printplayer()
kyrie = {
    "name": "Kyrie Irving",
    "age": 32,
    "position": "Point Guard",
    "team": "Brooklyn Nets"
}
player_kyrie = Player(kyrie)
player_kyrie.printplayer()


# cpnvertir los dicionarios en players

players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Foward",
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]
print("--------------------")
object_list= Player.get_team(players)
Player.print_new_team(object_list)

