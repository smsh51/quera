add_movie_count = -1
movies = []
cast_id_count = -1
cast_ids = []

database = {'movie': dict(),
            'cast': dict()}

n = int(input())
for i in range(n):
    inp = input()
    if 'ADD-MOVIE' in inp:
        title, date, quality = inp[len('ADD-MOVIE'):].split(' ')[1:]
        if len(title) > 20:
            print("invalid title")
        elif not (1888 <= int(date) <= 2024):
            print("invalid date")
        elif quality not in ["720p", "1080p", "4K"]:
            print("invalid quality")
        else:
            movie_id = add_movie_count + 1
            add_movie_count += 1
            print(f"added successfully {movie_id}")
            database['movie'][movie_id] = {'title': title, 'date': date, 'quality': quality, 'casts': []}
    elif 'REM-MOVIE' in inp:
        movie_id = int(inp[len('REM-MOVIE'):].split(' ')[1])
        if movie_id in database['movie']:
            database['movie'].pop(movie_id)
            print(f"removed successfully {movie_id}")
        else:
            print("invalid movie id")
    elif 'ADD-CAST' in inp:
        name = inp[len('ADD-CAST'):].split(' ')[1]
        if len(name) > 20 or not name.replace(" ", "").isalpha():
            print("invalid name")
        else:
            cast_id = cast_id_count + 1
            cast_id_count += 1
            database['cast'][cast_id] = {'name': name, 'movies': []}
            print(f"added successfully {cast_id}")
    elif 'REM-CAST' in inp:
        cast_id = int(inp[len('REM-CAST'):].split(' ')[1])
        if cast_id in database['cast']:
            database['cast'].pop(cast_id)
            print(f"removed successfully {cast_id}")
        else:
            print("invalid cast id")
    elif 'SHOW-MOVIE' in inp:
        movie_id = int(inp[len('SHOW-MOVIE'):].split(' ')[1])
        if movie_id not in database['movie']:
            print("invalid movie id")
        else:
            print(f'{{title:"{database["movie"][movie_id]["title"]}", date:"{database["movie"][movie_id]["date"]}", quality:"{database["movie"][movie_id]["quality"]}", casts:{database["movie"][movie_id]["casts"]}}}')

    elif 'SHOW-CAST' in inp:
        cast_id = int(inp[len('SHOW-CAST'):].split(' ')[1])
        if cast_id not in database['cast']:
            print("invalid cast id")
        else:
            print(f'{{name:"{database["cast"][cast_id]["name"]}", movies:{database["cast"][cast_id]["movies"]}}}')


    elif 'LINK-CAST-TO-MOVIE' in inp:
        cast_id, movie_id = inp[len('LINK-CAST-TO-MOVIE'):].split(' ')[1:]
        if int(cast_id) not in list(database['cast']):
            print("invalid cast id")
        elif int(movie_id) not in list(database['movie']):
            print("invalid movie id")
        elif int(movie_id) in database['movie'].get(cast_id, []):
            print("already linked")
        else:
            database['movie'][int(movie_id)]['casts'].append(int(cast_id))
            database['movie'][int(movie_id)]['casts'].sort()
            database['cast'][int(cast_id)]['movies'].append(int(movie_id))
            database['cast'][int(cast_id)]['movies'].sort()
            print(f"successfully linked {cast_id} to {movie_id}")
    elif 'FILTER-MOVIES-BY-TITLE' in inp:
        pattern = inp[len('FILTER-MOVIES-BY-TITLE'):].split(' ')[1]
        movies = database['movie']
        filtered_movies = [movie_id for movie_id, movie_details in movies.items() if
                           movie_details['title'].startswith(pattern)]
        filtered_movies.sort()
        print(f"[{', '.join(map(str, filtered_movies))}]")
    elif 'FILTER-MOVIES-BY-DATE' in inp:
        ineq = inp[len('FILTER-MOVIES-BY-DATE'):].split(' ')[1]
        n = int(inp[len('FILTER-MOVIES-BY-DATE'):].split(' ')[2])
        movies = database['movie']
        filtered_movies = []

        for movie_id, movie_details in movies.items():
            if 'date' in movie_details:
                date = int(movie_details['date'])
                if ineq == ">=" and date >= n:
                    filtered_movies.append(movie_id)
                elif ineq == ">" and date > n:
                    filtered_movies.append(movie_id)
                elif ineq == "=" and date == n:
                    filtered_movies.append(movie_id)
                elif ineq == "<" and date < n:
                    filtered_movies.append(movie_id)
                elif ineq == "<=" and date <= n:
                    filtered_movies.append(movie_id)

        filtered_movies.sort()
        print(f"[{', '.join(map(str, filtered_movies))}]")
    elif 'FILTER-MOVIES-BY-QUALITY' in inp:
        pattern = inp[len('FILTER-MOVIES-BY-QUALITY'):].split(' ')[1]
        movies = database['movie']
        filtered_movies = [movie_id for movie_id, movie_details in movies.items() if
                           movie_details.get('quality') == pattern]
        filtered_movies.sort()
        print(f"[{', '.join(map(str, filtered_movies))}]")
