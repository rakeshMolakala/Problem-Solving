class MedianFinder {
    PriorityQueue<Integer> maxHeap;
    PriorityQueue<Integer> minHeap;

    public MedianFinder() {
        maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        minHeap = new PriorityQueue<>();
    }
    
    public void addNum(int num) {
        maxHeap.add(num);
        minHeap.add(maxHeap.poll());
        if(maxHeap.size()+1<minHeap.size()){
            maxHeap.add(minHeap.poll());
        }
        
    }
    
    public double findMedian() {
        if(maxHeap.size()+1==minHeap.size()){
            return minHeap.peek();
        }
        else{
            Double d1 = Double.valueOf(maxHeap.peek());
            Double d2 = Double.valueOf(minHeap.peek());
            return (d1+d2)/2;
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */