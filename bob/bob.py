def response(hey_bob):
    hey_bob = hey_bob.strip()
    if not hey_bob: return "Fine. Be that way!"
    elif hey_bob.strip(' ')[-1] == "?" and not hey_bob.isupper(): return "Sure."
    elif hey_bob.isupper() and hey_bob[-1] != "?": return "Whoa, chill out!"
    elif hey_bob.isupper(): return "Calm down, I know what I'm doing!"
    else: return "Whatever."
    
    
        
