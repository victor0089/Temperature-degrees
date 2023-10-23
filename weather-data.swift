let apiKey = "YOUR_API_KEY"
let city = "YourCityName"
let urlString = "https://api.openweathermap.org/data/2.5/weather?q=\(city)&appid=\(apiKey)"

if let url = URL(string: urlString) {
    URLSession.shared.dataTask(with: url) { (data, response, error) in
        if let data = data {
            // Parse JSON response here and extract temperature data
        } else if let error = error {
            print("Error: \(error)")
        }
    }.resume()
}
