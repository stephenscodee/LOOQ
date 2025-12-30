import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../features/camera/presentation/pages/camera_page.dart';
import '../features/recognition/presentation/pages/recognition_results_page.dart';
import '../features/shopping/presentation/pages/product_detail_page.dart';
import '../features/outfits/presentation/pages/outfit_suggestions_page.dart';
import '../features/profile/presentation/pages/profile_page.dart';
import '../shared/widgets/splash_page.dart';

class AppRouter {
  static final GoRouter router = GoRouter(
    initialLocation: '/',
    routes: [
      // Splash
      GoRoute(
        path: '/',
        builder: (context, state) => const SplashPage(),
      ),
      
      // Camera - Feature principal
      GoRoute(
        path: '/camera',
        builder: (context, state) => const CameraPage(),
      ),
      
      // Recognition Results
      GoRoute(
        path: '/recognition-results',
        builder: (context, state) {
          final imageData = state.extra as Map<String, dynamic>?;
          return RecognitionResultsPage(imageData: imageData);
        },
      ),
      
      // Product Detail
      GoRoute(
        path: '/product/:productId',
        builder: (context, state) {
          final productId = state.pathParameters['productId']!;
          return ProductDetailPage(productId: productId);
        },
      ),
      
      // Outfit Suggestions
      GoRoute(
        path: '/outfits/:garmentId',
        builder: (context, state) {
          final garmentId = state.pathParameters['garmentId']!;
          return OutfitSuggestionsPage(garmentId: garmentId);
        },
      ),
      
      // Profile
      GoRoute(
        path: '/profile',
        builder: (context, state) => const ProfilePage(),
      ),
    ],
    errorBuilder: (context, state) => Scaffold(
      body: Center(
        child: Text('Página no encontrada: ${state.location}'),
      ),
    ),
  );
}

class App extends StatelessWidget {
  const App({super.key});

  @override
  Widget build(BuildContext context) {
    return const Scaffold(
      body: SizedBox.shrink(),
    );
  }
}
