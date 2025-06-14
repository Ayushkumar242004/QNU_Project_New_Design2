from django.http import JsonResponse
from tests.frequency_test import FrequencyTest  # Adjust the import path accordingly
from tests.runs_test import RunTest  # Adjust the import path accordingly
from tests.approximate_entropy_test import ApproximateEntropy
from tests.linear_complexity_test import ComplexityTest
from tests.template_matching_test import TemplateMatching
from tests.universal_test import Universal
from tests.serial_test import Serial
from tests.cumulative_sums_test import CumulativeSums
from tests. random_excursions_test import RandomExcursions
from tests.Matrix import Matrix
from tests.spectral import SpectralTest
from tests.autocorrelation_test import AutocorrelationTest
from tests.adaptive_statistical_test import AdaptiveStatisticalTest
from PIL import Image as PILImage
from tests.autocorrelation_test import AutocorrelationTest
from tests.adaptive_statistical_test import AdaptiveStatisticalTest
from reportlab.platypus import PageBreak

from tests.mcv_test import MostCommonValueTest
from tests.chiSquare_test import ChiSquareTest
from tests.collision_test import CollisionTest
from tests.compression_test import CompressionTest
from tests.l278y_test import LZ78YTest
from tests.markov_test import MarkovTest
from tests.minEntropy_test import MinEntropyTest
from tests.multiBlock_test import MultiBlockEntropyTest
from tests.predictor_test import PredictorTest
from tests.ttuple_test import TTupleTest


from tests.Birthday_spacings_test import BirthdaySpacingsTest
from tests.parking_lot_test import ParkingLotTest
from tests.overlapping_5_permutation_test import Overlapping5PermutationTest
from tests.minimum_distance_test import MinimumDistanceTest
from tests.rank_31matrix_test import Ranks31x31MatricesTest
from tests.spheres_test import Spheres3DTest
from tests.rank_32matrix_test import Ranks32x32MatricesTest
from tests.craps_test import CrapsTest
from tests.bitstream_test import BitstreamTest
from tests.gcd_test import MarsagliaTsangGCDTest
from tests.opso_test import OPSOTest
from tests.oqso_test import OQSOTest
from tests.dna_test import DNATest
from tests.count_one_stream_test import CountThe1sStreamTest
from tests.count_one_byte_test import CountThe1sByteTest
from tests.simple_gcd_test import MarsagliaTsangSimpleGCDTest
from tests.generalized_minimum_test import GeneralizedMinimumDistanceTest
from tests.u01_linear_complexity_test import TestU01LinearComplexityTest
from tests.u01_longest_substring_test import TestU01LongestRepeatedSubstringTest
from tests.u01_matrix_rank_test import TestU01MatrixRankTest

from tests.minEntropy_test import MinEntropyTest
from tests.collision_test import CollisionTest
from tests.markov_test import MarkovTest
from tests.compression_test import CompressionTest
from tests.ttuple_test import TTupleTest
from tests.mcv_test import MostCommonValueTest
from tests.chiSquare_test import ChiSquareTest
from tests.l278y_test import LZ78YTest
from tests.multiBlock_test import MultiBlockEntropyTest
from tests.predictor_test import PredictorTest

from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib import colors
from io import BytesIO
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

from django.http import StreamingHttpResponse
from reportlab.platypus import Image
from reportlab.lib.utils import ImageReader
import mimetypes
import numpy as np

from django.conf import settings
import os
#streaming
import base64
import time
import datetime
import requests
from django.http import StreamingHttpResponse
from django.shortcuts import render
#report
import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend for Matplotlib
import matplotlib.pyplot as plt
import io
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
import reportlab
from reportlab.platypus import Image
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfform
# from reportlab.pdfimage import ImageReader
from io import BytesIO
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from google import genai
# import google.generativeai as genai  # ✅ Correct

from google.genai import types
from django.core.cache import cache
import  uuid

client = genai.Client(api_key="AIzaSyBEgltUoSm5vFEvDxOd29yZ1hJ3apSYpqg") # place your api key here in inverted commas

@csrf_exempt  # Remove this in production, only for testing purposes
def run_frequency_test(request):
    if request.method == 'POST':
        try:
            # Parse the JSON body
            data = json.loads(request.body)
            binary_data = data.get('binary_data', '')
        
            # Validate binary data
            if not binary_data:
                return JsonResponse({"error": "binary_data is missing or empty"}, status=400)

            # Run the monobit test
            p_value, result = FrequencyTest.monobit_test(binary_data)

            print("FrequencyTest p_value:", p_value)
            print("FrequencyTest Result:", result)
            
            # Prepare the response data
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text,
            }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            print("JSON Decode Error")
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    else:
        print("Invalid request method")
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)


@csrf_exempt  # Remove this in production or secure with CSRF token handling
def run_frequency_block_test(request):
    if request.method == 'POST':
        try:
            # Parse the binary data from the JSON body
            data = json.loads(request.body)
            binary_data = data.get('binary_data', '')

            if not binary_data:
                # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
                return JsonResponse({}, status=204)

            # Call the block_frequency method from the FrequencyTest class
            p_value, result = FrequencyTest.block_frequency(binary_data)

            print("run_frequency_block_test p_value:", p_value)
            print("run_frequency_block_test Result:", result)
            
            # Prepare the response data
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)



@csrf_exempt  # Remove this in production or secure with CSRF token handling
def run_runs_test(request):
    if request.method == 'POST':
        try:
            # Parse the binary data from the JSON body
            data = json.loads(request.body)
            binary_data = data.get('binary_data', '')

            if not binary_data:
                # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
                return JsonResponse({}, status=204)

            # Call the run_test method from the RunTest class
            p_value, result = RunTest.run_test(binary_data)

            print("run_runs_test p_value:", p_value)
            print("run_runs_test Result:", result)
            
            # Prepare the response data
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)



@csrf_exempt  # Remove this in production or secure with CSRF token handling
def run_longest_one_block_test(request):
    if request.method == 'POST':
        try:
            # Parse the binary data from the JSON body
            data = json.loads(request.body)
            binary_data = data.get('binary_data', '')

            if not binary_data:
                # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
                return JsonResponse({}, status=204)

            # Call the longest_one_block_test method from RunTest
            p_value, result, error_message = RunTest.longest_one_block_test(binary_data)

            print("run_longest_one_block_test p_value:", p_value)
            print("run_longest_one_block_test Result:", result)
            
            # Prepare the response data
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text,
                'error_message': error_message  # Add error_message to response if needed
            }

            return JsonResponse(response_data)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)


@csrf_exempt  # Remove this in production or secure with CSRF token handling
def run_approximate_entropy_test(request):
    if request.method == 'POST':
        try:
            # Parse the binary data from the JSON body
            data = json.loads(request.body)
            binary_data = data.get('binary_data', '')

            if not binary_data:
                # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
                return JsonResponse({}, status=204)

            # Call the approximate_entropy_test method from ApproximateEntropy
            p_value, result = ApproximateEntropy.approximate_entropy_test(binary_data)

            print("run_approximate_entropy_test p_value:", p_value)
            print("run_approximate_entropy_test Result:", result)
            
            # Prepare the response data
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)



@csrf_exempt  # Remove this in production or secure with CSRF token handling
def run_linear_complexity_test(request):
    if request.method == 'POST':
        try:
            # Parse the binary data from the JSON body
            data = json.loads(request.body)
            binary_data = data.get('binary_data', '')

            if not binary_data:
                # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
                return JsonResponse({}, status=204)

            # Call the linear_complexity_test method from ComplexityTest
            p_value, result = ComplexityTest.linear_complexity_test(binary_data)

            print("run_linear_complexity_test p_value:", p_value)
            print("run_linear_complexity_test Result:", result)
            
            # Prepare the response data
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)
    


@csrf_exempt  # Remove this in production or secure with CSRF token handling
def run_non_overlapping_test(request):
    if request.method == 'POST':
        try:
            # Parse the binary data from the JSON body
            data = json.loads(request.body)
            binary_data = data.get('binary_data', '')

            if not binary_data:
                # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
                return JsonResponse({}, status=204)

            # Call the non_overlapping_test method from TemplateMatching
            p_value, result = TemplateMatching.non_overlapping_test(binary_data)

            print("run_non_overlapping_test p_value:", p_value)
            print("run_non_overlapping_test Result:", result)
            
            # Prepare the response data
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)



# def run_overlapping_test(request):
#     # Example binary data received from the request query parameters
#     binary_data = request.GET.get('binary_data', '')

#     # Print the request URL and parameters
#     # print("Request URL:", request.get_full_path())
#     # print("Request Parameters:", request.GET)

#     # Call the block_frequency method
#     p_value, result = TemplateMatching.overlapping_patterns(binary_data)

#     print("run_overlapping_test p_value:", p_value)
#     print("run_overlapping_test Result:", result)
    
#     # Prepare the response data
#     if result:
#         result_text = "random number"
#     else:
#         result_text = "non-random number"
        
#     response_data = {
#         'p_value': p_value,
#         'result': result_text
#     }

#     return JsonResponse(response_data)
@csrf_exempt  # Remove this in production or secure with CSRF token handling
def run_overlapping_test(request):
    if request.method == 'POST':
        try:
            # Parse the binary data from the JSON body
            data = json.loads(request.body)
            binary_data = data.get('binary_data', '')

            if not binary_data:
                # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
                return JsonResponse({}, status=204)

            # Call the overlapping_patterns method from TemplateMatching
            p_value, result = TemplateMatching.overlapping_patterns(binary_data)

            print("run_overlapping_test p_value:", p_value)
            print("run_overlapping_test Result:", result)
            
            # Prepare the response data
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)


# def run_statistical_test(request):
#     # Example binary data received from the request query parameters
#     binary_data = request.GET.get('binary_data', '')

#     # Print the request URL and parameters
#     # print("Request URL:", request.get_full_path())
#     # print("Request Parameters:", request.GET)

#     # Call the block_frequency method
#     p_value, result = Universal.statistical_test(binary_data)

#     print("run_statistical_test p_value:", p_value)
#     print("run_statistical_test Result:", result)
    
#     # Prepare the response data
#     if result:
#         result_text = "random number"
#     else:
#         result_text = "non-random number"
        
#     response_data = {
#         'p_value': p_value,
#         'result': result_text
#     }

#     return JsonResponse(response_data)

@csrf_exempt  # Remove this in production or secure with CSRF token handling
def run_statistical_test(request):
    if request.method == 'POST':
        try:
            # Parse the binary data from the JSON body
            data = json.loads(request.body)
            binary_data = data.get('binary_data', '')

            if not binary_data:
                # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
                return JsonResponse({}, status=204)

            # Call the statistical_test method from Universal
            p_value, result = Universal.statistical_test(binary_data)

            print("run_statistical_test p_value:", p_value)
            print("run_statistical_test Result:", result)
            
            # Prepare the response data
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)


# def run_serial_test(request):
#     # Example binary data received from the request query parameters
#     binary_data = request.GET.get('binary_data', '')

#     if not binary_data:
#         # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
#         return JsonResponse({}, status=204)

#     # Print the request URL and parameters
#     # print("Request URL:", request.get_full_path())
#     # print("Request Parameters:", request.GET)

#     # Call the block_frequency method
#     p_value, result = Serial.serial_test(binary_data)

#     print("run_serial_test p_value:", p_value)
#     print("run_serial_test Result:", result)
    
#     # Prepare the response data
#     if result:
#         result_text = "random number"
#     else:
#         result_text = "non-random number"
        
#     response_data = {
#         'p_value': p_value,
#         'result': result_text
#     }

#     return JsonResponse(response_data)

@csrf_exempt  # Use this only in development; secure with CSRF token handling for production
def run_serial_test(request):
    if request.method == 'POST':
        try:
            # Parse the binary data from the JSON body
            data = json.loads(request.body)
            binary_data = data.get('binary_data', '')

            if not binary_data:
                # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
                return JsonResponse({}, status=204)

            # Call the serial_test method from Serial
            p_value, result = Serial.serial_test(binary_data)

            print("run_serial_test p_value:", p_value)
            print("run_serial_test Result:", result)
            
            # Prepare the response data
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)



# def run_cumulative_sums_test(request):
#     # Example binary data received from the request query parameters
#     binary_data = request.GET.get('binary_data', '')

#     # # Print the request URL and parameters
#     # print("Request URL:", request.get_full_path())
#     # print("Request Parameters:", request.GET)

#     # Call the block_frequency method
#     p_value, result = CumulativeSums.cumulative_sums_test(binary_data)

#     print("run_cumulative_sums_test p_value:", p_value)
#     print("run_cumulative_sums_test Result:", result)
    
#     # Prepare the response data
#     if result:
#         result_text = "random number"
#     else:
#         result_text = "non-random number"
        
#     response_data = {
#         'p_value': p_value,
#         'result': result_text
#     }

#     return JsonResponse(response_data)

@csrf_exempt
def run_cumulative_sums_test(request):
    if request.method == 'POST':
        try:
            # Parse binary data from JSON body
            data = json.loads(request.body)
           
            binary_data = data.get('binary_data', '')
            print('hello', binary_data)
           
           
            # Call the cumulative_sums_test method from CumulativeSums
            try:
                p_value, result = CumulativeSums.cumulative_sums_test(binary_data)
            except ValueError as e:
                return JsonResponse({"error": f"Processing error: {str(e)}"}, status=500)

            print("run_cumulative_sums_test p_value:", p_value)
            print("run_cumulative_sums_test Result:", result)
            
            # Prepare the response data
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)

# def run_autocorrelation_test(request):
#     # Example binary data received from the request query parameters
#     binary_data = request.GET.get('binary_data', '')

#     if not binary_data:
#         # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
#         return JsonResponse({}, status=204)


#     max_lag = 20 

#     # Print the request URL and parameters
#     # print("Request URL:", request.get_full_path())
#     # print("Request Parameters:", request.GET)

#     # Call the block_frequency method
#     p_value, result = AutocorrelationTest.autocorrelation_test(binary_data, max_lag, verbose=True)

#     print("run_autocorrelation_test p_value:", p_value)
#     print("run_autocorrelation_test Result:", result)
    
#     # Prepare the response data
#     if result:
#         result_text = "random number"
#     else:
#         result_text = "non-random number"
        
#     response_data = {
#         'p_value': p_value,
#         'result': result_text
#     }

#     return JsonResponse(response_data)


@csrf_exempt  # Use only in development; ensure CSRF handling in production
def run_autocorrelation_test(request):
    if request.method == 'POST':
        try:
            # Parse JSON data
            data = json.loads(request.body)
            binary_data = data.get('binary_data', '')

            if not binary_data:
                # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
                return JsonResponse({}, status=204)

            max_lag = data.get('max_lag', 20)  # Default value is 20 if not provided

            # Call the autocorrelation_test method from AutocorrelationTest
            p_value, result = AutocorrelationTest.autocorrelation_test(binary_data, max_lag, verbose=True)

            print("run_autocorrelation_test p_value:", p_value)
            print("run_autocorrelation_test Result:", result)
            
            # Prepare the response data
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)


# def run_adaptive_statistical_test(request):
#     # Example binary data received from the request query parameters
#     binary_data = request.GET.get('binary_data', '')

#     if not binary_data:
#         # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
#         return JsonResponse({}, status=204)

#     # Print the request URL and parameters
#     # print("Request URL:", request.get_full_path())
#     # print("Request Parameters:", request.GET)

#     # Call the block_frequency method
#     p_value, result = AdaptiveStatisticalTest.adaptive_statistical_test(binary_data)

#     print("run_adaptive_statistical_test p_value:", p_value)
#     print("run_adaptive_statistical_test Result:", result)
    
#     # Prepare the response data
#     if result:
#         result_text = "random number"
#     else:
#         result_text = "non-random number"
        
#     response_data = {
#         'p_value': p_value,
#         'result': result_text
#     }

#     return JsonResponse(response_data)

@csrf_exempt  # Use only in development; ensure CSRF handling in production
def run_adaptive_statistical_test(request):
    if request.method == 'POST':
        try:
            # Parse JSON data
            data = json.loads(request.body)
            binary_data = data.get('binary_data', '')

            if not binary_data:
                # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
                return JsonResponse({}, status=204)

            print('hi adaptive ',binary_data)
            # Call the adaptive_statistical_test method from AdaptiveStatisticalTest
            p_value, result = AdaptiveStatisticalTest.adaptive_statistical_test(binary_data)

            print("run_adaptive_statistical_test p_value:", p_value)
            print("run_adaptive_statistical_test Result:", result)
            
            # Prepare the response data
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)


# def run_random_excursions_test(request):
#     # Example binary data received from the request query parameters
#     binary_data = request.GET.get('binary_data', '')
   
#     if not binary_data:
#                 # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
#                 return JsonResponse({}, status=204)
#     # Print the request URL and parameters
#     # print("Request URL:", request.get_full_path())
#     # print("Request Parameters:", request.GET)

#     # Call the block_frequency method
#     chi_sq, p_value, result = RandomExcursions.random_excursions_test(binary_data)

#     print("run_random_excursions_test chi^2:", chi_sq)
#     print("run_random_excursions_test p_value:", p_value)
#     print("run_random_excursions_test Result:", result)
    
#     # Prepare the response data
#     if result:
#         result_text = "random number"
#     else:
#         result_text = "non-random number"
        
#     response_data = {
#         'chi^2': chi_sq,
#         'p_value': p_value,
#         'result': result_text
#     }

#     return JsonResponse(response_data)


@csrf_exempt  # Use only in development; ensure CSRF handling in production
def run_random_excursions_test(request):
    if request.method == 'POST':
        try:
            # Parse JSON data
            data = json.loads(request.body)
            binary_data = data.get('binary_data', '')

            if not binary_data:
                # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
                return JsonResponse({}, status=204)

            print('hi random excursions', binary_data)

            # Call the random_excursions_test method from RandomExcursions
            chi_sq, p_value, result = RandomExcursions.random_excursions_test(binary_data)

            print("run_random_excursions_test chi^2:", chi_sq)
            print("run_random_excursions_test p_value:", p_value)
            print("run_random_excursions_test Result:", result)

            # Prepare the response data
            result_text = "random number" if result else "non-random number"
            response_data = {
                'chi^2': chi_sq,
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)


# def random_excursions_variant_test(request):
#     # Example binary data received from the request query parameters
#     binary_data = request.GET.get('binary_data', '')

#     if not binary_data:
#             # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
#             return JsonResponse({}, status=204)
#     # Print the request URL and parameters
#     # print("Request URL:", request.get_full_path())
#     # print("Request Parameters:", request.GET)

#     # Call the block_frequency method
#     chi_sq, p_value, result = RandomExcursions.variant_test(binary_data)

#     print("random_excursions_variant_test chi^2:", chi_sq)
#     print("random_excursions_variant_test p_value:", p_value)
#     print("random_excursions_variant_test Result:", result)
    
#     # Prepare the response data
#     if result:
#         result_text = "random number"
#     else:
#         result_text = "non-random number"
        
#     response_data = {
#         'chi^2': chi_sq,
#         'p_value': p_value,
#         'result': result_text
#     }

#     return JsonResponse(response_data)

@csrf_exempt 
def random_excursions_variant_test(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)
            binary_data = data.get('binary_data', '')

            if not binary_data:
                # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
                return JsonResponse({}, status=204)

            # Call the variant_test method from RandomExcursions
            chi_sq, p_value, result = RandomExcursions.variant_test(binary_data)

            print("random_excursions_variant_test chi^2:", chi_sq)
            print("random_excursions_variant_test p_value:", p_value)
            print("random_excursions_variant_test Result:", result)

            # Prepare the response data
            result_text = "random number" if result else "non-random number"
            response_data = {
                'chi^2': chi_sq,
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
    
    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)


# def run_binary_matrix_rank_text(request):
#     # Example binary data received from the request query parameters
#     binary_data = request.GET.get('binary_data', '')

#     # # Print the request URL and parameters
#     # print("Request URL:", request.get_full_path())
#     # print("Request Parameters:", request.GET)

#     # Call the block_frequency method
#     p_value, result = Matrix.binary_matrix_rank_text(binary_data)

#     print("run_binary_matrix_rank_text p_value:", p_value)
#     print("run_binary_matrix_rank_text Result:", result)
    
#     # Prepare the response data
#     if result:
#         result_text = "random number"
#     else:
#         result_text = "non-random number"
        
#     response_data = {
#         'p_value': p_value,
#         'result': result_text
#     }

#     return JsonResponse(response_data)

