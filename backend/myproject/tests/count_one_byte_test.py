import numpy as np
from scipy.stats import chi2
from concurrent.futures import ThreadPoolExecutor, as_completed

class CountThe1sByteTest:
    @staticmethod
    def CountThe1sByteTest(data, verbose=False):
        data = data.replace(',', '').strip()

        if not data:
            return None 
        
        if len(data) == 0:
            return -2, False
        
        # Clean and convert input data to integers
        try:
            # Validate and filter binary input data
            cleaned_data = []
            for char in data:
                if char in ['0', '1']:
                    cleaned_data.append(int(char))

            # Ensure the input data is a numpy array of integers (0s and 1s)
            data = np.array(cleaned_data, dtype=int)

            # Check if the length of data is a multiple of 8
            if len(data) % 8 != 0:
                return -2, False

            n = len(data) // 8
            num_chunks = min(8, n)  # Use up to 8 threads or fewer based on data size
            chunk_size = n // num_chunks

            # Parallel calculation of 1's counts
            ones_counts = []
            with ThreadPoolExecutor() as executor:
                futures = [
                    executor.submit(
                        CountThe1sByteTest.process_chunk, 
                        data[i * 8 * chunk_size : (i + 1) * 8 * chunk_size], 
                        chunk_size
                    ) 
                    for i in range(num_chunks)
                ]
                for future in as_completed(futures):
                    ones_counts.extend(future.result())

            expected = 4  # Expected number of 1s in each byte
            variance = 2  # Variance in the distribution
            chi_square = np.sum([(count - expected) ** 2 / variance for count in ones_counts])
            p_value = 1 - chi2.cdf(chi_square, n - 1)

            if verbose:
                print(f"Count-the-1s (Byte) Test - Chi-square: {chi_square}, p-value: {p_value}")

            return p_value, (p_value >= 0.01)  # Return p-value and boolean for pass/fail

        except ValueError as e:
            print(f"ValueError: {e}")
            return -7, False  # Return -1 if there's a ValueError
        except Exception as e:
            print(f"Error: {e}")
            return -4, False  # Return -1 for any other error

    @staticmethod
    def process_chunk(chunk, chunk_size):
        # Calculate the number of 1s in each 8-bit segment of the chunk
        return [np.sum(chunk[i * 8:(i + 1) * 8]) for i in range(chunk_size)]


# import numpy as np
# from scipy.stats import chi2
# from concurrent.futures import ThreadPoolExecutor, as_completed, TimeoutError

# class CountThe1sByteTest:
#     @staticmethod
#     def _count_ones_in_bytes(data_chunk):
#         """Count the number of 1s in each byte (8-bit segment) of a chunk."""
#         return np.sum(data_chunk.reshape(-1, 8), axis=1)  # Efficient sum in each byte

#     @staticmethod
#     def CountThe1sByteTest(data, verbose=False, time_limit=5):
#         """Optimized Count-The-1s (Byte) Test with parallel processing."""
#         print("count1byte")

#         # Step 1: Data Preprocessing
#         data = np.array([int(bit) for bit in data.strip() if bit in '01'], dtype=np.uint8)
#         n = len(data)

#         if n == 0 or n % 8 != 0:
#             return -2, False  # Invalid input (empty or not multiple of 8)

#         num_bytes = n // 8
#         num_chunks = min(8, num_bytes)  # Use up to 8 parallel threads
#         chunk_size = num_bytes // num_chunks

#         ones_counts = []

#         # Step 2: Parallel Processing
#         try:
#             with ThreadPoolExecutor() as executor:
#                 futures = [
#                     executor.submit(
#                         CountThe1sByteTest._count_ones_in_bytes,
#                         data[i * chunk_size * 8 : (i + 1) * chunk_size * 8]
#                     )
#                     for i in range(num_chunks)
#                 ]

#                 for future in as_completed(futures, timeout=time_limit):
#                     ones_counts.extend(future.result())

#         except TimeoutError:
#             return -3, False  # Timeout occurred

#         # Step 3: Statistical Test
#         expected = 4  # Expected number of 1s per byte
#         variance = 2  # Variance in the distribution
#         chi_square = np.sum((np.array(ones_counts) - expected) ** 2 / variance)
#         p_value = 1 - chi2.cdf(chi_square, num_bytes - 1)

#         if verbose:
#             print(f"Count-the-1s (Byte) Test - Chi-square: {chi_square}, p-value: {p_value}")

#         return p_value, (p_value >= 0.01)
