import 'dart:io';

abstract class ProductRepository {
  Future<Map<String, dynamic>> analyzeImage(File imageFile);
}