@csrf_exempt  # Use this only in development; secure with CSRF token handling for production
def run_binary_matrix_rank_text(request):
    if request.method == 'POST':
        try:
            # Parse binary data from JSON body
            data = json.loads(request.body)
            binary_data = data.get('binary_data', '')

            if not binary_data:
                # If no binary data, return an empty JsonResponse with status code 204 (No Content)
                return JsonResponse({}, status=204)

            # Call the binary_matrix_rank_text method from Matrix
            p_value, result = Matrix.binary_matrix_rank_text(binary_data)

            print("run_binary_matrix_rank_text p_value:", p_value)
            print("run_binary_matrix_rank_text Result:", result)
            
            # Prepare the response data
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)


# def run_spectral_test(request):
#     # Example binary data received from the request query parameters
#     binary_data = request.GET.get('binary_data', '')

#     if not binary_data:
#         # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
#         return JsonResponse({}, status=204)
    
#     # Print the request URL and parameters
#     # print("Request URL:", request.get_full_path())
#     # print("Request Parameters:", request.GET)

#     # Call the block_frequency method
#     p_value, result = SpectralTest.spectral_test(binary_data)

#     print("run_spectral_test p_value:", p_value)
#     print("run_spectral_test Result:", result)
    
#     # Prepare the response data
#     if result:
#         result_text = "random number"
#     else:
#         result_text = "non-random number"
        
#     response_data = {
#         'p_value': p_value,
#         'result': result_text
#     }

#     return JsonResponse(response_data)

@csrf_exempt  # Use only in development; ensure CSRF handling in production
def run_spectral_test(request):
    if request.method == 'POST':
        try:
            # Parse binary data from JSON body
            data = json.loads(request.body)
            binary_data = data.get('binary_data', '')
            
            if not binary_data:
                # If no binary data, return an empty JsonResponse with status code 204 (No Content)
                return JsonResponse({}, status=204)
            
            # Call the spectral_test method from SpectralTest
            p_value, result = SpectralTest.spectral_test(binary_data)

            print("run_spectral_test p_value:", p_value)
            print("run_spectral_test Result:", result)
            
            # Prepare the response data
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)


# def run_birthday_spacings_test(request):
#     # Example binary data received from the request query parameters
#     binary_data_str = request.GET.get('binary_data', '')

#     # Print the request URL and parameters for debugging
#     # print("Request URL:", request.get_full_path())
#     # print("Request Parameters:", request.GET)

#     # Convert binary string to a list of integers
#     if binary_data_str:
#         # Ensure only '0' and '1' are considered
#         binary_data = [int(bit) for bit in binary_data_str if bit in '01']
#     else:
#         return JsonResponse({'error': 'Invalid or missing binary data.'}, status=400)

#     # Check if the converted data has at least two points
#     if len(binary_data) < 2:
#         return JsonResponse({'error': 'Insufficient data. At least two data points are required.'}, status=400)

#     # Call the Birthday Spacings Test method
#     p_value, result = BirthdaySpacingsTest.BirthdaySpacingsTest(binary_data)

#     print("run_birthday_spacings_test p_value:", p_value)
#     print("run_birthday_spacings_test Result:", result)

#     # Prepare the response data
#     result_text = "random number" if result else "non-random number"
        
#     response_data = {
#         'p_value': p_value,
#         'result': result_text
#     }

#     return JsonResponse(response_data)


@csrf_exempt
def run_birthday_spacings_test(request):
    if request.method == 'POST':
        try:
            # Parse JSON data
            data = json.loads(request.body)
            binary_data = data.get('binary_data', [])
            print('data is printing:',binary_data)

            

            if isinstance(binary_data, list):
                # If binary_data is a list, filter out any empty or whitespace-only strings
                filtered_binary_data = next((item for item in binary_data if item.strip()), None)
            elif isinstance(binary_data, str):
                # If binary_data is a string, just use it directly
                filtered_binary_data = binary_data.strip()  # Strip to remove any extra spaces or newlines
            else:
                # If neither string nor list, return an error
                return JsonResponse({"error": "Invalid data format for binary_data"}, status=400)

            if not filtered_binary_data:
                # If no valid binary string is found, return an error
                return JsonResponse({"error": "No valid binary data provided"}, status=400)

            
            # Call the Birthday Spacings Test method
            p_value, result = BirthdaySpacingsTest.BirthdaySpacingsTest(filtered_binary_data)

            # Prepare the response
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except ValueError as ve:
            # Handle invalid binary data conversion
            print("ValueError:", str(ve))
            return JsonResponse({"error": "Invalid binary data format"}, status=400)
        except Exception as e:
            # Log the error and return a 500 status code
            print("Error in run_birthday_spacings_test:", str(e))
            return JsonResponse({"error": "Internal server error"}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)


# def run_bitstream_test(request):
#     # Example binary data received from the request query parameters
#     binary_data = request.GET.get('binary_data', '')

#     if not binary_data:
#         # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
#         return JsonResponse({}, status=204)
    
#     # Print the request URL and parameters
#     # print("Request URL:", request.get_full_path())
#     # print("Request Parameters:", request.GET)

#     # Call the block_frequency method
#     p_value, result = BitstreamTest.BitstreamTest(binary_data)

#     print("run_bitstream_test p_value:", p_value)
#     print("run_bitstream_test Result:", result)
    
#     # Prepare the response data
#     if result:
#         result_text = "random number"
#     else:
#         result_text = "non-random number"
        
#     response_data = {
#         'p_value': p_value,
#         'result': result_text
#     }

#     return JsonResponse(response_data)


def run_bitstream_test(request):
    # Check if the request method is POST
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)
            binary_data = data.get('binary_data', '')

            # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
            if not binary_data:
                return JsonResponse({}, status=204)
            
            # Handle both string and list formats for binary_data
            if isinstance(binary_data, str):
                # If binary_data is a string, strip it of any leading/trailing spaces
                filtered_binary_data = binary_data.strip()
            elif isinstance(binary_data, list):
                # If binary_data is a list, filter out any empty or whitespace-only strings
                filtered_binary_data = next((item for item in binary_data if item.strip()), None)
            else:
                # If neither a string nor list, return an error
                return JsonResponse({"error": "Invalid data format for binary_data"}, status=400)

            # If no valid binary string is found, return an error
            if not filtered_binary_data:
                return JsonResponse({"error": "No valid binary data provided"}, status=400)

            # Call the BitstreamTest method
            p_value, result = BitstreamTest.BitstreamTest(filtered_binary_data)

            # Prepare the response
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except Exception as e:
            print("Error in run_bitstream_test:", str(e))
            return JsonResponse({"error": "Internal server error"}, status=500)
    else:
        # If the request method is not POST
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)


# def run_parking_lot_test(request):
#     # Example binary data received from the request query parameters
#     binary_data = request.GET.get('binary_data', '')

#     # Print the request URL and parameters
#     # print("Request URL:", request.get_full_path())
#     # print("Request Parameters:", request.GET)

#     # Call the block_frequency method
#     p_value, result = ParkingLotTest.ParkingLotTest(binary_data)

#     print("run_parking_lot_test p_value:", p_value)
#     print("run_parking_lot_test Result:", result)
    
#     # Prepare the response data
#     if result:
#         result_text = "random number"
#     else:
#         result_text = "non-random number"
        
#     response_data = {
#         'p_value': p_value,
#         'result': result_text
#     }

#     return JsonResponse(response_data)


@csrf_exempt
def run_parking_lot_test(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)
            binary_data = data.get('binary_data', '')

            # If no binary_data is provided, return an empty JsonResponse with status code 204 (No Content)
            if not binary_data:
                return JsonResponse({}, status=204)

            # Handle both string and list formats for binary_data
            if isinstance(binary_data, str):
                # If binary_data is a string, strip it of any leading/trailing spaces
                filtered_binary_data = binary_data.strip()
            elif isinstance(binary_data, list):
                # If binary_data is a list, filter out any empty or whitespace-only strings
                filtered_binary_data = next((item for item in binary_data if item.strip()), None)
            else:
                # If binary_data is neither a string nor a list, return an error
                return JsonResponse({"error": "Invalid data format for binary_data"}, status=400)

            # If no valid binary string is found, return an error
            if not filtered_binary_data:
                return JsonResponse({"error": "No valid binary data provided"}, status=400)

            print('Filtered binary data:', filtered_binary_data)

            # Call the Parking Lot Test method
            p_value, result = ParkingLotTest.ParkingLotTest(filtered_binary_data)

            # Prepare the response
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except ValueError as ve:
            # Handle invalid binary data conversion
            print("ValueError:", str(ve))
            return JsonResponse({"error": "Invalid binary data format"}, status=400)
        except Exception as e:
            # Log the error and return a 500 status code
            print("Error in run_parking_lot_test:", str(e))
            return JsonResponse({"error": "Internal server error"}, status=500)
    else:
        # If the request method is not POST
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)

# def run_overlapping_5_test(request):
#     # Example binary data received from the request query parameters
#     binary_data = request.GET.get('binary_data', '')

#     if not binary_data:
#         # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
#         return JsonResponse({}, status=204)
    
#     # Print the request URL and parameters
#     # print("Request URL:", request.get_full_path())
#     # print("Request Parameters:", request.GET)

#     # Call the block_frequency method
#     p_value, result = Overlapping5PermutationTest.Overlapping5PermutationTest(binary_data)

#     print("run_overlapping_5_test p_value:", p_value)
#     print("run_overlapping_5_test Result:", result)
    
#     # Prepare the response data
#     if result:
#         result_text = "random number"
#     else:
#         result_text = "non-random number"
        
#     response_data = {
#         'p_value': p_value,
#         'result': result_text
#     }

#     return JsonResponse(response_data)

@csrf_exempt
def run_overlapping_5_test(request):
    if request.method == 'POST':
        try:
            # Parse JSON data
            data = json.loads(request.body)
            binary_data = data.get('binary_data', [])

            if not binary_data:
                return JsonResponse({}, status=204)


            if isinstance(binary_data, str):
                # If binary_data is a string, strip it of any leading/trailing spaces
                filtered_binary_data = binary_data.strip()
            elif isinstance(binary_data, list):
                # If binary_data is a list, filter out any empty or whitespace-only strings
                filtered_binary_data = next((item for item in binary_data if item.strip()), None)
            else:
                # If binary_data is neither a string nor a list, return an error
                return JsonResponse({"error": "Invalid data format for binary_data"}, status=400)


            # Extract the first non-empty, non-whitespace string
            # filtered_binary_data = next((item for item in binary_data if item.strip()), None)

            if not filtered_binary_data:
                # If no valid binary string is found, return an error
                return JsonResponse({"error": "No valid binary data provided"}, status=400)

            # Call the Overlapping 5 Permutation Test method
            p_value, result = Overlapping5PermutationTest.Overlapping5PermutationTest(filtered_binary_data)

            # Prepare the response
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except ValueError as ve:
            # Handle invalid binary data conversion
            print("ValueError:", str(ve))
            return JsonResponse({"error": "Invalid binary data format"}, status=400)
        except Exception as e:
            # Log the error and return a 500 status code
            print("Error in run_overlapping_5_test:", str(e))
            return JsonResponse({"error": "Internal server error"}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)

@csrf_exempt
def run_minimum_distance_test(request):
    if request.method == 'POST':
        try:
            # Parse JSON data
            data = json.loads(request.body)
            binary_data = data.get('binary_data', [])

            if not binary_data:
                return JsonResponse({}, status=204)


            if isinstance(binary_data, str):
                # If binary_data is a string, strip it of any leading/trailing spaces
                filtered_binary_data = binary_data.strip()
            elif isinstance(binary_data, list):
                # If binary_data is a list, filter out any empty or whitespace-only strings
                filtered_binary_data = next((item for item in binary_data if item.strip()), None)
            else:
                # If binary_data is neither a string nor a list, return an error
                return JsonResponse({"error": "Invalid data format for binary_data"}, status=400)


            # Extract the first non-empty, non-whitespace string
            # filtered_binary_data = next((item for item in binary_data if item.strip()), None)

            if not filtered_binary_data:
                # If no valid binary string is found, return an error
                return JsonResponse({"error": "No valid binary data provided"}, status=400)

            # Call the Minimum Distance Test method
            p_value, result = MinimumDistanceTest.MinimumDistanceTest(filtered_binary_data)

            # Prepare the response
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except ValueError as ve:
            # Handle invalid binary data conversion
            print("ValueError:", str(ve))
            return JsonResponse({"error": "Invalid binary data format"}, status=400)
        except Exception as e:
            # Log the error and return a 500 status code
            print("Error in run_minimum_distance_test:", str(e))
            return JsonResponse({"error": "Internal server error"}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)




@csrf_exempt
def run_31matrix_test(request):
    if request.method == 'POST':
        try:
            # Parse JSON data
            data = json.loads(request.body)
            binary_data = data.get('binary_data', [])

            if not binary_data:
                return JsonResponse({}, status=204)


            if isinstance(binary_data, str):
                # If binary_data is a string, strip it of any leading/trailing spaces
                filtered_binary_data = binary_data.strip()
            elif isinstance(binary_data, list):
                # If binary_data is a list, filter out any empty or whitespace-only strings
                filtered_binary_data = next((item for item in binary_data if item.strip()), None)
            else:
                # If binary_data is neither a string nor a list, return an error
                return JsonResponse({"error": "Invalid data format for binary_data"}, status=400)


            # Extract the first non-empty, non-whitespace string
            # filtered_binary_data = next((item for item in binary_data if item.strip()), None)

            if not filtered_binary_data:
                # If no valid binary string is found, return an error
                return JsonResponse({"error": "No valid binary data provided"}, status=400)

            # Call the Ranks 31x31 Matrices Test method
            p_value, result = Ranks31x31MatricesTest.Ranks31x31MatricesTest(filtered_binary_data)

            # Prepare the response
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except ValueError as ve:
            # Handle invalid binary data conversion
            print("ValueError:", str(ve))
            return JsonResponse({"error": "Invalid binary data format"}, status=400)
        except Exception as e:
            # Log the error and return a 500 status code
            print("Error in run_31matrix_test:", str(e))
            return JsonResponse({"error": "Internal server error"}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)

@csrf_exempt
def run_spheres_test(request):
    if request.method == 'POST':
        try:
            # Parse JSON data
            data = json.loads(request.body)
            binary_data = data.get('binary_data', [])

            if not binary_data:
                return JsonResponse({}, status=204)


            if isinstance(binary_data, str):
                # If binary_data is a string, strip it of any leading/trailing spaces
                filtered_binary_data = binary_data.strip()
            elif isinstance(binary_data, list):
                # If binary_data is a list, filter out any empty or whitespace-only strings
                filtered_binary_data = next((item for item in binary_data if item.strip()), None)
            else:
                # If binary_data is neither a string nor a list, return an error
                return JsonResponse({"error": "Invalid data format for binary_data"}, status=400)


            # Extract the first non-empty, non-whitespace string
            
            if not filtered_binary_data:
                # If no valid binary string is found, return an error
                return JsonResponse({"error": "No valid binary data provided"}, status=400)

            # Call the Spheres 3D Test method
            p_value, result = Spheres3DTest.Spheres3DTest(filtered_binary_data)

            # Prepare the response
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except ValueError as ve:
            # Handle invalid binary data conversion
            print("ValueError:", str(ve))
            return JsonResponse({"error": "Invalid binary data format"}, status=400)
        except Exception as e:
            # Log the error and return a 500 status code
            print("Error in run_spheres_test:", str(e))
            return JsonResponse({"error": "Internal server error"}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)

@csrf_exempt
def run_32matrix_test(request):
    if request.method == 'POST':
        try:
            # Parse JSON data
            data = json.loads(request.body)
            binary_data = data.get('binary_data', [])

            if not binary_data:
                return JsonResponse({}, status=204)


            if isinstance(binary_data, str):
                # If binary_data is a string, strip it of any leading/trailing spaces
                filtered_binary_data = binary_data.strip()
            elif isinstance(binary_data, list):
                # If binary_data is a list, filter out any empty or whitespace-only strings
                filtered_binary_data = next((item for item in binary_data if item.strip()), None)
            else:
                # If binary_data is neither a string nor a list, return an error
                return JsonResponse({"error": "Invalid data format for binary_data"}, status=400)

            if not filtered_binary_data:
                # If no valid binary string is found, return an error
                return JsonResponse({"error": "No valid binary data provided"}, status=400)

            # Call the Ranks 32x32 Matrices Test method
            p_value, result = Ranks32x32MatricesTest.Ranks32x32MatricesTest(filtered_binary_data)

            # Prepare the response
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except ValueError as ve:
            # Handle invalid binary data conversion
            print("ValueError:", str(ve))
            return JsonResponse({"error": "Invalid binary data format"}, status=400)
        except Exception as e:
            # Log the error and return a 500 status code
            print("Error in run_32matrix_test:", str(e))
            return JsonResponse({"error": "Internal server error"}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)



@csrf_exempt
def run_craps_test(request):
    if request.method == 'POST':
        try:
            # Parse JSON data
            data = json.loads(request.body)
            binary_data = data.get('binary_data', [])

            if not binary_data:
                return JsonResponse({}, status=204)


            if isinstance(binary_data, str):
                # If binary_data is a string, strip it of any leading/trailing spaces
                filtered_binary_data = binary_data.strip()
            elif isinstance(binary_data, list):
                # If binary_data is a list, filter out any empty or whitespace-only strings
                filtered_binary_data = next((item for item in binary_data if item.strip()), None)
            else:
                # If binary_data is neither a string nor a list, return an error
                return JsonResponse({"error": "Invalid data format for binary_data"}, status=400)

            if not filtered_binary_data:
                return JsonResponse({"error": "No valid binary data provided"}, status=400)

            # Call the Craps Test method
            p_value, result = CrapsTest.CrapsTest(filtered_binary_data)

            # Prepare the response
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except ValueError as ve:
            print("ValueError:", str(ve))
            return JsonResponse({"error": "Invalid binary data format"}, status=400)
        except Exception as e:
            print("Error in run_craps_test:", str(e))
            return JsonResponse({"error": "Internal server error"}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)


@csrf_exempt
def run_bitstream_test(request):
    if request.method == 'POST':
        try:
            # Parse JSON data
            data = json.loads(request.body)
            binary_data = data.get('binary_data', [])

            if not binary_data:
                return JsonResponse({}, status=204)


            if isinstance(binary_data, str):
                # If binary_data is a string, strip it of any leading/trailing spaces
                filtered_binary_data = binary_data.strip()
            elif isinstance(binary_data, list):
                # If binary_data is a list, filter out any empty or whitespace-only strings
                filtered_binary_data = next((item for item in binary_data if item.strip()), None)
            else:
                # If binary_data is neither a string nor a list, return an error
                return JsonResponse({"error": "Invalid data format for binary_data"}, status=400)

            if not filtered_binary_data:
                return JsonResponse({"error": "No valid binary data provided"}, status=400)

            # Call the Bitstream Test method
            p_value, result = BitstreamTest.BitstreamTest(filtered_binary_data)

            # Prepare the response
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except ValueError as ve:
            print("ValueError:", str(ve))
            return JsonResponse({"error": "Invalid binary data format"}, status=400)
        except Exception as e:
            print("Error in run_bitstream_test:", str(e))
            return JsonResponse({"error": "Internal server error"}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)


@csrf_exempt
def run_gcd_test(request):
    if request.method == 'POST':
        try:
            # Parse JSON data
            data = json.loads(request.body)
            binary_data = data.get('binary_data', [])

            if not binary_data:
                return JsonResponse({}, status=204)


            if isinstance(binary_data, str):
                # If binary_data is a string, strip it of any leading/trailing spaces
                filtered_binary_data = binary_data.strip()
            elif isinstance(binary_data, list):
                # If binary_data is a list, filter out any empty or whitespace-only strings
                filtered_binary_data = next((item for item in binary_data if item.strip()), None)
            else:
                # If binary_data is neither a string nor a list, return an error
                return JsonResponse({"error": "Invalid data format for binary_data"}, status=400)

            if not filtered_binary_data:
                return JsonResponse({"error": "No valid binary data provided"}, status=400)

            # Call the GCD Test method
            p_value, result = MarsagliaTsangGCDTest.MarsagliaTsangGCDTest(filtered_binary_data)

            # Prepare the response
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except ValueError as ve:
            print("ValueError:", str(ve))
            return JsonResponse({"error": "Invalid binary data format"}, status=400)
        except Exception as e:
            print("Error in run_gcd_test:", str(e))
            return JsonResponse({"error": "Internal server error"}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)



