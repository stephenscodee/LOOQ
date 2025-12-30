import 'package:go_router/go_router.dart';
import '../../features/camera/presentation/pages/camera_page.dart';
import '../../features/results/presentation/pages/results_page.dart';
import '../../features/home/presentation/pages/home_page.dart';

class AppRouter {
  static final GoRouter router = GoRouter(
    initialLocation: '/',
    routes: [
      GoRoute(
        path: '/',
        builder: (context, state) => const HomePage(),
      ),
      GoRoute(
        path: '/camera',
        builder: (context, state) => const CameraPage(),
      ),
      GoRoute(
        path: '/results',
        builder: (context, state) {
          final extra = state.extra as Map<String, dynamic>?;
          return ResultsPage(
            prediction: extra?['prediction'],
            products: extra?['products'] ?? [],
            outfits: extra?['outfits'] ?? [],
          );
        },
      ),
    ],
  );
}

