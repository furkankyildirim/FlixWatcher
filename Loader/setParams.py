def setParams(code):
    params = {}
    if code == "tr":
        params["code"] = "tr"
        params["willDelete"] = "https://tr.flixable.com/leaving-netflix/?page="
        params["popularMovies"] = "https://tr.flixable.com/popular/"
        params["url"] = "https://tr.flixable.com"
    elif code == "us":
        params["code"] = "us"
        params["willDelete"] = "https://flixable.com/leaving-netflix/?page="
        params["popularMovies"] = "https://flixable.com/popular/"
        params["url"] = "https://flixable.com"
    elif code == "uk":
        params["code"] = "uk"
        params["willDelete"] = "https://uk.flixable.com/leaving-netflix/?page="
        params["popularMovies"] = "https://uk.flixable.com/popular/"
        params["url"] = "https://uk.flixable.com"
    elif code == "se":
        params["code"] = "se"
        params["willDelete"] = "https://se.flixable.com/leaving-netflix/?page="
        params["popularMovies"] = "https://se.flixable.com/popular/"
        params["url"] = "https://se.flixable.com"
    elif code == "pt":
        params["code"] = "pt"
        params["willDelete"] = "https://pt.flixable.com/leaving-netflix/?page="
        params["popularMovies"] = "https://pt.flixable.com/popular/"
        params["url"] = "https://pt.flixable.com"

    elif code == "pl":
        params["code"] = "pl"
        params["willDelete"] = "https://pl.flixable.com/leaving-netflix/?page="
        params["popularMovies"] = "https://pl.flixable.com/popular/"
        params["url"] = "https://pl.flixable.com"
    elif code == "nl":
        params["code"] = "nl"
        params["willDelete"] = "https://nl.flixable.com/leaving-netflix/?page="
        params["popularMovies"] = "https://nl.flixable.com/popular/"
        params["url"] = "https://nl.flixable.com"
    elif code == "mx":
        params["code"] = "mx"
        params["willDelete"] = "https://mx.flixable.com/leaving-netflix/?page="
        params["popularMovies"] = "https://mx.flixable.com/popular/"
        params["url"] = "https://mx.flixable.com"
    elif code == "it":
        params["code"] = "it"
        params["willDelete"] = "https://it.flixable.com/leaving-netflix/?page="
        params["popularMovies"] = "https://it.flixable.com/popular/"
        params["url"] = "https://it.flixable.com"
    elif code == "pl":
        params["code"] = "pl"
        params["willDelete"] = "https://pl.flixable.com/leaving-netflix/?page="
        params["popularMovies"] = "https://pl.flixable.com/popular/"
        params["url"] = "https://pl.flixable.com"
    elif code == "fr":
        params["code"] = "fr"
        params["willDelete"] = "https://fr.flixable.com/leaving-netflix/?page="
        params["popularMovies"] = "https://fr.flixable.com/popular/"
        params["url"] = "https://fr.flixable.com"
    elif code == "es":
        params["code"] = "es"
        params["willDelete"] = "https://es.flixable.com/leaving-netflix/?page="
        params["popularMovies"] = "https://es.flixable.com/popular/"
        params["url"] = "https://es.flixable.com"
    elif code == "de":
        params["code"] = "de"
        params["willDelete"] = "https://de.flixable.com/leaving-netflix/?page="
        params["popularMovies"] = "https://de.flixable.com/popular/"
        params["url"] = "https://de.flixable.com"
    elif code == "br":
        params["code"] = "br"
        params["willDelete"] = "https://br.flixable.com/leaving-netflix/?page="
        params["popularMovies"] = "https://br.flixable.com/popular/"
        params["url"] = "https://br.flixable.com"
    elif code == "ca":
        params["code"] = "ca"
        params["willDelete"] = "https://ca.flixable.com/leaving-netflix/?page="
        params["popularMovies"] = "https://ca.flixable.com/popular/"
        params["url"] = "https://ca.flixable.com"
    elif code == "au":
        params["code"] = "au"
        params["willDelete"] = "https://au.flixable.com/leaving-netflix/?page="
        params["popularMovies"] = "https://au.flixable.com/popular/"
        params["url"] = "https://au.flixable.com"
    elif code == "ar":
        params["code"] = "ar"
        params["willDelete"] = "https://ar.flixable.com/leaving-netflix/?page="
        params["popularMovies"] = "https://ar.flixable.com/popular/"
        params["url"] = "https://ar.flixable.com"
    elif code == "dk":
        params["code"] = "dk"
        params["willDelete"] = "https://dk.flixable.com/leaving-netflix/?page="
        params["popularMovies"] = "https://dk.flixable.com/popular/"
        params["url"] = "https://dk.flixable.com"
    elif code == "at":
        params["code"] = "at"
        params["willDelete"] = "https://at.flixable.com/leaving-netflix/?page="
        params["popularMovies"] = "https://at.flixable.com/popular/"
        params["url"] = "https://at.flixable.com"
    elif code == "ar":
        params["code"] = "ar"
        params["willDelete"] = "https://ar.flixable.com/leaving-netflix/?page="
        params["popularMovies"] = "https://ar.flixable.com/popular/"
        params["url"] = "https://ar.flixable.com"
    elif code == "no":
        params["code"] = "no"
        params["willDelete"] = "https://no.flixable.com/leaving-netflix/?page="
        params["popularMovies"] = "https://no.flixable.com/popular/"
        params["url"] = "https://no.flixable.com"
    elif code == "ar":
        params["code"] = "ar"
        params["willDelete"] = "https://ar.flixable.com/leaving-netflix/?page="
        params["popularMovies"] = "https://ar.flixable.com/popular/"
        params["url"] = "https://ar.flixable.com"
    else:
        params["code"] = "us"
        params["willDelete"] = "https://flixable.com/leaving-netflix/?page="
        params["popularMovies"] = "https://flixable.com/popular/"
        params["url"] = "https://flixable.com"
    return params
