# Python3 implementation for
# the above approach

# Function to find the longest
# subarray with increasing
# contiguous elements
def maxiConsecutiveSubarray(arr, N):

	# Stores the length of
	# required longest subarray
	maxi = 0;

	for i in range(N - 1):
		# Stores the length of
		# length of longest such
		# subarray from ith index
		cnt = 1;

		for j in range(i, N - 1):

			# If consecutive elements are
			# increasing and differ by 1
			if (arr[j + 1] == arr[j] + 1):
				cnt += 1;

			# Otherwise
			else:
				break;

		# Update the longest subarray
		# obtained so far
		maxi = max(maxi, cnt);
		i = j;

	# Return the length obtained
	return maxi;

# Driver Code
if __name__ == '__main__':

	N = 11;
	arr = [1, 3, 4, 2, 3,
		4, 2, 3, 5, 6, 7];

	print(maxiConsecutiveSubarray(arr, N));

# This code is contributed by Rajput-Ji
