#weather fectching using open API , meteo API, and geocoding API
'''import requests
def get_weather(city):
    api_key = "your_api_key_here"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key
    response = requests.get(complete_url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        weather_desc = data['weather'][0]['description']
        print(f"Temperature: {temperature}")
        print(f"Humidity: {humidity}")
        print(f"Weather Description: {weather_desc}")
    else:
        print("City Not Found")
# Test the function
get_weather("London")
get_weather("New York")
get_weather("Tokyo")
'''

##public transport fare fetching using transport API, route API, and station validation API with error handling
'''import requests
def get_fare(origin, destination):
    api_key = "your_api_key_here"
    base_url = "http://api.transportapi.com/v3/uk/public/journey/from/" + origin + "/to/" + destination + "?app_id=your_app_id_here&app_key=" + api_key
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        if 'error' in data:
            print("Error: " + data['error'])
        else:
            fare = data['fare']
            print(f"Fare from {origin} to {destination}: {fare}")
    else:
        print("Error fetching fare information")
# Test the function
get_fare("London", "Manchester")
get_fare("New York", "Boston")
get_fare("InvalidCity", "AnotherInvalidCity")
'''

#currency exchange rate fetching using forex API, currency conversion API, and input validation with error handling
'''import requests
def get_exchange_rate(base_currency, target_currency):
    api_key = "your_api_key_here"
    base_url = "https://api.exchangerate-api.com/v4/latest/" + base_currency
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        if target_currency in data['rates']:
            exchange_rate = data['rates'][target_currency]
            print(f"Exchange rate from {base_currency} to {target_currency}: {exchange_rate}")
        else:
            print("Error: Target currency not found")
    else:
        print("Error fetching exchange rate information")
# Test the function
get_exchange_rate("USD", "EUR")
get_exchange_rate("GBP", "JPY")
get_exchange_rate("InvalidCurrency", "AnotherInvalidCurrency")
'''


#github repository info fetching using GitHub API, REST API requests, and input validation with error handling
'''import requests
def get_repo_info(owner, repo):
    base_url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        repo_name = data['name']
        description = data['description']
        stars = data['stargazers_count']
        forks = data['forks_count']
        print(f"Repository Name: {repo_name}")
        print(f"Description: {description}")
        print(f"Stars: {stars}")
        print(f"Forks: {forks}")
    else:
        print("Error fetching repository information")
# Test the function
get_repo_info("octocat", "Hello-World")
get_repo_info("torvalds", "linux")
get_repo_info("InvalidOwner", "InvalidRepo")
'''

#news headlines fetching using news API, category-based filtering, and retry mechanism with error handling
'''import requests
def get_news(category):
    api_key = "your_api_key_here"
    base_url = f"https://newsapi.org/v2/top-headlines?category={category
}&apiKey={api_key}"
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        articles = data['articles']
        for article in articles:
            print(f"Title: {article['title']}")
            print(f"Description: {article['description']}")
            print(f"URL: {article['url']}\n")
    else:
        print("Error fetching news headlines")
# Test the function
get_news("technology")
get_news("sports")
get_news("invalidCategory")
'''
#covid-19 statistics fetching using public health API, country-based query, and rate-limit retry handling with error management
'''import requests
def get_covid_stats(country):
    base_url = f"https://disease.sh/v3/covid-19/countries/{country}"
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        cases = data['cases']
        deaths = data['deaths']
        recovered = data['recovered']
        print(f"COVID-19 Statistics for {country}:")
        print(f"Cases: {cases}")
        print(f"Deaths: {deaths}")
        print(f"Recovered: {recovered}")
    else:
        print("Error fetching COVID-19 statistics")
# Test the function
get_covid_stats("USA")
get_covid_stats("India")
get_covid_stats("InvalidCountry")
'''
