class AppConstants {
  // App Information
  static const String appName = 'Fashion Lens';
  static const String tagline = 'Foto → Dónde comprar + outfits';
  static const String version = '1.0.0';

  // API Configuration
  static const String apiBaseUrl = 'http://localhost:8000';
  static const String apiVersion = 'v1';
  static const Duration apiTimeout = Duration(seconds: 30);

  // Image Configuration
  static const int maxImageSize = 5 * 1024 * 1024; // 5MB
  static const List<String> supportedImageFormats = ['jpg', 'jpeg', 'png'];
  static const double imageCompressionQuality = 0.8;

  // Camera Configuration
  static const ResolutionPreset cameraResolution = ResolutionPreset.high;
  static const double cameraAspectRatio = 16.0 / 9.0;

  // UI Constants
  static const double borderRadius = 12.0;
  static const double cardElevation = 2.0;
  static const double buttonHeight = 48.0;

  // Animation Durations
  static const Duration shortAnimation = Duration(milliseconds: 200);
  static const Duration mediumAnimation = Duration(milliseconds: 300);
  static const Duration longAnimation = Duration(milliseconds: 500);

  // Storage Keys
  static const String userTokenKey = 'user_token';
  static const String userProfileKey = 'user_profile';
  static const String isFirstLaunchKey = 'is_first_launch';
  static const String preferencesKey = 'app_preferences';

  // Error Messages
  static const String networkErrorMessage = 'Error de conexión. Verifica tu internet.';
  static const String genericErrorMessage = 'Algo salió mal. Inténtalo de nuevo.';
  static const String cameraPermissionMessage = 'Se necesita permiso de cámara para continuar.';
  static const String imageUploadErrorMessage = 'Error al subir la imagen. Inténtalo de nuevo.';

  // Categories (MVP - solo tops)
  static const List<String> mvpCategories = ['top'];
  static const List<String> topSubcategories = [
    't-shirt',
    'shirt',
    'blouse',
    'sweater',
    'hoodie',
    'tank_top',
  ];

  // Colors
  static const List<String> commonColors = [
    'black', 'white', 'gray', 'navy', 'red', 'blue', 
    'green', 'yellow', 'pink', 'purple', 'brown', 'beige'
  ];

  // Patterns
  static const List<String> commonPatterns = [
    'solid', 'striped', 'checked', 'floral', 'polka_dot', 'geometric'
  ];

  // Occasions
  static const List<String> occasions = [
    'casual', 'formal', 'business', 'sport', 'party', 'date'
  ];

  // Seasons
  static const List<String> seasons = [
    'spring', 'summer', 'fall', 'winter'
  ];
}
