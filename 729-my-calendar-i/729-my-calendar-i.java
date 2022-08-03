class MyCalendar {
    TreeMap<Integer,Integer> calen;

    public MyCalendar() {
        calen = new TreeMap();
    }
    
    public boolean book(int start, int end) {
        Integer next = calen.ceilingKey(start);
        Integer prev = calen.floorKey(start);
        boolean valid = true;
        if(prev!=null){
            int prevEnd = calen.get(prev);
            if(start<prevEnd){
                valid = false;
            }
        }
        if(next!=null){
            int nextStart = next;
            if(end>nextStart){
                valid = false;
            }
        }
        if(valid){
            calen.put(start,end);
        }
        return valid;
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * boolean param_1 = obj.book(start,end);
 */