@csrf_exempt
def run_opso_test(request):
    if request.method == 'POST':
        try:
            # Parse JSON data
            data = json.loads(request.body)
            binary_data = data.get('binary_data', [])

            if not binary_data:
                return JsonResponse({}, status=204)


            if isinstance(binary_data, str):
                # If binary_data is a string, strip it of any leading/trailing spaces
                filtered_binary_data = binary_data.strip()
            elif isinstance(binary_data, list):
                # If binary_data is a list, filter out any empty or whitespace-only strings
                filtered_binary_data = next((item for item in binary_data if item.strip()), None)
            else:
                # If binary_data is neither a string nor a list, return an error
                return JsonResponse({"error": "Invalid data format for binary_data"}, status=400)

            if not filtered_binary_data:
                return JsonResponse({"error": "No valid binary data provided"}, status=400)

            # Call the OPSO Test method
            p_value, result = OPSOTest.OPSOTest(filtered_binary_data)

            # Prepare the response
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except ValueError as ve:
            print("ValueError:", str(ve))
            return JsonResponse({"error": "Invalid binary data format"}, status=400)
        except Exception as e:
            print("Error in run_opso_test:", str(e))
            return JsonResponse({"error": "Internal server error"}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)


@csrf_exempt
def run_oqso_test(request):
    if request.method == 'POST':
        try:
            # Parse JSON data
            data = json.loads(request.body)
            binary_data = data.get('binary_data', [])

            if not binary_data:
                return JsonResponse({}, status=204)


            if isinstance(binary_data, str):
                # If binary_data is a string, strip it of any leading/trailing spaces
                filtered_binary_data = binary_data.strip()
            elif isinstance(binary_data, list):
                # If binary_data is a list, filter out any empty or whitespace-only strings
                filtered_binary_data = next((item for item in binary_data if item.strip()), None)
            else:
                # If binary_data is neither a string nor a list, return an error
                return JsonResponse({"error": "Invalid data format for binary_data"}, status=400)

            if not filtered_binary_data:
                return JsonResponse({"error": "No valid binary data provided"}, status=400)

            # Call the OQSO Test method
            p_value, result = OQSOTest.OQSOTest(filtered_binary_data)

            # Prepare the response
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except ValueError as ve:
            print("ValueError:", str(ve))
            return JsonResponse({"error": "Invalid binary data format"}, status=400)
        except Exception as e:
            print("Error in run_oqso_test:", str(e))
            return JsonResponse({"error": "Internal server error"}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)


@csrf_exempt
def run_dna_test(request):
    if request.method == 'POST':
        try:
            # Parse JSON data
            data = json.loads(request.body)
            binary_data = data.get('binary_data', [])

            if not binary_data:
                return JsonResponse({}, status=204)


            if isinstance(binary_data, str):
                # If binary_data is a string, strip it of any leading/trailing spaces
                filtered_binary_data = binary_data.strip()
            elif isinstance(binary_data, list):
                # If binary_data is a list, filter out any empty or whitespace-only strings
                filtered_binary_data = next((item for item in binary_data if item.strip()), None)
            else:
                # If binary_data is neither a string nor a list, return an error
                return JsonResponse({"error": "Invalid data format for binary_data"}, status=400)

            if not filtered_binary_data:
                return JsonResponse({"error": "No valid binary data provided"}, status=400)

            # Call the DNA Test method
            p_value, result = DNATest.DNATest(filtered_binary_data)

            # Prepare the response
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except ValueError as ve:
            print("ValueError:", str(ve))
            return JsonResponse({"error": "Invalid binary data format"}, status=400)
        except Exception as e:
            print("Error in run_dna_test:", str(e))
            return JsonResponse({"error": "Internal server error"}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)


@csrf_exempt
def run_count_one_test(request):
    if request.method == 'POST':
        try:
            # Parse JSON data
            data = json.loads(request.body)
            binary_data = data.get('binary_data', [])

            if not binary_data:
                return JsonResponse({}, status=204)


            if isinstance(binary_data, str):
                # If binary_data is a string, strip it of any leading/trailing spaces
                filtered_binary_data = binary_data.strip()
            elif isinstance(binary_data, list):
                # If binary_data is a list, filter out any empty or whitespace-only strings
                filtered_binary_data = next((item for item in binary_data if item.strip()), None)
            else:
                # If binary_data is neither a string nor a list, return an error
                return JsonResponse({"error": "Invalid data format for binary_data"}, status=400)

            
            if not filtered_binary_data:
                return JsonResponse({"error": "No valid binary data provided"}, status=400)

            # Call the Count The 1s Stream Test method
            p_value, result = CountThe1sStreamTest.CountThe1sStreamTest(filtered_binary_data)

            # Prepare the response
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except ValueError as ve:
            print("ValueError:", str(ve))
            return JsonResponse({"error": "Invalid binary data format"}, status=400)
        except Exception as e:
            print("Error in run_count_one_test:", str(e))
            return JsonResponse({"error": "Internal server error"}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)



@csrf_exempt
def run_count_one_byte_test(request):
    if request.method == 'POST':
        try:
            # Parse JSON data
            data = json.loads(request.body)
            binary_data = data.get('binary_data', [])

            if not binary_data:
                return JsonResponse({}, status=204)


            if isinstance(binary_data, str):
                # If binary_data is a string, strip it of any leading/trailing spaces
                filtered_binary_data = binary_data.strip()
            elif isinstance(binary_data, list):
                # If binary_data is a list, filter out any empty or whitespace-only strings
                filtered_binary_data = next((item for item in binary_data if item.strip()), None)
            else:
                # If binary_data is neither a string nor a list, return an error
                return JsonResponse({"error": "Invalid data format for binary_data"}, status=400)

            # Call the CountThe1sByteTest method with the binary data
            p_value, result = CountThe1sByteTest.CountThe1sByteTest(filtered_binary_data)

            # Prepare the response based on the result
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except Exception as e:
            print("Error in run_count_one_byte_test:", str(e))
            return JsonResponse({"error": "Internal server error"}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)

@csrf_exempt
def run_simple_gcd_test(request):
    if request.method == 'POST':
        try:
            # Parse JSON data
            data = json.loads(request.body)
            binary_data = data.get('binary_data', [])

            if not binary_data:
                return JsonResponse({}, status=204)


            if isinstance(binary_data, str):
                # If binary_data is a string, strip it of any leading/trailing spaces
                filtered_binary_data = binary_data.strip()
            elif isinstance(binary_data, list):
                # If binary_data is a list, filter out any empty or whitespace-only strings
                filtered_binary_data = next((item for item in binary_data if item.strip()), None)
            else:
                # If binary_data is neither a string nor a list, return an error
                return JsonResponse({"error": "Invalid data format for binary_data"}, status=400)

            if not filtered_binary_data:
                return JsonResponse({"error": "No valid binary data provided"}, status=400)


            # Call the Marsaglia Tsang Simple GCD Test method with the binary data
            p_value, result = MarsagliaTsangSimpleGCDTest.MarsagliaTsangSimpleGCDTest(filtered_binary_data)

            # Prepare the response based on the result
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except Exception as e:
            print("Error in run_simple_gcd_test:", str(e))
            return JsonResponse({"error": "Internal server error"}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)



@csrf_exempt
def run_general_minimum_distance_test(request):
    if request.method == 'POST':
        try:
            # Parse JSON data
            data = json.loads(request.body)
            binary_data = data.get('binary_data', [])

            if not binary_data:
                return JsonResponse({}, status=204)


            if isinstance(binary_data, str):
                # If binary_data is a string, strip it of any leading/trailing spaces
                filtered_binary_data = binary_data.strip()
            elif isinstance(binary_data, list):
                # If binary_data is a list, filter out any empty or whitespace-only strings
                filtered_binary_data = next((item for item in binary_data if item.strip()), None)
            else:
                # If binary_data is neither a string nor a list, return an error
                return JsonResponse({"error": "Invalid data format for binary_data"}, status=400)

            if not filtered_binary_data:
                return JsonResponse({"error": "No valid binary data provided"}, status=400)


            # Call the Generalized Minimum Distance Test method with the binary data
            p_value, result = GeneralizedMinimumDistanceTest.GeneralizedMinimumDistanceTest(filtered_binary_data)

            # Prepare the response based on the result
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except Exception as e:
            print("Error in run_general_minimum_distance_test:", str(e))
            return JsonResponse({"error": "Internal server error"}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)


@csrf_exempt
def run_u01_linear_complexity_test(request):
    if request.method == 'POST':
        try:
            # Parse JSON data
            data = json.loads(request.body)
            binary_data = data.get('binary_data', [])

            if not binary_data:
                return JsonResponse({}, status=204)


            if isinstance(binary_data, str):
                # If binary_data is a string, strip it of any leading/trailing spaces
                filtered_binary_data = binary_data.strip()
            elif isinstance(binary_data, list):
                # If binary_data is a list, filter out any empty or whitespace-only strings
                filtered_binary_data = next((item for item in binary_data if item.strip()), None)
            else:
                # If binary_data is neither a string nor a list, return an error
                return JsonResponse({"error": "Invalid data format for binary_data"}, status=400)

            if not filtered_binary_data:
                return JsonResponse({"error": "No valid binary data provided"}, status=400)


            # Call the TestU01 Linear Complexity Test method with the binary data
            p_value, result = TestU01LinearComplexityTest.TestU01LinearComplexityTest(filtered_binary_data)

            # Prepare the response based on the result
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except Exception as e:
            print("Error in run_u01_linear_complexity_test:", str(e))
            return JsonResponse({"error": "Internal server error"}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)


@csrf_exempt
def run_u01_longest_repeated_substring_test(request):
    if request.method == 'POST':
        try:
            # Parse JSON data
            data = json.loads(request.body)
            binary_data = data.get('binary_data', [])

            if not binary_data:
                return JsonResponse({}, status=204)


            if isinstance(binary_data, str):
                # If binary_data is a string, strip it of any leading/trailing spaces
                filtered_binary_data = binary_data.strip()
            elif isinstance(binary_data, list):
                # If binary_data is a list, filter out any empty or whitespace-only strings
                filtered_binary_data = next((item for item in binary_data if item.strip()), None)
            else:
                # If binary_data is neither a string nor a list, return an error
                return JsonResponse({"error": "Invalid data format for binary_data"}, status=400)

            if not filtered_binary_data:
                return JsonResponse({"error": "No valid binary data provided"}, status=400)


            # Call the TestU01 Longest Repeated Substring Test method with the binary data
            p_value, result = TestU01LongestRepeatedSubstringTest.TestU01LongestRepeatedSubstringTest(filtered_binary_data)

            # Prepare the response based on the result
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except Exception as e:
            print("Error in run_u01_longest_repeated_substring_test:", str(e))
            return JsonResponse({"error": "Internal server error"}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)


@csrf_exempt
def run_matrix_rank_test(request):
    if request.method == 'POST':
        try:
            # Parse JSON data
            data = json.loads(request.body)
            binary_data = data.get('binary_data', [])

            if not binary_data:
                return JsonResponse({}, status=204)


            if isinstance(binary_data, str):
                # If binary_data is a string, strip it of any leading/trailing spaces
                filtered_binary_data = binary_data.strip()
            elif isinstance(binary_data, list):
                # If binary_data is a list, filter out any empty or whitespace-only strings
                filtered_binary_data = next((item for item in binary_data if item.strip()), None)
            else:
                # If binary_data is neither a string nor a list, return an error
                return JsonResponse({"error": "Invalid data format for binary_data"}, status=400)

            if not filtered_binary_data:
                return JsonResponse({"error": "No valid binary data provided"}, status=400)


            # Call the TestU01 Matrix Rank Test method with the binary data
            p_value, result = TestU01MatrixRankTest.TestU01MatrixRankTest(filtered_binary_data)

            # Prepare the response based on the result
            result_text = "random number" if result else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except Exception as e:
            print("Error in run_matrix_rank_test:", str(e))
            return JsonResponse({"error": "Internal server error"}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)



@csrf_exempt  # Remove this in production, only for testing purposes
def run_chi_square_test(request):
    if request.method == 'POST':
        try:
            # Parse the binary data from the JSON body
            data = json.loads(request.body)
            binary_data = data.get('binary_data', '')

            # Ensure binary_data is in the expected format, otherwise return an error
            if not binary_data:
                return JsonResponse({"error": "binary_data is missing or empty"}, status=400)

            # Call the chi_square_test method from the ChiSquareTest class
            p_value, result = ChiSquareTest.ChiSquareTest(binary_data)

            print("ChiSquareTest p_value:", p_value)  # Debugging line
            print("ChiSquareTest Result:", result)    # Debugging line
            
            # Prepare the response data
            result_text = "random number" if result == 1 else "non-random number"
            response_data = {
                'p_value': p_value,
                'result': result_text
            }

            return JsonResponse(response_data)
        
        except json.JSONDecodeError:
            print("JSON Decode Error")  # Debugging line
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    else:
        print("Invalid request method")  # Debugging line
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)



@csrf_exempt
def run_mcv_test(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            binary_data = data.get('binary_data', '')

            if not binary_data:
                return JsonResponse({"error": "binary_data is missing or empty"}, status=400)

            p_value, result = MostCommonValueTest.MostCommonValueTest(binary_data)

            result_text = "random number" if result == 1 else "non-random number"
            return JsonResponse({'p_value': p_value, 'result': result_text})
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)

@csrf_exempt
def run_collision_test(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            binary_data = data.get('binary_data', '')

            if not binary_data:
                return JsonResponse({"error": "binary_data is missing or empty"}, status=400)

            p_value, result = CollisionTest.CollisionTest(binary_data)

            result_text = "random number" if result == 1 else "non-random number"
            return JsonResponse({'p_value': p_value, 'result': result_text})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)

@csrf_exempt
def run_markov_test(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            binary_data = data.get('binary_data', '')

            if not binary_data:
                return JsonResponse({"error": "binary_data is missing or empty"}, status=400)

            p_value, result = MarkovTest.MarkovTest(binary_data)

            result_text = "random number" if result == 1 else "non-random number"
            return JsonResponse({'p_value': p_value, 'result': result_text})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)

@csrf_exempt
def run_compression_test(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            binary_data = data.get('binary_data', '')

            if not binary_data:
                return JsonResponse({"error": "binary_data is missing or empty"}, status=400)

            p_value, result = CompressionTest.CompressionTest(binary_data)

            result_text = "random number" if result == 1 else "non-random number"
            return JsonResponse({'p_value': p_value, 'result': result_text})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)

@csrf_exempt
def run_t_tuple_test(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            binary_data = data.get('binary_data', '')

            if not binary_data:
                return JsonResponse({"error": "binary_data is missing or empty"}, status=400)

            p_value, result = TTupleTest.TTupleTest(binary_data)

            result_text = "random number" if result == 1 else "non-random number"
            return JsonResponse({'p_value': p_value, 'result': result_text})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)

@csrf_exempt
def run_longest_repeated_substring_test(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            binary_data = data.get('binary_data', '')

            if not binary_data:
                return JsonResponse({"error": "binary_data is missing or empty"}, status=400)

            p_value, result = TestU01LongestRepeatedSubstringTest.TestU01LongestRepeatedSubstringTest(binary_data)

            result_text = "random number" if result == 1 else "non-random number"
            return JsonResponse({'p_value': p_value, 'result': result_text})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)

@csrf_exempt
def run_multi_block_entropy_test(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            binary_data = data.get('binary_data', '')

            if not binary_data:
                return JsonResponse({"error": "binary_data is missing or empty"}, status=400)

            p_value, result = MultiBlockEntropyTest.MultiBlockEntropyTest(binary_data)

            result_text = "random number" if result == 1 else "non-random number"
            return JsonResponse({'p_value': p_value, 'result': result_text})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)


@csrf_exempt
def run_lz78y_test(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            binary_data = data.get('binary_data', '')

            if not binary_data:
                return JsonResponse({"error": "binary_data is missing or empty"}, status=400)

            p_value, result = LZ78YTest.LZ78YTest(binary_data)

            result_text = "random number" if result == 1 else "non-random number"
            return JsonResponse({'p_value': p_value, 'result': result_text})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)

@csrf_exempt
def run_min_entropy_test(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            binary_data = data.get('binary_data', '')

            if not binary_data:
                return JsonResponse({"error": "binary_data is missing or empty"}, status=400)

            p_value, result = MinEntropyTest.MinEntropyTest(binary_data)

            result_text = "random number" if result == 1 else "non-random number"
            return JsonResponse({'p_value': p_value, 'result': result_text})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)


@csrf_exempt
def run_predictor_test(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            binary_data = data.get('binary_data', '')

            if not binary_data:
                return JsonResponse({"error": "binary_data is missing or empty"}, status=400)

            p_value, result = PredictorTest.PredictorTest(binary_data)

            result_text = "random number" if result == 1 else "non-random number"
            return JsonResponse({'p_value': p_value, 'result': result_text})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)



def send_binary_data(request):
    binary_data = '101010'  # Example binary data as a string
    response_data = {
        'binary_data': binary_data
    }
    return JsonResponse(response_data)

def fetch_binary_data():
    # Replace this URL with the actual URL of the external server
    url = "https://www.random.org/integers/?num=1&min=1&max=100&col=1&base=10&format=plain&rnd=new"
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.content

def binary_event_stream():
    while True:
        try:
            binary_data = fetch_binary_data()
            encoded_data = base64.b64encode(binary_data).decode('utf-8')
            yield f'data: {encoded_data}\n\n'
        except requests.RequestException as e:
            yield f'data: Error fetching data: {e}\n\n'
        time.sleep(0.5)  # Adjust the sleep time as needed

def sse_binary_view(request):
    response = StreamingHttpResponse(binary_event_stream(), content_type='text/event-stream')
    response['Cache-Control'] = 'no-cache'
    response['X-Accel-Buffering'] = 'no'  # Disable buffering for nginx
    return response

def sse_binary_example_view(request):
    return render(request, 'myapp/sse_binary_example.html')



 

global_graph_image=None



@csrf_exempt
def create_graph(request):
    # Parse the incoming JSON data
    try:
        data = json.loads(request.body)
        binary_data = data.get('binary_data', '')
        
        job_id = data.get('job_id', str(uuid.uuid4()))

    except json.JSONDecodeError as e:
        print('Error parsing JSON:', e)
        return HttpResponse("Invalid JSON data.", status=400)

    # Check if binary_data is empty
    if not binary_data:
        return HttpResponse("Binary data is required.", status=400)

    # Dictionary to store p-values with error handling
    test_p_values = {}

    cache.set(f"{job_id}_progressGraph", 0)

    # Function to safely call each test
    def safe_test_call(test_func, test_name, binary_data):
        try:
            result = test_func(binary_data)
            p_value = result[0]
            print(f'{test_name} p_value:', p_value)  # Log the p-value
            # Handle invalid or out-of-range p-values
            if p_value is None or p_value == -1 or str(p_value).strip() == '':
                return 0
            if p_value > 1:
                return 0
            return float(p_value)
        except Exception as e:
            print(f'Error in {test_name}:', e)
            return 0

    # Call the statistical tests and collect p-values
    test_p_values['Frequency Monobit'] = safe_test_call(FrequencyTest.monobit_test, 'Frequency Monobit', binary_data)
    cache.set(f"{job_id}_progressGraph", 1)

    test_p_values['Frequency Block Test'] = safe_test_call(FrequencyTest.block_frequency, 'Frequency Block Test', binary_data)
    cache.set(f"{job_id}_progressGraph", 2)

    test_p_values['Approximate Entropy Test'] = safe_test_call(ApproximateEntropy.approximate_entropy_test, 'Approximate Entropy Test', binary_data)
    cache.set(f"{job_id}_progressGraph", 3)
    test_p_values['Runs Test'] = safe_test_call(RunTest.run_test, 'Runs Test', binary_data)
    cache.set(f"{job_id}_progressGraph", 4)
    test_p_values['Longest Run of Ones Test'] = safe_test_call(RunTest.longest_one_block_test, 'Longest Run of Ones Test', binary_data)
    cache.set(f"{job_id}_progressGraph", 5)
    test_p_values['Binary Matrix Rank Test'] = safe_test_call(Matrix.binary_matrix_rank_text, 'Binary Matrix Rank Test', binary_data)
    cache.set(f"{job_id}_progressGraph", 6)
    test_p_values['Discrete Fourier Transform Test'] = safe_test_call(SpectralTest.spectral_test, 'Discrete Fourier Transform Test', binary_data)
    cache.set(f"{job_id}_progressGraph", 7)
    test_p_values['Non-overlapping Template Match Test'] = safe_test_call(TemplateMatching.non_overlapping_test, 'Non-overlapping Template Match Test', binary_data)
    cache.set(f"{job_id}_progressGraph", 8)
    test_p_values['Overlapping Template Match Test'] = safe_test_call(TemplateMatching.overlapping_patterns, 'Overlapping Template Match Test', binary_data)
    cache.set(f"{job_id}_progressGraph", 9)
    test_p_values['Maurer’s Universal Statistical Test'] = safe_test_call(Universal.statistical_test, 'Maurer’s Universal Statistical Test', binary_data)
    cache.set(f"{job_id}_progressGraph", 10)
    test_p_values['Linear Complexity Test'] = safe_test_call(ComplexityTest.linear_complexity_test, 'Linear Complexity Test', binary_data)
    cache.set(f"{job_id}_progressGraph", 11)
    test_p_values['Serial Test'] = safe_test_call(Serial.serial_test, 'Serial Test', binary_data)
    cache.set(f"{job_id}_progressGraph", 12)
    test_p_values['Cumulative Sums Test'] = safe_test_call(CumulativeSums.cumulative_sums_test, 'Cumulative Sums Test', binary_data)
    cache.set(f"{job_id}_progressGraph", 13)
    test_p_values['Random Excursions Test'] = safe_test_call(RandomExcursions.random_excursions_test, 'Random Excursions Test', binary_data)
    cache.set(f"{job_id}_progressGraph", 14)
    test_p_values['Random Excursions Variant Test'] = safe_test_call(RandomExcursions.variant_test, 'Random Excursions Variant Test', binary_data)
    cache.set(f"{job_id}_progressGraph", 15)
    test_p_values['Autocorrelation Test'] = safe_test_call(AutocorrelationTest.autocorrelation_test, 'Autocorrelation Test', binary_data)
    cache.set(f"{job_id}_progressGraph", 16)
    test_p_values['Adaptive Statistical Test'] = safe_test_call(AdaptiveStatisticalTest.adaptive_statistical_test, 'Adaptive Statistical Test', binary_data)
    cache.set(f"{job_id}_progressGraph", 17)

    # Filter valid tests where p-value is within a valid range
    valid_tests = {k: (0 if v is None or v > 1 else v) for k, v in test_p_values.items()}
    print('Valid tests:', valid_tests)

    # If no valid tests are found, return an error
    if not valid_tests:
        return HttpResponse("No valid test results to plot.", status=400)

    # Extract test names and p-values for plotting
    x = list(valid_tests.keys())
    y = list(valid_tests.values())

    # Create the plot
    fig, ax = plt.subplots(figsize=(16, 9))

    # Assign color based on the p-value threshold (0.01)
    colors = ['green' if p > 0.01 else 'blue' for p in y]

    # Plot the histogram with colors based on the condition
    ax.bar(x, y, color=colors)

    # Draw a horizontal dotted red line at p_value = 0.01
    ax.axhline(y=0.01, color='red', linestyle='--', linewidth=2, label='p-value = 0.01')

    # Label the axes
    ax.set_xlabel('NIST Sp 800-22 Tests', fontsize=20)
    ax.set_ylabel('P-values', fontsize=20)
    

    # Set y-axis ticks at intervals of 0.1
    ax.set_yticks([i / 10.0 for i in range(0, 11)])

    # Set y-axis limits between 0 and 1
    ax.set_ylim(0, 1)

    # Rotate x-axis labels for better visibility
    plt.xticks(rotation=45, ha='right', fontsize=12)

    # Ensure tight layout to avoid overlap
    plt.tight_layout()

    from matplotlib.patches import Patch
    # Add a custom legend for the color categories
    legend_elements = [Patch(facecolor='green', edgecolor='green', label='Random (p > 0.01)'),
                       Patch(facecolor='blue', edgecolor='blue', label='Non-random (p ≤ 0.01)')]
    ax.legend(handles=legend_elements, loc='upper right', prop={'size': 14})

    cache.set(f"{job_id}_progressGraph", 18)
    # Create a BytesIO object to hold the image
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)

    global_graph_image = buf
   

    # Close the figure to free memory
    plt.close(fig)

    # Return the image as a response
    # return HttpResponse(buf, content_type='image/png')
    return HttpResponse(buf, content_type='image/png')

