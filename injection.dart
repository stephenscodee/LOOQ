import 'package:get_it/get_it.dart';
import 'package:dio/dio.dart';
import '../../core/config/app_config.dart';
import '../../data/repositories/product_repository_impl.dart';
import '../../domain/repositories/product_repository.dart';
import '../../data/datasources/api_client.dart';

final getIt = GetIt.instance;

Future<void> configureDependencies() async {
  // Configuration
  getIt.registerSingleton<AppConfig>(AppConfig());
  
  // HTTP Client
  getIt.registerSingleton<Dio>(
    Dio(
      BaseOptions(
        baseUrl: getIt<AppConfig>().apiBaseUrl,
        connectTimeout: const Duration(seconds: 30),
        receiveTimeout: const Duration(seconds: 30),
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
        },
      ),
    ),
  );
  
  // Data Sources
  getIt.registerSingleton<ApiClient>(ApiClient(getIt<Dio>()));
  
  // Repositories
  getIt.registerSingleton<ProductRepository>(
    ProductRepositoryImpl(getIt<ApiClient>()),
  );
  
  // Use Cases (if needed in future)
  // getIt.registerSingleton<RecognizeGarmentUseCase>(...);
}
