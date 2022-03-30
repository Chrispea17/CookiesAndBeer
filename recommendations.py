class Recommendation:
    def ranking(response):
        rankings = {"good": True, "bad": False}
        if rankings[response] == True:
            return 1
        elif rankings[response] == False:
            return 0
