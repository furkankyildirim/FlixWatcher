def setParams(code):
    params = {}
    if code == "tr":
        params["code"] = "tr"
        params["willDelete"] = "https://turflix.com/kaldirildi"
        params["newMovies"] = "https://turflix.com/filmler/-/-/date/any"
        params["url"] = "https://turflix.com"
        params["hrefMovies"] = 'a[href^="/filmler"]'
        params["hrefSeries"] = 'a[href^="/diziler"]'
    elif code == "us":
        params["code"] = "us"
        params["willDelete"] = "https://flixboss.com/leaving"
        params["newMovies"] = "https://flixboss.com/movies/-/-/date/any"
        params["url"] = "https://flixboss.com"
        params["hrefMovies"] = 'a[href^="/movies"]'
        params["hrefSeries"] = 'a[href^="/tv-series"]'
    elif code == "uk":
        params["code"] = "uk"
        params["willDelete"] = "https://uk.flixboss.com/leaving"
        params["newMovies"] = "https://uk.flixboss.com/movies/-/-/date/any"
        params["url"] = "https://uk.flixboss.com"
        params["hrefMovies"] = 'a[href^="/movies"]'
        params["hrefSeries"] = 'a[href^="/tv-series"]'
    elif code == "se":
        params["code"] = "se"
        params["willDelete"] = "https://netflixguiden.se/sista-chansen"
        params["newMovies"] = "https://netflixguiden.se/filmer/-/-/date/any"
        params["url"] = "https://netflixguiden.se"
        params["hrefMovies"] = 'a[href^="/filmer"]'
        params["hrefSeries"] = 'a[href^="/serier"]'
    elif code == "za":
        params["code"] = "za"
        params["willDelete"] = "https://za.flixboss.com/leaving"
        params["newMovies"] = "https://za.flixboss.com/movies/-/-/date/any"
        params["url"] = "https://za.flixboss.com"
        params["hrefMovies"] = 'a[href^="/movies"]'
        params["hrefSeries"] = 'a[href^="/tv-series"]'
    elif code == "ch":
        params["code"] = "ch"
        params["willDelete"] = "https://ch.flixboss.com/verlasst-netflix"
        params["newMovies"] = "https://ch.flixboss.com/filme/-/-/date/any"
        params["url"] = "https://za.flixboss.com"
        params["hrefMovies"] = 'a[href^="/filme"]'
        params["hrefSeries"] = 'a[href^="/serien"]'
    elif code == "pt":
        params["code"] = "pt"
        params["willDelete"] = "https://pt.flixboss.com/deixando-a-netflix"
        params["newMovies"] = "https://pt.flixboss.com/filmes/-/-/date/any"
        params["url"] = "https://pt.flixboss.com"
        params["hrefMovies"] = 'a[href^="/filmes"]'
        params["hrefSeries"] = 'a[href^="/series"]'
    elif code == "pl":
        params["code"] = "pl"
        params["willDelete"] = "https://bestflix.pl/ostatnia-szansa"
        params["newMovies"] = "https://bestflix.pl/filmy/-/-/date/any"
        params["url"] = "https://bestflix.pl"
        params["hrefMovies"] = 'a[href^="/filmy"]'
        params["hrefSeries"] = 'a[href^="/seriale"]'
    elif code == "nl ":
        params["code"] = "nl"
        params["willDelete"] = "https://nl.flixboss.com/laatste-kans"
        params["newMovies"] = "https://nl.flixboss.com/films/-/-/date/any"
        params["url"] = "https://nl.flixboss.com"
        params["hrefMovies"] = 'a[href^="/films"]'
        params["hrefSeries"] = 'a[href^="/series"]'
    elif code == "mx ":
        params["code"] = "mx"
        params["willDelete"] = "https://mx.flixboss.com/que-sale"
        params["newMovies"] = "https://mx.flixboss.com/peliculas/-/-/date/any"
        params["url"] = "https://nl.flixboss.com"
        params["hrefMovies"] = 'a[href^="/peliculas"]'
        params["hrefSeries"] = 'a[href^="/series"]'
    elif code == "it":
        params["code"] = "it"
        params["willDelete"] = "https://it.flixboss.com/in-scadenza"
        params["newMovies"] = "https://it.flixboss.com/film/-/-/date/any"
        params["url"] = "https://it.flixboss.com"
        params["hrefMovies"] = 'a[href^="/film"]'
        params["hrefSeries"] = 'a[href^="/serie"]'
    elif code == "in":
        params["code"] = "in"
        params["willDelete"] = "https://in.flixboss.com/leaving"
        params["newMovies"] = "https://in.flixboss.com/movies/-/-/date/any"
        params["url"] = "https://in.flixboss.com"
        params["hrefMovies"] = 'a[href^="/movies"]'
        params["hrefSeries"] = 'a[href^="/tv-series"]'
    elif code == "hk":
        params["code"] = "hk"
        params["willDelete"] = "https://hk.flixboss.com/leaving"
        params["newMovies"] = "https://hk.flixboss.com/movies/-/-/date/any"
        params["url"] = "https://hk.flixboss.com"
        params["hrefMovies"] = 'a[href^="/movies"]'
        params["hrefSeries"] = 'a[href^="/tv-series"]'
    elif code == "fr":
        params["code"] = "fr"
        params["willDelete"] = "https://fr.flixboss.com/partant"
        params["newMovies"] = "https://fr.flixboss.com/films/-/-/date/any"
        params["url"] = "https://fr.flixboss.com"
        params["hrefMovies"] = 'a[href^="/films"]'
        params["hrefSeries"] = 'a[href^="/series"]'
    elif code == "es":
        params["code"] = "es"
        params["willDelete"] = "https://bestflix.es/que-sale"
        params["newMovies"] = "https://bestflix.es/peliculas/-/-/date/any"
        params["url"] = "https://bestflix.es"
        params["hrefMovies"] = 'a[href^="/peliculas"]'
        params["hrefSeries"] = 'a[href^="/series"]'
    elif code == "de":
        params["code"] = "de"
        params["willDelete"] = "https://de.flixboss.com/verlasst-netflix"
        params["newMovies"] = "https://de.flixboss.com/filme/-/-/date/any"
        params["url"] = "https://de.flixboss.com"
        params["hrefMovies"] = 'a[href^="/filme"]'
        params["hrefSeries"] = 'a[href^="/serien"]'
    elif code == "co":
        params["code"] = "co"
        params["willDelete"] = "https://co.flixboss.com/que-sale"
        params["newMovies"] = "https://co.flixboss.com/peliculas/-/-/date/any"
        params["url"] = "https://co.flixboss.com"
        params["hrefMovies"] = 'a[href^="/peliculas"]'
        params["hrefSeries"] = 'a[href^="/series"]'
    elif code == "br":
        params["code"] = "br"
        params["willDelete"] = "https://br.flixboss.com/deixando-a-netflix"
        params["newMovies"] = "https://br.flixboss.com/filmes/-/-/date/any"
        params["url"] = "https://br.flixboss.com"
        params["hrefMovies"] = 'a[href^="/filmes"]'
        params["hrefSeries"] = 'a[href^="/series"]'
    elif code == "ca":
        params["code"] = "ca"
        params["willDelete"] = "https://ca.flixboss.com/leaving"
        params["newMovies"] = "https://ca.flixboss.com/movies/-/-/date/any"
        params["url"] = "https://ca.flixboss.com"
        params["hrefMovies"] = 'a[href^="/movies"]'
        params["hrefSeries"] = 'a[href^="/tv-series"]'
    elif code == "au":
        params["code"] = "au"
        params["willDelete"] = "https://au.flixboss.com/leaving"
        params["newMovies"] = "https://au.flixboss.com/movies/-/-/date/any"
        params["url"] = "https://au.flixboss.com"
        params["hrefMovies"] = 'a[href^="/movies"]'
        params["hrefSeries"] = 'a[href^="/tv-series"]'
    elif code == "ar":
        params["code"] = "ar"
        params["willDelete"] = "https://ar.flixboss.com/que-sale"
        params["newMovies"] = "https://ar.flixboss.com/peliculas/-/-/date/any"
        params["url"] = "https://ar.flixboss.com"
        params["hrefMovies"] = 'a[href^="/peliculas"]'
        params["hrefSeries"] = 'a[href^="/series"]'
    else:
        params["code"] = "us"
        params["willDelete"] = "https://flixboss.com/leaving"
        params["newMovies"] = "https://flixboss.com/movies/-/-/date/any"
        params["url"] = "https://flixboss.com"
        params["hrefMovies"] = 'a[href^="/movies"]'
        params["hrefSeries"] = 'a[href^="/tv-series"]'

    return params
