# LOOQ Mobile App

Flutter mobile application for fashion recognition and shopping.

## Features

- 📸 Camera integration for taking photos
- 🖼️ Image gallery selection
- 🔍 Real-time garment recognition
- 🛍️ Product browsing and purchase links
- 👔 Outfit recommendations
- 🎨 Modern, clean UI

## Setup

### Prerequisites

- Flutter SDK 3.0+
- Android Studio / Xcode
- iOS Simulator or Android Emulator / Physical device

### Installation

1. Install dependencies:
```bash
flutter pub get
```

2. Configure API endpoint:

Edit `lib/core/config/app_config.dart`:
```dart
// For Android emulator
static const String _baseUrl = 'http://10.0.2.2:8000';

// For iOS simulator
static const String _baseUrl = 'http://localhost:8000';

// For physical device (use your computer's IP)
static const String _baseUrl = 'http://192.168.1.100:8000';
```

3. Run the app:
```bash
flutter run
```

## Project Structure

```
lib/
├── core/              # Core functionality
│   ├── config/        # App configuration
│   ├── di/            # Dependency injection
│   ├── routing/       # Navigation
│   └── theme/         # App theming
├── data/              # Data layer
│   ├── datasources/   # API clients
│   └── repositories/  # Repository implementations
├── domain/            # Business logic
│   └── repositories/  # Repository interfaces
└── features/          # Feature modules
    ├── camera/        # Camera feature
    ├── home/          # Home screen
    └── results/       # Results screen
```

## Features

### Camera Screen
- Take photo with camera
- Select image from gallery
- Image upload and analysis

### Results Screen
- **Products Tab**: Browse similar products with buy links
- **Outfits Tab**: View outfit recommendations

## Development

### Build for Release

```bash
# Android
flutter build apk --release

# iOS
flutter build ios --release
```

### Run Tests

```bash
flutter test
```

### Code Formatting

```bash
dart format lib/
```

## Platform-Specific Setup

### Android

Add permissions in `android/app/src/main/AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.CAMERA"/>
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
<uses-permission android:name="android.permission.INTERNET"/>
```

### iOS

Add permissions in `ios/Runner/Info.plist`:

```xml
<key>NSCameraUsageDescription</key>
<string>We need camera access to take photos of clothing items</string>
<key>NSPhotoLibraryUsageDescription</key>
<string>We need photo library access to select clothing images</string>
```

## Troubleshooting

- **API connection errors**: Check API base URL matches your backend address
- **Camera not working**: Ensure permissions are granted
- **Build errors**: Run `flutter clean` and `flutter pub get`