@csrf_exempt
def get_progress_graph(request, job_id):
    progress = cache.get(f"{job_id}_progressGraph", 0)
    return JsonResponse({"progress": int(progress)})

@csrf_exempt
def create_graph_nist90b(request):
    # Parse the incoming JSON data
    try:
        data = json.loads(request.body)
        binary_data = data.get('binary_data', '')
        job_id = data.get('job_id', str(uuid.uuid4()))

    except json.JSONDecodeError as e:
        print('Error parsing JSON:', e)
        return HttpResponse("Invalid JSON data.", status=400)

    # Check if binary_data is empty
    if not binary_data:
        return HttpResponse("Binary data is required.", status=400)

    # Dictionary to store p-values with error handling
    test_p_values = {}
    cache.set(f"{job_id}_progressGraph", 0)


    # Function to safely call each test
    def safe_test_call(test_func, test_name, binary_data):
        try:
            result = test_func(binary_data)
            p_value = result[0]
            print(f'{test_name} p_value:', p_value)  # Log the p-value
            # Handle invalid or out-of-range p-values
            if p_value is None or p_value == -1 or str(p_value).strip() == '':
                return 0
            if p_value > 1:
                return 0
            return float(p_value)
        except Exception as e:
            print(f'Error in {test_name}:', e)
            return 0

    # Call the statistical tests and collect p-values
    test_p_values['MCV Test'] = safe_test_call(MostCommonValueTest.MostCommonValueTest, 'Frequency Monobit', binary_data)
    cache.set(f"{job_id}_progressGraph90b", 1)

    test_p_values['Collision Test'] = safe_test_call(CollisionTest.CollisionTest, 'Frequency Block Test', binary_data)
    cache.set(f"{job_id}_progressGraph90b", 2)

    test_p_values['Markov Test'] = safe_test_call(MarkovTest.MarkovTest, 'Approximate Entropy Test', binary_data)
    cache.set(f"{job_id}_progressGraph90b", 3)

    test_p_values['Compression Test'] = safe_test_call(CompressionTest.CompressionTest, 'Runs Test', binary_data)
    cache.set(f"{job_id}_progressGraph90b", 4)

    test_p_values['T-tuple Test'] = safe_test_call(TTupleTest.TTupleTest, 'Longest Run of Ones Test', binary_data)
    cache.set(f"{job_id}_progressGraph90b", 5)

    test_p_values['Longest Repeated Substring Test'] = safe_test_call(TestU01LongestRepeatedSubstringTest.TestU01LongestRepeatedSubstringTest, 'Binary Matrix Rank Test', binary_data)
    cache.set(f"{job_id}_progressGraph90b", 6)

    test_p_values['MultiBlock Entropy Test'] = safe_test_call(MultiBlockEntropyTest.MultiBlockEntropyTest, 'Discrete Fourier Transform Test', binary_data)
    cache.set(f"{job_id}_progressGraph90b", 7)

    test_p_values['Chi-Square Test'] = safe_test_call(ChiSquareTest.ChiSquareTest, 'Non-overlapping Template Match Test', binary_data)
    cache.set(f"{job_id}_progressGraph90b", 8)

    test_p_values['LZ78Y Test'] = safe_test_call(LZ78YTest.LZ78YTest, 'Overlapping Template Match Test', binary_data)
    cache.set(f"{job_id}_progressGraph90b", 9)

    test_p_values['Min Entropy Test'] = safe_test_call(MinEntropyTest.MinEntropyTest, 'Maurer’s Universal Statistical Test', binary_data)
    cache.set(f"{job_id}_progressGraph90b", 10)

    # Filter valid tests where p-value is within a valid range
    valid_tests = {k: (0 if v is None or v > 1 else v) for k, v in test_p_values.items()}
    print('Valid tests:', valid_tests)

    # If no valid tests are found, return an error
    if not valid_tests:
        return HttpResponse("No valid test results to plot.", status=400)

    # Extract test names and p-values for plotting
    x = list(valid_tests.keys())
    y = list(valid_tests.values())

    # Create the plot
    fig, ax = plt.subplots(figsize=(16, 9))

    # Assign color based on the p-value threshold (0.01)
    colors = ['green' if p > 0.01 else 'blue' for p in y]

    # Plot the histogram with colors based on the condition
    ax.bar(x, y, color=colors)

    # Draw a horizontal dotted red line at p_value = 0.01
    ax.axhline(y=0.01, color='red', linestyle='--', linewidth=2, label='p-value = 0.01')

    # Label the axes
    ax.set_xlabel('NIST SP 800-90B Tests', fontsize=20)
    ax.set_ylabel('P-values', fontsize=20)
    

    # Set y-axis ticks at intervals of 0.1
    ax.set_yticks([i / 10.0 for i in range(0, 11)])

    # Set y-axis limits between 0 and 1
    ax.set_ylim(0, 1)

    # Rotate x-axis labels for better visibility
    plt.xticks(rotation=45, ha='right', fontsize=12)

    # Ensure tight layout to avoid overlap
    plt.tight_layout()

    from matplotlib.patches import Patch
    # Add a custom legend for the color categories
    legend_elements = [Patch(facecolor='green', edgecolor='green', label='Random (p > 0.01)'),
                       Patch(facecolor='blue', edgecolor='blue', label='Non-random (p ≤ 0.01)')]
    ax.legend(handles=legend_elements, loc='upper right', prop={'size': 10})

    # Create a BytesIO object to hold the image
    cache.set(f"{job_id}_progressGraph90b", 18)

    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)

    global_graph_image = buf
  

    # Close the figure to free memory
    plt.close(fig)

    # Return the image as a response
    # return HttpResponse(buf, content_type='image/png')
    return HttpResponse(buf, content_type='image/png')

@csrf_exempt
def get_progress_graph90b(request, job_id):
    progress = cache.get(f"{job_id}_progressGraph90b", 0)
    return JsonResponse({"progress": int(progress)})


@csrf_exempt
def get_progress_graphDieharder(request, job_id):
    progress = cache.get(f"{job_id}_progressGraphDieharder", 0)
    return JsonResponse({"progress": int(progress)})


@csrf_exempt
def create_graph_dieharder(request):
   

    # binary_data = request.GET.get('binary_data', '')

    try:
        data = json.loads(request.body)
        binary_data = data.get('binary_data', '')
        job_id = data.get('job_id', str(uuid.uuid4()))
    except json.JSONDecodeError as e:
        print('Error parsing JSON:', e)
        return HttpResponse("Invalid JSON data.", status=400)


    binary_data = binary_data.replace('%0A', '').replace('%20', '').replace(' ', '').replace('\n', '').replace('\r', '')
    
    if not binary_data:
        return HttpResponse("Binary data is required.", status=400)

    # Dictionary to store p-values with error handling
    test_p_values = {}
    cache.set(f"{job_id}_progressGraphDieharder", 0)

    # Wrap test calls in try-except blocks and ensure p-values are numeric
    def safe_test_call(test_func, test_name, binary_data):
        result = test_func(binary_data)

        p_value = result[0]
        print(test_name, p_value)

        # If p_value is not defined (None) or equals -1, return 0
        if p_value is None or p_value == -1  or str(p_value).strip() == '':
            return 0
        if p_value > 1:
            return 0
        try:
            return float(p_value)
        except ZeroDivisionError:
            # Handle float division by zero
            return 0

    
    test_p_values['Birthday Spacing Test'] = safe_test_call(BirthdaySpacingsTest.BirthdaySpacingsTest, 'Birthday Spacing Test', binary_data)
    cache.set(f"{job_id}_progressGraphDieharder", 1)
    test_p_values['Parking Lot Test'] = safe_test_call(ParkingLotTest.ParkingLotTest, 'Parking Lot Test', binary_data)
    cache.set(f"{job_id}_progressGraphDieharder", 2)
    test_p_values['Overlapping Permutation 5 Test'] = safe_test_call(Overlapping5PermutationTest.Overlapping5PermutationTest, 'Overlapping Permutation 5 Test', binary_data)
    cache.set(f"{job_id}_progressGraphDieharder", 3)
    test_p_values['Minimum Distance Test'] = safe_test_call(MinimumDistanceTest.MinimumDistanceTest, 'Minimum Distance Test', binary_data)
    cache.set(f"{job_id}_progressGraphDieharder", 4)
    test_p_values['Ranks of 31x31 Test'] = safe_test_call(Ranks31x31MatricesTest.Ranks31x31MatricesTest, 'Ranks of 31x31 Test', binary_data)
    cache.set(f"{job_id}_progressGraphDieharder", 5)
    test_p_values['3d Spheres Test'] = safe_test_call(Spheres3DTest.Spheres3DTest, '3d Spheres Test', binary_data)
    cache.set(f"{job_id}_progressGraphDieharder", 6)
    test_p_values['Ranks of 32x32 Test'] = safe_test_call(Ranks32x32MatricesTest.Ranks32x32MatricesTest, 'Ranks of 32x32 Test', binary_data)
    cache.set(f"{job_id}_progressGraphDieharder", 7)
    test_p_values['Craps Test'] = safe_test_call(CrapsTest.CrapsTest, 'Craps Test', binary_data)
    cache.set(f"{job_id}_progressGraphDieharder", 8)
    test_p_values['Bitstream Test'] = safe_test_call(BitstreamTest.BitstreamTest, 'Bitstream Test', binary_data)
    cache.set(f"{job_id}_progressGraphDieharder", 9)
    test_p_values['Marsaglia-Tsang GCD Test'] = safe_test_call(MarsagliaTsangGCDTest.MarsagliaTsangGCDTest, 'Marsaglia-Tsang GCD Test', binary_data)
    cache.set(f"{job_id}_progressGraphDieharder", 10)
    test_p_values['OPSO Test'] = safe_test_call(OPSOTest.OPSOTest, 'OPSO Test', binary_data)
    cache.set(f"{job_id}_progressGraphDieharder", 11)
    test_p_values['OQSO Test'] = safe_test_call(OQSOTest.OQSOTest, 'OQSO Test', binary_data)
    cache.set(f"{job_id}_progressGraphDieharder", 12)
    test_p_values['DNA Test'] = safe_test_call(DNATest.DNATest, 'DNA Test', binary_data)
    cache.set(f"{job_id}_progressGraphDieharder", 13)
    test_p_values['Count the one(stream) Test'] = safe_test_call(CountThe1sStreamTest.CountThe1sStreamTest, 'Count the one(stream) Test', binary_data)
    cache.set(f"{job_id}_progressGraphDieharder", 14)
    test_p_values['Count the one(byte) Test'] = safe_test_call(CountThe1sByteTest.CountThe1sByteTest, 'Count the one(byte) Test', binary_data)
    cache.set(f"{job_id}_progressGraphDieharder", 15)
    test_p_values['Marsaglia Tsang Simple GCD Test'] = safe_test_call(MarsagliaTsangSimpleGCDTest.MarsagliaTsangSimpleGCDTest, 'Marsaglia Tsang Simple GCD Test', binary_data)
    cache.set(f"{job_id}_progressGraphDieharder", 16)
    test_p_values['Generalized Minimum Distance Test'] = safe_test_call(GeneralizedMinimumDistanceTest.GeneralizedMinimumDistanceTest, 'Generalized Minimum Distance Test', binary_data)
    cache.set(f"{job_id}_progressGraphDieharder", 17)
    test_p_values['TestU01 Linear Complexity Test'] = safe_test_call(TestU01LinearComplexityTest.TestU01LinearComplexityTest, 'TestU01 Linear Complexity Test', binary_data)
    cache.set(f"{job_id}_progressGraphDieharder", 18)
    test_p_values['TestU01 Longest Repeated Substring Test'] = safe_test_call(TestU01LongestRepeatedSubstringTest.TestU01LongestRepeatedSubstringTest, 'TestU01 Longest Repeated Substring Test', binary_data)
    cache.set(f"{job_id}_progressGraphDieharder", 19)
    test_p_values['TestU01 Matrix Rank Test'] = safe_test_call(TestU01MatrixRankTest.TestU01MatrixRankTest, 'TestU01 Matrix Rank Test', binary_data)
    cache.set(f"{job_id}_progressGraphDieharder", 20)

    
    
    valid_tests = {k: (0 if v is None or v > 1 else v) for k, v in test_p_values.items()}

    if not valid_tests:
        return HttpResponse("No valid test results to plot.", status=400)

    # Extract test names and p-values for plotting
    x = list(valid_tests.keys())
    y = list(valid_tests.values())

    # Create the plot
    fig, ax = plt.subplots(figsize=(16, 9))

    # Assign color based on the p-value threshold (0.05)
    colors = ['green' if p > 0.01 else 'blue' for p in y]

    # Plot the histogram with colors based on the condition
    ax.bar(x, y, color=colors)

    # Draw a horizontal dotted red line at p_value = 0.05
    ax.axhline(y=0.01, color='red', linestyle='--', linewidth=2, label='p-value = 0.01')

    # Label the axes
    ax.set_xlabel('Dieharder Tests', fontsize=20)
    ax.set_ylabel('P-values', fontsize=20)
    ax.set_title('P-values of Dieharder Tests', fontsize=20)

    # Set y-axis ticks at intervals of 0.1
    ax.set_yticks([i / 10.0 for i in range(0, 11)])  # 0.0, 0.1, 0.2, ..., 1.0

    # Set y-axis limits between 0 and 1
    ax.set_ylim(0, 1)

    # Rotate x-axis labels for better visibility
    plt.xticks(rotation=45, ha='right', fontsize=12)

    # Ensure tight layout to avoid overlap
    plt.tight_layout()

    # Add a custom legend for the color categories
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor='green', edgecolor='green', label='Random (p > 0.01)'),
                       Patch(facecolor='blue', edgecolor='blue', label='Non-random (p ≤ 0.01)')]

    # Add the legend for the colors
    ax.legend(handles=legend_elements, loc='upper right', prop={'size': 14})

    # Create a BytesIO object to hold the image
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)

    global_graph_image = buf
   
    # Close the figure to free memory
    plt.close(fig)

    # Return the image as a response
    # return HttpResponse(buf, content_type='image/png')
    return HttpResponse(buf, content_type='image/png')


