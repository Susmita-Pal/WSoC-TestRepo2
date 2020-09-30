class sport():

    def __init__(self):
        self.n = 0
        self.n2 = 0

    def disp(self):
        print("\nSports:\n1.Indoor Games\n2.Outdoor Games\n3.Exit")

    def selection(self):
        self.n = int(input("\nSelect a game to get its details: "))
        while self.n > 5 or self.n < 1:
            print("Oops, Invalid Choice!\nEnter an option in b/w(1-5)")
            self.n = int(input("\nSelect a game to get its details: "))

    def temp(self, args):
        print(
            "\n1.Popular heads of " + args.games(self.n) + "\n2.Details of " + args.games(
                self.n) + "\n3.Different formats of " + args.games(self.n))
        self.n2 = int(input("\nSelect one of the subcategory: "))
        if self.n2 == 1:
            print(args.lead(self.n))
        elif self.n2 == 2:
            print(args.properties(self.n))
        elif self.n2 == 3:
            print(args.format(self.n))
        else:
            print("Invalid choice!Exiting...")
            exit(0)


class indoor(sport):

    def format(self, arg):
        switcher = {
            1: "Badminton:\nSingle format",
            2: "Weightlifting:\n1.Squash\n2.Bench Press\n3.Deadlift\n4.Power Clean\n5.Row\n6.Pull-Ups andDip",
            3: "Table Tennnis:\nSingle format",
            4: "Chess:\nSingle format",
            5: "Carrom:\nSingle format"
        }
        return switcher.get(arg)

    def disp(self):
        print("\nIndoor Games: \n1.Badminton\n2.Weightlifting\n3.Table Tennis\n4.Chess\n5.Carrom")

    def properties(self, arg):
        switcher = {
            1: "Badminton Details:\nBadminton is a racquet sport played using racquets to hit a shuttlecock across a "
               "net. Although it may be played with larger teams, the most common forms of the game are \"singles\" ("
               "with one player per side) and \"doubles\" (with two players per side). Badminton is often played as a "
               "casual outdoor activity in a yard or on a beach; formal games are played on a rectangular indoor "
               "court. Points are scored by striking the shuttlecock with the racquet and landing it within the "
               "opposing side's half of the court. ",
            2: "Olympic weightlifting, or Olympic-style weightlifting, often simply referred to as weightlifting, "
               "is a sport in which the athlete attempts a maximum-weight single lift of a barbell loaded with weight "
               "plates.",
            3: "Table tennis, also known as ping-pong and whiff-whaff, is a sport in which two or four players hit a "
               "lightweight ball, also known as the ping-pong ball, back and forth across a table using small "
               "rackets. The game takes place on a hard table divided by a net. Except for the initial serve, "
               "the rules are generally as follows: players must allow a ball played toward them to bounce one time "
               "on their side of the table, and must return it so that it bounces on the opposite side at least once. "
               "A point is scored when a player fails to return the ball within the rules. Play is fast and demands "
               "quick reactions. Spinning the ball alters its trajectory and limits an opponent's options, "
               "giving the hitter a great advantage",
            4: "Chess is a two-player strategy board game played on a checkered board with 64 squares arranged in an "
               "8×8 square grid. Each player begins with 16 pieces: one king, one queen, two rooks, two knights, "
               "two bishops, and eight pawns. Each piece type moves differently, with the most powerful being the "
               "queen and the least powerful the pawn. The objective is to checkmate the opponent's king by placing "
               "it under an inescapable threat of capture.",
            5: "Carrom or Karom is a game that has long been played throughout India and South East Asia but the game "
               "has become increasingly popular throughout much of the rest of the world during the last century. "
               "Players take turns to play. A turn consists of one or more strikes. A player wins by pocketing all of "
               "the pieces of their chosen colour first. However, neither player can win until one or other player "
               "has \"covered the Queen\". To cover the Queen, a player must pocket one of her own pieces immediately "
               "after pocketing the Queen. If the Queen is pocketed but not covered, the Queen is returned to the "
               "board. Both players normally try to cover the Queen in addition to trying to win the game because a "
               "player who wins and also covers the Queen receives bonus points. "
        }
        return switcher.get(arg)

    def games(self, arg):
        switcher = {
            1: "Badminton",
            2: "Weightlifting",
            3: "Table Tennis",
            4: "Chess",
            5: "Carrom"
        }
        return switcher.get(arg)

    def lead(self, arg):
        switcher = {
            1: "Badminton Players:\n1.Men's Singles: (Japan) Kento MOMOTA "
               "\n2.Women's Singles: (Chinese Taipei) Tai TZU Ying"
               "\n3.Men's Doubles:  (Indonesia)Marcus Fernaldi GIDEON & Kevin Sanjaya SUKAMULJO "
               "\n4.Women's Doubles: (China) CHEN Qing Chen & JIA Yi Fan "
               "\n5.Mixed Doubles: (China)  ZHENG Si Wei & HUANG Ya Qiong ",
            2: "Weightlifting player:\nLasha Talakhadze: Georgian super heavyweight Lasha Talakhadze, who capped the "
               "world weightlifting championships by breaking his own world record, totaling 484 kilograms (1,"
               "067 pounds) between the snatch and clean and jerk.r",
            3: "Table Tennis Player:\nFan Zhendong(Chinese: 樊振东; pinyin: Fán Zhèndōng: born 22 January 1997):He is a "
               "Chinese professional table tennis player who is currently ranked world No. 1 for men's singles by the "
               "International Table Tennis Federation (ITTF)",
            4: "Chess Player:\n1.Sven Magnus Øen Carlsen: He is a Norwegian chess grandmaster who is the current World "
               "Chess Champion, World Rapid Chess Champion, and World Blitz Chess Champion. Carlsen first reached the "
               "top of the FIDE world rankings in 2010, and trails only Garry Kasparov in time spent as the highest "
               "rated player in the world.\n2.Viswanathan \"Vishy\" Anand is an Indian chess grandmaster and former "
               "world chess champion. He became the first grandmaster from India in 1988, and is one of the few "
               "players to have surpassed an Elo rating of 2800, a feat he first achieved in 2006. Anand is a "
               "five-time world chess champion",
            5: "Carrom Players: No top player"
        }
        return switcher.get(arg)


