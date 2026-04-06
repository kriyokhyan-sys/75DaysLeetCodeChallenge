int findMin(int* nums, int numsSize) {
    int left = 0;
    int right = numsSize - 1;

    while (left < right) {
        // Prevents potential overflow for large arrays
        int mid = left + (right - left) / 2;

        if (nums[mid] > nums[right]) {
            // The pivot point is in the right half
            left = mid + 1;
        } else {
            // The pivot point is in the left half, or mid IS the minimum
            right = mid;
        }
    }

    // When left == right, we've found the smallest element
    return nums[left];
}