@csrf_exempt
def generate_pdf_report(request):
    global global_graph_image

    try:
        data = json.loads(request.body)
        binary_data = data.get('binary_data', '')
       
        job_id = data.get('job_id', str(uuid.uuid4()))
    except json.JSONDecodeError as e:
        print('Error parsing JSON:', e)
        return HttpResponse("Invalid JSON data.", status=400)

    # Create an HttpResponse object with PDF headers
    graph_response = create_graph(request)
    graph_buffer = graph_response.content
    graph_image_io = BytesIO(graph_buffer)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="report.pdf"'

    # Set up the PDF buffer and document template with margins
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4,
                             rightMargin=10, leftMargin=10,
                             topMargin=10, bottomMargin=30, title="QNU Labs")

    # Set up styles
    styles = getSampleStyleSheet()

    # current_date = datetime.now().strftime("%B %d, %Y")  # Format as "December 06, 2024"

    # Add a paragraph with the current date
    date_style = ParagraphStyle('Date', parent=styles['Normal'], fontSize=10, fontName='Helvetica-Bold',  alignment=2, spaceAfter=10)
    # date_paragraph = Paragraph(f"Date: {current_date}", date_style)

    # Add a headline (title)
    title = Paragraph("Report-QNu Labs", styles['Title'])
    title_space = Spacer(1, 0.0 * inch)  # Small spacer below the title

    # Add subtitles with underlining
    subtitle_style = styles['Heading2']
    subtitle_style.fontName = 'Helvetica-Bold'
    subtitle_style.fontSize = 12
    subtitle_style.underline = True

    nist_subtitle = Paragraph("NIST SP 800-22 Tests:", subtitle_style)
    graph_subtitle = Paragraph("Graphical Analysis:", subtitle_style)
    description_subtitle = Paragraph("Test Descriptions:", subtitle_style)
    subtitle_space = Spacer(1, 0.0 * inch)  # Spacer below the subtitles
    graph_space= Spacer(1, 0.0 * inch) 
    # Initialize x to 0
    x = 0
    
    cache.set(f"{job_id}_progressReport", 0)

  

    # Perform the tests and check results
    frequency_test_result = FrequencyTest.monobit_test(binary_data)[1]
    if frequency_test_result:
        x += 1
    cache.set(f"{job_id}_progressReport", 1)
    frequency_test_block_result = FrequencyTest.block_frequency(binary_data)[1]
    if frequency_test_block_result:
        x += 1
    cache.set(f"{job_id}_progressReport", 2)
    runs_test_result = RunTest.run_test(binary_data)[1]
    if runs_test_result:
        x += 1
    cache.set(f"{job_id}_progressReport", 3)
    approximate_entropy_test_result = ApproximateEntropy.approximate_entropy_test(binary_data)[1]
    if approximate_entropy_test_result:
        x += 1
    cache.set(f"{job_id}_progressReport", 4)
    longest_run_of_one_test_result = RunTest.longest_one_block_test(binary_data)[1]
    if longest_run_of_one_test_result:
        x += 1
    cache.set(f"{job_id}_progressReport", 5)
    binary_matrix_rank_test_result = Matrix.binary_matrix_rank_text(binary_data)[1]
    if binary_matrix_rank_test_result:
        x += 1
    cache.set(f"{job_id}_progressReport", 6)
    dft_test_result = SpectralTest.spectral_test(binary_data)[1]
    if dft_test_result:
        x += 1
    cache.set(f"{job_id}_progressReport", 7)
    non_overlapping_test_result = TemplateMatching.non_overlapping_test(binary_data)[1]
    if non_overlapping_test_result:
        x += 1
    cache.set(f"{job_id}_progressReport", 8)
    overlapping_test_result = TemplateMatching.overlapping_patterns(binary_data)[1]
    if overlapping_test_result:
        x += 1
    cache.set(f"{job_id}_progressReport", 9)
    maurers_universal_test_result = Universal.statistical_test(binary_data)[1]
    if maurers_universal_test_result:
        x += 1
    cache.set(f"{job_id}_progressReport", 10)
    linear_complexity_test_result = ComplexityTest.linear_complexity_test(binary_data)[1]
    if linear_complexity_test_result:
        x += 1
    cache.set(f"{job_id}_progressReport", 11)
    serial_test_result = Serial.serial_test(binary_data)[1]
    if serial_test_result:
        x += 1
    cache.set(f"{job_id}_progressReport", 12)
    cumulative_sums_test_result = CumulativeSums.cumulative_sums_test(binary_data)[1]
    if cumulative_sums_test_result:
        x += 1
    cache.set(f"{job_id}_progressReport", 13)
    random_excursions_test_result = RandomExcursions.random_excursions_test(binary_data)[1]
    if random_excursions_test_result:
        x += 1
    cache.set(f"{job_id}_progressReport", 14)
    random_excursion_variant_test_result = RandomExcursions.variant_test(binary_data)[1]
    if random_excursion_variant_test_result:
        x += 1
    cache.set(f"{job_id}_progressReport", 15)
    autocorrelation_test_result = AutocorrelationTest.autocorrelation_test(binary_data)[1]
    if autocorrelation_test_result:
        x += 1
    cache.set(f"{job_id}_progressReport", 16)
    adaptive_statistical_test_result = AdaptiveStatisticalTest.adaptive_statistical_test(binary_data)[1]
    if adaptive_statistical_test_result:
        x += 1
    cache.set(f"{job_id}_progressReport", 17)

    # Now x contains the count of tests that returned True
    final_text = 'random number' if x > 10 else 'non-random number'

    # Dynamically set the result text based on the test outcome
    frequency_test_text = 'random number' if frequency_test_result else 'non-random number'
    frequency_test_block_text = 'random number' if frequency_test_block_result else 'non-random number'
    runs_text = 'random number' if runs_test_result else 'non-random number'
    approximate_entropy_text = 'random number' if approximate_entropy_test_result else 'non-random number'
    longest_run_of_ones_text = 'random number' if longest_run_of_one_test_result else 'non-random number'
    binary_matrix_rank_text = 'random number' if binary_matrix_rank_test_result else 'non-random number'
    dft_text = 'random number' if dft_test_result else 'non-random number'
    non_overlapping_text = 'random number' if non_overlapping_test_result else 'non-random number'
    overlapping_text = 'random number' if overlapping_test_result else 'non-random number'
    maurers_universal_text = 'random number' if maurers_universal_test_result else 'non-random number'
    linear_complexity_text = 'random number' if linear_complexity_test_result else 'non-random number'
    serial_text = 'random number' if serial_test_result else 'non-random number'
    cumulative_sums_text = 'random number' if cumulative_sums_test_result else 'non-random number'
    random_excursion_variant_text = 'random number' if random_excursion_variant_test_result else 'non-random number'
    random_excursion_text = 'random number' if random_excursions_test_result else 'non-random number'
    autocorrelation_text = 'random number' if autocorrelation_test_result else 'non-random number'
    adaptive_statistical_text = 'random number' if adaptive_statistical_test_result else 'non-random number'

    bold_red_style = ParagraphStyle(
        'BoldRed',
        parent=styles['Normal'],
        fontSize=12,
        fontName='Helvetica-Bold',
        textColor='red'
    )

    bold_black_style = ParagraphStyle(
        'BoldBlack',
        parent=styles['Normal'],
        fontSize=12,
        fontName='Helvetica-Bold',
        textColor='black'
    )

    # Sample Table Data for the first table with "Final Result" in the last row
    data1 = [
        [Paragraph('Test type', styles['Normal']), 'Result', 'Test type', 'Result'],
        [Paragraph('1. Frequency Test', styles['Normal']), frequency_test_text,
         Paragraph('2. Frequency Test within a Block', styles['Normal']), frequency_test_block_text],
        [Paragraph('3. Runs Test', styles['Normal']), runs_text,
         Paragraph('4. Test for the longest Run of Ones', styles['Normal']), longest_run_of_ones_text],
        [Paragraph('5. Binary Matrix Rank Test', styles['Normal']), binary_matrix_rank_text,
         Paragraph('6. Discrete Fourier Transform Test', styles['Normal']), dft_text],
        [Paragraph('7. Non-overlapping Template Match', styles['Normal']), non_overlapping_text,
         Paragraph('8. Overlapping Template Matching Test', styles['Normal']), overlapping_text],
        [Paragraph('9. Maurers Universal test', styles['Normal']), maurers_universal_text,
         Paragraph('10. Linear complexity Test', styles['Normal']), linear_complexity_text],
        [Paragraph('11. Serial Test', styles['Normal']), serial_text,
         Paragraph('12. Approximate Entropy Test', styles['Normal']), approximate_entropy_text],
        [Paragraph('13. Cumulative Sum Test', styles['Normal']), cumulative_sums_text,
         Paragraph('14. Random Excursions Test', styles['Normal']), random_excursion_text],
        [Paragraph('15. Random Excursions Variant Test', styles['Normal']), random_excursion_variant_text,
         Paragraph('16. Autocorrelation Test', styles['Normal']), autocorrelation_text],
        [Paragraph('17. Adaptive Statistical Test', styles['Normal']), adaptive_statistical_text],
        [Paragraph('Final Result', styles['Normal']), Paragraph(final_text, bold_red_style)],
    ]

    # Adjust column widths
    colWidths = [2 * inch, 1.5 * inch, 2 * inch, 1.5 * inch]

    # Create the first table object with adjusted column widths
    table1 = Table(data1, colWidths=colWidths)

    # Apply styles to the first table
    table1.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.blue),  # Header background color
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center text alignment
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Bold header
        ('FONTSIZE', (0, 0), (-1, -1), 10),  # Set font size
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Add gridlines
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Center vertically
    ]))

    # Create the second table with graphical analysis
    data2 = [
        [Image(graph_image_io, width=400, height=370)]
    ]
    table2 = Table(data2, colWidths=[4 * inch])
    table2.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER')]))

    # Add logo on the top-right corner (adjust the path of your logo)
    logo_path = os.path.join(os.path.dirname(__file__), 'qnulogo.png')
    logo_image = Image(logo_path, width=0.5 * inch, height=0.5 * inch)
    logo_table = Table([[logo_image]], colWidths=[6.5 * inch], rowHeights=[0.5 * inch])
    logo_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (0, 0), 'CENTRE'),  # Align logo to the left
        ('VALIGN', (100, 100), (0, 0), 'TOP'),  # Align logo to the top
    ]))

    # Add the descriptions of the NIST and Dieharder tests
    nist_description = """
    <b>NIST Statistical Tests Description:</b><br/><br/>

    1. <b>Frequency Test</b>: This test checks the proportion of zeros and ones in the entire binary sequence. For a random sequence, the number of ones and zeros should be approximately equal. If the sequence is too skewed towards either ones or zeros, it indicates non-randomness.<br/><br/>

    2. <b>Frequency Test within a Block</b>: This test divides the binary sequence into smaller blocks and checks the proportion of ones within each block. It ensures that local subsequences are also balanced and do not deviate significantly from the expected 50% distribution of ones and zeros.<br/><br/>

    3. <b>Runs Test</b>: A run is a sequence of consecutive identical bits (either all ones or all zeros). This test counts the total number of runs in the sequence. Too many or too few runs can indicate non-randomness, as a random sequence should have an expected number of runs based on its length.<br/><br/>

    4. <b>Test for the Longest Run of Ones</b>: This test focuses on the longest run of ones within a block of the sequence. It checks if the length of the longest run of ones is consistent with what is expected in a random sequence. Unusually long runs of ones may indicate non-randomness.<br/><br/>

    5. <b>Binary Matrix Rank Test</b>: This test evaluates the rank of disjoint sub-matrices created from the binary sequence. It checks for linear dependence among fixed-length subsequences. A random sequence should produce matrices with full rank, while non-random sequences may result in matrices with lower rank.<br/><br/>

    6. <b>Discrete Fourier Transform Test</b>: This test analyzes the sequence in the frequency domain using a Fourier transform. It detects periodic patterns or regularities in the sequence that would not be present in a truly random sequence. Peaks in the frequency domain may indicate non-randomness.<br/><br/>

    7. <b>Non-overlapping Template Matching Test</b>: This test searches for the occurrence of specific non-periodic patterns (templates) in the sequence. It ensures that the sequence does not contain predictable patterns that could indicate non-randomness.<br/><br/>

    8. <b>Overlapping Template Matching Test</b>: Similar to the non-overlapping test, this test looks for specific patterns but allows for overlapping occurrences. It detects if the sequence contains recurring patterns, which would suggest non-randomness.<br/><br/>

    9. <b>Maurer’s Universal Test</b>: This test measures the compressibility of the sequence. A truly random sequence should not be compressible, as it lacks patterns or regularities. If the sequence can be compressed significantly, it indicates non-randomness.<br/><br/>

    10. <b>Linear Complexity Test</b>: This test assesses the complexity of the sequence using linear feedback shift registers (LFSRs). It checks if the sequence can be generated by a simple linear process. A random sequence should have high linear complexity, while a non-random sequence may have low complexity.<br/><br/>

    11. <b>Serial Test</b>: This test examines the frequency of all possible overlapping m-bit patterns in the sequence. It ensures that all possible patterns of a given length appear with approximately the same frequency in a random sequence.<br/><br/>

    12. <b>Approximate Entropy Test</b>: This test measures the frequency of m-bit and (m+1)-bit patterns in the sequence. It checks for irregularities in the sequence by comparing the frequencies of these patterns. A random sequence should have consistent frequencies for all patterns.<br/><br/>

    13. <b>Cumulative Sums Test</b>: This test converts the binary sequence into a random walk (where each bit contributes to a cumulative sum) and checks if the cumulative sums are too large or too small. A random sequence should have cumulative sums that stay close to zero.<br/><br/>

    14. <b>Random Excursions Test</b>: This test analyzes the number of cycles in a random walk derived from the binary sequence. It checks if the sequence has too many or too few cycles, which would indicate non-randomness.<br/><br/>

    15. <b>Random Excursions Variant Test</b>: Similar to the Random Excursions Test, this test focuses on specific states in the random walk. It checks if the sequence deviates from the expected behavior in certain states, which could indicate non-randomness.<br/><br/>

    16. <b>Autocorrelation Test</b>: This test measures the correlation between the binary sequence and a shifted version of itself. It detects if there are dependencies between bits that are separated by a certain distance. A random sequence should have low autocorrelation for all shifts.<br/><br/>

    17. <b>Adaptive Statistical Test</b>: This test combines multiple statistical tests to detect deviations from randomness. <br/><br/>
    """

    description_style = ParagraphStyle(
        'Description',
        parent=styles['Normal'],
        fontSize=10,
        fontName='Helvetica',
        leading=12,
        spaceAfter=10
    )

    nist_description_paragraph = Paragraph(nist_description, description_style)

    # Send test results to Gemini for analysis
    test_results = {
        "Frequency Test": frequency_test_text,
        "Frequency Test within a Block": frequency_test_block_text,
        "Runs Test": runs_text,
        "Test for the Longest Run of Ones": longest_run_of_ones_text,
        "Binary Matrix Rank Test": binary_matrix_rank_text,
        "Discrete Fourier Transform Test": dft_text,
        "Non-overlapping Template Match": non_overlapping_text,
        "Overlapping Template Matching Test": overlapping_text,
        "Maurers Universal test": maurers_universal_text,
        "Linear complexity Test": linear_complexity_text,
        "Serial Test": serial_text,
        "Approximate Entropy Test": approximate_entropy_text,
        "Cumulative Sum Test": cumulative_sums_text,
        "Random Excursions Test": random_excursion_text,
        "Random Excursions Variant Test": random_excursion_variant_text,
        "Autocorrelation Test": autocorrelation_text,
        "Adaptive Statistical Test": adaptive_statistical_text,
    }

    AIAnalysis_subtitle = Paragraph("AI Analysis:", subtitle_style)

    # Create the prompt
    prompt = "Perform a detailed analysis of the results from all the statistical tests. For each test, display the test name along with its p-value and indicate whether the result is Random or Non-Random based on the condition that if p-value > 0.05 e.g: test_name: test_result, the number is considered Random; otherwise, it is Non-Random. In the analysis, mention that basis of selecting random or non random is majority of tests response. Finally tell these many tests give random number or non random number as a result along with their names"

    # Send request to Gemini
    response1 = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[{"text": prompt}, {"text": json.dumps(test_results)}],
    )
    if response1.candidates:
        gemini_analysis = response1.candidates[0].content.parts[0].text
        # print(gemini_analysis)
    else:
        print("No response received from Gemini.")
    
    cache.set(f"{job_id}_progressReport", 18)


    formatted_output = format_markdown(gemini_analysis)

    # Convert the formatted output into a list of bullet points
    bullet_points = formatted_output.replace("<ul>", "").replace("</ul>", "").split("<li>")
    bullet_points = [point.replace("</li>", "").strip() for point in bullet_points if point.strip()]

    # Create a ListFlowable for the bullet points
    gemini_analysis_paragraph = ListFlowable(
        [ListItem(Paragraph(point, styles['Normal'])) for point in bullet_points],
        bulletType='bullet',
        
    )
    

    # Build the PDF document
    elements = [
        logo_table,
        # date_paragraph,
        title,
        title_space,
        nist_subtitle,
        subtitle_space,
        table1,
        subtitle_space,
        graph_subtitle,
        table2,
        subtitle_space,
        description_subtitle,
        subtitle_space,
        nist_description_paragraph,
        AIAnalysis_subtitle,
        gemini_analysis_paragraph,
    ]
    doc.build(elements)

    # Get the PDF data and write it to the response
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response

@csrf_exempt
def get_progress_nist(request, job_id):
    progress = cache.get(f"{job_id}_progressReport", 0)
    return JsonResponse({"progress": int(progress)})

import markdown
def format_markdown(gemini_analysis):
    """Convert the text response into a list of bullet points with bold text up to the first semicolon."""
    # Remove any extra "*" and split the response into lines
    cleaned_analysis = gemini_analysis.replace("*", "").splitlines()

    # Process each line to ensure proper formatting
    formatted_points = []
    for line in cleaned_analysis:
        line = line.strip()
        if ";" in line:
            # Split the line at the first semicolon
            parts = line.split(";", 1)
            bold_part = f"<b>{parts[0].strip()}</b>"  # Make the part before the semicolon bold
            rest_part = parts[1].strip()  # Keep the rest of the line as is
            line = f"{bold_part}; {rest_part}"  # Combine the bold and non-bold parts
        if line:  # Add non-empty lines as list items
            formatted_points.append(f"<li>{line}</li>")

    # Combine the formatted points into an unordered list
    return f"<ul>{''.join(formatted_points)}</ul>"

@csrf_exempt
def get_progress_nist90b(request, job_id):
    progress = cache.get(f"{job_id}_progressReport90b", 0)
    return JsonResponse({"progress": int(progress)})

from reportlab.platypus import ListFlowable, ListItem