class outdoor(sport):
    def properties(self, arg):
        switcher = {
            1: "Tennis Detail:\nThe game of tennis played on a rectangular court with a net running across the "
               "centre. The aim is to hit the ball over the net landing the ball within the margins of the court and "
               "in a way that results in your opponent being unable to return the ball. You win a point every time "
               "your opponent is unable to return the ball within the court.",
            2: "Cricket detail:\nTest cricket is a game that spans over two innings. This means that one team needs "
               "to bowl the other team out twice and score more runs then them to win the match. Another key "
               "difference between test cricket and other forms of cricket is the length of the innings. In test "
               "cricket there is no limit to the innings length. Whereas in one day cricket & Twenty20 cricket there "
               "are a certain amount of overs per innings. The only limits in test cricket is a 5 day length. Before "
               "the game begins an official will toss a coin. The captain who guesses the correct side of the coin "
               "will then choose if they want to bat or field first. One team will then bat while the other will bowl "
               "& field. The aim of the batting team is to score runs while the aim of the fielding team is to bowl "
               "ten people out and close the batting teams’ innings. Although there are eleven people in each team "
               "only ten people need to be bowled out as you cannot have one person batting alone. Batting is done in "
               "pairs",
            3: "Volleyball is a team sport in which two teams of six players are separated by a net. Each team tries "
               "to score points by grounding a ball on the other team's court under organized rules.[1] It has been a "
               "part of the official program of the Summer Olympic Games since Tokyo 1964.",
            4: "Basketball Details:\nTwo teams of five players each try to score by shooting a ball through a hoop "
               "elevated 10 feet above the ground. The game is played on a rectangular floor called the court, "
               "and there is a hoop at each end. The court is divided into two main sections by the mid-court line. "
               "If the offensive team puts the ball into play behind the mid-court line, it has ten seconds to get "
               "the ball over the mid-court line. If it doesn't, then the defense gets the ball. Once the offensive "
               "team gets the ball over the mid-court line, it can no longer have possession of the ball in the area "
               "behind the midcourt line. If it does, the defense is awarded the ball.",
            5: "Football details: In football, each team consists of 11 players. These are made up of one goalkeeper "
               "and ten outfield players. The pitch dimensions vary from each ground but are roughly 120 yards long "
               "and 75 yards wide. On each pitch you will have a 6 yard box next to the goal mouth, an 18 yard box "
               "surrounding the 6 yard box and a centre circle. Each half of the pitch must be a mirror image of the "
               "other in terms of dimensions.\nThe aim of football is to score more goals then your opponent in a 90 "
               "minute playing time frame. The match is split up into two halves of 45 minutes. After the first 45 "
               "minutes players will take a 15 minute rest period called half time. The second 45 minutes will resume "
               "and any time deemed fit to be added on by the referee (injury time) will be accordingly. "
        }
        return switcher.get(arg)

    def disp(self):
        print("\nOutdoor Games: \n1.Tennis\n2.Cricket\n3.Volleyball\n4.Basketball\n5.Football")

    def format(self, arg):
        switcher = {
            1: "\nFormats:\n1. Clay court\n2. Grass Court\n3. Hard Court\n4. Carpet Court",
            2: "\nFormats:\n1. Test cricket\n2. One Day Internationals (ODIs)\n3. Twenty20 Internationals (T20Is)",
            3: "\nFormats:\n1. Beach aquatic volleyball\n2.Beach volleyball\n3.Footvolley\n4.Snow "
               "volleyball\n5.Bossaball\n6.Ecua-volley.\n7.Fistball",
            4: "\nFormats:\n1. Four quarters of 10 (FIBA)\n2. 12 minutes (NBA)",
            5: "\nFormats:\n1. Copa Del Ray\n2. UEFA Champions League\n3. FIFA World Cup\n4. UEFA Europa League"
        }
        return switcher.get(arg);

    def games(self, arg):
        switcher = {
            1: "Tennis",
            2: "Cricket",
            3: "Volleyball",
            4: "Basketball",
            5: "Football"
        }
        return switcher.get(arg)

    def lead(self, arg):
        switcher = {
            1: "Tennis Players:\n1.Novak Djokovic: He is a Serbian professional tennis player who is currently ranked world No. 1 in "
               "men's singles tennis by the Association of Tennis Professionals\n2.Ashleigh Barty: She is an Australian "
               "professional tennis player and former cricketer. She is ranked No. 1 in the world in singles by the "
               "Women's Tennis Association and is the second Australian WTA singles No. 1 after fellow Indigenous "
               "Australian Evonne Goolagong Cawley.",
            2: "Cricket Players:\nTop Batsmen:\n1.ICC Test:(Australia) Steve Smith "
               "\n2.ICC ODI: (India) Virat Kohli"
               "\n3.ICC T20I: (England) Dawid Malan"
               "\nTop Bowlers:\n1.ICC Test : (Australia) Pat Cummins"
               "\n2.ICC ODI: (New Zealand) Trent Boult"
               "\n3.ICC T20I: (Afghanistan) Rashid Khan",
            3: "Volleyball Players:\n1.Bruno Rezende Setter (Brazil)\n2.Facundo Conte Outside Hitter("
               "Argentina)\n3.Osmany Juantorena Outside Hitter(Italy)\n4.Yuji Nishida Opposite(Japan)\n5.Fernando"
               "Kreling Setter(Brazil)\n6.Evandro Guerra Opposite(Brazil)\n7.Alexey Kononov Middle-blocker("
               "Russia)\n8.Loran Alekno Setter(Russia)",
            4: "Basketball Players:\n1.LeBron Raymone James Sr.: He is an American professional basketball player for the Los "
               "Angeles Lakers of the National Basketball Association. He is widely considered to be one of the "
               "greatest basketball players in NBA history",
            5: "Football Players:\n1.Lionel Messsi: Lionel Andrés Messi is an Argentine professional footballer who "
               "plays as a forward and captains both Spanish club Barcelona and the Argentina national "
               "team\n2.Cristiano Ronaldo dos Santos Aveiro GOIH ComM: He is a Portuguese professional footballer who plays "
               "as a forward for Serie A club Juventus and captains the Portugal national team "
        }
        return switcher.get(arg)


def main():
    ch = 'y'
    print("\nWelcome to Spotopedia!\nHere you can find the details of a lot of sports.")
    while ch == 'y' or ch == 'Y':
        spObj.disp()
        n1 = int(input("\nEnter Choice: "))
        if n1 == 1:
            print(inObj.disp())
            spObj.selection()
            spObj.temp(inObj)

        elif n1 == 2:
            print(otObj.disp())
            spObj.selection()
            spObj.temp(otObj)

        elif n1 == 3:
            print("Thank You for Reading!!!")
            exit(0)

        else:
            print("Sorry this option isn't available.\nExiting...")
            exit(0)
        ch = input("\n\nDo you still want to continue(y/n): ")


if __name__ == '__main__':
    # object Sport,Indoor,Outdoor
    spObj = sport()
    inObj = indoor()
    otObj = outdoor()
    main()
    print("Thank you for having a look at Spotopedia!!!Hope you've got some valuable insights on different sports.")
