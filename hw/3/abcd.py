import collections

class Abcd():
    def __init__(self):
        self.featureSet = set()
        self.aMap = {}
        self.bMap = {}
        self.cMap = {}
        self.dMap = {}
        self.num = 0

    def abcd1(self, actual, predicted):
        self.num += 1
        if actual == predicted:
            self.featureSet.add(actual)
            if actual in self.dMap:
                self.dMap[actual] += 1
            else:
                self.dMap[actual] = 1
                self.aMap[actual] = 0
                self.bMap[actual] = 0
                self.cMap[actual] = 0
                count = 0
                for key, _ in self.dMap.items():
                    if key != actual:
                        count += self.dMap[key]
                self.aMap[actual] = count
            for key, _ in self.aMap.items():
                if key != actual:
                    self.aMap[key] += 1
        else:
            self.featureSet.add(actual)
            self.featureSet.add(predicted)
            if actual in self.bMap:
                self.bMap[actual] += 1
            else:
                self.dMap[actual] = 0
                self.aMap[actual] = 0
                self.bMap[actual] = 1
                self.cMap[actual] = 0
                count = 0
                for key, _ in self.dMap.items():
                    if key != actual:
                        count += self.dMap[key]
                self.aMap[actual] = count
            if predicted in self.bMap:
                self.cMap[predicted] += 1
            else:
                self.dMap[actual] = 0
                self.aMap[actual] = 0
                self.bMap[actual] = 0
                self.cMap[actual] = 1
                count = 0
                for key, _ in self.dMap.items():
                    if key != predicted:
                        count += self.dMap[key]
                self.aMap[predicted] = count
            for key, _ in self.aMap.items():
                if key != actual and key != predicted:
                    self.aMap[key] += 1

    def report(self):
        """ print the Abcd report """
        bar = "---------"

        print(
            "db        |rx         |num        |a          | b         | c         | d         | acc       | pre       | pd        | pf        | f         | g         | class")
        print("%5s | %5s | %5s | %5s | %5s | %5s | %5s | %5s | %5s | %5s | %5s | %5s | %5s | %5s" % (
            bar, bar, bar, bar, bar, bar, bar, bar, bar, bar, bar, bar, bar, "----"))

        # iterate through symbol dictionary
        for sym in self.featureSet:
            pd = pf = pn = prec = g = f = acc = 0
            a = self.aMap[sym]
            b = self.bMap[sym]
            c = self.cMap[sym]
            d = self.dMap[sym]

            if (b + d) > 0:
                pd = float(d / (b + d))
            if (a + c) > 0:
                pf = float(c / (a + c))
            if (a + c) > 0:
                pn = (b + d) / (a + c)
            if (c + d) > 0:
                prec = float(d / (c + d))
            if (1 - pf + pd) > 0:
                f = float((2 * prec * pd) / (prec + pd))
            if (prec + pd) > 0:
                g = float(2 * (1 - pf) * pd / (1 - pf + pd))
            acc = float((a + d) / self.num)

            print(
                "%5s     |%5s      |%5s      |%5s      | %5s     | %5s     | %5s     | %5s     | %5s     | %5s     | %5s     | %5s     | %5s     | %5s    " % (
                    "data", "rx", self.num, a, b, c, d, round(acc, 2), round(prec, 2), round(pd, 2), round(pf, 2),
                    round(f, 2), round(g, 2), sym))


abcd = Abcd()
for i in range(6):
    abcd.abcd1('yes', 'yes')
for i in range(2):
    abcd.abcd1("no", "no")
for i in range(5):
    abcd.abcd1("maybe", "maybe")
abcd.abcd1("maybe", "no")
abcd.report()