@csrf_exempt
def generate_pdf_report_nist90b(request):
    global global_graph_image

    try:
        data = json.loads(request.body)
        binary_data = data.get('binary_data', '')
        job_id = data.get('job_id', str(uuid.uuid4()))
       
    except json.JSONDecodeError as e:
        print('Error parsing JSON:', e)
        return HttpResponse("Invalid JSON data.", status=400)

    # Create an HttpResponse object with PDF headers
    graph_response = create_graph_nist90b(request)
    graph_buffer = graph_response.content
    graph_image_io = BytesIO(graph_buffer)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="report.pdf"'

    # Set up the PDF buffer and document template with margins
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4,
                             rightMargin=10, leftMargin=10,
                             topMargin=10, bottomMargin=30, title="QNU Labs")

    # Set up styles
    styles = getSampleStyleSheet()

    # current_date = datetime.now().strftime("%B %d, %Y")  # Format as "December 06, 2024"

    # Add a paragraph with the current date
    date_style = ParagraphStyle('Date', parent=styles['Normal'], fontSize=10, fontName='Helvetica-Bold',  alignment=2, spaceAfter=10)
    # date_paragraph = Paragraph(f"Date: {current_date}", date_style)

    # Add a headline (title)
    title = Paragraph("Report-QNu Labs", styles['Title'])
    title_space = Spacer(1, 0.0 * inch)  # Small spacer below the title

    # Add subtitles with underlining
    subtitle_style = styles['Heading2']
    subtitle_style.fontName = 'Helvetica-Bold'
    subtitle_style.fontSize = 12
    subtitle_style.underline = True

    nist_subtitle = Paragraph("NIST SP 800-90B Tests:", subtitle_style)
    graph_subtitle = Paragraph("Graphical Analysis:", subtitle_style)
    description_subtitle = Paragraph("Test Descriptions:", subtitle_style)

    subtitle_space = Spacer(1, 0.0 * inch)  # Spacer below the subtitles
    graph_space= Spacer(1, 0.0 * inch) 
    # Initialize x to 0
    x = 0
    cache.set(f"{job_id}_progressReport90b", 0)


    min_entropy_test_result = MinEntropyTest.MinEntropyTest(binary_data)[1]
    if min_entropy_test_result:
        x += 1
    cache.set(f"{job_id}_progressReport90b", 1)
    collision_test_result = CollisionTest.CollisionTest(binary_data)[1]
    if collision_test_result:
        x += 1
    cache.set(f"{job_id}_progressReport90b", 2)
    markov_test_result = MarkovTest.MarkovTest(binary_data)[1]
    if markov_test_result:
        x += 1
    cache.set(f"{job_id}_progressReport90b", 3)
    compression_test_result = CompressionTest.CompressionTest(binary_data)[1]
    if compression_test_result:
        x += 1
    cache.set(f"{job_id}_progressReport90b", 4)
    t_tuple_test_result = TTupleTest.TTupleTest(binary_data)[1]
    if t_tuple_test_result:
        x += 1
    cache.set(f"{job_id}_progressReport90b", 5)
    mcv_test_result = MostCommonValueTest.MostCommonValueTest(binary_data)[1]
    if mcv_test_result:
        x += 1
    cache.set(f"{job_id}_progressReport90b", 6)
    chiSquare_test_result = ChiSquareTest.ChiSquareTest(binary_data)[1]
    if chiSquare_test_result:
        x += 1
    cache.set(f"{job_id}_progressReport90b", 7)
    lz78y_test_result = LZ78YTest.LZ78YTest(binary_data)[1]
    if lz78y_test_result:
        x += 1
    cache.set(f"{job_id}_progressReport90b", 8)
    multiBlock_test_result = MultiBlockEntropyTest.MultiBlockEntropyTest(binary_data)[1]
    if multiBlock_test_result:
        x += 1
    cache.set(f"{job_id}_progressReport90b", 9)
    predictor_test_result = PredictorTest.PredictorTest(binary_data)[1]
    if predictor_test_result:
        x += 1
    cache.set(f"{job_id}_progressReport90b", 10)
    # Now x contains the count of tests that returned True
    final_text = 'random number' if x > 5 else 'non-random number'

    # Dynamically set the result text based on the test outcome
    min_entropy_test_text = 'random number' if min_entropy_test_result else 'non-random number'
    collision_test_text = 'random number' if collision_test_result else 'non-random number'
    markov_test_text = 'random number' if markov_test_result else 'non-random number'
    compression_test_text = 'random number' if compression_test_result else 'non-random number'
    t_tuple_test_text = 'random number' if t_tuple_test_result else 'non-random number'
    mcv_test_text = 'random number' if mcv_test_result else 'non-random number'
    chiSquare_test_text = 'random number' if chiSquare_test_result else 'non-random number'
    lz78y_test_text = 'random number' if lz78y_test_result else 'non-random number'
    multiBlock_test_text = 'random number' if multiBlock_test_result else 'non-random number'
    predictor_test_text = 'random number' if predictor_test_result else 'non-random number'
   

    bold_red_style = ParagraphStyle(
        'BoldRed',
        parent=styles['Normal'],
        fontSize=12,
        fontName='Helvetica-Bold',
        textColor='red'
    )

    bold_black_style = ParagraphStyle(
        'BoldBlack',
        parent=styles['Normal'],
        fontSize=12,
        fontName='Helvetica-Bold',
        textColor='black'
    )

    # Sample Table Data for the first table with "Final Result" in the last row
    data1 = [
        [Paragraph('Test type', styles['Normal']), 'Result', 'Test type', 'Result'],
        [Paragraph('1. Minimum Entropy Test', styles['Normal']), min_entropy_test_text,
         Paragraph('2. Collision Test', styles['Normal']), collision_test_text],
        [Paragraph('3. Markov Test', styles['Normal']), markov_test_text,
         Paragraph('4. Compression Test', styles['Normal']), compression_test_text],
        [Paragraph('5. T-Tuple Test', styles['Normal']), t_tuple_test_text,
         Paragraph('6. MCV Test', styles['Normal']), mcv_test_text],
        [Paragraph('7. Chi-Square Test', styles['Normal']), chiSquare_test_text,
         Paragraph('8. LZ78Y Test', styles['Normal']), lz78y_test_text],
        [Paragraph('9. MultiBlock test', styles['Normal']), multiBlock_test_text,
         Paragraph('10. Predictor Test', styles['Normal']), predictor_test_text],
        [Paragraph('Final Result', styles['Normal']), Paragraph(final_text, bold_red_style)],
    ]


    # Adjust column widths
    colWidths = [2 * inch, 1.5 * inch, 2 * inch, 1.5 * inch]

    # Create the first table object with adjusted column widths
    table1 = Table(data1, colWidths=colWidths)

    # Apply styles to the first table
    table1.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.blue),  # Header background color
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center text alignment
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Bold header
        ('FONTSIZE', (0, 0), (-1, -1), 10),  # Set font size
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Add gridlines
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Center vertically
    ]))

    # Create the second table with graphical analysis
    data2 = [
        [Image(graph_image_io, width=400, height=350)]
    ]
    table2 = Table(data2, colWidths=[4 * inch])
    table2.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER')]))

    # Add logo on the top-right corner (adjust the path of your logo)
    logo_path = os.path.join(os.path.dirname(__file__), 'qnulogo.png')
    logo_image = Image(logo_path, width=0.5 * inch, height=0.5 * inch)
    logo_table = Table([[logo_image]], colWidths=[6.5 * inch], rowHeights=[0.5 * inch])
    logo_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (0, 0), 'CENTRE'),  # Align logo to the left
        ('VALIGN', (100, 100), (0, 0), 'TOP'),  # Align logo to the top
    ]))

    # Add the descriptions of the NIST and Dieharder tests
    nist_description = """
    <b>NIST Statistical Tests Description:</b><br/><br/>

    1. <b>Minimum Entropy Test</b>: Measures the lowest possible entropy among all probabilities of symbols in the sequence. It helps determine the unpredictability of the data.<br/><br/>

    2. <b>Collision Test</b>: Evaluates how often identical sequences (or "collisions") appear in the data. Frequent collisions indicate a lack of randomness.<br/><br/>

    3. <b>Markov Test</b>:Analyzes the transition probabilities between symbols in a sequence to detect dependencies. A truly random sequence should have transitions that are statistically independent.<br/><br/>

    4. <b>Compression Test</b>:Checks whether the sequence can be significantly compressed. Highly compressible sequences are likely non-random, as random sequences should have little redundancy.<br/><br/>

    5. <bT-Tuple Test</b>: Examines the frequency of t-bit patterns appearing in the sequence. A deviation from expected frequencies suggests non-randomness.<br/><br/>

    6. <b>MCV Test</b>:  Identifies the most frequent value in the sequence and assesses whether it appears too often, which would indicate a lack of randomness.<br/><br/>

    7. <b>Chi-Square Test</b>:Compares the observed frequency distribution of symbols in the sequence to the expected uniform distribution. Large deviations suggest a biased sequence.<br/><br/>

    8. <b>LZ78Y Test</b>: Based on the Lempel-Ziv compression algorithm, this test measures the complexity of the sequence by checking how efficiently it can be parsed into unique substrings.<br/><br/>

    9. <b>MultiBlock Test</b>:Splits the sequence into multiple blocks and examines randomness across each block to detect local patterns or biases.<br/><br/>

    10. <b>Predictor Test</b>:Assesses whether future bits in the sequence can be predicted based on past bits. If the sequence is predictable, it is not truly random.<br/><br/>

    """


    description_style = ParagraphStyle(
        'Description',
        parent=styles['Normal'],
        fontSize=10,
        fontName='Helvetica',
        leading=12,
        spaceAfter=10
    )

    nist_description_paragraph = Paragraph(nist_description, description_style)
    

    test_results = {
        "Minimum Entropy Test":  min_entropy_test_text,
        "Collision Test":  collision_test_text ,
        "Markov Test": markov_test_text,
        "Compression Test": compression_test_text ,
        "T Tuple Test":  t_tuple_test_text,
        "MCV Test": mcv_test_text ,
        "Chi-Square Test": chiSquare_test_text,
        "Lz78Y Test": lz78y_test_text,
        "Multiblock test":  multiBlock_test_text,
        "Predictor Test": predictor_test_text ,
    }

    AIAnalysis_subtitle = Paragraph("AI Analysis:", subtitle_style)

    # Create the prompt
    prompt = "Perform a detailed analysis of the results from all the statistical tests. For each test, display the test name along with its p-value and indicate whether the result is Random or Non-Random based on the condition that if p-value > 0.05 e.g: test_name: test_result, the number is considered Random; otherwise, it is Non-Random. In the analysis, mention that basis of selecting random or non random is majority of tests response. Finally tell these many tests give random number or non random number as a result along with their names"

    # Send request to Gemini
    response1 = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[{"text": prompt}, {"text": json.dumps(test_results)}],
    )
    if response1.candidates:
        gemini_analysis = response1.candidates[0].content.parts[0].text
        # print(gemini_analysis)
    else:
        print("No response received from Gemini.")
    
    cache.set(f"{job_id}_progressReport90b", 11)

    # Format the Gemini analysis into bullet points
    formatted_output = format_markdown(gemini_analysis)

    # Convert the formatted output into a list of bullet points
    bullet_points = formatted_output.replace("<ul>", "").replace("</ul>", "").split("<li>")
    bullet_points = [point.replace("</li>", "").strip() for point in bullet_points if point.strip()]

    # Create a ListFlowable for the bullet points
    gemini_analysis_paragraph = ListFlowable(
        [ListItem(Paragraph(point, styles['Normal'])) for point in bullet_points],
        bulletType='bullet',
        
    )
    

    
    
    AIAnalysis_subtitle = Paragraph("AI Analysis:", subtitle_style)

    # print(gemini_analysis_paragraph)

    # Build the PDF document
    elements = [
        logo_table,
        # date_paragraph,
        title,
        title_space,
        nist_subtitle,
        subtitle_space,
        
        table1,
        subtitle_space,
        graph_subtitle,
        table2,
        subtitle_space,
        description_subtitle,
        subtitle_space,
        nist_description_paragraph,
        AIAnalysis_subtitle,
        gemini_analysis_paragraph
    ]
    doc.build(elements)

    # Get the PDF data and write it to the response
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response

@csrf_exempt
def get_progress_graph90b(request, job_id):
    progress = cache.get(f"{job_id}_progressReport90b", 0)
    return JsonResponse({"progress": int(progress)})

@csrf_exempt
def get_progress_ReportDieharder(request, job_id):
    progress = cache.get(f"{job_id}_progressReportDieharder", 0)
    return JsonResponse({"progress": int(progress)})

@csrf_exempt
def generate_pdf_report_dieharder(request):
    global global_graph_image

    try:
        data = json.loads(request.body)
        binary_data = data.get('binary_data', '')
        job_id = data.get('job_id', str(uuid.uuid4()))
    except json.JSONDecodeError as e:
        print('Error parsing JSON:', e)
        return HttpResponse("Invalid JSON data.", status=400)

    # Clean up binary data
    binary_data = binary_data.replace('%0A', '').replace('%20', '').replace(' ', '').replace('\n', '').replace('\r', '')

    # Create a HttpResponse object with PDF headers
    graph_response = create_graph_dieharder(request)
    graph_buffer = graph_response.content
    graph_image_io = BytesIO(graph_buffer)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="report.pdf"'

    # Set up the PDF buffer and document template with margins
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4,
                            rightMargin=10, leftMargin=10,
                            topMargin=10, bottomMargin=30, title="QNU Labs")

    # Set up styles
    styles = getSampleStyleSheet()

    # Add a headline (title)
    title = Paragraph("Report-QNu Labs", styles['Title'])
    title_space = Spacer(1, 0.0 * inch)  # Small spacer below the title

    # Add subtitles with underlining
    subtitle_style = styles['Heading2']
    subtitle_style.fontName = 'Helvetica-Bold'
    subtitle_style.fontSize = 12
    subtitle_style.underline = True

    dieharder_subtitle = Paragraph("Dieharder Tests:", subtitle_style)
    graph_subtitle = Paragraph("Graphical Analysis:", subtitle_style)

    subtitle_space = Spacer(2, 0.0 * inch)  # Spacer below the subtitles

    x = 0  # Counter for random results
    cache.set(f"{job_id}_progressReportDieharder", 0)

    # Perform tests and increment x for each test that returns True
    birthday_test_result = BirthdaySpacingsTest.BirthdaySpacingsTest(binary_data)[1]
    x += 1 if birthday_test_result else 0
    cache.set(f"{job_id}_progressReportDieharder", 1)
    parking_test_block_result = ParkingLotTest.ParkingLotTest(binary_data)[1]
    x += 1 if parking_test_block_result else 0
    cache.set(f"{job_id}_progressReportDieharder", 2)

    overlapping_5_test_result = Overlapping5PermutationTest.Overlapping5PermutationTest(binary_data)[1]
    x += 1 if overlapping_5_test_result else 0
    cache.set(f"{job_id}_progressReportDieharder", 3)

    minimum_distance_test_result = MinimumDistanceTest.MinimumDistanceTest(binary_data)[1]
    x += 1 if minimum_distance_test_result else 0
    cache.set(f"{job_id}_progressReportDieharder", 4)

    rank_31_test_result = Ranks31x31MatricesTest.Ranks31x31MatricesTest(binary_data)[1]
    x += 1 if rank_31_test_result else 0
    cache.set(f"{job_id}_progressReportDieharder", 5)

    spheres_test_result = Spheres3DTest.Spheres3DTest(binary_data)[1]
    x += 1 if spheres_test_result else 0
    cache.set(f"{job_id}_progressReportDieharder", 6)

    rank_32_result = Ranks32x32MatricesTest.Ranks32x32MatricesTest(binary_data)[1]
    x += 1 if rank_32_result else 0
    cache.set(f"{job_id}_progressReportDieharder", 7)

    craps_test_result = CrapsTest.CrapsTest(binary_data)[1]
    x += 1 if craps_test_result else 0
    cache.set(f"{job_id}_progressReportDieharder", 8)

    bitstream_test_result = BitstreamTest.BitstreamTest(binary_data)[1]
    x += 1 if bitstream_test_result else 0
    cache.set(f"{job_id}_progressReportDieharder", 9)

    gcd_test_result = MarsagliaTsangGCDTest.MarsagliaTsangGCDTest(binary_data)[1]
    x += 1 if gcd_test_result else 0
    cache.set(f"{job_id}_progressReportDieharder", 10)

    opso_test_result = OPSOTest.OPSOTest(binary_data)[1]
    x += 1 if opso_test_result else 0
    cache.set(f"{job_id}_progressReportDieharder", 11)

    oqsq_test_result = OQSOTest.OQSOTest(binary_data)[1]
    x += 1 if oqsq_test_result else 0
    cache.set(f"{job_id}_progressReportDieharder", 12)

    dna_test_result = DNATest.DNATest(binary_data)[1]
    x += 1 if dna_test_result else 0
    cache.set(f"{job_id}_progressReportDieharder", 13)

    count_one_stream_test_result = CountThe1sStreamTest.CountThe1sStreamTest(binary_data)[1]
    x += 1 if count_one_stream_test_result else 0
    cache.set(f"{job_id}_progressReportDieharder", 14)

    count_one_byte_test_result = CountThe1sByteTest.CountThe1sByteTest(binary_data)[1]
    x += 1 if count_one_byte_test_result else 0
    cache.set(f"{job_id}_progressReportDieharder", 15)

    simple_gcd_test_result = MarsagliaTsangSimpleGCDTest.MarsagliaTsangSimpleGCDTest(binary_data)[1]
    x += 1 if simple_gcd_test_result else 0
    cache.set(f"{job_id}_progressReportDieharder", 16)

    generalized_minimum_test_result = GeneralizedMinimumDistanceTest.GeneralizedMinimumDistanceTest(binary_data)[1]
    x += 1 if generalized_minimum_test_result else 0
    cache.set(f"{job_id}_progressReportDieharder", 17)

    u01_linear_complexity_test_result = TestU01LinearComplexityTest.TestU01LinearComplexityTest(binary_data)[1]
    x += 1 if u01_linear_complexity_test_result else 0
    cache.set(f"{job_id}_progressReportDieharder", 18)

    u01_longest_repeated_test_result = TestU01LongestRepeatedSubstringTest.TestU01LongestRepeatedSubstringTest(binary_data)[1]
    x += 1 if u01_longest_repeated_test_result else 0
    cache.set(f"{job_id}_progressReportDieharder", 19)

    u01_matrix_rank_test_result = TestU01MatrixRankTest.TestU01MatrixRankTest(binary_data)[1]
    x += 1 if u01_matrix_rank_test_result else 0
    cache.set(f"{job_id}_progressReportDieharder", 20)

    final_text = 'random number' if x > 10 else 'non-random number'

    # Dynamically set the result text based on the test outcome
    birthday_text = 'random number' if birthday_test_result else 'non-random number'
    parking_text = 'random number' if parking_test_block_result else 'non-random number'
    overlapping_5_text = 'random number' if overlapping_5_test_result else 'non-random number'
    minimum_distance_text = 'random number' if minimum_distance_test_result else 'non-random number'
    rank31x31_text = 'random number' if rank_31_test_result else 'non-random number'
    spheres_text = 'random number' if spheres_test_result else 'non-random number'
    rank32x32_text = 'random number' if rank_32_result else 'non-random number'
    craps_text = 'random number' if craps_test_result else 'non-random number'
    bitstream_text = 'random number' if bitstream_test_result else 'non-random number'
    gcd_text = 'random number' if gcd_test_result else 'non-random number'
    opso_text = 'random number' if opso_test_result else 'non-random number'
    oqsq_text = 'random number' if oqsq_test_result else 'non-random number'
    dna_text = 'random number' if dna_test_result else 'non-random number'
    one_stream_text = 'random number' if count_one_stream_test_result else 'non-random number'
    one_byte_text = 'random number' if count_one_byte_test_result else 'non-random number'
    simple_gcd_text = 'random number' if simple_gcd_test_result else 'non-random number'
    generalized_minimum_text = 'random number' if generalized_minimum_test_result else 'non-random number'
    u01_linear_text = 'random number' if u01_linear_complexity_test_result else 'non-random number'
    u01longest_text = 'random number' if u01_longest_repeated_test_result else 'non-random number'
    u01_matrix_text = 'random number' if u01_matrix_rank_test_result else 'non-random number'

    # Sample Table Data for the first table with "Final Result" in the last row
    data1 = [
        [Paragraph('Test type', styles['Normal']), 'Result', 'Test type', 'Result'],
        [Paragraph('1. Birthday Spacing', styles['Normal']), birthday_text, Paragraph('2. Parking Lot Test', styles['Normal']), parking_text],
        [Paragraph('3. Overlapping 5 Permutation', styles['Normal']), overlapping_5_text, Paragraph('4. Minimum Distance Test', styles['Normal']), minimum_distance_text],
        [Paragraph('5. Ranks of 31x31 Test', styles['Normal']), rank31x31_text, Paragraph('6. 3D Spheres Test', styles['Normal']), spheres_text],
        [Paragraph('7. Ranks of 32x32 Test', styles['Normal']), rank32x32_text, Paragraph('8. Craps Test', styles['Normal']), craps_text],
        [Paragraph('9. Bitstream Test', styles['Normal']), bitstream_text, Paragraph('10. Marsaglia-Tsang GCD Test', styles['Normal']), gcd_text],
        [Paragraph('11. OPSO Test', styles['Normal']), opso_text, Paragraph('12. OQSO Test', styles['Normal']), oqsq_text],
        [Paragraph('13. DNA Test', styles['Normal']), dna_text, Paragraph('14. Count the Ones (Stream) Test', styles['Normal']), one_stream_text],
        [Paragraph('15. Count the Ones (Bytes) Test', styles['Normal']), one_byte_text, Paragraph('16. Marsaglia-Tsang Simple GCD Test', styles['Normal']), simple_gcd_text],
        [Paragraph('17. Generalized Minimum Distance Test', styles['Normal']), generalized_minimum_text, Paragraph('18. TestU01 Linear Complexity Test', styles['Normal']), u01_linear_text],
        [Paragraph('19. TestU01 Longest Repeated Substring Test', styles['Normal']), u01longest_text, Paragraph('20. TestU01 Matrix Rank Test', styles['Normal']), u01_matrix_text],
        [Paragraph('Final Result', styles['Normal']), Paragraph(final_text, styles['Heading2'])],
    ]

    test_results = {
        "Birthday Test":  birthday_text,
        "Parking Test": parking_text,
        "Overlapping Test": overlapping_5_text,
        "Minimum Distance Test": minimum_distance_text,
        "31x31 Rank Test":  rank31x31_text,
        "Spheres Test": spheres_text ,
        "32x32 Rank Test": rank32x32_text,
        "Craps Test": craps_text,
        "Bitstream test":  bitstream_text,
        "GCD Test": gcd_text,
        "OPSO Test": opso_text,
        "OQSO Test": oqsq_text,
        "DNA Test": dna_text,
        "One stream Test": one_stream_text,
        "One byte Test": one_byte_text,
        "Simple Gcd Test": simple_gcd_text,
        "Generalised Minimum Test": generalized_minimum_text,
        "U01 Linear Test": u01_linear_text,
        "U01 Longest Test": u01longest_text,
        "U01 Matrix Test": u01_matrix_text,
    }

    AIAnalysis_subtitle = Paragraph("AI Analysis:", subtitle_style)

    # Create the prompt
    prompt = "Perform a detailed analysis of the results from all the statistical tests. For each test, display the test name along with its p-value and indicate whether the result is Random or Non-Random based on the condition that if p-value > 0.05 e.g: test_name: test_result, the number is considered Random; otherwise, it is Non-Random. In the analysis, mention that basis of selecting random or non random is majority of tests response. Finally tell these many tests give random number or non random number as a result along with their names"

    # Send request to Gemini
    response1 = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[{"text": prompt}, {"text": json.dumps(test_results)}],
    )
    if response1.candidates:
        gemini_analysis = response1.candidates[0].content.parts[0].text
        # print(gemini_analysis)
    else:
        print("No response received from Gemini.")
    
    cache.set(f"{job_id}_progressReportDieharder", 21)

    description_style = ParagraphStyle(
        'Description',
        parent=styles['Normal'],
        fontSize=10,
        fontName='Helvetica',
        leading=12,
        spaceAfter=10
    )

    formatted_output = format_markdown(gemini_analysis)

    # Convert the formatted output into a list of bullet points
    bullet_points = formatted_output.replace("<ul>", "").replace("</ul>", "").split("<li>")
    bullet_points = [point.replace("</li>", "").strip() for point in bullet_points if point.strip()]

    # Create a ListFlowable for the bullet points
    gemini_analysis_paragraph = ListFlowable(
        [ListItem(Paragraph(point, styles['Normal'])) for point in bullet_points],
        bulletType='bullet',
        
    )
    
    AIAnalysis_subtitle = Paragraph("AI Analysis:", subtitle_style)



    # Adjust column widths
    colWidths = [2 * inch, 1.5 * inch, 2 * inch, 1.5 * inch]

    # Create the first table object with adjusted column widths
    table1 = Table(data1, colWidths=colWidths)

    # Apply styles to the first table
    table1.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.blue),  # Header background color
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center text alignment
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Bold header
        ('FONTSIZE', (0, 0), (-1, -1), 10),  # Set font size
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Add gridlines
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Center vertically
    ]))

    # Use the BytesIO object to create an Image
    graph_image = Image(graph_image_io, width=7 * inch, height=4.5 * inch)

    cache.set(f"{job_id}_progressReportDieharder", 22)

    # Add a paragraph with the current date
    # current_date = datetime.now().strftime("%B %d, %Y")  # Format as "December 06, 2024"
    date_style = ParagraphStyle('Date', parent=styles['Normal'], fontSize=10, fontName='Helvetica-Bold', alignment=2, spaceAfter=10)
    # date_paragraph = Paragraph(f"Date: {current_date}", date_style)

    # Add logo on the top-right corner
    logo_path = os.path.join(os.path.dirname(__file__), 'qnulogo.png')
    logo_image = Image(logo_path, width=0.5 * inch, height=0.5 * inch)
    logo_table = Table([[logo_image]], colWidths=[6.5 * inch], rowHeights=[0.5 * inch])
    logo_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (0, 0), 'CENTRE'),  # Align logo to the left
        ('VALIGN', (100, 100), (0, 0), 'TOP'),  # Align logo to the top
    ]))

    description_subtitle = Paragraph("Dieharder Tests Description:", subtitle_style)
    # Dieharder Tests Description
    dieharder_description = """
    1. <b>Birthday Spacing</b>: This test simulates the "birthday paradox" by generating random "birthdays" and measuring the spacing between them. It checks if the spacings between these random points are uniformly distributed. Non-random sequences may show clustering or gaps in the spacings.<br/><br/>
    2. <b>Overlapping Permutations</b>: This test checks the frequency of overlapping sequences of five random numbers. It ensures that all possible permutations of five numbers appear with approximately equal frequency. Non-random sequences may show biases in certain permutations.<br/><br/>
    3. <b>Ranks of 31x31 and 32x32 Matrices</b>: This test evaluates the rank of random matrices generated from the sequence. It checks if the matrices are of full rank, as expected in a random sequence. Non-random sequences may produce matrices with lower rank due to dependencies.<br/><br/>
    4. <b>Ranks of 6x8 Matrices</b>: Similar to the above test, but it uses smaller matrices (6x8). It checks for linear independence in smaller subsets of the sequence. Non-random sequences may fail to produce full-rank matrices.<br/><br/>
    5. <b>Monkey Tests</b>: This test simulates monkeys randomly typing on a keyboard. It checks if the sequence behaves like random typing, where all possible patterns should appear with equal probability. Non-random sequences may show biases or missing patterns.<br/><br/>
    6. <b>Count the 1s</b>: This test counts the number of ones in specific bit lengths of the sequence. It ensures that the count of ones is consistent with the expected binomial distribution. Non-random sequences may show deviations in the number of ones.<br/><br/>
    7. <b>Count the 1s in Specific Bytes</b>: This test focuses on the number of ones in specific byte lengths. It checks if the distribution of ones within bytes is uniform. Non-random sequences may show biases in certain byte patterns.<br/><br/>
    8. <b>Parking Lot Test</b>: This test simulates parking cars randomly in a parking lot. It checks if the placement of cars (points) is uniformly distributed. Non-random sequences may show clustering or gaps in the placement of points.<br/><br/>
    9. <b>Minimum Distance Test</b>: This test measures the minimum distance between random points placed in a square. It checks if the distances between points follow the expected distribution. Non-random sequences may show points that are too close or too far apart.<br/><br/>
    10. <b>Random Spheres Test</b>: This test places random points in a cube and checks the distribution of distances between them. It ensures that the distances are consistent with a random distribution. Non-random sequences may show unusual clustering or spacing.<br/><br/>
    11. <b>Squeeze Test</b>: This test compresses the sequence and checks for compressibility. A truly random sequence should not be compressible, as it lacks patterns. If the sequence can be compressed significantly, it indicates non-randomness.<br/><br/>
    12. <b>Overlapping Sums Test</b>: This test checks the distribution of sums of overlapping subsequences. It ensures that the sums are normally distributed, as expected in a random sequence. Non-random sequences may show deviations in the distribution of sums.<br/><br/>
    13. <b>Runs Test</b>: Similar to the NIST Runs Test, this test counts the number of runs (sequences of consecutive identical bits) in the sequence. It checks if the number of runs is consistent with a random sequence. Non-random sequences may have too many or too few runs.<br/><br/>
    14. <b>Craps Test</b>: This test simulates the game of craps using the sequence as a source of random numbers. It checks if the outcomes of the dice rolls are consistent with the expected probabilities. Non-random sequences may show biases in the outcomes.<br/><br/>
    15. <b>Marsaglia and Tsang GCD Test</b>: This test uses the greatest common divisor (GCD) of pairs of numbers generated from the sequence. It checks if the distribution of GCD values is consistent with a random sequence. Non-random sequences may show deviations in the GCD distribution.<br/><br/>
    16. <b>STS Monobit Test</b>: This test checks the proportion of ones and zeros in the sequence. It ensures that the sequence has an approximately equal number of ones and zeros. Non-random sequences may show a bias towards ones or zeros.<br/><br/>
    17. <b>STS Runs Test</b>: Similar to the NIST Runs Test, this test counts the number of runs in the sequence. It checks if the sequence has the expected number of runs for a random sequence. Non-random sequences may have too many or too few runs.<br/><br/>
    18. <b>STS Serial Test</b>: This test examines the frequency of overlapping m-bit patterns in the sequence. It ensures that all possible patterns appear with approximately equal frequency. Non-random sequences may show biases in certain patterns.<br/><br/>
    19. <b>RGB Bit Distribution Test</b>: This test checks the distribution of bits in RGB color values generated from the sequence. It ensures that the bits are uniformly distributed across the color channels. Non-random sequences may show biases in certain color channels.<br/><br/>
    20. <b>RGB Generalized Minimum Distance Test</b>: This test measures the minimum distance between RGB color values generated from the sequence. It checks if the distances between colors are consistent with a random distribution. Non-random sequences may show unusual clustering or spacing in color values.<br/><br/>
    """

    description_style = ParagraphStyle(
        'Description',
        parent=styles['Normal'],
        fontSize=10,
        fontName='Helvetica',
        leading=12,
        spaceAfter=10
    )

    dieharder_description_paragraph = Paragraph(dieharder_description, description_style)

    # Build the PDF document
    elements = [
        logo_table,
        # date_paragraph,
        title,
        title_space,
        dieharder_subtitle,
        subtitle_space,
        table1,
        subtitle_space,
        graph_subtitle,
        subtitle_space,
        graph_image,
        subtitle_space,
        description_subtitle,
        dieharder_description_paragraph,
        AIAnalysis_subtitle,
        gemini_analysis_paragraph,
    ]

    doc.build(elements)

    # Write the PDF to the HttpResponse
    response.write(buffer.getvalue())
    buffer.close()

    return response


