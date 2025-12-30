class AppConfig {
  // API Configuration
  // In production, use environment variables or config files
  static const String _baseUrl = String.fromEnvironment(
    'API_BASE_URL',
    defaultValue: 'http://localhost:8000',
  );
  
  String get apiBaseUrl => _baseUrl;
  
  // API Endpoints
  String get recognizeEndpoint => '$apiBaseUrl/api/v1/complete/analyze';
  String get productsEndpoint => '$apiBaseUrl/api/v1/products/search';
  String get outfitsEndpoint => '$apiBaseUrl/api/v1/outfits/generate';
  
  // App Configuration
  static const String appName = 'LOOQ';
  static const String appVersion = '1.0.0';
  
  // Image Configuration
  static const int maxImageSize = 10 * 1024 * 1024; // 10MB
  static const List<String> allowedImageTypes = ['image/jpeg', 'image/png', 'image/webp'];
}

