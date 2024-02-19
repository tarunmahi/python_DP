#include <iostream>
#include <vector>
using namespace std;
int main() {
    int N;
    std::cin >> N;

    std::vector<int> arr(N);
    for (int i = 0; i < N; i++) {
        std::cin >> arr[i];
    }

    int totalSumOfDeletions = 0;

    while (arr.size() > 0) {
        int minIndex = 0;

        // Find the index of the minimum number (and the left adjacent element)
        for (int i = 1; i < arr.size(); i++) {
            if (arr[i] < arr[minIndex]) {
                minIndex = i;
            }
        }

        // Add the minimum number to the total sum
        totalSumOfDeletions += arr[minIndex];

        // Delete the minimum element and its adjacent elements
        if (minIndex > 0) {
            totalSumOfDeletions += arr[minIndex - 1];
            arr.erase(arr.begin() + minIndex - 1, arr.begin() + minIndex + 2);
        } else {
            totalSumOfDeletions += arr[minIndex + 1];
            arr.erase(arr.begin(), arr.begin() + 2);
        }
    }

    cout<<totalSumOfDeletions;

    return 0;
}