@csrf_exempt
def generate_pdf_report_server(request):
    global global_graph_image
    try:
        data = json.loads(request.body)
        binary_data = data.get('binary_data', '')
        job_id = data.get('job_id', str(uuid.uuid4()))
        
    except json.JSONDecodeError as e:
        print('Error parsing JSON:', e)
        return HttpResponse("Invalid JSON data.", status=400)

    cache.set(f"{job_id}_progressReportServer", 0)

    binary_data = binary_data.replace('%0A', '').replace('%20', '').replace(' ', '').replace('\n', '').replace('\r', '')

    
    # Create a HttpResponse object with PDF headers
    graph_response1 = create_graph(request)
    graph_response = create_graph_dieharder(request)
    graph_response2 = create_graph_nist90b(request)

    graph_buffer1 = graph_response1.content
    graph_buffer = graph_response.content
    graph_buffer2 = graph_response2.content

    graph_image_io1 = BytesIO(graph_buffer1)
    graph_image_io = BytesIO(graph_buffer)
    graph_image_io2 = BytesIO(graph_buffer2)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="report.pdf"'

    # Set up the PDF buffer and document template with margins
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4,
                            rightMargin=10, leftMargin=10,
                            topMargin=10, bottomMargin=30, title="QNU Labs")

    cache.set(f"{job_id}_progressReportServer", 1)
    # Set up styles
    styles = getSampleStyleSheet()

    # Add a headline (title)
    title = Paragraph("Report-QNu Labs", styles['Title'])
    title_space = Spacer(1, 0.0 * inch)  # Small spacer below the title

    # Add subtitles with underlining
    subtitle_style = styles['Heading2']
    subtitle_style.fontName = 'Helvetica-Bold'
    subtitle_style.fontSize = 12
    subtitle_style.underline = True

    nist_subtitle = Paragraph("Statistical Tests:", subtitle_style)
    subtitle_space = Spacer(1, 0.5 * inch)  # Spacer below the subtitles
    
    graph_subtitle = Paragraph("Graphical Analysis:", subtitle_style)



    x = 0

    bold_red_style = ParagraphStyle(
    'BoldRed', 
    parent=styles['Normal'], 
    fontSize=12,          # Adjust the font size as needed
    fontName='Helvetica-Bold',  # Bold font
    textColor='red'       # Red color
    )
    
    cache.set(f"{job_id}_progressReportServer", 2)
    # Perform tests and increment x for each test that returns True
    birthday_test_result = BirthdaySpacingsTest.BirthdaySpacingsTest(binary_data)[1]
    x += 1 if birthday_test_result else 0
    cache.set(f"{job_id}_progressReportServer", 3)
 

    parking_test_block_result = ParkingLotTest.ParkingLotTest(binary_data)[1]
    x += 1 if parking_test_block_result else 0
    cache.set(f"{job_id}_progressReportServer", 4)
    

    overlapping_5_test_result = Overlapping5PermutationTest.Overlapping5PermutationTest(binary_data)[1]
    x += 1 if overlapping_5_test_result else 0
    cache.set(f"{job_id}_progressReportServer", 5)

    minimum_distance_test_result = MinimumDistanceTest.MinimumDistanceTest(binary_data)[1]
    x += 1 if minimum_distance_test_result else 0
    cache.set(f"{job_id}_progressReportServer", 6)

    rank_31_test_result = Ranks31x31MatricesTest.Ranks31x31MatricesTest(binary_data)[1]
    x += 1 if rank_31_test_result else 0
    cache.set(f"{job_id}_progressReportServer", 7)

    spheres_test_result = Spheres3DTest.Spheres3DTest(binary_data)[1]
    x += 1 if spheres_test_result else 0
    cache.set(f"{job_id}_progressReportServer", 8)

    rank_32_result = Ranks32x32MatricesTest.Ranks32x32MatricesTest(binary_data)[1]
    x += 1 if rank_32_result else 0
    cache.set(f"{job_id}_progressReportServer", 9)

    craps_test_result = CrapsTest.CrapsTest(binary_data)[1]
    x += 1 if craps_test_result else 0
    cache.set(f"{job_id}_progressReportServer", 10)

    bitstream_test_result = BitstreamTest.BitstreamTest(binary_data)[1]
    x += 1 if bitstream_test_result else 0
    cache.set(f"{job_id}_progressReportServer", 11)

    gcd_test_result = MarsagliaTsangGCDTest.MarsagliaTsangGCDTest(binary_data)[1]
    x += 1 if gcd_test_result else 0
    cache.set(f"{job_id}_progressReportServer", 12)

    opso_test_result = OPSOTest.OPSOTest(binary_data)[1]
    x += 1 if opso_test_result else 0
    cache.set(f"{job_id}_progressReportServer", 13)

    oqsq_test_result = OQSOTest.OQSOTest(binary_data)[1]
    x += 1 if oqsq_test_result else 0
    cache.set(f"{job_id}_progressReportServer", 14)

    dna_test_result = DNATest.DNATest(binary_data)[1]
    x += 1 if dna_test_result else 0
    cache.set(f"{job_id}_progressReportServer", 15)

    count_one_stream_test_result = CountThe1sStreamTest.CountThe1sStreamTest(binary_data)[1]
    x += 1 if count_one_stream_test_result else 0
    cache.set(f"{job_id}_progressReportServer", 16)

    count_one_byte_test_result = CountThe1sByteTest.CountThe1sByteTest(binary_data)[1]
    x += 1 if count_one_byte_test_result else 0
    cache.set(f"{job_id}_progressReportServer", 17)

    simple_gcd_test_result = MarsagliaTsangSimpleGCDTest.MarsagliaTsangSimpleGCDTest(binary_data)[1]
    x += 1 if simple_gcd_test_result else 0
    cache.set(f"{job_id}_progressReportServer", 18)

    generalized_minimum_test_result = GeneralizedMinimumDistanceTest.GeneralizedMinimumDistanceTest(binary_data)[1]
    x += 1 if generalized_minimum_test_result else 0
    cache.set(f"{job_id}_progressReportServer", 19)

    u01_linear_complexity_test_result = TestU01LinearComplexityTest.TestU01LinearComplexityTest(binary_data)[1]
    x += 1 if u01_linear_complexity_test_result else 0
    cache.set(f"{job_id}_progressReportServer", 20)

    u01_longest_repeated_test_result = TestU01LongestRepeatedSubstringTest.TestU01LongestRepeatedSubstringTest(binary_data)[1]
    x += 1 if u01_longest_repeated_test_result else 0
    cache.set(f"{job_id}_progressReportServer", 21)

    u01_matrix_rank_test_result = TestU01MatrixRankTest.TestU01MatrixRankTest(binary_data)[1]
    x += 1 if u01_matrix_rank_test_result else 0
    cache.set(f"{job_id}_progressReportServer", 22)

    frequency_test_result = FrequencyTest.monobit_test(binary_data)[1]
    if frequency_test_result:
        x += 1
    cache.set(f"{job_id}_progressReportServer", 23)

    frequency_test_block_result = FrequencyTest.block_frequency(binary_data)[1]
    if frequency_test_block_result:
        x += 1
    cache.set(f"{job_id}_progressReportServer", 24)

    runs_test_result = RunTest.run_test(binary_data)[1]
    if runs_test_result:
        x += 1
    cache.set(f"{job_id}_progressReportServer", 25)

    approximate_entropy_test_result = ApproximateEntropy.approximate_entropy_test(binary_data)[1]
    if approximate_entropy_test_result:
        x += 1
    cache.set(f"{job_id}_progressReportServer", 26)

    longest_run_of_one_test_result = RunTest.longest_one_block_test(binary_data)[1]
    if longest_run_of_one_test_result:
        x += 1
    cache.set(f"{job_id}_progressReportServer", 27)

    binary_matrix_rank_test_result = Matrix.binary_matrix_rank_text(binary_data)[1]
    if binary_matrix_rank_test_result:
        x += 1
    cache.set(f"{job_id}_progressReportServer", 28)

    dft_test_result = SpectralTest.spectral_test(binary_data)[1]
    if dft_test_result:
        x += 1
    cache.set(f"{job_id}_progressReportServer", 29)

    non_overlapping_test_result = TemplateMatching.non_overlapping_test(binary_data)[1]
    if non_overlapping_test_result:
        x += 1
    cache.set(f"{job_id}_progressReportServer", 30)

    overlapping_test_result = TemplateMatching.overlapping_patterns(binary_data)[1]
    if overlapping_test_result:
        x += 1
    cache.set(f"{job_id}_progressReportServer", 31)

    maurers_universal_test_result = Universal.statistical_test(binary_data)[1]
    if maurers_universal_test_result:
        x += 1
    cache.set(f"{job_id}_progressReportServer", 32)

    linear_complexity_test_result = ComplexityTest.linear_complexity_test(binary_data)[1]
    if linear_complexity_test_result:
        x += 1
    cache.set(f"{job_id}_progressReportServer", 33)

    serial_test_result = Serial.serial_test(binary_data)[1]
    if serial_test_result:
        x += 1
    cache.set(f"{job_id}_progressReportServer", 34)

    cumulative_sums_test_result = CumulativeSums.cumulative_sums_test(binary_data)[1]
    if cumulative_sums_test_result:
        x += 1
    cache.set(f"{job_id}_progressReportServer", 35)

    random_excursions_test_result = RandomExcursions.random_excursions_test(binary_data)[1]
    if random_excursions_test_result:
        x += 1
    cache.set(f"{job_id}_progressReportServer", 36)

    random_excursion_variant_test_result = RandomExcursions.variant_test(binary_data)[1]
    if random_excursion_variant_test_result:
        x += 1
    cache.set(f"{job_id}_progressReportServer", 37)

    autocorrelation_test_result = AutocorrelationTest.autocorrelation_test(binary_data)[1]
    if autocorrelation_test_result:
        x += 1
    cache.set(f"{job_id}_progressReportServer", 38)

    adaptive_statistical_test_result = AdaptiveStatisticalTest.adaptive_statistical_test(binary_data)[1]
    if adaptive_statistical_test_result:
        x += 1
    cache.set(f"{job_id}_progressReportServer", 39)

    
    minEntropy_test_result = MinEntropyTest.MinEntropyTest(binary_data)[1]
    if minEntropy_test_result:
        x += 1
    cache.set(f"{job_id}_progressReportServer", 40)

    
    collision_test_result = CollisionTest.CollisionTest(binary_data)[1]
    if collision_test_result:
        x += 1
    cache.set(f"{job_id}_progressReportServer", 41)

    
    markov_test_result = MarkovTest.MarkovTest(binary_data)[1]
    if markov_test_result:
        x += 1
    cache.set(f"{job_id}_progressReportServer", 42)

    
    compression_test_result = CompressionTest.CompressionTest(binary_data)[1]
    if compression_test_result:
        x += 1
    cache.set(f"{job_id}_progressReportServer", 43)

    
    ttuple_test_result = TTupleTest.TTupleTest(binary_data)[1]
    if ttuple_test_result:
        x += 1
    cache.set(f"{job_id}_progressReportServer", 44)

    
    mcv_test_result = MostCommonValueTest.MostCommonValueTest(binary_data)[1]
    if mcv_test_result:
        x += 1
    cache.set(f"{job_id}_progressReportServer", 45)


    chiSquare_test_result = ChiSquareTest.ChiSquareTest(binary_data)[1]
    if chiSquare_test_result:
        x += 1
    cache.set(f"{job_id}_progressReportServer", 46)

    
    l278y_test_result = LZ78YTest.LZ78YTest(binary_data)[1]
    if l278y_test_result:
        x += 1
    cache.set(f"{job_id}_progressReportServer", 47)

    
    multiBlock_test_result = MultiBlockEntropyTest.MultiBlockEntropyTest(binary_data)[1]
    if multiBlock_test_result:
        x += 1
    cache.set(f"{job_id}_progressReportServer", 48)

    
    predictor_test_result = PredictorTest.PredictorTest(binary_data)[1]
    if predictor_test_result:
        x += 1
    cache.set(f"{job_id}_progressReportServer", 49)


    final_text='random number' if x > 23 else 'non-random number'

    
    # Dynamically set the result text based on the test outcome
    birthday_text = 'random number' if birthday_test_result else 'non-random number'
    parking_text= 'random number' if parking_test_block_result else 'non-random number'
    oevrlapping_5_text= 'random number' if overlapping_5_test_result else 'non-random number'
    minimum_distance_text= 'random number' if minimum_distance_test_result else 'non-random number'
    rank31x31_text= 'random number' if rank_31_test_result else 'non-random number'
    spheres_text= 'random number' if spheres_test_result else 'non-random number'
    rank32x32_text= 'random number' if rank_32_result else 'non-random number'
    craps_text= 'random number' if craps_test_result else 'non-random number'
    bitstream_text= 'random number' if bitstream_test_result else 'non-random number'
    gcd_text= 'random number' if gcd_test_result else 'non-random number'
    opso_text= 'random number' if opso_test_result else 'non-random number'
    oqsq_text= 'random number' if oqsq_test_result else 'non-random number'
    dna_text= 'random number' if dna_test_result else 'non-random number'
    one_stream_text= 'random number' if count_one_stream_test_result else 'non-random number'
    one_byte_text= 'random number' if count_one_byte_test_result else 'non-random number'
    simple_gcd_text= 'random number' if simple_gcd_test_result else 'non-random number'
    generalised_minimum_text= 'random number' if generalized_minimum_test_result else 'non-random number'
    u01_linear_text= 'random number' if u01_linear_complexity_test_result else 'non-random number'
    u01longest_text= 'random number' if u01_longest_repeated_test_result else 'non-random number'
    u01_matrix_text= 'random number' if u01_matrix_rank_test_result else 'non-random number'

    frequency_test_text = 'random number' if frequency_test_result else 'non-random number'
    frequency_test_block_text = 'random number' if frequency_test_block_result else 'non-random number'
    runs_text = 'random number' if runs_test_result else 'non-random number'
    approximate_entropy_text = 'random number' if approximate_entropy_test_result else 'non-random number'
    longest_run_of_ones_text = 'random number' if longest_run_of_one_test_result else 'non-random number'
    binary_matrix_rank_text = 'random number' if binary_matrix_rank_test_result else 'non-random number'
    dft_text = 'random number' if dft_test_result else 'non-random number'
    non_overlapping_text = 'random number' if non_overlapping_test_result else 'non-random number'
    overlapping_text = 'random number' if overlapping_test_result else 'non-random number'
    maurers_universal_text = 'random number' if maurers_universal_test_result else 'non-random number'
    linear_complexity_text = 'random number' if linear_complexity_test_result else 'non-random number'
    serial_text = 'random number' if serial_test_result else 'non-random number'
    cumulative_sums_text = 'random number' if cumulative_sums_test_result else 'non-random number'
    random_excursion_variant_text = 'random number' if random_excursion_variant_test_result else 'non-random number'
    random_excursion_text = 'random number' if random_excursions_test_result else 'non-random number'
    autocorrelation_text = 'random number' if autocorrelation_test_result else 'non-random number'
    adaptive_statistical_text = 'random number' if adaptive_statistical_test_result else 'non-random number'

    minEntropy_text = 'random number' if minEntropy_test_result else 'non-random number'
    collision_text = 'random number' if collision_test_result else 'non-random number'
    markov_text = 'random number' if markov_test_result else 'non-random number'
    compression_text = 'random number' if compression_test_result else 'non-random number'
    ttuple_text = 'random number' if ttuple_test_result else 'non-random number'
    mcv_text = 'random number' if mcv_test_result else 'non-random number'
    chiSquare_text = 'random number' if chiSquare_test_result else 'non-random number'
    l278y_text = 'random number' if l278y_test_result else 'non-random number'
    multiBlock_text = 'random number' if multiBlock_test_result else 'non-random number'
    predictor_text = 'random number' if predictor_test_result else 'non-random number'


    # Sample Table Data for the first table with "Final Result" in the last row
    data1 = [
        ['Test Type', 'Result', 'Test type', 'Result'],
        [Paragraph('1. Birthday Spacing', styles['Normal']), birthday_text, Paragraph('2. Parking Lot Test', styles['Normal']), parking_text],
        [Paragraph('3. Overlapping 5 Permutation', styles['Normal']), oevrlapping_5_text, Paragraph('4. Minimum Distance Test', styles['Normal']), minimum_distance_text],
        [Paragraph('5. Ranks of 31x31 Test', styles['Normal']), rank31x31_text, Paragraph('6. 3d Spheres Test', styles['Normal']), spheres_text],
        [Paragraph('7. Ranks of 32x32 Test', styles['Normal']), rank32x32_text, Paragraph('8. Craps Test', styles['Normal']), craps_text],
        [Paragraph('9. Bitstream test', styles['Normal']), bitstream_text, Paragraph('10. Marsaglia-Tsang GCD Test', styles['Normal']), gcd_text],
        [Paragraph('11. OPSO Test', styles['Normal']), opso_text, Paragraph('12. OQSO Test', styles['Normal']),oqsq_text],
        [Paragraph('13. DNA Test', styles['Normal']), dna_text, Paragraph('14. Count the Ones(Stream) Test', styles['Normal']), one_stream_text],
        [Paragraph('15. Count the Ones(Bytes) Test', styles['Normal']),one_byte_text,Paragraph('16. Marsalia-Tsang Simple GCD Test', styles['Normal']), simple_gcd_text],
        [Paragraph('17. Generalized Minimum DIstance Test', styles['Normal']),generalised_minimum_text,Paragraph('18. TestU01 Linear Complexity Test', styles['Normal']), u01_linear_text],
        [Paragraph('18. TestU01 Longest Repeated Substring Test', styles['Normal']), u01longest_text,Paragraph('20. TestU01 Matrix Rank Test', styles['Normal']),u01_matrix_text],
        
        [Paragraph('21. Frequency Test', styles['Normal']), frequency_test_text,
         Paragraph('22. Frequency Test within a Block', styles['Normal']), frequency_test_block_text],
        [Paragraph('23. Runs Test', styles['Normal']), runs_text,
         Paragraph('24. Test for the longest Run of Ones', styles['Normal']), longest_run_of_ones_text],
        [Paragraph('25. Binary Matrix Rank Test', styles['Normal']), binary_matrix_rank_text,
         Paragraph('26. Discrete Fourier Transform Test', styles['Normal']), dft_text],
        [Paragraph('27. Non-overlapping Template Match', styles['Normal']), non_overlapping_text,
         Paragraph('28. Overlapping Template Matching Test', styles['Normal']), overlapping_text],
        [Paragraph('29. Maurers Universal test', styles['Normal']), maurers_universal_text,
         Paragraph('30. Linear complexity Test', styles['Normal']), linear_complexity_text],
        [Paragraph('31. Serial Test', styles['Normal']), serial_text,
         Paragraph('32. Approximate Entropy Test', styles['Normal']), approximate_entropy_text],
        [Paragraph('33. Cumulative Sum Test', styles['Normal']), cumulative_sums_text,
         Paragraph('34. Random Excursions Test', styles['Normal']), random_excursion_text],
        [Paragraph('35. Random Excursions Variant Test', styles['Normal']), random_excursion_variant_text,
         Paragraph('36. Autocorrelation Test', styles['Normal']), autocorrelation_text],
        [Paragraph('37. Adaptive Statistical Test', styles['Normal']), adaptive_statistical_text,
         Paragraph('38. Minimum Entropy Test', styles['Normal']), minEntropy_text],
        [Paragraph('39. Collision Test', styles['Normal']), collision_text,
         Paragraph('40. Markov Test', styles['Normal']),  markov_text],
        [Paragraph('41. Compression Test', styles['Normal']), compression_text,
         Paragraph('42. T-Tuple Test', styles['Normal']), ttuple_text],
        [Paragraph('43. MCV Test', styles['Normal']), mcv_text,
         Paragraph('44. Chi-Square Test', styles['Normal']), chiSquare_text],
        [Paragraph('45. LZ78Y Test', styles['Normal']), l278y_text,
         Paragraph('46. MultiBlock Test', styles['Normal']), multiBlock_text],
        [Paragraph('47. Predictor Test', styles['Normal']), predictor_text],


        [Paragraph(' Final Result', styles['Normal']),  Paragraph(final_text, bold_red_style)],
       
    ]

    # Adjust column widths
    colWidths = [2 * inch, 1.5 * inch, 2 * inch, 1.5 * inch]

    # Create the first table object with adjusted column widths
    table1 = Table(data1, colWidths=colWidths)

    # Apply styles to the first table
    table1.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.blue),  # Header background color
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center text alignment
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Bold header
        ('FONTSIZE', (0, 0), (-1, -1), 10),  # Set font size
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Add gridlines
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Vertically align text to the middle
        ('WORDWRAP', (0, 0), (-1, -1), True),  # Enable text wrapping
    ]))
    

    test_results = {
        "Frequency Test": frequency_test_text,
        "Frequency Test within a Block": frequency_test_block_text,
        "Runs Test": runs_text,
        "Test for the Longest Run of Ones": longest_run_of_ones_text,
        "Binary Matrix Rank Test": binary_matrix_rank_text,
        "Discrete Fourier Transform Test": dft_text,
        "Non-overlapping Template Match": non_overlapping_text,
        "Overlapping Template Matching Test": overlapping_text,
        "Maurers Universal test": maurers_universal_text,
        "Linear complexity Test": linear_complexity_text,
        "Serial Test": serial_text,
        "Approximate Entropy Test": approximate_entropy_text,
        "Cumulative Sum Test": cumulative_sums_text,
        "Random Excursions Test": random_excursion_text,
        "Random Excursions Variant Test": random_excursion_variant_text,
        "Autocorrelation Test": autocorrelation_text,
        "Adaptive Statistical Test": adaptive_statistical_text,
        
        "Birthday Test":  birthday_text,
        "Parking Test": parking_text,
        "Overlapping Test": oevrlapping_5_text,
        "Minimum Distance Test": minimum_distance_text,
        "31x31 Rank Test":  rank31x31_text,
        "Spheres Test": spheres_text ,
        "32x32 Rank Test": rank32x32_text,
        "Craps Test": craps_text,
        "Bitstream test":  bitstream_text,
        "GCD Test": gcd_text,
        "OPSO Test": opso_text,
        "OQSO Test": oqsq_text,
        "DNA Test": dna_text,
        "One stream Test": one_stream_text,
        "One byte Test": one_byte_text,
        "Simple Gcd Test": simple_gcd_text,
        "Generalised Minimum Test": generalised_minimum_text,
        "U01 Linear Test": u01_linear_text,
        "U01 Longest Test": u01longest_text,
        "U01 Matrix Test": u01_matrix_text,

        "Minimum Entropy Test":  minEntropy_text,
        "Collision Test":  collision_text ,
        "Markov Test": markov_text,
        "Compression Test": compression_text ,
        "T Tuple Test":  ttuple_text,
        "MCV Test": mcv_text ,
        "Chi-Square Test": chiSquare_text,
        "Lz78Y Test": l278y_text,
        "Multiblock test":  multiBlock_text,
        "Predictor Test": predictor_text ,
    }

    cache.set(f"{job_id}_progressReportServer", 50)
    AIAnalysis_subtitle = Paragraph("AI Analysis:", subtitle_style)

    # Create the prompt
    prompt = "Perform a detailed analysis of the results from all the statistical tests. For each test, display the test name along with its p-value and indicate whether the result is Random or Non-Random based on the condition that if p-value > 0.05 e.g: test_name: test_result, the number is considered Random; otherwise, it is Non-Random. In the analysis, mention that basis of selecting random or non random is majority of tests response. Finally tell these many tests give random number or non random number as a result along with their names"

    # Send request to Gemini
    response1 = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[{"text": prompt}, {"text": json.dumps(test_results)}],
    )
    if response1.candidates:
        gemini_analysis = response1.candidates[0].content.parts[0].text
        # print(gemini_analysis)
    else:
        print("No response received from Gemini.")
    
    cache.set(f"{job_id}_progressReportServer", 51)


    formatted_output = format_markdown(gemini_analysis)

    # Convert the formatted output into a list of bullet points
    bullet_points = formatted_output.replace("<ul>", "").replace("</ul>", "").split("<li>")
    bullet_points = [point.replace("</li>", "").strip() for point in bullet_points if point.strip()]

    # Create a ListFlowable for the bullet points
    gemini_analysis_paragraph = ListFlowable(
        [ListItem(Paragraph(point, styles['Normal'])) for point in bullet_points],
        bulletType='bullet',
        
    )
    

    # Use the BytesIO object to create an Image
    graph_image1 = Image(graph_image_io1)
    graph_image = Image(graph_image_io)
    graph_image2 = Image(graph_image_io2)
    
    # Automatically scale the image
    graph_image.drawHeight = 4.5 * inch  # Set height
    graph_image.drawWidth = 7 * inch  # Set width

    graph_image1.drawHeight = 4.5 * inch  # Set height
    graph_image1.drawWidth = 7 * inch  # Set width

    graph_image2.drawHeight = 4.5 * inch  # Set height
    graph_image2.drawWidth = 7 * inch  # Set width


    # Ensure the image fits within the page margins
    max_width = A4[0] - 20  # A4 width minus margins
    max_height = A4[1] - 20  # A4 height minus margins

    # Adjust if necessary
    if graph_image.drawWidth > max_width or graph_image.drawHeight > max_height:
        aspect_ratio = graph_image.drawWidth / graph_image.drawHeight
        if graph_image.drawWidth > max_width:
            graph_image.drawWidth = max_width
            graph_image.drawHeight = max_width / aspect_ratio
        if graph_image.drawHeight > max_height:
            graph_image.drawHeight = max_height
            graph_image.drawWidth = max_height * aspect_ratio


    

     # Add a paragraph with the current date
    date_style = ParagraphStyle('Date', parent=styles['Normal'], fontSize=10, fontName='Helvetica-Bold',  alignment=2, spaceAfter=10)
    

    logo_path = os.path.join(os.path.dirname(__file__), 'qnulogo.png')

    logo_image = Image(logo_path, width=0.5 * inch, height=0.5 * inch)
    # logo_image.hAlign = 'LEFT'  # Right-align the image on the page
    # logo_image.vAlign = 'TOP'    # Top-align the image on the page

    logo_table = Table([[logo_image]], colWidths=[6.5 * inch], rowHeights=[0.5 * inch])
    logo_table.setStyle(TableStyle([
    ('ALIGN', (0, 0), (0, 0), 'CENTRE'),  # Align logo to the left
    ('VALIGN', (100, 100), (0, 0), 'TOP'),  # Align logo to the top
    
    ]))
    
    cache.set(f"{job_id}_progressReportServer", 52)

    # Build the PDF with the title, subtitles, tables, graph, and spacers
    elements = []
    # elements.append(binary_data)
    elements.append(logo_table)
    elements.append(title)
    
    elements.append(title_space)  # Add space after the title
    elements.append(nist_subtitle)
    
    elements.append(table1)
    # elements.append(Spacer(1, 0.5 * inch))  # Spacer between tables
    # elements.append(other_tests_subtitle)
    elements.append(subtitle_space)  # Spacer below the second subtitle
    # elements.append(table2)
    elements.append(PageBreak())
    elements.append(graph_subtitle)
    elements.append(subtitle_space)  # Spacer below the graph subtitle
    
    elements.append(graph_image1)
    elements.append(subtitle_space)
    elements.append(graph_image)
    elements.append(subtitle_space)
    elements.append(graph_image2)
    
    elements.append(AIAnalysis_subtitle)
    elements.append(gemini_analysis_paragraph)


    
    doc.build(elements)

    # Write the PDF to the HttpResponse
    response.write(buffer.getvalue())
    buffer.close()

    return response

