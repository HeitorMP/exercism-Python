def convert(number):
    raindrops = ""
    if number % 3 == 0: raindrops += 'Pling'
    if number % 5 == 0: raindrops += 'Plang'
    if number % 7 == 0:  raindrops += 'Plong'

    return str(number) if len(raindrops) == 0 else raindrops
