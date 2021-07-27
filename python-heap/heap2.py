from heapq import heappop, heappush, heapify


nums = [12, 3, 0, -2, 6, 4, 8, 9];

def test_heappop(inputDataArray):
    heap = [];
    for el in inputDataArray:
        heappush(heap, el);

    while heap:
        print(heappop(heap));

def test_heapify(inputDataArray):
    temp = inputDataArray[:];
    heapify(temp);
    print(temp);


# test_heappop(nums);

test_heapify(nums);
