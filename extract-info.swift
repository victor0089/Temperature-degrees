if let json = try? JSONSerialization.jsonObject(with: data, options: []) as? [String: Any] {
    if let main = json["main"] as? [String: Any], let temperature = main["temp"] as? Double {
        // Use the temperature data in your app
    }
}
