import 'dart:io';
import '../../domain/repositories/product_repository.dart';
import '../datasources/api_client.dart';

class ProductRepositoryImpl implements ProductRepository {
  final ApiClient _apiClient;

  ProductRepositoryImpl(this._apiClient);

  @override
  Future<Map<String, dynamic>> analyzeImage(File imageFile) async {
    return await _apiClient.analyzeImage(imageFile);
  }
}

