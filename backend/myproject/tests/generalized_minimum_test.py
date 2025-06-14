from math import sqrt
from scipy.stats import norm
import numpy as np
from concurrent.futures import ThreadPoolExecutor, as_completed

class GeneralizedMinimumDistanceTest:
    @staticmethod
    def calculate_distances(coords):
        """
        Calculate distances between consecutive coordinate pairs.
        """
        return np.array([np.linalg.norm(coords[i] - coords[i + 1]) for i in range(len(coords) - 1)])

    @staticmethod
    def GeneralizedMinimumDistanceTest(data, d=2, verbose=False):
        # Clean the input binary string
        data = data.replace(',', '').strip()

        if not data:
            return None 
        
        # Convert the binary string to a list of floats
        cleaned_data = []
        for char in data:
            if char in '01':  # Keep only '0' and '1'
                cleaned_data.append(float(char))  # Convert to float

        # Ensure the input is now cleaned and contains numeric values
        cleaned_data = np.array(cleaned_data, dtype=float)

        # Check if there are enough data points for the given dimension
        n = len(cleaned_data)
        if n < d + 1:
            return -2, False  # Not enough data points for the test

        # Reshape data into coordinates of dimension 'd'
        coords = np.array([cleaned_data[i:i + d] for i in range(n - d + 1)])

        # Define the number of threads for parallel processing
        num_threads = 4  # Adjust this based on your CPU capabilities
        chunk_size = (len(coords) - 1) // num_threads + 1  # Size of each chunk

        distances_results = []

        # Use ThreadPoolExecutor to parallelize the distance calculation
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = []
            for i in range(0, len(coords) - 1, chunk_size):
                futures.append(executor.submit(GeneralizedMinimumDistanceTest.calculate_distances, coords[i:i + chunk_size + 1]))

            for future in as_completed(futures):
                distances_results.append(future.result())
        
        # Flatten the list of results into a single array
        distances = np.concatenate(distances_results)

        # Calculate mean and expected distance
        mean_distance = np.mean(distances)
        expected = sqrt(d) / 2
        variance = np.var(distances)

        # Calculate Z-statistic
        z_statistic = (mean_distance - expected) / sqrt(variance / len(distances))
        p_value = 2 * (1 - norm.cdf(abs(z_statistic)))

        if verbose:
            print(f"Generalized Minimum Distance Test - Z-statistic: {z_statistic}, p-value: {p_value}")
        
        # Return p-value and pass/fail result (p-value >= 0.01 passes the test)
        return p_value, (p_value >= 0.01)

# from math import sqrt
# from scipy.stats import norm
# import numpy as np
# from concurrent.futures import ThreadPoolExecutor, as_completed, TimeoutError

# class GeneralizedMinimumDistanceTest:
#     @staticmethod
#     def _calculate_distances(coords_chunk):
#         """Compute Euclidean distances for a chunk of coordinate pairs."""
#         return np.linalg.norm(coords_chunk[:-1] - coords_chunk[1:], axis=1)

#     @staticmethod
#     def GeneralizedMinimumDistanceTest(data, d=2, verbose=False, time_limit=5):
#         """Optimized Generalized Minimum Distance Test with parallel execution."""
#         print("generalisedmin")

#         # Step 1: Data Preprocessing
#         data = np.array([float(char) for char in data.strip() if char in '01'], dtype=np.float64)
#         n = len(data)

#         if n < d + 1:
#             return -2, False  # Not enough data points

#         # Convert into d-dimensional coordinates
#         coords = np.lib.stride_tricks.sliding_window_view(data, d)

#         num_threads = min(8, len(coords) // 10 + 1)  # Adaptive threading
#         chunk_size = len(coords) // num_threads

#         distances_results = []

#         # Step 2: Parallel Distance Computation
#         try:
#             with ThreadPoolExecutor(max_workers=num_threads) as executor:
#                 futures = [
#                     executor.submit(
#                         GeneralizedMinimumDistanceTest._calculate_distances,
#                         coords[i * chunk_size : (i + 1) * chunk_size + 1]
#                     )
#                     for i in range(num_threads)
#                 ]

#                 for future in as_completed(futures, timeout=time_limit):
#                     distances_results.append(future.result())

#         except TimeoutError:
#             return -3, False  # Timeout occurred

#         # Step 3: Statistical Test
#         distances = np.concatenate(distances_results)
#         mean_distance = np.mean(distances)
#         expected = sqrt(d) / 2
#         variance = np.var(distances)

#         if variance == 0:
#             return 0.0, False  # Avoid division by zero

#         z_statistic = (mean_distance - expected) / sqrt(variance / len(distances))
#         p_value = 2 * (1 - norm.cdf(abs(z_statistic)))

#         if verbose:
#             print(f"Generalized Minimum Distance Test - Z-statistic: {z_statistic}, p-value: {p_value}")

#         return p_value, (p_value >= 0.01)