@csrf_exempt
def get_progress_server(request, job_id):
    progress = cache.get(f"{job_id}_progressReportServer", 0)
    return JsonResponse({"progress": int(progress)})

import uuid
from django.core.cache import cache

@csrf_exempt
def generate_final_ans(request):
    if request.method == 'POST':
        try:
           
            data = json.loads(request.body)
            binary_data = data.get('binary_data', '')
            scheduled_time_str = data.get('scheduled_time', '')
            job_id = data.get('job_id', str(uuid.uuid4()))

            if not binary_data:
                return JsonResponse({"error": "binary_data is missing or empty"}, status=400)

            if not scheduled_time_str:
                return JsonResponse({"error": "scheduled_time is required"}, status=400)

            try:
                scheduled_time = datetime.datetime.strptime(scheduled_time_str, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                return JsonResponse({"error": "Invalid scheduled_time format. Use 'YYYY-MM-DD HH:MM:SS'."}, status=400)

            current_time = datetime.datetime.now()
            time_difference = (scheduled_time - current_time).total_seconds()
            if time_difference > 0:
                time.sleep(time_difference)

            x = 0

            tests = [
                FrequencyTest.monobit_test,
                FrequencyTest.block_frequency,
                RunTest.run_test,
                ApproximateEntropy.approximate_entropy_test,
                RunTest.longest_one_block_test,
                Matrix.binary_matrix_rank_text,
                SpectralTest.spectral_test,
                TemplateMatching.non_overlapping_test,
                TemplateMatching.overlapping_patterns,
                Universal.statistical_test,
                ComplexityTest.linear_complexity_test,
                Serial.serial_test,
                CumulativeSums.cumulative_sums_test,
                RandomExcursions.random_excursions_test,
                RandomExcursions.variant_test,
                AutocorrelationTest.autocorrelation_test,
                AdaptiveStatisticalTest.adaptive_statistical_test
            ]

            total_tests = len(tests)
            cache.set(f"{job_id}_progress", 0)

            for i, test in enumerate(tests):
                try:
                    result = test(binary_data)[1]
                    if result:
                        x += 1
                except Exception as e:
                    print(f"Error in test {test.__name__}: {e}")
                finally:
                    cache.set(f"{job_id}_progress", i + 1)

            final_text = 'random number' if x > 10 else 'non-random number'

            response_data = {
                "final_result": final_text,
                "executed_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)

@csrf_exempt
def get_progress(request, job_id):
    progress = cache.get(f"{job_id}_progress", 0)
    return JsonResponse({"progress": int(progress)})


@csrf_exempt
def generate_final_ans_nist90b(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request
            data = json.loads(request.body)
            binary_data = data.get('binary_data', '')
            scheduled_time_str = data.get('scheduled_time', '')
            job_id = data.get('job_id', str(uuid.uuid4()))
           
            # Validate binary data
            if not binary_data:
                return JsonResponse({"error": "binary_data is missing or empty"}, status=400)

            # Validate scheduled time format
            if not scheduled_time_str:
                return JsonResponse({"error": "scheduled_time is required"}, status=400)

            try:
                # Convert scheduled_time to a datetime object
                scheduled_time = datetime.datetime.strptime(scheduled_time_str, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                return JsonResponse({"error": "Invalid scheduled_time format. Use 'YYYY-MM-DD HH:MM:SS'."}, status=400)

            # Get the current time
            current_time = datetime.datetime.now()

            # Calculate the time difference in seconds
            time_difference = (scheduled_time - current_time).total_seconds()
            if time_difference > 0:
                print(f"Waiting {time_difference:.2f} seconds until the scheduled time...")
                time.sleep(time_difference)  # Sleep until the scheduled time

            # Initialize x to 0
            x = 0
            

            # Perform the NIST 800-90B tests and check results
            try:
                tests = [
                    MinEntropyTest.MinEntropyTest,
                    CollisionTest.CollisionTest,
                    MarkovTest.MarkovTest,
                    CompressionTest.CompressionTest,
                    TTupleTest.TTupleTest,
                    MostCommonValueTest.MostCommonValueTest,
                    ChiSquareTest.ChiSquareTest,
                    LZ78YTest.LZ78YTest,
                    MultiBlockEntropyTest.MultiBlockEntropyTest,
                    PredictorTest.PredictorTest
                ]
                cache.set(f"{job_id}_progress90b", 0)
                for i, test in enumerate(tests):
                    try:
                        result = test(binary_data)[1]  # Assuming test returns a tuple
                        if result:
                            x += 1
                    except Exception as e:
                        print(f"Error in test {test.__name__}: {e}")
                    finally:
                        cache.set(f"{job_id}_progress90b", i + 1)


            except Exception as e:
                print(f"Error during testing: {e}")
                return HttpResponse("Error during randomness tests.", status=500)

            # Determine if the number is random or not
            final_text = 'random number' if x > 5 else 'non-random number'
            
            # Prepare the response data
            response_data = {
                "final_result": final_text,
                "executed_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)

@csrf_exempt
def get_progress90b(request, job_id):
    progress = cache.get(f"{job_id}_progress90b", 0)
    return JsonResponse({"progress": int(progress)})



@csrf_exempt
def generate_final_ans_dieharder(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            binary_data = data.get('binary_data', '')
            scheduled_time_str = data.get('scheduled_time', '')
            job_id = data.get('job_id', str(uuid.uuid4()))

            if not binary_data:
                return JsonResponse({"error": "binary_data is missing or empty"}, status=400)

            if not scheduled_time_str:
                return JsonResponse({"error": "scheduled_time is required"}, status=400)

            try:
                scheduled_time = datetime.datetime.strptime(scheduled_time_str, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                return JsonResponse({"error": "Invalid scheduled_time format. Use 'YYYY-MM-DD HH:MM:SS'."}, status=400)

            current_time = datetime.datetime.now()
            time_difference = (scheduled_time - current_time).total_seconds()
            if time_difference > 0:
                time.sleep(time_difference)

            x = 0

            tests = [
                BirthdaySpacingsTest.BirthdaySpacingsTest,
                ParkingLotTest.ParkingLotTest,
                Overlapping5PermutationTest.Overlapping5PermutationTest,
                MinimumDistanceTest.MinimumDistanceTest,
                Ranks31x31MatricesTest.Ranks31x31MatricesTest,
                Spheres3DTest.Spheres3DTest,
                Ranks32x32MatricesTest.Ranks32x32MatricesTest,
                CrapsTest.CrapsTest,
                BitstreamTest.BitstreamTest,
                MarsagliaTsangGCDTest.MarsagliaTsangGCDTest,
                OPSOTest.OPSOTest,
                OQSOTest.OQSOTest,
                DNATest.DNATest,
                CountThe1sStreamTest.CountThe1sStreamTest,
                CountThe1sByteTest.CountThe1sByteTest,
                MarsagliaTsangSimpleGCDTest.MarsagliaTsangSimpleGCDTest,
                GeneralizedMinimumDistanceTest.GeneralizedMinimumDistanceTest,
                TestU01LinearComplexityTest.TestU01LinearComplexityTest,
                TestU01LongestRepeatedSubstringTest.TestU01LongestRepeatedSubstringTest,
                TestU01MatrixRankTest.TestU01MatrixRankTest
            ]

            total_tests = len(tests)
            cache.set(f"{job_id}_progress_dieharder", 0)

            for i, test in enumerate(tests):
                try:
                    result = test(binary_data)[1]
                    print(i)
                    if result:
                        x += 1
                except Exception as e:
                    print(f"Error in test {test.__name__}: {e}")
                finally:
                    cache.set(f"{job_id}_progress_dieharder", i + 1)

            final_text = 'random number' if x > 10 else 'non-random number'

            response_data = {
                "final_result": final_text,
                "executed_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)


@csrf_exempt
def get_progress_dieharder(request, job_id):
    progress = cache.get(f"{job_id}_progress_dieharder", 0)
    return JsonResponse({"progress": int(progress)})
