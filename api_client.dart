import 'dart:io';
import 'package:dio/dio.dart';
import '../../core/config/app_config.dart';

class ApiClient {
  final Dio _dio;
  final AppConfig _config = AppConfig();

  ApiClient(this._dio);

  Future<Map<String, dynamic>> analyzeImage(File imageFile) async {
    try {
      final formData = FormData.fromMap({
        'file': await MultipartFile.fromFile(
          imageFile.path,
          filename: imageFile.path.split('/').last,
        ),
      });

      final response = await _dio.post(
        _config.recognizeEndpoint,
        data: formData,
        options: Options(
          contentType: 'multipart/form-data',
          receiveTimeout: const Duration(seconds: 60),
        ),
      );

      if (response.statusCode == 200) {
        return response.data as Map<String, dynamic>;
      } else {
        throw Exception('Failed to analyze image: ${response.statusCode}');
      }
    } on DioException catch (e) {
      throw Exception('Network error: ${e.message}');
    } catch (e) {
      throw Exception('Error analyzing image: $e');
    }
  }
}

